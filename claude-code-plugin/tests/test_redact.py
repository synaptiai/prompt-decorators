"""Tests for the `redact()` secret-stripping helper.

Scope: the `pd_common.redact` function and its pattern coverage. Other
pd_common concerns (parse_registry_json, walk shadowing) live in
`test_pd_common.py`. The recursion-guard hook-behavior test lives in
`test_hook.py`.
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


def test_redact_anthropic_sk_ant(pd_common):
    assert pd_common.redact("sk-ant-abcdef0123456789abcdef") == "sk-ant-<redacted>"


def test_redact_openai_sk(pd_common):
    out = pd_common.redact("key is sk-ABCDEFGHIJKLMNOPQRSTUVWX boom")
    assert "sk-ABCDEFGH" not in out
    assert "<redacted>" in out


def test_redact_bearer_token(pd_common):
    out = pd_common.redact("Authorization: Bearer abc.def.ghi.012345")
    assert "abc.def.ghi" not in out
    assert "<redacted>" in out


def test_redact_anthropic_env_form(pd_common):
    # Long enough to trigger both the sk-ant pattern (minimum 10 chars of
    # body) and the ANTHROPIC_API_KEY env-form pattern.
    out = pd_common.redact("ANTHROPIC_API_KEY=sk-ant-0123456789abcdef")
    assert "0123456789abcdef" not in out
    assert "<redacted>" in out


def test_redact_openai_env_form(pd_common):
    out = pd_common.redact("OPENAI_API_KEY=sk-real-key-xxx")
    assert "sk-real-key-xxx" not in out


def test_redact_x_api_key_header(pd_common):
    out = pd_common.redact("X-Api-Key: my-secret-value-xyz")
    assert "my-secret-value-xyz" not in out


def test_redact_leaves_innocent_text_alone(pd_common):
    text = "A perfectly normal error message with no secrets in it."
    assert pd_common.redact(text) == text
