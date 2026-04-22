"""Tests for pd_common's registry-walking and JSON-parsing helpers.

Extracted from test_redact.py so each test module has one concern.
"""

from __future__ import annotations

import importlib

import pytest


@pytest.fixture
def pd_common(monkeypatch, tmp_path):
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(tmp_path / "cfg"))
    monkeypatch.delenv("PROMPT_DECORATORS_USER_REGISTRY", raising=False)
    import pd_common as mod

    importlib.reload(mod)
    return mod


def test_parse_registry_json_rejects_non_dict(tmp_path, pd_common):
    """E1 regression: `[1,2,3]` / `"hi"` / `null` in the registry must not
    crash `/decorate list` or the hook. Extracted from test_redact.py so
    it lives next to the rest of the pd_common tests."""
    user_reg = tmp_path / "reg"
    (user_reg / "foo").mkdir(parents=True)
    (user_reg / "foo" / "list.json").write_text("[1, 2, 3]")
    (user_reg / "foo" / "scalar.json").write_text('"just a string"')
    (user_reg / "foo" / "null.json").write_text("null")
    (user_reg / "foo" / "bad.json").write_text("{not even json")

    for p in (user_reg / "foo").glob("*.json"):
        assert pd_common._parse_registry_json(p, user_reg) is None


def test_walk_registry_skips_non_dict_user_json(tmp_path, monkeypatch):
    """End-to-end: with bad JSON in the user dir, `registry_decorators()`
    still returns the vendored catalogue without crashing."""
    user_reg = tmp_path / "reg"
    user_reg.mkdir()
    (user_reg / "array.json").write_text("[1, 2, 3]")
    (user_reg / "string.json").write_text('"no"')

    monkeypatch.setenv("PROMPT_DECORATORS_USER_REGISTRY", str(user_reg))
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(tmp_path / "cfg"))

    import pd_common as mod

    importlib.reload(mod)
    mod._REGISTRY_CACHE = None
    decorators = mod.registry_decorators()
    assert any(d["name"] == "Concise" for d in decorators)
