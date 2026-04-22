#!/usr/bin/env python3
"""UserPromptSubmit hook for prompt-decorators.

- Detects `::Name(params)` and `+++Name(params)` decorator sigils on their
  own line at the start of a prompt line.
- Expands them via the vendored `prompt_decorators` engine.
- Applies always-on decorators from config and (optionally) runs the
  auto-decorate selector when `auto.mode == "on"` or `auto.once_armed` is set.
- Emits the expanded instructions as `hookSpecificOutput.additionalContext`
  so they appear adjacent to the user's original message.
"""

from __future__ import annotations

import json
import os
import re
import sys
import traceback
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

from pd_common import (  # noqa: E402
    AUTO_MODE,
    AUTO_MODEL,
    AUTO_ONCE,
    CFG_ALWAYS_ON,
    CFG_AUTO,
    CFG_DISABLED,
    CONFIG_PATH,
    LOG_DEBUG,
    MODE_OFF,
    MODE_ON,
    bare_name,
    ensure_engine_on_path,
    load_config,
    log,
    redact,
    save_config,
    user_registry_dir,
)

# Derive sigil regexes from the engine's canonical `DECORATOR_PATTERN` so the
# plugin's `::` syntax and the library's `+++` syntax can never drift. The
# engine owns the grammar of a decorator reference (name, optional version,
# optional parenthesised params); this file only owns the alternative
# start-of-line sigil prefix.
ensure_engine_on_path()
try:
    from prompt_decorators.core.dynamic_decorator import (
        DECORATOR_PATTERN as _ENGINE_DECORATOR_PATTERN,
    )

    # Engine pattern shape: r"\+\+\+(NAME_VERSION)(?:\((PARAMS)\))?"
    # Drop the `\+\+\+` prefix and the two capture groups to get a
    # non-capturing body we can embed under arbitrary prefixes.
    _ENGINE_BODY = _ENGINE_DECORATOR_PATTERN.replace(r"\+\+\+", "", 1)
    # Replace the engine's two capture groups with non-capturing groups so
    # the plugin's single outer group always captures the whole decorator
    # reference in .group(1).
    _SIGIL_BODY = (
        _ENGINE_BODY.replace(r"([A-Za-z]", r"(?:[A-Za-z]", 1)
        .replace(r"(\(", r"(?:\(", 1)
        .replace(r"\(([^)]*)\)", r"\([^)]*\)", 1)
    )
except Exception:  # noqa: BLE001
    # Fallback if the engine's pattern constant ever moves or changes. Covers
    # the same grammar - if this diverges from the engine, the test suite
    # catches it via the end-to-end hook tests.
    _SIGIL_BODY = (
        r"[A-Za-z][A-Za-z0-9]*"
        r"(?::v[0-9]+(?:\.[0-9]+(?:\.[0-9]+)?)?)?"
        r"(?:\([^)]*\))?"
    )

SIGIL_COLON_RE = re.compile(rf"(?m)^::({_SIGIL_BODY})")
SIGIL_PLUS_RE = re.compile(rf"(?m)^\+\+\+({_SIGIL_BODY})")
STRIP_RE = re.compile(rf"(?m)^\+\+\+{_SIGIL_BODY}\s*\n?")


def _prompt_might_have_sigils(prompt: str) -> bool:
    """Cheap substring check before any regex work."""
    return "::" in prompt or "+++" in prompt


def _config_is_active(cfg: dict) -> bool:
    """True if always-on or auto mode could inject decorators on any prompt."""
    if cfg.get(CFG_ALWAYS_ON):
        return True
    auto = cfg.get(CFG_AUTO, {}) or {}
    return auto.get(AUTO_MODE) == MODE_ON or auto.get(AUTO_ONCE, False)


def normalise_sigil(prompt: str) -> tuple[str, list[str]]:
    """Rewrite `::Name(...)` -> `+++Name(...)` at start-of-line only."""
    detected: list[str] = []

    def _sub(m: re.Match) -> str:
        detected.append("::" + m.group(1))
        return "+++" + m.group(1)

    return SIGIL_COLON_RE.sub(_sub, prompt), detected


def strip_sigils(prompt: str) -> str:
    return STRIP_RE.sub("", prompt)


def apply_always_on(prompt: str, cfg: dict) -> str:
    always = cfg.get(CFG_ALWAYS_ON, []) or []
    disabled = {bare_name(d) for d in (cfg.get(CFG_DISABLED, []) or [])}
    if not always:
        return prompt
    existing = {m.group(1).split("(")[0] for m in SIGIL_PLUS_RE.finditer(prompt)}
    to_add = [
        name
        for name in always
        if bare_name(name) not in existing and bare_name(name) not in disabled
    ]
    if not to_add:
        return prompt
    return "\n".join(f"+++{d}" for d in to_add) + "\n" + prompt


def apply_auto(prompt: str, cfg: dict) -> tuple[str, list[str], bool]:
    """If auto mode is armed, run the selector and prepend its picks.

    Returns `(new_prompt, names, should_consume_once)`. The caller is
    responsible for clearing `once_armed` in config - but only after a
    successful emit, so a late-path failure doesn't silently consume the
    user's one-shot arm.
    """
    auto_cfg = cfg.get(CFG_AUTO, {}) or {}
    mode = auto_cfg.get(AUTO_MODE, MODE_OFF)
    once = auto_cfg.get(AUTO_ONCE, False)
    if mode != MODE_ON and not once:
        return prompt, [], False

    try:
        from auto_decorate import select_decorators  # type: ignore

        disabled = {bare_name(d) for d in (cfg.get(CFG_DISABLED, []) or [])}
        names = [
            n
            for n in select_decorators(prompt, model=auto_cfg.get(AUTO_MODEL))
            if n not in disabled
        ]
    except Exception as e:  # noqa: BLE001
        log(
            {
                "phase": "auto_error",
                "error": redact(str(e))[:300],
                "tb": redact(traceback.format_exc())[:2000],
            }
        )
        names = []

    if not names:
        return prompt, [], False
    prefix = "\n".join(f"+++{n}" for n in names)
    return f"{prefix}\n{prompt}", names, once


def _consume_once_armed(cfg: dict) -> None:
    """Clear the one-shot auto arm. Called only after a successful emit."""
    cfg[CFG_AUTO][AUTO_ONCE] = False
    try:
        save_config(cfg)
    except Exception as e:  # noqa: BLE001
        # save_config can raise OSError / TypeError / anything. Losing a
        # once_armed clear is preferable to blocking the user's prompt
        # (the whole hook is fail-open). Next prompt will re-fire auto,
        # which the user will notice and can turn off.
        log(
            {
                "phase": "auto_once_save_error",
                "error_type": type(e).__name__,
                "error": redact(str(e))[:200],
            }
        )


# Forbidden fields in user-supplied decorator JSON. The engine's
# `register_decorator` -> `apply` path calls `exec(transform_function, ...)`
# on the raw string, which would give any user-supplied JSON the ability
# to run arbitrary Python in the hook process. No core/extensions
# decorator in the vendored registry uses these fields - they all use
# `transformationTemplate`, which is a safe string-template path.
_UNSAFE_USER_FIELDS = ("transform_function", "transformFunction")


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


# `parameterMapping` keys are interpolated unquoted into Python source via
# `.format(param=param_name)` at engine `dynamic_decorator.py:125-131`. A key
# like `foo" and __import__("os").system("id") or "` would break out of the
# `"{param}"` wrapper without using triple-quote or backslash characters.
# The engine's own parameter-name grammar accepts only identifier-like
# strings; enforce that same grammar before registration.
_SAFE_PARAM_KEY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


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


def _register_user_decorators() -> None:
    """Inject user-local decorators into the engine's registry.

    User decorators live under `$PROMPT_DECORATORS_USER_REGISTRY` (or
    `~/.config/prompt-decorators/extensions/` by default) and survive
    `vendor/` re-syncs. Without this step, user decorators would appear in
    `/decorate list` but the hook couldn't actually expand them.

    Security: user JSON is NOT trusted. Rejects outright:
      - Files declaring `transform_function` / `transformFunction` - the
        engine's raw exec-a-string-of-Python path.
      - Files whose `transformationTemplate.instruction` or any
        `parameterMapping[*].format` contains characters that can escape
        the engine's triple-quoted string literal and smuggle code into
        the `exec()` rendering.
    """
    user_dir = user_registry_dir()
    if user_dir is None or not user_dir.exists():
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
            DynamicDecorator.register_decorator(data)
            loaded += 1
        except Exception as e:  # noqa: BLE001
            log(
                {
                    "phase": "user_registry_load_error",
                    "file": str(path),
                    "error_type": type(e).__name__,
                }
            )
    if loaded or rejected:
        log({"phase": "user_registry_loaded", "count": loaded, "rejected": rejected})


def _emit_import_error_to_stderr(exc: Exception) -> None:
    """Engine import failures are a configuration bug worth surfacing loudly
    in addition to the log. Keep stdout clean (would corrupt hook protocol).
    """
    sys.stderr.write(
        f"[prompt-decorators] engine import failed: {exc!r}\n"
        "  (prompt passed through unchanged; set PROMPT_DECORATORS_LOG_DEBUG=1 "
        "and check the log)\n"
    )


def _received_event(prompt: str, event: dict) -> dict:
    """Log event - include prompt preview only when debug is opted in."""
    payload = {"phase": "received", "cwd": event.get("cwd"), "prompt_len": len(prompt)}
    if LOG_DEBUG:
        payload["prompt_preview"] = prompt[:200]
    return payload


def _main_impl() -> int:
    raw = sys.stdin.read()
    try:
        event = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as e:
        log({"phase": "parse_error", "error": redact(str(e))[:300]})
        return 0

    prompt: str = event.get("prompt", "")

    # Recursion guard: if the hook is firing from a subprocess we launched
    # (auto_decorate calling `claude --print`), don't re-apply. Cheap to
    # check, blocks infinite loops if the user enables auto mode in a
    # project where `claude --print` re-invokes the same plugin.
    if os.environ.get("PROMPT_DECORATORS_NESTED") == "1":
        return 0

    # Ultra-fast path: no sigils possible AND no config file on disk means
    # nothing could inject a decorator. Skip load_config entirely so the
    # common case (~99% of prompts for unconfigured users) does zero reads
    # beyond stdin + one stat.
    might_have_sigils = _prompt_might_have_sigils(prompt)
    if not might_have_sigils and not CONFIG_PATH.exists():
        return 0

    cfg = load_config()

    # Slower fast path: config exists but no sigils and config isn't active.
    if not might_have_sigils and not _config_is_active(cfg):
        return 0

    log(_received_event(prompt, event))

    normalised, colon_sigils = normalise_sigil(prompt)
    normalised = apply_always_on(normalised, cfg)
    normalised, auto_picks, consume_once = apply_auto(normalised, cfg)

    if not SIGIL_PLUS_RE.search(normalised):
        log({"phase": "no_decorators", "colon_sigils": colon_sigils})
        return 0

    ensure_engine_on_path()
    try:
        from prompt_decorators.dynamic_decorators_module import apply_dynamic_decorators
    except Exception as e:  # noqa: BLE001
        log(
            {
                "phase": "import_error",
                "error": redact(str(e))[:300],
                "tb": redact(traceback.format_exc())[:2000],
            }
        )
        _emit_import_error_to_stderr(e)
        return 0

    _register_user_decorators()

    clean = strip_sigils(normalised)
    try:
        expanded = apply_dynamic_decorators(normalised)
    except Exception as e:  # noqa: BLE001
        log(
            {
                "phase": "apply_error",
                "error": redact(str(e))[:300],
                "tb": redact(traceback.format_exc())[:2000],
            }
        )
        return 0

    expanded_stripped = expanded.strip()
    if expanded_stripped == clean.strip() or expanded_stripped == normalised.strip():
        log({"phase": "no_change_or_unknown", "colon_sigils": colon_sigils})
        return 0

    header = ""
    if auto_picks:
        header = f"[auto-decorate: {' '.join('+' + n for n in auto_picks)}]\n\n"

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": header + expanded,
        }
    }
    log(
        {
            "phase": "emit",
            "expanded_len": len(expanded),
            "colon_sigils": colon_sigils,
            "auto_picks": auto_picks,
            "always_on": cfg.get(CFG_ALWAYS_ON, []),
        }
    )
    sys.stdout.write(json.dumps(output))
    # ONLY clear the one-shot auto arm after a successful emit - a late
    # failure above would otherwise silently consume the user's single
    # armed prompt.
    if consume_once:
        _consume_once_armed(cfg)
    return 0


def main() -> int:
    """Outer fail-open guard. A non-zero exit blocks the user's prompt, so
    any unexpected exception (BrokenPipeError, UnicodeDecodeError on stdin,
    TypeError from malformed config, etc.) must be logged and swallowed.
    """
    try:
        return _main_impl()
    except Exception as e:  # noqa: BLE001
        try:
            log(
                {
                    "phase": "unhandled_error",
                    "error_type": type(e).__name__,
                    "error": redact(str(e))[:500],
                    "tb": redact(traceback.format_exc())[:2000],
                }
            )
        except Exception:  # noqa: BLE001
            pass
        return 0


if __name__ == "__main__":
    sys.exit(main())
