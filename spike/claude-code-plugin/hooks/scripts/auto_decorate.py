#!/usr/bin/env python3
"""Auto-decorate prototype: pick decorators for a user prompt via a small model.

Shape of the flow (works the same with Anthropic SDK direct calls):

    1. Read the user prompt + a compressed catalog manifest.
    2. Ask a fast model (Haiku) to return 0-3 decorator names best suited.
    3. Prepend those as `+++Name` lines so the main decorate hook can expand them.

For the spike we shell out to `claude --print --model haiku`. In production
this would be a direct Anthropic SDK call with prompt caching on the manifest.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def build_manifest(max_items: int = 40) -> str:
    """Cheap catalog summary: name + one-line description. Cache-friendly."""
    from prompt_decorators.core.dynamic_decorator import DynamicDecorator

    DynamicDecorator.load_registry()
    decorators = DynamicDecorator.get_available_decorators()
    lines = []
    for d in decorators[:max_items]:
        name = getattr(d, "name", None) or d.get("name")
        desc = getattr(d, "description", None) or d.get("description", "")
        desc = (desc or "").splitlines()[0][:120]
        lines.append(f"- {name}: {desc}")
    return "\n".join(lines)


SELECTOR_PROMPT = """You are a decorator selector. Given a user prompt and a catalog
of prompt decorators, return a JSON array of 0-3 decorator names that would most
improve the response. Return ONLY the JSON array, no prose.

Catalog:
{manifest}

User prompt:
{user_prompt}

Answer (JSON array of names, e.g. ["Concise","StepByStep"]):"""


def select_decorators(user_prompt: str) -> list[str]:
    manifest = build_manifest()
    selector_input = SELECTOR_PROMPT.format(manifest=manifest, user_prompt=user_prompt)
    # Stand-in for a direct Haiku API call. Cost/latency profile in production
    # will be much better since we can cache the manifest prefix.
    result = subprocess.run(
        ["claude", "--print", "--model", "haiku", selector_input],
        capture_output=True,
        text=True,
        timeout=30,
    )
    raw = result.stdout.strip()
    match = re.search(r"\[[^\]]*\]", raw)
    if not match:
        return []
    try:
        names = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
    return [n for n in names if isinstance(n, str)][:3]


def decorate(user_prompt: str) -> str:
    names = select_decorators(user_prompt)
    if not names:
        return user_prompt
    prefix = "\n".join(f"+++{n}" for n in names)
    return f"{prefix}\n{user_prompt}"


if __name__ == "__main__":
    prompt = sys.stdin.read() if not sys.stdin.isatty() else " ".join(sys.argv[1:])
    sys.stdout.write(decorate(prompt))
