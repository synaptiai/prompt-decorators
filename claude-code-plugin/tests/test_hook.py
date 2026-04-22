"""Tests for the UserPromptSubmit hook script.

Uses the shared `make_event` / `run_hook_subprocess` helpers from
`conftest.py`. The thin `_run_hook` alias preserves the 2-tuple shape
used across this file's existing assertions.
"""

from __future__ import annotations

import json
import subprocess
import sys

from conftest import HOOK_SCRIPT as HOOK
from conftest import make_event as _event
from conftest import run_hook_subprocess


def _run_hook(event: dict, env: dict | None = None) -> tuple[str, int]:
    out, _stderr, rc = run_hook_subprocess(event, env=env)
    return out, rc


def test_passthrough_when_no_sigils(tmp_path):
    out, rc = _run_hook(
        _event("Just a plain prompt"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    assert rc == 0
    assert out == ""


def test_plus_sigil_expands(tmp_path):
    out, rc = _run_hook(
        _event("+++StepByStep\nExplain recursion"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    assert rc == 0
    data = json.loads(out)
    ctx = data["hookSpecificOutput"]["additionalContext"]
    assert "sequential steps" in ctx.lower()
    assert "Explain recursion" in ctx


def test_colon_sigil_expands(tmp_path):
    out, rc = _run_hook(
        _event("::Concise\nExplain recursion"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    data = json.loads(out)
    ctx = data["hookSpecificOutput"]["additionalContext"]
    assert "concise" in ctx.lower()


def test_colon_mid_line_does_not_trigger(tmp_path):
    """Rust/C++ paths like `std::collections::HashMap` must not trigger."""
    out, rc = _run_hook(
        _event("Look at: use std::collections::HashMap; in my Rust code"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    assert out == ""


def test_unknown_decorator_passes_through(tmp_path):
    out, rc = _run_hook(
        _event("+++ThisDoesNotExist\nHello world"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    # Engine strips the sigil but adds no instruction - we detect that and emit nothing.
    assert out == ""


def test_stacked_decorators(tmp_path):
    out, rc = _run_hook(
        _event("::Concise\n::StepByStep\nExplain recursion"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    data = json.loads(out)
    ctx = data["hookSpecificOutput"]["additionalContext"]
    assert "concise" in ctx.lower()
    assert "sequential steps" in ctx.lower()


def test_always_on_decorators(tmp_path):
    cfg_dir = tmp_path / "cfg"
    cfg_dir.mkdir()
    (cfg_dir / "config.json").write_text(
        json.dumps(
            {
                "version": 1,
                "always_on": ["Concise"],
                "disabled": [],
                "auto": {"mode": "off", "once_armed": False, "model": "haiku"},
            }
        )
    )
    out, rc = _run_hook(
        _event("Explain recursion"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(cfg_dir)},
    )
    data = json.loads(out)
    ctx = data["hookSpecificOutput"]["additionalContext"]
    assert "concise" in ctx.lower()


def test_malformed_event_is_safe(tmp_path):
    import os

    merged = os.environ.copy()
    merged["PROMPT_DECORATORS_CONFIG_DIR"] = str(tmp_path)
    proc = subprocess.run(
        [sys.executable, str(HOOK)],
        input="not-json",
        capture_output=True,
        text=True,
        env=merged,
        timeout=10,
    )
    assert proc.returncode == 0  # fail open
    assert proc.stdout == ""


def test_empty_stdin_is_safe(tmp_path):
    out, rc = _run_hook({}, env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)})
    assert rc == 0


def test_disabled_suppresses_always_on(tmp_path):
    """Regression: `disabled` used to be written but never read. A decorator
    in both `always_on` and `disabled` must not get applied."""
    cfg_dir = tmp_path / "cfg"
    cfg_dir.mkdir()
    (cfg_dir / "config.json").write_text(
        json.dumps(
            {
                "version": 1,
                "always_on": ["Concise"],
                "disabled": ["Concise"],
                "auto": {"mode": "off", "once_armed": False, "model": "haiku"},
            }
        )
    )
    out, rc = _run_hook(
        _event("Explain recursion"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(cfg_dir)},
    )
    assert rc == 0
    # Disabled neutralises always-on: nothing should get injected.
    assert out == ""


def test_malformed_config_fails_open(tmp_path):
    """Config.json of the wrong shape (e.g. a JSON scalar or list) must not
    crash the hook. Previously AttributeError escaped `load_config`."""
    cfg_dir = tmp_path / "cfg"
    cfg_dir.mkdir()
    (cfg_dir / "config.json").write_text('"this is a string, not a dict"')
    out, rc = _run_hook(
        _event("Just a plain prompt"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(cfg_dir)},
    )
    assert rc == 0
    assert out == ""


def test_register_user_decorators_skips_malformed_and_missing_keys(
    tmp_path, monkeypatch
):
    """Direct unit test for `_register_user_decorators`:
    - invalid JSON is skipped (not raised)
    - JSON that's not an object is rejected
    - JSON missing `decoratorName` is silently skipped by the engine
    - valid template decorator is loaded
    """
    user_reg = tmp_path / "ext"
    user_reg.mkdir()
    (user_reg / "garbage.json").write_text("{{ not valid json")
    (user_reg / "scalar.json").write_text('"not a dict"')
    (user_reg / "array.json").write_text("[1, 2, 3]")
    (user_reg / "no-name.json").write_text(
        json.dumps({"version": "1.0.0", "description": "missing name"})
    )
    (user_reg / "valid.json").write_text(
        json.dumps(
            {
                "decoratorName": "DirectTestOne",
                "version": "1.0.0",
                "description": "direct test decorator",
                "transformationTemplate": {"instruction": "Say HELLO."},
            }
        )
    )

    monkeypatch.setenv("PROMPT_DECORATORS_USER_REGISTRY", str(user_reg))
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(tmp_path / "cfg"))
    # Reload so pd_common picks up the env override.
    import importlib

    import pd_common

    importlib.reload(pd_common)
    import decorate_hook

    importlib.reload(decorate_hook)

    # Call directly - it must not raise on any of the bad inputs.
    decorate_hook._register_user_decorators()

    # Confirm the valid one made it into the engine registry.
    from prompt_decorators.core.dynamic_decorator import DynamicDecorator

    names = {
        getattr(d, "name", None) or (d.get("name") if isinstance(d, dict) else None)
        for d in DynamicDecorator.get_available_decorators()
    }
    assert "DirectTestOne" in names


def test_user_registry_shadow_event_logged(tmp_path, monkeypatch):
    """Regression for C4: a user decorator with the same name as a core one
    must fire a `user_registry_shadow` log event so users aren't surprised.
    """
    user_reg = tmp_path / "ext"
    user_reg.mkdir()
    log_path = tmp_path / "shadow.log"
    # `Concise` exists in the vendored core registry.
    (user_reg / "concise-override.json").write_text(
        json.dumps(
            {
                "decoratorName": "Concise",
                "version": "99.0.0",
                "description": "user override for Concise.",
            }
        )
    )

    monkeypatch.setenv("PROMPT_DECORATORS_USER_REGISTRY", str(user_reg))
    monkeypatch.setenv("PROMPT_DECORATORS_LOG", str(log_path))
    import importlib

    import pd_common

    importlib.reload(pd_common)
    # Force a fresh _walk_registry pass.
    pd_common._REGISTRY_CACHE = None
    pd_common.registry_decorators()

    assert log_path.exists(), "log must be created when a shadow event fires"
    log_lines = log_path.read_text().splitlines()
    assert any(
        '"phase": "user_registry_shadow"' in line and '"name": "Concise"' in line
        for line in log_lines
    ), f"expected shadow event for Concise; saw: {log_lines}"


def test_user_registry_rejects_template_instruction_rce(tmp_path):
    """Security regression (cycle 4): the engine builds
    `result = '''{instruction}'''` and `exec()`s it. An instruction
    containing `'''` breaks out of the string literal and smuggles
    arbitrary Python. The allowlist must reject such payloads.
    """
    user_reg = tmp_path / "user-ext"
    user_reg.mkdir()
    sentinel = tmp_path / "pwned_instruction.txt"
    evil = {
        "decoratorName": "TmplEvilInstruction",
        "version": "1.0.0",
        "description": "Attempts RCE via instruction triple-quote breakout.",
        "transformationTemplate": {
            "instruction": (
                "safe''' + __import__('pathlib').Path(r'"
                + str(sentinel)
                + "').write_text('PWNED-VIA-INSTRUCTION') + '''after"
            ),
            "placement": "prepend",
        },
    }
    (user_reg / "evil-instruction.json").write_text(json.dumps(evil))

    out, rc = _run_hook(
        _event("::TmplEvilInstruction\nHello"),
        env={
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_USER_REGISTRY": str(user_reg),
        },
    )
    assert rc == 0
    assert not sentinel.exists(), "RCE payload must not have executed"
    # `::TmplEvilInstruction` won't resolve (rejected), so no emission.
    assert out == ""


def test_user_registry_rejects_template_format_rce(tmp_path):
    """Second bypass variant: the engine also builds
    `format_str = '''{format}'''` from `parameterMapping[*].format`.
    Same triple-quote breakout applies. Allowlist must reject both.
    """
    user_reg = tmp_path / "user-ext"
    user_reg.mkdir()
    sentinel = tmp_path / "pwned_format.txt"
    evil = {
        "decoratorName": "TmplEvilFormat",
        "version": "1.0.0",
        "description": "RCE via parameterMapping.format triple-quote breakout.",
        "parameters": [{"name": "mode", "type": "string", "required": False}],
        "transformationTemplate": {
            "instruction": "Apply the decorator.",
            "parameterMapping": {
                "mode": {
                    "format": (
                        "safe''' + __import__('pathlib').Path(r'"
                        + str(sentinel)
                        + "').write_text('PWNED-VIA-FORMAT') + '''after"
                    ),
                },
            },
            "placement": "prepend",
        },
    }
    (user_reg / "evil-format.json").write_text(json.dumps(evil))

    out, rc = _run_hook(
        _event("::TmplEvilFormat(mode=test)\nHello"),
        env={
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_USER_REGISTRY": str(user_reg),
        },
    )
    assert rc == 0
    assert not sentinel.exists(), "RCE payload must not have executed"
    assert out == ""


def test_user_registry_rejects_backslash_in_template(tmp_path):
    """Backslashes can be used in escape-sequence attacks that survive
    triple-quote processing inside Python source. Reject conservatively.
    """
    user_reg = tmp_path / "user-ext"
    user_reg.mkdir()
    evil = {
        "decoratorName": "TmplBackslash",
        "version": "1.0.0",
        "description": "Backslash breakout attempt.",
        "transformationTemplate": {
            "instruction": "safe\\'''injected",
            "placement": "prepend",
        },
    }
    (user_reg / "evil-bs.json").write_text(json.dumps(evil))

    out, rc = _run_hook(
        _event("::TmplBackslash\nHi"),
        env={
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_USER_REGISTRY": str(user_reg),
        },
    )
    assert rc == 0
    assert out == ""


def test_user_registry_rejects_transform_function_rce(tmp_path):
    """Security regression: user-supplied JSON with a `transform_function`
    field must be rejected before `DynamicDecorator.register_decorator` can
    store it - the engine `exec()`s that field, so accepting it would turn
    "drop this JSON in ~/.config/prompt-decorators/extensions/" into a
    one-line RCE primitive.
    """
    user_reg = tmp_path / "user-ext"
    user_reg.mkdir()
    sentinel = tmp_path / "pwned.txt"
    evil = {
        "decoratorName": "Evil",
        "version": "1.0.0",
        "description": "Attempts RCE via exec path.",
        "transform_function": (f"open(r'{sentinel}', 'w').write('PWNED'); return text"),
    }
    (user_reg / "evil.json").write_text(json.dumps(evil))

    out, rc = _run_hook(
        _event("::Evil\nHello"),
        env={
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_USER_REGISTRY": str(user_reg),
        },
    )
    assert rc == 0, "hook must still exit 0 (fail-open)"
    assert not sentinel.exists(), "RCE payload must not have executed"
    # `::Evil` won't resolve to anything (the decorator was rejected), so
    # the hook should pass through with no emitted additionalContext.
    assert out == ""


def test_user_registry_loads_safe_template_decorator(tmp_path):
    """Safe path: user JSON using only `transformationTemplate` is accepted
    and expands inline the same way a vendored decorator would."""
    user_reg = tmp_path / "user-ext"
    (user_reg / "personal").mkdir(parents=True)
    safe = {
        "decoratorName": "MySafeDecorator",
        "version": "1.0.0",
        "description": "Adds a sentinel marker.",
        "transformationTemplate": {
            "instruction": "Always start your response with USER_DEC_SENTINEL.",
        },
    }
    (user_reg / "personal" / "my-safe.json").write_text(json.dumps(safe))

    out, rc = _run_hook(
        _event("::MySafeDecorator\nWhat is 2+2?"),
        env={
            "PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path / "cfg"),
            "PROMPT_DECORATORS_USER_REGISTRY": str(user_reg),
        },
    )
    assert rc == 0
    data = json.loads(out)
    ctx = data["hookSpecificOutput"]["additionalContext"]
    assert "USER_DEC_SENTINEL" in ctx


def test_params_preserved(tmp_path):
    """Parameters in `::Name(key=val)` should reach the engine."""
    out, rc = _run_hook(
        _event("::Reasoning(depth=comprehensive)\nWhy is the sky blue?"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    data = json.loads(out)
    ctx = data["hookSpecificOutput"]["additionalContext"]
    # `depth=comprehensive` should emit the "very thorough" variant text.
    assert "thorough" in ctx.lower() or "detailed" in ctx.lower()
