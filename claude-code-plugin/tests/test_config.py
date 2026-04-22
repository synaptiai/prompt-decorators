"""Tests for pd_common config helpers."""

from __future__ import annotations

import json

import pytest


@pytest.fixture
def pd_common_mod(monkeypatch, tmp_path):
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(tmp_path / "cfg"))
    import importlib

    import pd_common

    importlib.reload(pd_common)
    return pd_common, tmp_path / "cfg"


def test_load_config_defaults_when_missing(pd_common_mod):
    pd_common, cfg_dir = pd_common_mod
    cfg = pd_common.load_config()
    assert cfg["auto"]["mode"] == "off"
    assert cfg["always_on"] == []


def test_save_then_load_roundtrip(pd_common_mod):
    pd_common, cfg_dir = pd_common_mod
    cfg = pd_common.load_config()
    cfg["always_on"].append("Concise")
    cfg["auto"]["mode"] = "on"
    pd_common.save_config(cfg)
    re_read = pd_common.load_config()
    assert re_read["always_on"] == ["Concise"]
    assert re_read["auto"]["mode"] == "on"


def test_load_config_ignores_unknown_keys(pd_common_mod):
    pd_common, cfg_dir = pd_common_mod
    cfg_dir.mkdir(parents=True, exist_ok=True)
    (cfg_dir / "config.json").write_text(
        json.dumps(
            {
                "always_on": ["StepByStep"],
                "bogus_top_level": 42,
                "auto": {"mode": "on"},
            }
        )
    )
    cfg = pd_common.load_config()
    assert cfg["always_on"] == ["StepByStep"]
    assert cfg["auto"]["mode"] == "on"
    # Auto defaults not provided should still be present.
    assert "once_armed" in cfg["auto"]
    assert "bogus_top_level" not in cfg


def test_load_config_corrupt_file_returns_default(pd_common_mod):
    pd_common, cfg_dir = pd_common_mod
    cfg_dir.mkdir(parents=True, exist_ok=True)
    (cfg_dir / "config.json").write_text("{ not valid json")
    cfg = pd_common.load_config()
    assert cfg == pd_common.DEFAULT_CONFIG or cfg["auto"]["mode"] == "off"


def test_registry_loads_decorators(pd_common_mod):
    pd_common, _ = pd_common_mod
    decorators = pd_common.registry_decorators()
    assert len(decorators) > 100
    assert any(d["name"] == "Concise" for d in decorators)
    assert all({"name", "description", "category"} <= set(d) for d in decorators)
