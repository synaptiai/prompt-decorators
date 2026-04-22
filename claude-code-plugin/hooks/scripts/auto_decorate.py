"""Auto-decorate selector.

Two-pass design:
  1. Keyword/category pre-filter narrows the 140+ catalogue to ~20 relevant
     candidates (cheap, deterministic).
  2. A small model (Haiku by default) picks 0-3 decorator names from the
     narrowed list, returning a JSON array.

If the `anthropic` SDK is available and ANTHROPIC_API_KEY is set, we call it
directly (supports prompt caching on the catalogue manifest). Otherwise we
fall back to `claude --print --model <model>` via subprocess so the plugin
works out-of-the-box for users already signed into Claude Code.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

from pd_common import log, registry_decorators  # noqa: E402

DEFAULT_MODEL = "claude-haiku-4-5"
MAX_PICKS = 3
SHORTLIST_SIZE = 20

# Category weight heuristics - tuned so the shortlist leans toward categories
# the user's prompt seems to need. Keywords are lowercase; values are additive.
CATEGORY_HINTS: dict[str, tuple[str, ...]] = {
    "reasoning": (
        "why",
        "how",
        "explain",
        "analyze",
        "analyse",
        "understand",
        "reason",
        "think",
        "compare",
        "evaluate",
        "pros",
        "cons",
        "trade-off",
        "tradeoff",
    ),
    "structure": (
        "list",
        "steps",
        "outline",
        "summary",
        "summarize",
        "format",
        "table",
        "organize",
        "bullet",
        "section",
        "headings",
    ),
    "verification": (
        "verify",
        "check",
        "confirm",
        "accurate",
        "correct",
        "fact",
        "source",
        "cite",
        "evidence",
    ),
    "tone": (
        "concise",
        "brief",
        "detailed",
        "formal",
        "casual",
        "friendly",
        "professional",
    ),
    "minimal": (
        "short",
        "quick",
        "tl;dr",
        "one sentence",
        "one line",
    ),
    "meta": (
        "decorator",
        "prompt-decorators",
    ),
}

SELECTOR_INSTRUCTIONS = (
    "You choose prompt decorators. Given a user prompt and a short list of "
    "available decorators (one per line: `name: description`), respond with a "
    "JSON array of 0 to 3 decorator names that would most improve the response "
    "quality. Prefer diversity - don't pick two decorators from the same "
    "category unless clearly beneficial. Return ONLY the JSON array with no "
    "prose, code fences, or explanation."
)


def _score(prompt_lower: str, category: str) -> int:
    hints = CATEGORY_HINTS.get(category, ())
    return sum(1 for h in hints if h in prompt_lower)


def shortlist(prompt: str, size: int = SHORTLIST_SIZE) -> list[dict]:
    """Narrow the catalogue to `size` candidates most relevant to the prompt."""
    all_decorators = registry_decorators()
    prompt_lower = prompt.lower()

    category_scores = {c: _score(prompt_lower, c) for c in CATEGORY_HINTS}
    # Ensure every category gets at least one slot when scores are zero.
    if sum(category_scores.values()) == 0:
        category_scores = {c: 1 for c in CATEGORY_HINTS}

    total = sum(category_scores.values()) or 1
    quotas: dict[str, int] = {
        c: max(1, int(round(size * s / total))) for c, s in category_scores.items()
    }

    by_cat: dict[str, list[dict]] = {}
    for d in all_decorators:
        by_cat.setdefault(d["category"], []).append(d)

    picked: list[dict] = []
    for cat, quota in quotas.items():
        for d in by_cat.get(cat, [])[:quota]:
            picked.append(d)

    if len(picked) < size:
        seen = {d["name"] for d in picked}
        for d in all_decorators:
            if d["name"] not in seen:
                picked.append(d)
                seen.add(d["name"])
                if len(picked) >= size:
                    break

    return picked[:size]


def _manifest(candidates: Iterable[dict]) -> str:
    lines = [f"- {d['name']}: {d['description']}" for d in candidates]
    return "\n".join(lines)


def _call_anthropic_sdk(
    prompt: str, candidates: list[dict], model: str
) -> str | None:
    try:
        import anthropic  # type: ignore
    except ImportError:
        return None
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=model,
        max_tokens=200,
        system=[
            {
                "type": "text",
                "text": SELECTOR_INSTRUCTIONS
                + "\n\nAvailable decorators:\n"
                + _manifest(candidates),
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": f"User prompt:\n{prompt}"}],
    )
    # Messages.create returns content as a list of content blocks.
    parts: list[str] = []
    for block in resp.content:
        text = getattr(block, "text", None)
        if text:
            parts.append(text)
    return "".join(parts).strip() or None


def _call_claude_cli(prompt: str, candidates: list[dict], model: str) -> str | None:
    selector_input = (
        f"{SELECTOR_INSTRUCTIONS}\n\n"
        f"Available decorators:\n{_manifest(candidates)}\n\n"
        f"User prompt:\n{prompt}\n\n"
        f"Answer (JSON array of names):"
    )
    try:
        result = subprocess.run(
            ["claude", "--print", "--model", model, selector_input],
            capture_output=True,
            text=True,
            timeout=30,
            cwd="/tmp",
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        log({"phase": "auto_cli_error", "error": str(e)})
        return None
    return result.stdout.strip() or None


def _parse_names(raw: str, valid_names: set[str]) -> list[str]:
    match = re.search(r"\[[^\]]*\]", raw)
    if not match:
        return []
    try:
        arr = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
    out: list[str] = []
    for item in arr:
        if isinstance(item, str) and item in valid_names:
            out.append(item)
        if len(out) >= MAX_PICKS:
            break
    return out


def select_decorators(prompt: str, model: str | None = None) -> list[str]:
    model = model or DEFAULT_MODEL
    candidates = shortlist(prompt)
    valid_names = {d["name"] for d in candidates}
    log({"phase": "auto_shortlist", "names": sorted(valid_names)})

    raw = _call_anthropic_sdk(prompt, candidates, model)
    if raw is None:
        raw = _call_claude_cli(prompt, candidates, model)
    if not raw:
        return []
    picks = _parse_names(raw, valid_names)
    log({"phase": "auto_picks", "raw_preview": raw[:200], "picks": picks})
    return picks


if __name__ == "__main__":
    user_prompt = sys.stdin.read() if not sys.stdin.isatty() else " ".join(sys.argv[1:])
    print(json.dumps(select_decorators(user_prompt)))
