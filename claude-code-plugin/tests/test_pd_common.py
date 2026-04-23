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


# -----------------------------------------------------------------------------
# Engine numeric-parameter parsing (cycle-6 vendor patch)
# -----------------------------------------------------------------------------


@pytest.mark.parametrize(
    "param_text, expected_value, expected_type",
    [
        ("5", 5, int),
        ("-5", -5, int),
        ("0", 0, int),
        ("3.14", 3.14, float),
        ("-3.14", -3.14, float),
        ("1e3", 1000.0, float),
        ("-1e-3", -0.001, float),
        ("notanumber", "notanumber", str),
        ("true", True, bool),
        ("false", False, bool),
    ],
)
def test_numeric_parameter_values_parsed(
    pd_common, param_text, expected_value, expected_type
):
    """Cycle-6 vendor patch: the engine used `.isdigit()` which only
    matched non-negative non-float ints. After the patch, negatives
    and floats (and scientific notation) are parsed to their numeric
    types; non-numeric strings stay as strings. Exercised end-to-end
    through the engine's public `parse_decorator`.
    """
    from prompt_decorators.core.dynamic_decorator import parse_decorator

    name, params = parse_decorator(f"+++BuildOn(reference={param_text})")
    assert name == "BuildOn"
    assert "reference" in params
    actual = params["reference"]
    assert actual == expected_value
    assert type(actual) is expected_type


def test_parse_decorator_negative_number_direct(pd_common):
    """Direct regression for the isdigit() -> int()/float() patch:
    `+++Foo(n=-5)` must parse `n` as the int `-5`, not the string."""
    from prompt_decorators.core.dynamic_decorator import parse_decorator

    _, params = parse_decorator("+++BuildOn(reference=-42)")
    assert params["reference"] == -42
    assert isinstance(params["reference"], int)
