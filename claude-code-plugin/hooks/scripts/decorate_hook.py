#!/usr/bin/env python3
"""UserPromptSubmit hook for prompt-decorators.

- Detects `::Name(params)` and `+++Name(params)` decorator sigils on their own
  line at the start of a prompt line.
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
    ensure_engine_on_path,
    load_config,
    log,
    save_config,
)

SIGIL_COLON_RE = re.compile(
    r"(?m)^::([A-Za-z][A-Za-z0-9]*(?::v[0-9]+(?:\.[0-9]+(?:\.[0-9]+)?)?)?(?:\([^)]*\))?)"
)
SIGIL_PLUS_RE = re.compile(
    r"(?m)^\+\+\+([A-Za-z][A-Za-z0-9]*(?::v[0-9]+(?:\.[0-9]+(?:\.[0-9]+)?)?)?(?:\([^)]*\))?)"
)


def normalise_sigil(prompt: str) -> tuple[str, list[str]]:
    """Rewrite `::Name(...)` -> `+++Name(...)` at start-of-line only.

    Returns (rewritten_prompt, list_of_detected_colon_sigils).
    """
    detected: list[str] = []

    def _sub(m: re.Match) -> str:
        detected.append("::" + m.group(1))
        return "+++" + m.group(1)

    return SIGIL_COLON_RE.sub(_sub, prompt), detected


def strip_sigils(prompt: str) -> str:
    """Remove `+++Name(...)` lines entirely (including trailing newline)."""
    return re.sub(
        r"(?m)^\+\+\+[A-Za-z][A-Za-z0-9]*(?::v[0-9]+(?:\.[0-9]+(?:\.[0-9]+)?)?)?(?:\([^)]*\))?\s*\n?",
        "",
        prompt,
    )


def apply_always_on(prompt: str, cfg: dict) -> str:
    always = cfg.get("always_on", []) or []
    if not always:
        return prompt
    # Only prepend decorators not already present in the user's prompt.
    existing = set(m.group(1).split("(")[0] for m in SIGIL_PLUS_RE.finditer(prompt))
    to_add = [name for name in always if name.split("(")[0] not in existing]
    if not to_add:
        return prompt
    return "\n".join(f"+++{d}" for d in to_add) + "\n" + prompt


def apply_auto(prompt: str, cfg: dict) -> tuple[str, list[str]]:
    """If auto mode is armed, run the selector and prepend its picks.

    Returns (new_prompt, selected_names). Empty selected_names means auto was
    skipped or returned nothing.
    """
    auto_cfg = cfg.get("auto", {}) or {}
    mode = auto_cfg.get("mode", "off")
    once = auto_cfg.get("once_armed", False)
    if mode != "on" and not once:
        return prompt, []

    try:
        from auto_decorate import select_decorators  # type: ignore

        names = select_decorators(prompt, model=auto_cfg.get("model"))
    except Exception as e:  # noqa: BLE001
        log({"phase": "auto_error", "error": str(e), "tb": traceback.format_exc()})
        names = []

    if once:
        # Consume the one-shot flag regardless of selection outcome.
        cfg["auto"]["once_armed"] = False
        try:
            save_config(cfg)
        except OSError as e:
            log({"phase": "auto_once_save_error", "error": str(e)})

    if not names:
        return prompt, []
    prefix = "\n".join(f"+++{n}" for n in names)
    return f"{prefix}\n{prompt}", names


def main() -> int:
    raw = sys.stdin.read()
    try:
        event = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as e:
        log({"phase": "parse_error", "error": str(e), "raw_prefix": raw[:200]})
        return 0

    prompt: str = event.get("prompt", "")
    log({"phase": "received", "prompt_preview": prompt[:200], "cwd": event.get("cwd")})

    cfg = load_config()

    # Normalise `::` to `+++` so the library's parser picks it up.
    normalised, colon_sigils = normalise_sigil(prompt)

    # Layer in always-on decorators from config.
    normalised = apply_always_on(normalised, cfg)

    # Run auto-select if armed (adds its picks as `+++Name` lines).
    normalised, auto_picks = apply_auto(normalised, cfg)

    # No decorators at all? Pass through unchanged.
    if not SIGIL_PLUS_RE.search(normalised):
        log({"phase": "no_decorators", "colon_sigils": colon_sigils})
        return 0

    ensure_engine_on_path()
    try:
        from prompt_decorators.dynamic_decorators_module import (
            apply_dynamic_decorators,
        )
    except Exception as e:  # noqa: BLE001
        log({"phase": "import_error", "error": str(e), "tb": traceback.format_exc()})
        return 0

    clean = strip_sigils(normalised)
    try:
        expanded = apply_dynamic_decorators(normalised)
    except Exception as e:  # noqa: BLE001
        log({"phase": "apply_error", "error": str(e), "tb": traceback.format_exc()})
        return 0

    if expanded.strip() == clean.strip() or expanded.strip() == normalised.strip():
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
            "always_on": cfg.get("always_on", []),
        }
    )
    sys.stdout.write(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
