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
    register_user_decorators,
    save_config,
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

    # Defensive: stdin JSON could be a list, scalar, or null - all valid
    # JSON but not what UserPromptSubmit is specified to send. Treating
    # them as dicts would AttributeError on the first `.get(...)` below.
    if not isinstance(event, dict):
        log({"phase": "event_not_dict", "type": type(event).__name__})
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

    register_user_decorators()

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

    We extend `Exception` with `SystemExit` specifically because a bug or
    library call chain inside the engine could raise `SystemExit` (e.g.
    argparse-style exits in an imported module), which doesn't inherit
    from `Exception` and would otherwise bypass our fail-open guarantee
    and block the user's prompt with a non-zero exit. `KeyboardInterrupt`
    is deliberately NOT caught so the user can Ctrl-C out of a hung hook.
    """
    try:
        return _main_impl()
    except (Exception, SystemExit) as e:  # noqa: BLE001
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
