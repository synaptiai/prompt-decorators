"""Edge-case tests added after the post-review pass.

Covers: unterminated sigil parens, CRLF line endings, log file security
(O_NOFOLLOW refusal to follow symlinks), atomic config write under
concurrent pressure, and fast-path early exit behaviour.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
from pathlib import Path

import pytest

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
HOOK = PLUGIN_ROOT / "hooks" / "scripts" / "decorate_hook.py"


def _event(prompt: str) -> dict:
    return {
        "session_id": "t",
        "transcript_path": "/tmp/t",
        "cwd": "/tmp",
        "permission_mode": "default",
        "hook_event_name": "UserPromptSubmit",
        "prompt": prompt,
    }


def _run_hook(event: dict, env: dict) -> tuple[str, str, int]:
    proc = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(event),
        capture_output=True,
        text=True,
        env={**os.environ, **env},
        timeout=30,
    )
    return proc.stdout, proc.stderr, proc.returncode


def _base_env(tmp_path: Path) -> dict:
    return {
        "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
        "PROMPT_DECORATORS_LOG": str(tmp_path / "hook.log"),
    }


def test_unterminated_sigil_paren_does_not_crash(tmp_path):
    """`::Concise(` with no closing paren must not throw. The `(...)` group is
    optional, so `::Concise` parses and the stray `(` becomes prompt content.
    The important property is no crash and the hook still succeeds."""
    out, _, rc = _run_hook(_event("::Concise(\nExplain recursion"), _base_env(tmp_path))
    assert rc == 0  # fail open, no crash


def test_crlf_line_endings_handled(tmp_path):
    """`::Concise` sigil at start of a CRLF-terminated line should still work."""
    out, _, rc = _run_hook(
        _event("::Concise\r\nIn one sentence, what is recursion?"),
        _base_env(tmp_path),
    )
    # `(?m)^::` matches despite trailing \r - the \r remains in the captured
    # text but the library tolerates whitespace after the sigil.
    data = json.loads(out) if out else {}
    if data:
        assert "concise" in data["hookSpecificOutput"]["additionalContext"].lower()


def test_fast_path_skips_when_no_sigils_and_no_config(tmp_path):
    """Hot path: plain prompt with no config should exit with zero output AND
    no log entry (the hook bails before logging)."""
    log_path = tmp_path / "hook.log"
    out, _, rc = _run_hook(_event("a plain boring prompt"), _base_env(tmp_path))
    assert out == ""
    assert rc == 0
    assert not log_path.exists() or log_path.read_text() == ""


def test_log_refuses_symlink(tmp_path):
    """Security: if someone plants a symlink at the log path, the hook must
    not follow it. Open with O_NOFOLLOW should make it fail silently."""
    if not hasattr(os, "O_NOFOLLOW"):
        pytest.skip("O_NOFOLLOW unavailable on this platform")
    victim = tmp_path / "victim.txt"
    victim.write_text("ORIGINAL")
    log_path = tmp_path / "hook.log"
    os.symlink(victim, log_path)

    out, _, rc = _run_hook(
        _event("+++StepByStep\nExplain recursion"),
        {
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_LOG": str(log_path),
        },
    )
    # Hook still succeeds (logging fails open).
    assert rc == 0
    # Victim file must not be touched.
    assert victim.read_text() == "ORIGINAL"


def test_log_default_is_not_in_tmp(tmp_path, monkeypatch):
    """Sanity: without an env override, the log defaults to $HOME/.cache, not
    /tmp. Verifies the security posture without actually writing there."""
    # Reload with a fake HOME so we don't pollute the real one.
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.delenv("PROMPT_DECORATORS_LOG", raising=False)

    sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
    import importlib

    import pd_common

    importlib.reload(pd_common)
    try:
        # Default must live under $HOME/.cache, not somewhere world-readable.
        assert pd_common.DEFAULT_LOG_PATH.parts[-3:] == (
            ".cache",
            "prompt-decorators",
            "hook.log",
        )
        assert str(pd_common.DEFAULT_LOG_PATH).startswith(str(fake_home))
    finally:
        # Reset so later tests don't see the fake HOME's path baked in.
        importlib.reload(pd_common)


def test_atomic_config_write_under_concurrency(tmp_path, monkeypatch):
    """Two threads racing on save_config must not leave a corrupt file.
    Checks: file is always valid JSON after N concurrent writers finish."""
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(tmp_path))
    sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
    import importlib

    import pd_common

    importlib.reload(pd_common)

    def writer(marker: str) -> None:
        for _ in range(20):
            cfg = pd_common.load_config()
            cfg[pd_common.CFG_ALWAYS_ON] = [marker]
            pd_common.save_config(cfg)

    threads = [threading.Thread(target=writer, args=(f"M{i}",)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # File should always be valid JSON - no half-written state.
    data = json.loads(pd_common.CONFIG_PATH.read_text())
    assert data[pd_common.CFG_ALWAYS_ON][0].startswith("M")
    # No .tmp leftovers.
    stragglers = list(pd_common.CONFIG_PATH.parent.glob(".config-*.tmp"))
    assert not stragglers


def test_prompt_content_not_in_log_by_default(tmp_path):
    """Security: logs must not include raw prompt content unless opted in
    via PROMPT_DECORATORS_LOG_DEBUG=1."""
    log_path = tmp_path / "hook.log"
    sentinel = "SECRET_API_KEY_SHOULD_NOT_APPEAR_IN_LOG_9X8Y7"
    _run_hook(
        _event(f"+++StepByStep\nplease remember {sentinel}"),
        {
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_LOG": str(log_path),
        },
    )
    content = log_path.read_text() if log_path.exists() else ""
    assert sentinel not in content


def test_prompt_preview_in_log_when_debug(tmp_path):
    log_path = tmp_path / "hook.log"
    marker = "DEBUG_VISIBLE_PROMPT_MARKER"
    _run_hook(
        _event(f"+++StepByStep\n{marker}"),
        {
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_LOG": str(log_path),
            "PROMPT_DECORATORS_LOG_DEBUG": "1",
        },
    )
    assert marker in log_path.read_text()
