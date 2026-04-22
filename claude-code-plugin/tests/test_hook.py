"""Tests for the UserPromptSubmit hook script."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
HOOK = PLUGIN_ROOT / "hooks" / "scripts" / "decorate_hook.py"


def _run_hook(event: dict, env: dict | None = None) -> tuple[str, int]:
    """Run the hook script as a subprocess with a given event on stdin."""
    import os

    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    proc = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(event),
        capture_output=True,
        text=True,
        env=merged_env,
        timeout=30,
    )
    return proc.stdout, proc.returncode


def _event(prompt: str) -> dict:
    return {
        "session_id": "test",
        "transcript_path": "/tmp/t",
        "cwd": "/tmp",
        "permission_mode": "default",
        "hook_event_name": "UserPromptSubmit",
        "prompt": prompt,
    }


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
