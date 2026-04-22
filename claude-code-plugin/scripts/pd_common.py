"""Shared helpers for the prompt-decorators Claude Code plugin.

Keeps engine bootstrap, config read/write, registry walk, and logging in one
place so the hook and dispatcher stay short.
"""

from __future__ import annotations

import copy
import json
import os
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
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(payload)
        os.replace(tmp, CONFIG_PATH)
    except Exception:
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
    """Strip `(params)` from a decorator sigil to get its bare name."""
    return sigil.split("(", 1)[0]


_REGISTRY_CACHE: list[dict[str, Any]] | None = None


def _walk_registry() -> list[dict[str, Any]]:
    """Walk the vendored registry JSON files and infer category from path.

    The engine defaults `category` to "General" when the JSON doesn't declare
    one (and most don't), so we derive it from the directory layout where the
    catalogue's taxonomy actually lives.
    """
    import json as _json

    registry_roots = [
        VENDOR_DIR / "prompt_decorators" / "registry" / "core",
        VENDOR_DIR / "prompt_decorators" / "registry" / "extensions",
    ]
    out: list[dict[str, Any]] = []
    for root in registry_roots:
        if not root.exists():
            continue
        for path in root.rglob("*.json"):
            try:
                data = _json.loads(path.read_text(encoding="utf-8"))
            except (OSError, _json.JSONDecodeError):
                continue
            name = data.get("decoratorName") or data.get("name")
            if not name:
                continue
            rel_parts = path.relative_to(root).parts
            category = rel_parts[0] if len(rel_parts) > 1 else "other"
            desc = (data.get("description") or "").splitlines()
            out.append(
                {
                    "name": name,
                    "description": desc[0][:160] if desc else "",
                    "category": category,
                }
            )
    return sorted(out, key=lambda x: (x["category"], x["name"]))


def registry_decorators() -> list[dict[str, Any]]:
    """Load the catalogue as plain dicts (name, description, category)."""
    global _REGISTRY_CACHE
    if _REGISTRY_CACHE is None:
        _REGISTRY_CACHE = _walk_registry()
    return _REGISTRY_CACHE


def registry_names() -> set[str]:
    """Set of all valid decorator names - O(1) lookup for existence checks."""
    return {d["name"] for d in registry_decorators()}
