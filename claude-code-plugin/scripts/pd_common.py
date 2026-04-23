"""Shared helpers for the prompt-decorators Claude Code plugin.

Keeps engine bootstrap, config read/write, registry walk, logging, and
user-extension decorator registration in one place so the hook and
dispatcher stay short.
"""

from __future__ import annotations

import copy
import json
import os
import re
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
VENDOR_DIR = PLUGIN_ROOT / "vendor"

# Config key constants so typos fail at import instead of silently misreading.
CFG_VERSION = "version"
CFG_ALWAYS_ON = "always_on"
CFG_DISABLED = "disabled"
CFG_AUTO = "auto"
AUTO_MODE = "mode"
AUTO_ONCE = "once_armed"
AUTO_MODEL = "model"
MODE_ON = "on"
MODE_OFF = "off"

DEFAULT_MODEL = "claude-haiku-4-5"

DEFAULT_CONFIG: dict[str, Any] = {
    CFG_VERSION: 1,
    CFG_ALWAYS_ON: [],
    CFG_DISABLED: [],
    CFG_AUTO: {AUTO_MODE: MODE_OFF, AUTO_ONCE: False, AUTO_MODEL: DEFAULT_MODEL},
}

DEFAULT_CONFIG_DIR = Path(
    os.environ.get(
        "PROMPT_DECORATORS_CONFIG_DIR",
        str(Path.home() / ".config" / "prompt-decorators"),
    )
)
CONFIG_PATH = DEFAULT_CONFIG_DIR / "config.json"

# Logs default to the user's cache dir (0o600, O_NOFOLLOW). Never /tmp by
# default - it's world-readable and symlinkable by other local users.
DEFAULT_LOG_PATH = Path.home() / ".cache" / "prompt-decorators" / "hook.log"
LOG_PATH = Path(os.environ.get("PROMPT_DECORATORS_LOG", str(DEFAULT_LOG_PATH)))
LOG_MAX_BYTES = 5_000_000
LOG_DEBUG = os.environ.get("PROMPT_DECORATORS_LOG_DEBUG") == "1"


def ensure_engine_on_path() -> None:
    vendor = str(VENDOR_DIR)
    if vendor not in sys.path:
        sys.path.insert(0, vendor)


def _normalise_list(value: Any, default: list) -> list:
    """Coerce loaded JSON to a list, dropping non-str entries."""
    if not isinstance(value, list):
        return list(default)
    return [v for v in value if isinstance(v, str)]


def _normalise_auto(value: Any) -> dict:
    """Coerce loaded auto block to the expected dict shape."""
    base = copy.deepcopy(DEFAULT_CONFIG[CFG_AUTO])
    if isinstance(value, dict):
        for k in (AUTO_MODE, AUTO_ONCE, AUTO_MODEL):
            if k in value:
                base[k] = value[k]
    return base


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return copy.deepcopy(DEFAULT_CONFIG)
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return copy.deepcopy(DEFAULT_CONFIG)
    # Defensive: config.json must be a dict. Malformed values (null, lists,
    # scalars) would have raised AttributeError in the old code path; guard
    # so the hook can still fail open with defaults.
    if not isinstance(data, dict):
        return copy.deepcopy(DEFAULT_CONFIG)
    merged = copy.deepcopy(DEFAULT_CONFIG)
    merged[CFG_ALWAYS_ON] = _normalise_list(
        data.get(CFG_ALWAYS_ON), DEFAULT_CONFIG[CFG_ALWAYS_ON]
    )
    merged[CFG_DISABLED] = _normalise_list(
        data.get(CFG_DISABLED), DEFAULT_CONFIG[CFG_DISABLED]
    )
    merged[CFG_AUTO] = _normalise_auto(data.get(CFG_AUTO))
    if isinstance(data.get(CFG_VERSION), int):
        merged[CFG_VERSION] = data[CFG_VERSION]
    return merged


def save_config(cfg: dict[str, Any]) -> None:
    """Write config atomically: tempfile + os.replace. Prevents corruption on
    concurrent writes (two `/decorate` invocations, or crash mid-write).
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    payload = json.dumps(cfg, indent=2) + "\n"
    fd, tmp = tempfile.mkstemp(
        prefix=".config-", suffix=".tmp", dir=str(CONFIG_PATH.parent)
    )
    # `mkstemp` returns an open fd. If `os.fdopen` below fails (MemoryError,
    # OSError) BEFORE the context manager claims the fd, the fd would leak.
    # Wrap fdopen in its own try so we only ever os.close() a still-owned
    # fd - calling os.close on an already-closed/reused fd can clobber an
    # unrelated file descriptor.
    try:
        try:
            writer = os.fdopen(fd, "w", encoding="utf-8")
        except BaseException:
            os.close(fd)
            raise
        with writer as f:
            f.write(payload)
        os.replace(tmp, CONFIG_PATH)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _rotate_log_if_needed() -> None:
    try:
        size = LOG_PATH.stat().st_size
    except OSError:
        return
    if size > LOG_MAX_BYTES:
        rotated = LOG_PATH.with_suffix(LOG_PATH.suffix + ".1")
        try:
            os.replace(LOG_PATH, rotated)
        except OSError:
            pass


def log(event: dict[str, Any]) -> None:
    if os.environ.get("PROMPT_DECORATORS_LOG_DISABLE") == "1":
        return
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        _rotate_log_if_needed()
        # O_NOFOLLOW blocks symlink games on any shared-dir logs; 0o600 means
        # only the owner can read the logged prompts.
        flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(str(LOG_PATH), flags, 0o600)
        # O_CREAT honours umask, and pre-existing log files keep their old
        # mode - enforce 0o600 on every open to plug that gap.
        try:
            os.fchmod(fd, 0o600)
        except OSError:
            pass
        with os.fdopen(fd, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": time.time(), **event}) + "\n")
    except (OSError, TypeError):
        pass


def bare_name(sigil: str) -> str:
    """Strip `(params)` and `:vX.Y.Z` from a decorator sigil.

    Used for dedup / existence checks - both `Concise` and `Concise:v1` and
    `Concise(depth=deep)` must collapse to the same key `Concise`.
    """
    name = sigil.split("(", 1)[0]
    name = name.split(":v", 1)[0]
    return name


# Credentials / tokens that sometimes leak into exception messages from
# upstream libraries. Redact before logging tracebacks or `str(exception)`.
_SECRET_PATTERNS = (
    # Anthropic API keys (post-2023 `sk-ant-...` format).
    (re.compile(r"sk-ant-[A-Za-z0-9\-_]{10,}"), "sk-ant-<redacted>"),
    # OpenAI API keys (`sk-...` without the `ant-` infix).
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"), "sk-<redacted>"),
    # Generic Authorization headers / Bearer tokens.
    (re.compile(r"(?i)bearer\s+[A-Za-z0-9\-._~+/=]{10,}"), "Bearer <redacted>"),
    (
        re.compile(r"(?i)authorization:\s*[A-Za-z]+\s+[A-Za-z0-9\-._~+/=]{10,}"),
        "Authorization: <redacted>",
    ),
    # Env-style key embeds (anthropic/openai style).
    (re.compile(r"ANTHROPIC_API_KEY=[^\s'\"]+"), "ANTHROPIC_API_KEY=<redacted>"),
    (re.compile(r"OPENAI_API_KEY=[^\s'\"]+"), "OPENAI_API_KEY=<redacted>"),
    # X-Api-Key header pattern.
    (re.compile(r"(?i)x-api-key:\s*[^\s'\",]+"), "x-api-key: <redacted>"),
)


def redact(text: str) -> str:
    """Strip Claude / Bearer tokens from log strings."""
    for pattern, replacement in _SECRET_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


_REGISTRY_CACHE: list[dict[str, Any]] | None = None


def user_registry_dir() -> Path | None:
    """User-local extension directory for personal decorators.

    Survives `vendor/` re-syncs (which wipe the vendored copy). Enabled by
    setting PROMPT_DECORATORS_USER_REGISTRY or by populating the default
    path at `$HOME/.config/prompt-decorators/extensions/`.
    """
    override = os.environ.get("PROMPT_DECORATORS_USER_REGISTRY")
    if override:
        return Path(override)
    default = Path.home() / ".config" / "prompt-decorators" / "extensions"
    return default if default.exists() else None


def _walk_registry() -> list[dict[str, Any]]:
    """Walk registry JSON files and infer category from path.

    Reads both the vendored catalogue (shipped with the plugin) and the
    user's personal extension directory (if present). The engine defaults
    `category` to "General" when the JSON doesn't declare one, so we
    derive it from the directory layout - the first path segment is the
    category bucket.

    Shadowing: a user decorator with the same name as a vendored one wins
    (user dir is iterated last). The shadow is intentional (per the
    authoring skill) but surprising, so we log a `user_registry_shadow`
    event for each name replaced. Inspect with
    `PROMPT_DECORATORS_LOG_DEBUG=1`.
    """
    vendored_roots: list[Path] = [
        VENDOR_DIR / "prompt_decorators" / "registry" / "core",
        VENDOR_DIR / "prompt_decorators" / "registry" / "extensions",
    ]
    user_dir = user_registry_dir()

    seen: dict[str, dict[str, Any]] = {}
    # Pass 1: vendored catalogue.
    for root in vendored_roots:
        if not root.exists():
            continue
        for path in root.rglob("*.json"):
            entry = _parse_registry_json(path, root)
            if entry is not None:
                seen[entry["name"]] = entry

    # Pass 2: user extensions override by name. Log each shadow so users
    # aren't surprised when their custom Concise overrides the core Concise.
    if user_dir is not None and user_dir.exists():
        for path in user_dir.rglob("*.json"):
            entry = _parse_registry_json(path, user_dir)
            if entry is None:
                continue
            name = entry["name"]
            if name in seen:
                log(
                    {
                        "phase": "user_registry_shadow",
                        "name": name,
                        "file": str(path),
                    }
                )
            seen[name] = entry
    return sorted(seen.values(), key=lambda x: (x["category"], x["name"]))


def _parse_registry_json(path: Path, root: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    # Defensive: a user could drop `[1, 2, 3]` or `"hi"` or `null` into the
    # registry. Skip silently instead of raising AttributeError on
    # `.get(...)` - that would propagate through `/decorate list` and
    # crash the dispatcher.
    if not isinstance(data, dict):
        return None
    name = data.get("decoratorName") or data.get("name")
    if not name:
        return None
    rel_parts = path.relative_to(root).parts
    category = rel_parts[0] if len(rel_parts) > 1 else "user"
    desc = (data.get("description") or "").splitlines()
    return {
        "name": name,
        "description": desc[0][:160] if desc else "",
        "category": category,
    }


def registry_decorators() -> list[dict[str, Any]]:
    """Load the catalogue as plain dicts (name, description, category)."""
    global _REGISTRY_CACHE
    if _REGISTRY_CACHE is None:
        _REGISTRY_CACHE = _walk_registry()
    return _REGISTRY_CACHE


def registry_names() -> set[str]:
    """Set of all valid decorator names - O(1) lookup for existence checks."""
    return {d["name"] for d in registry_decorators()}


# --- User-extension decorator registration ----------------------------------
#
# The hook and the `/decorate preview` dispatcher both need to register
# user-authored decorators with the engine before calling
# `apply_dynamic_decorators`. The security validators below gate what is
# allowed into the engine's `exec()` path at expansion time; they live here
# so both call sites share a single source of truth.


# Forbidden fields in user-supplied decorator JSON. The engine's
# `register_decorator` -> `apply` path calls `exec(transform_function, ...)`
# on the raw string, which would give any user-supplied JSON the ability
# to run arbitrary Python in the hook process. No core/extensions
# decorator in the vendored registry uses these fields - they all use
# `transformationTemplate`, which is a safe string-template path.
_UNSAFE_USER_FIELDS = ("transform_function", "transformFunction")


# `parameterMapping` keys are interpolated unquoted into Python source via
# `.format(param=param_name)` at engine `dynamic_decorator.py:125-131`. A key
# like `foo" and __import__("os").system("id") or "` would break out of the
# `"{param}"` wrapper without using triple-quote or backslash characters.
# The engine's own parameter-name grammar accepts only identifier-like
# strings; enforce that same grammar before registration.
_SAFE_PARAM_KEY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def _is_safe_template_string(s: Any) -> tuple[bool, str | None]:
    # Reject strings that can escape the engine's triple-quoted Python
    # string literals during template->exec rendering.
    #
    # The engine builds Python source like ``result = (triple-single-quote){
    # instruction}(triple-single-quote)`` and then exec()s it. A user-supplied
    # sequence of three single quotes inside the instruction closes the
    # string literal and injects arbitrary code. A sequence of three double
    # quotes does the same against any future variant that switches quote
    # styles. A backslash can combine with quote characters to engineer
    # equivalent breakouts via escape-sequence processing inside triple-
    # quoted literals.
    #
    # Benign instructions do not need any of those characters; reject all
    # three conservatively. Return a reason tag so downstream can emit a
    # specific `user_registry_rejected` event (helps users distinguish
    # "used backslash legitimately" vs "attempted triple-quote breakout").
    if not isinstance(s, str):
        return False, "not_a_string"
    if "'''" in s or '"""' in s:
        return False, "triple_quote"
    if "\\" in s:
        return False, "backslash"
    return True, None


def _validate_user_template(data: dict) -> tuple[bool, str | None]:
    """Validate every exec-reachable value inside a user decorator's
    `transformationTemplate`. Returns `(safe, reason)`.
    """
    tpl = data.get("transformationTemplate")
    if not isinstance(tpl, dict):
        return True, None
    instruction = tpl.get("instruction", "")
    if instruction:
        safe, kind = _is_safe_template_string(instruction)
        if not safe:
            return False, f"unsafe_template_instruction_{kind}"
    mapping = tpl.get("parameterMapping")
    if mapping is None:
        return True, None
    if not isinstance(mapping, dict):
        # List / scalar `parameterMapping` values break the engine at apply
        # time anyway. Reject explicitly so the user sees why.
        return False, "unsafe_template_param_mapping_shape"
    for param_name, param_cfg in mapping.items():
        if not _SAFE_PARAM_KEY_RE.match(str(param_name)):
            return False, "unsafe_template_param_key"
        if not isinstance(param_cfg, dict):
            continue
        fmt = param_cfg.get("format")
        if fmt is not None:
            safe, kind = _is_safe_template_string(fmt)
            if not safe:
                return False, f"unsafe_template_format_{kind}:{param_name}"
    return True, None


def register_user_decorators() -> None:
    """Inject user-local decorators into the engine's registry.

    User decorators live under `$PROMPT_DECORATORS_USER_REGISTRY` (or
    `~/.config/prompt-decorators/extensions/` by default) and survive
    `vendor/` re-syncs. Without this step, user decorators would appear in
    `/decorate list` but neither the hook nor `/decorate preview` could
    actually expand them.

    Security: user JSON is NOT trusted. Rejects outright:
      - Files declaring `transform_function` / `transformFunction` - the
        engine's raw exec-a-string-of-Python path.
      - Files whose `transformationTemplate.instruction` or any
        `parameterMapping[*].format` contains characters that can escape
        the engine's triple-quoted string literal and smuggle code into
        the `exec()` rendering.
    """
    # Engine must be on sys.path whether or not a user dir exists — callers
    # depend on that side effect to then import the engine themselves.
    ensure_engine_on_path()
    user_dir = user_registry_dir()
    if user_dir is None:
        return
    if not user_dir.exists():
        # Default path legitimately may not exist (user hasn't authored any
        # personal decorators yet). But if they set an override and point it
        # somewhere absent, that's almost always a typo worth surfacing.
        if os.environ.get("PROMPT_DECORATORS_USER_REGISTRY"):
            log({"phase": "user_registry_missing", "path": str(user_dir)})
        return
    try:
        from prompt_decorators.core.dynamic_decorator import DynamicDecorator
    except Exception as e:  # noqa: BLE001
        log(
            {
                "phase": "user_registry_import_error",
                "error": redact(str(e))[:300],
            }
        )
        return
    DynamicDecorator.load_registry()
    loaded = 0
    rejected = 0
    # Track names seen in THIS pass so we can flag user-over-user collisions
    # (two user JSON files declaring the same decoratorName). User-over-
    # vendored shadows are already logged by _walk_registry; this catches
    # the otherwise-silent within-extensions case.
    user_seen: set[str] = set()
    for path in user_dir.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                rejected += 1
                log(
                    {
                        "phase": "user_registry_rejected",
                        "file": str(path),
                        "reason": "not_a_dict",
                    }
                )
                continue
            unsafe = [k for k in _UNSAFE_USER_FIELDS if k in data]
            if unsafe:
                rejected += 1
                log(
                    {
                        "phase": "user_registry_rejected",
                        "file": str(path),
                        "reason": "unsafe_field",
                        "fields": unsafe,
                    }
                )
                continue
            safe, reason = _validate_user_template(data)
            if not safe:
                rejected += 1
                log(
                    {
                        "phase": "user_registry_rejected",
                        "file": str(path),
                        "reason": reason,
                    }
                )
                continue
            name = data.get("decoratorName") or data.get("name")
            if name and name in user_seen:
                log(
                    {
                        "phase": "user_registry_duplicate",
                        "file": str(path),
                        "name": name,
                    }
                )
            DynamicDecorator.register_decorator(data)
            loaded += 1
            if name:
                user_seen.add(name)
        except Exception as e:  # noqa: BLE001
            log(
                {
                    "phase": "user_registry_load_error",
                    "file": str(path),
                    "error_type": type(e).__name__,
                    "error": redact(str(e))[:300],
                }
            )
    if loaded or rejected:
        log({"phase": "user_registry_loaded", "count": loaded, "rejected": rejected})
