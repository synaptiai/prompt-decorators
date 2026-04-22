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
import re
import sys
import traceback
from pathlib import Path

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
    LOG_DEBUG,
    MODE_OFF,
    MODE_ON,
    bare_name,
    ensure_engine_on_path,
    load_config,
    log,
    save_config,
    user_registry_dir,
)

# Sigil grammar: name, optional :vX[.Y[.Z]] version, optional (...) params.
_SIGIL_BODY = (
    r"[A-Za-z][A-Za-z0-9]*" r"(?::v[0-9]+(?:\.[0-9]+(?:\.[0-9]+)?)?)?" r"(?:\([^)]*\))?"
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


def apply_auto(prompt: str, cfg: dict) -> tuple[str, list[str]]:
    """If auto mode is armed, run the selector and prepend its picks."""
    auto_cfg = cfg.get(CFG_AUTO, {}) or {}
    mode = auto_cfg.get(AUTO_MODE, MODE_OFF)
    once = auto_cfg.get(AUTO_ONCE, False)
    if mode != MODE_ON and not once:
        return prompt, []

    try:
        from auto_decorate import select_decorators  # type: ignore

        disabled = {bare_name(d) for d in (cfg.get(CFG_DISABLED, []) or [])}
        names = [
            n
            for n in select_decorators(prompt, model=auto_cfg.get(AUTO_MODEL))
            if n not in disabled
        ]
    except Exception as e:  # noqa: BLE001
        log({"phase": "auto_error", "error": str(e), "tb": traceback.format_exc()})
        names = []

    if once:
        cfg[CFG_AUTO][AUTO_ONCE] = False
        try:
            save_config(cfg)
        except Exception as e:  # noqa: BLE001
            # save_config can raise OSError (disk), TypeError (unserialisable
            # value sneaked in), or anything else - swallow and log. Losing a
            # once_armed clear is preferable to blocking the user's prompt.
            log(
                {
                    "phase": "auto_once_save_error",
                    "error_type": type(e).__name__,
                    "error": str(e)[:200],
                }
            )

    if not names:
        return prompt, []
    prefix = "\n".join(f"+++{n}" for n in names)
    return f"{prefix}\n{prompt}", names


def _register_user_decorators() -> None:
    """Inject user-local decorators into the engine's registry.

    User decorators live under `$PROMPT_DECORATORS_USER_REGISTRY` (or
    `~/.config/prompt-decorators/extensions/` by default) and survive
    `vendor/` re-syncs. Without this step, user decorators would appear in
    `/decorate list` but the hook couldn't actually expand them.
    """
    user_dir = user_registry_dir()
    if user_dir is None or not user_dir.exists():
        return
    try:
        from prompt_decorators.core.dynamic_decorator import DynamicDecorator
    except Exception as e:  # noqa: BLE001
        log({"phase": "user_registry_import_error", "error": str(e)})
        return
    DynamicDecorator.load_registry()
    loaded = 0
    for path in user_dir.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
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
    if loaded:
        log({"phase": "user_registry_loaded", "count": loaded})


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
        log({"phase": "parse_error", "error": str(e)})
        return 0

    prompt: str = event.get("prompt", "")
    cfg = load_config()

    # Fast path: skip all work when the prompt can't possibly contain sigils
    # AND no config option would inject decorators. Keeps the hot path cheap.
    if not _prompt_might_have_sigils(prompt) and not _config_is_active(cfg):
        return 0

    log(_received_event(prompt, event))

    normalised, colon_sigils = normalise_sigil(prompt)
    normalised = apply_always_on(normalised, cfg)
    normalised, auto_picks = apply_auto(normalised, cfg)

    if not SIGIL_PLUS_RE.search(normalised):
        log({"phase": "no_decorators", "colon_sigils": colon_sigils})
        return 0

    ensure_engine_on_path()
    try:
        from prompt_decorators.dynamic_decorators_module import apply_dynamic_decorators
    except Exception as e:  # noqa: BLE001
        log({"phase": "import_error", "error": str(e), "tb": traceback.format_exc()})
        _emit_import_error_to_stderr(e)
        return 0

    _register_user_decorators()

    clean = strip_sigils(normalised)
    try:
        expanded = apply_dynamic_decorators(normalised)
    except Exception as e:  # noqa: BLE001
        log({"phase": "apply_error", "error": str(e), "tb": traceback.format_exc()})
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
                    "error": str(e)[:500],
                    "tb": traceback.format_exc()[:2000],
                }
            )
        except Exception:  # noqa: BLE001
            pass
        return 0


if __name__ == "__main__":
    sys.exit(main())
