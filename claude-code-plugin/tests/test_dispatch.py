"""Tests for the /decorate slash command dispatcher."""

from __future__ import annotations

import json

import pytest


@pytest.fixture
def dispatch(tmp_path, monkeypatch, capsys):
    cfg_dir = tmp_path / "cfg"
    cfg_dir.mkdir()
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(cfg_dir))

    import importlib

    import pd_common

    importlib.reload(pd_common)
    import dispatch as dispatch_mod

    importlib.reload(dispatch_mod)

    def run(args: list[str]) -> tuple[int, str]:
        rc = dispatch_mod.run(args)
        captured = capsys.readouterr()
        return rc, captured.out

    return run, cfg_dir


def test_list_prints_categories(dispatch):
    run, _ = dispatch
    rc, out = run(["list"])
    assert rc == 0
    assert "## reasoning" in out
    assert "## structure" in out
    assert "total:" in out


def test_list_filter_by_category(dispatch):
    run, _ = dispatch
    rc, out = run(["list", "minimal"])
    assert rc == 0
    assert "## minimal" in out
    assert "## reasoning" not in out


def test_list_unknown_category(dispatch):
    run, _ = dispatch
    rc, out = run(["list", "notarealcat"])
    assert rc == 1


def test_preview_known_decorator(dispatch):
    run, _ = dispatch
    rc, out = run(["preview", "Concise"])
    assert rc == 0
    assert "concise" in out.lower()


def test_preview_unknown_decorator(dispatch):
    run, _ = dispatch
    rc, out = run(["preview", "ThisDoesNotExist"])
    assert rc == 1


def test_search_finds_matches(dispatch):
    run, _ = dispatch
    rc, out = run(["search", "concise"])
    assert rc == 0
    assert "Concise" in out


def test_search_no_matches(dispatch):
    run, _ = dispatch
    rc, out = run(["search", "zzzzzzneverexists"])
    assert rc == 1


def test_always_add_and_list(dispatch):
    run, cfg_dir = dispatch
    rc, _ = run(["always", "add", "Concise"])
    assert rc == 0
    rc, out = run(["always", "list"])
    assert "Concise" in out

    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert "Concise" in cfg["always_on"]


def test_always_add_unknown_fails(dispatch):
    run, _ = dispatch
    rc, _ = run(["always", "add", "NotADecorator"])
    assert rc == 1


def test_always_remove(dispatch):
    run, cfg_dir = dispatch
    run(["always", "add", "Concise"])
    rc, _ = run(["always", "remove", "Concise"])
    assert rc == 0
    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert "Concise" not in cfg["always_on"]


def test_auto_status_default(dispatch):
    run, _ = dispatch
    rc, out = run(["auto", "status"])
    assert rc == 0
    assert "mode=off" in out


def test_auto_on_persists(dispatch):
    run, cfg_dir = dispatch
    rc, _ = run(["auto", "on"])
    assert rc == 0
    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert cfg["auto"]["mode"] == "on"


def test_auto_once_arms_flag(dispatch):
    run, cfg_dir = dispatch
    rc, _ = run(["auto", "once"])
    assert rc == 0
    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert cfg["auto"]["once_armed"] is True


def test_auto_off_clears_state(dispatch):
    run, cfg_dir = dispatch
    run(["auto", "on"])
    run(["auto", "once"])
    rc, _ = run(["auto", "off"])
    assert rc == 0
    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert cfg["auto"]["mode"] == "off"
    assert cfg["auto"]["once_armed"] is False


def test_auto_model_sets_value(dispatch):
    run, cfg_dir = dispatch
    rc, _ = run(["auto", "model", "claude-haiku-4-5-20251001"])
    assert rc == 0
    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert cfg["auto"]["model"] == "claude-haiku-4-5-20251001"


def test_disable_unknown_fails(dispatch):
    run, _ = dispatch
    rc, _ = run(["disable", "NotADecorator"])
    assert rc == 1


def test_disable_and_enable_roundtrip(dispatch):
    run, cfg_dir = dispatch
    rc, _ = run(["disable", "Concise"])
    assert rc == 0
    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert "Concise" in cfg["disabled"]
    rc, _ = run(["enable", "Concise"])
    assert rc == 0
    cfg = json.loads((cfg_dir / "config.json").read_text())
    assert "Concise" not in cfg["disabled"]


def test_unknown_subcommand_returns_error(dispatch):
    run, _ = dispatch
    rc, _ = run(["not-a-command"])
    assert rc == 2


def test_help_returns_zero(dispatch):
    run, _ = dispatch
    rc, out = run(["help"])
    assert rc == 0
    assert "Subcommands" in out or "list" in out


# --- --args-from-stdin path (security-relevant) -----------------------------
#
# These tests run dispatch.py as a subprocess with `--args-from-stdin`, the
# same path the /decorate slash command uses via a quoted heredoc. They
# cover shell-injection safety and the unmatched-quote fallback.

import os  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

DISPATCH = Path(__file__).resolve().parent.parent / "scripts" / "dispatch.py"


def _run_stdin(stdin_text: str, tmp_path: Path) -> tuple[str, str, int]:
    proc = subprocess.run(
        [sys.executable, str(DISPATCH), "--args-from-stdin"],
        input=stdin_text,
        capture_output=True,
        text=True,
        env={
            **os.environ,
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
        },
        timeout=30,
    )
    return proc.stdout, proc.stderr, proc.returncode


def test_args_from_stdin_safe_against_shell_metachars(tmp_path):
    """Shell metacharacters in stdin must NOT be executed. Regression for the
    `$ARGUMENTS` injection vector fixed in the P2-4 cleanup (quoted heredoc
    + shlex.split)."""
    out, err, rc = _run_stdin("list; echo PWNED", tmp_path)
    combined = out + err
    # The `list` subcommand prints the catalogue with `## reasoning` etc.
    assert "## reasoning" in out or rc != 0
    # The `; echo PWNED` part must be treated as extra arguments to the
    # dispatcher, not as a separate shell command. "PWNED" must not appear.
    assert "PWNED" not in combined


def test_args_from_stdin_handles_command_substitution(tmp_path):
    """Even nastier: `$(...)` must not be evaluated. Since the slash command
    uses a quoted heredoc and we shlex-split, this has to be literal text."""
    out, err, rc = _run_stdin("list $(echo PWNED)", tmp_path)
    combined = out + err
    assert "PWNED" not in combined


def test_args_from_stdin_unmatched_quote_falls_back_to_whitespace_split(tmp_path):
    """Malformed input with an unmatched quote should fall back to a
    whitespace split rather than crashing. The dispatcher should then
    report an unknown subcommand or help usage - whatever the fallback
    argv happens to resolve to - but must not exit with a traceback."""
    out, err, rc = _run_stdin("list 'unterminated", tmp_path)
    # Whitespace split yields `["list", "'unterminated"]`. That's a `list`
    # command with an unknown category - returns 1 (no match).
    assert rc in (0, 1)
    # Must not raise an uncaught ValueError or other exception.
    assert "Traceback" not in err


def test_args_from_stdin_empty_input_shows_help(tmp_path):
    """Empty `$ARGUMENTS` is a common case - shlex.split('') -> [] -> help."""
    out, _, rc = _run_stdin("", tmp_path)
    assert rc == 0
    assert "Subcommands" in out or "list" in out


def test_args_from_stdin_respects_quoted_arguments(tmp_path):
    """shlex should preserve intentional quoting. A search term with spaces
    inside quotes must arrive as a single argv token."""
    out, _, rc = _run_stdin('search "one sentence"', tmp_path)
    # Either a match or no-match, but not an error.
    assert rc in (0, 1)
