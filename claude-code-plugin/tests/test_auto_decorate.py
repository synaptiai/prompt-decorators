"""Tests for the auto-decorate selector (pure-logic parts)."""
from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def auto_module(monkeypatch, tmp_path):
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(tmp_path / "cfg"))
    import importlib

    import pd_common

    importlib.reload(pd_common)
    import auto_decorate

    importlib.reload(auto_decorate)
    return auto_decorate


def test_shortlist_returns_size(auto_module):
    picks = auto_module.shortlist("Write a Python function", size=15)
    assert 1 <= len(picks) <= 15
    assert all("name" in d and "category" in d for d in picks)


def test_shortlist_biases_by_category(auto_module):
    # A comparison prompt should include structure/reasoning decorators.
    picks = auto_module.shortlist(
        "Compare REST and GraphQL - pros and cons in a table"
    )
    categories = {d["category"] for d in picks}
    assert "structure" in categories or "reasoning" in categories


def test_parse_names_handles_valid_json(auto_module):
    valid = {"Concise", "StepByStep", "Reasoning"}
    out = auto_module._parse_names('["Concise","StepByStep"]', valid)
    assert out == ["Concise", "StepByStep"]


def test_parse_names_filters_invalid(auto_module):
    valid = {"Concise"}
    out = auto_module._parse_names('["Concise","NotReal","AlsoNotReal"]', valid)
    assert out == ["Concise"]


def test_parse_names_caps_at_max(auto_module):
    valid = {"A", "B", "C", "D", "E"}
    out = auto_module._parse_names('["A","B","C","D","E"]', valid)
    assert len(out) <= auto_module.MAX_PICKS


def test_parse_names_handles_prose_wrapping(auto_module):
    """Some models wrap the JSON in markdown or commentary."""
    valid = {"Concise"}
    out = auto_module._parse_names(
        'Here is my answer: ["Concise"]. Hope it helps!', valid
    )
    assert out == ["Concise"]


def test_parse_names_returns_empty_on_bad_input(auto_module):
    valid = {"Concise"}
    assert auto_module._parse_names("not json at all", valid) == []
    assert auto_module._parse_names("[not-quoted]", valid) == []


def test_select_decorators_no_network(auto_module, monkeypatch):
    """Without SDK or CLI available, selector returns an empty list safely."""
    monkeypatch.setattr(auto_module, "_call_anthropic_sdk", lambda *a, **k: None)
    monkeypatch.setattr(auto_module, "_call_claude_cli", lambda *a, **k: None)
    assert auto_module.select_decorators("hello") == []


def test_select_decorators_uses_sdk_when_available(auto_module, monkeypatch):
    monkeypatch.setattr(
        auto_module, "_call_anthropic_sdk", lambda *a, **k: '["Concise"]'
    )
    monkeypatch.setattr(
        auto_module,
        "_call_claude_cli",
        lambda *a, **k: pytest.fail("CLI fallback should not run"),
    )
    out = auto_module.select_decorators("be brief please")
    assert out == ["Concise"]
