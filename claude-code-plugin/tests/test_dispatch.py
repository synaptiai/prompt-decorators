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
