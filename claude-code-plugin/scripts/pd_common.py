"""Shared helpers for the prompt-decorators Claude Code plugin.

Keeps engine bootstrap, config read/write, and logging in one place so the
hook + dispatcher stay short.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
VENDOR_DIR = PLUGIN_ROOT / "vendor"

DEFAULT_CONFIG_DIR = Path(
    os.environ.get(
        "PROMPT_DECORATORS_CONFIG_DIR",
        str(Path.home() / ".config" / "prompt-decorators"),
    )
)
CONFIG_PATH = DEFAULT_CONFIG_DIR / "config.json"
LOG_PATH = Path(os.environ.get("PROMPT_DECORATORS_LOG", "/tmp/pd_hook.log"))

DEFAULT_CONFIG: dict[str, Any] = {
    "version": 1,
    "always_on": [],
    "disabled": [],
    "auto": {"mode": "off", "once_armed": False, "model": "claude-haiku-4-5"},
}


def ensure_engine_on_path() -> None:
    vendor = str(VENDOR_DIR)
    if vendor not in sys.path:
        sys.path.insert(0, vendor)


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return json.loads(json.dumps(DEFAULT_CONFIG))
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return json.loads(json.dumps(DEFAULT_CONFIG))
    merged = json.loads(json.dumps(DEFAULT_CONFIG))
    merged.update({k: v for k, v in data.items() if k in DEFAULT_CONFIG})
    if "auto" in data and isinstance(data["auto"], dict):
        merged["auto"] = {**DEFAULT_CONFIG["auto"], **data["auto"]}
    return merged


def save_config(cfg: dict[str, Any]) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def log(event: dict[str, Any]) -> None:
    if os.environ.get("PROMPT_DECORATORS_LOG_DISABLE") == "1":
        return
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": time.time(), **event}) + "\n")
    except OSError:
        pass


_REGISTRY_CACHE: list[dict[str, Any]] | None = None


def _walk_registry() -> list[dict[str, Any]]:
    """Walk the vendored registry JSON files and infer category from path.

    The engine itself defaults category to "General" when the JSON doesn't
    declare one, so we derive it from the directory layout (core/<cat>/ or
    extensions/<cat>/) which is where the catalogue's structure lives.
    """
    import json as _json

    registry_roots = [
        VENDOR_DIR / "prompt_decorators" / "registry" / "core",
        VENDOR_DIR / "prompt_decorators" / "registry" / "extensions",
    ]
    out: list[dict[str, Any]] = []
    for root in registry_roots:
        if not root.exists():
            continue
        for path in root.rglob("*.json"):
            try:
                data = _json.loads(path.read_text(encoding="utf-8"))
            except (OSError, _json.JSONDecodeError):
                continue
            name = data.get("decoratorName") or data.get("name")
            if not name:
                continue
            # Category is the first directory under the registry root.
            rel_parts = path.relative_to(root).parts
            category = rel_parts[0] if len(rel_parts) > 1 else "other"
            desc = (data.get("description") or "").splitlines()
            out.append(
                {
                    "name": name,
                    "description": desc[0][:160] if desc else "",
                    "category": category,
                }
            )
    return sorted(out, key=lambda x: (x["category"], x["name"]))


def registry_decorators(force_reload: bool = False) -> list[dict[str, Any]]:
    """Load the catalogue as plain dicts (name, description, category)."""
    global _REGISTRY_CACHE
    if _REGISTRY_CACHE is None or force_reload:
        _REGISTRY_CACHE = _walk_registry()
    return _REGISTRY_CACHE
