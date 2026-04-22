"""Common pytest setup - add plugin script dirs to sys.path and isolate config."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PLUGIN_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
sys.path.insert(0, str(PLUGIN_ROOT / "hooks" / "scripts"))


@pytest.fixture(autouse=True)
def _isolated_config(tmp_path, monkeypatch):
    """Redirect config + log to a temp dir for every test."""
    cfg_dir = tmp_path / "pd_cfg"
    cfg_dir.mkdir()
    log_path = tmp_path / "pd.log"
    monkeypatch.setenv("PROMPT_DECORATORS_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("PROMPT_DECORATORS_LOG", str(log_path))

    # Force pd_common to pick up the new env - it caches module-level paths.
    for mod in ("pd_common", "dispatch", "decorate_hook", "auto_decorate"):
        sys.modules.pop(mod, None)
    yield
