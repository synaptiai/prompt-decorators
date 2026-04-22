"""Tests for the `redact()` secret-stripping helper and pd_common edges."""

from __future__ import annotations

import importlib
import os
import subprocess
import sys

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


def test_parse_registry_json_rejects_non_dict(tmp_path, pd_common):
    """E1 regression: `[1,2,3]` / `"hi"` / `null` in the registry must not
    crash `/decorate list` or the hook."""
    user_reg = tmp_path / "reg"
    (user_reg / "foo").mkdir(parents=True)
    (user_reg / "foo" / "list.json").write_text("[1, 2, 3]")
    (user_reg / "foo" / "scalar.json").write_text('"just a string"')
    (user_reg / "foo" / "null.json").write_text("null")
    (user_reg / "foo" / "bad.json").write_text("{not even json")

    # Should not raise.
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
    # Should have the full vendored catalogue, no crash from user files.
    assert any(d["name"] == "Concise" for d in decorators)


def test_recursion_guard_short_circuits_hook(tmp_path):
    """E6 regression: PROMPT_DECORATORS_NESTED=1 in the env must make the
    hook exit 0 with no output even when sigils are present. Protects
    against infinite recursion when the plugin is installed globally and
    auto_decorate shells out to `claude --print`.
    """
    plugin_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hook = os.path.join(plugin_root, "hooks", "scripts", "decorate_hook.py")

    event = (
        '{"hook_event_name":"UserPromptSubmit",'
        '"prompt":"::StepByStep\\nhello world"}'
    )
    proc = subprocess.run(
        [sys.executable, hook],
        input=event,
        capture_output=True,
        text=True,
        env={
            **os.environ,
            "PROMPT_DECORATORS_NESTED": "1",
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path),
        },
        timeout=30,
    )
    assert proc.returncode == 0
    # Critically: NO output - the nested guard ran before any expansion work.
    assert proc.stdout == ""
