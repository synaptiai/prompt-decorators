"""Common pytest setup - add plugin script dirs to sys.path and isolate config."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
HOOK_SCRIPT = PLUGIN_ROOT / "hooks" / "scripts" / "decorate_hook.py"

sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
sys.path.insert(0, str(PLUGIN_ROOT / "hooks" / "scripts"))


def make_event(prompt: str) -> dict:
    """Build a synthetic UserPromptSubmit event payload."""
    return {
        "session_id": "test",
        "transcript_path": "/tmp/t",
        "cwd": "/tmp",
        "permission_mode": "default",
        "hook_event_name": "UserPromptSubmit",
        "prompt": prompt,
    }


def run_hook_subprocess(
    event: dict, env: dict | None = None, stdin: str | None = None
) -> tuple[str, str, int]:
    """Run the hook script as a subprocess. Returns (stdout, stderr, rc).

    Centralised in conftest so test modules share one definition. `stdin`
    overrides `json.dumps(event)` when provided - useful for the malformed-
    JSON fail-open test.
    """
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    payload = stdin if stdin is not None else json.dumps(event)
    proc = subprocess.run(
        [sys.executable, str(HOOK_SCRIPT)],
        input=payload,
        capture_output=True,
        text=True,
        env=merged_env,
        timeout=30,
    )
    return proc.stdout, proc.stderr, proc.returncode


@pytest.fixture(autouse=True)
def _isolated_config(tmp_path, monkeypatch):
    """Redirect config + log to a temp dir for every test."""
    cfg_dir = tmp_path / "pd_cfg"
    cfg_dir.mkdir()
    log_path = tmp_path / "pd.log"
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("PROMPT_DECORATORS_LOG", str(log_path))

    # Force pd_common to pick up the new env - it caches module-level paths.
    for mod in ("pd_common", "dispatch", "decorate_hook", "auto_decorate"):
        sys.modules.pop(mod, None)
    yield
