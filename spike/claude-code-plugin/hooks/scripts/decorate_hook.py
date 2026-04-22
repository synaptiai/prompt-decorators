#!/usr/bin/env python3
"""UserPromptSubmit hook: detect decorator sigils, expand via prompt-decorators engine.

Reads JSON event on stdin, writes hook output JSON on stdout.
Event shape (Claude Code UserPromptSubmit):
  { "session_id": str, "transcript_path": str, "cwd": str,
    "permission_mode": str, "hook_event_name": "UserPromptSubmit",
    "prompt": str }

Output shape (on success with decorators detected):
  { "hookSpecificOutput": { "hookEventName": "UserPromptSubmit",
                             "additionalContext": <expanded instructions> } }

Syntax support:
  - Native `+++Name(param=val)` (the library's built-in regex)
  - Alias `::Name(param=val)` is normalised to `+++Name(...)` before parsing
    (lets us evaluate the `::` sigil without modifying the upstream engine)

Debug log:
  - Writes a JSONL trace to $PROMPT_DECORATORS_LOG (default: /tmp/pd_hook.log)
    so the spike can inspect what the hook received and emitted.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import traceback
from pathlib import Path

LOG_PATH = os.environ.get("PROMPT_DECORATORS_LOG", "/tmp/pd_hook.log")

# Make the repo package importable when run from the spike directory
REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def log(event: dict) -> None:
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": time.time(), **event}) + "\n")
    except Exception:
        pass


def normalise_sigil(prompt: str) -> tuple[str, list[str]]:
    """Rewrite `::Name(...)` -> `+++Name(...)` so the library parser picks it up.

    Returns (rewritten_prompt, list_of_sigils_detected).
    Only matches `::` at start-of-line to minimise collision with code snippets
    (Rust paths, C++ scopes).
    """
    detected: list[str] = []
    pattern = re.compile(r"(?m)^::([A-Za-z][A-Za-z0-9]*(?:\([^)]*\))?)")

    def _sub(m: re.Match) -> str:
        detected.append("::" + m.group(1))
        return "+++" + m.group(1)

    return pattern.sub(_sub, prompt), detected


def has_decorators(prompt: str) -> bool:
    return bool(re.search(r"(?m)^\+\+\+[A-Za-z]", prompt))


def main() -> int:
    raw = sys.stdin.read()
    try:
        event = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as e:
        log({"phase": "parse_error", "error": str(e), "raw_prefix": raw[:200]})
        return 0  # fail open

    prompt: str = event.get("prompt", "")
    log({"phase": "received", "prompt": prompt, "cwd": event.get("cwd")})

    normalised, colon_sigils = normalise_sigil(prompt)
    if not has_decorators(normalised):
        log({"phase": "no_decorators", "colon_sigils": colon_sigils})
        return 0  # pass through unchanged

    try:
        from prompt_decorators.dynamic_decorators_module import apply_dynamic_decorators
    except Exception as e:
        log({"phase": "import_error", "error": str(e), "tb": traceback.format_exc()})
        return 0  # fail open

    # Compute the clean prompt (sigils stripped) so we can detect whether the
    # engine actually injected any instruction text. If expansion just produces
    # the clean prompt, all decorators were unknown — pass through.
    clean_prompt = re.sub(
        r"(?m)^\+\+\+[A-Za-z][A-Za-z0-9]*(?:\([^)]*\))?\s*\n?", "", normalised
    )

    try:
        expanded = apply_dynamic_decorators(normalised)
    except Exception as e:
        log({"phase": "apply_error", "error": str(e), "tb": traceback.format_exc()})
        return 0  # fail open

    if (
        expanded.strip() == clean_prompt.strip()
        or expanded.strip() == normalised.strip()
    ):
        log({"phase": "no_change_or_unknown"})
        return 0

    # The engine returns `<instructions>\n\n<clean prompt>`. We feed everything
    # as additionalContext so the user's literal prompt is preserved in history,
    # while the model also sees the expanded instructions.
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": expanded,
        }
    }
    log({"phase": "emit", "output": output, "expanded_len": len(expanded)})
    sys.stdout.write(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
