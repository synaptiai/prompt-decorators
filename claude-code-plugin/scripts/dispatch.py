#!/usr/bin/env python3
"""Dispatcher for the `/decorate` slash command.

Subcommands:
  list [category]            Show available decorators, optionally filtered
  preview <name> [args]      Show the instruction text a decorator expands to
  search <term>              Find decorators by name or description
  enable <name>              Re-enable a decorator disabled earlier
  disable <name>             Disable a decorator (auto-select will skip it)
  always add <name>          Add a decorator to the always-on list
  always remove <name>       Remove from always-on
  always list                Show the always-on list
  auto on                    Turn stateful auto-decorate on
  auto off                   Turn stateful auto-decorate off
  auto once                  Arm auto-decorate for the very next prompt only
  auto status                Print current auto mode
  config                     Dump current plugin config
  help                       Print this message
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from pd_common import (  # noqa: E402
    ensure_engine_on_path,
    load_config,
    registry_decorators,
    save_config,
)


def _print(obj) -> None:
    if isinstance(obj, str):
        sys.stdout.write(obj.rstrip() + "\n")
    else:
        sys.stdout.write(json.dumps(obj, indent=2) + "\n")


def cmd_list(args: list[str]) -> int:
    category_filter = args[0].lower() if args else None
    decorators = registry_decorators()
    if category_filter:
        decorators = [d for d in decorators if d["category"].lower() == category_filter]
        if not decorators:
            _print(f"No decorators found in category '{category_filter}'.")
            return 1
    current_cat = None
    lines: list[str] = []
    for d in decorators:
        if d["category"] != current_cat:
            current_cat = d["category"]
            lines.append(f"\n## {current_cat}")
        lines.append(f"  {d['name']:30}  {d['description']}")
    lines.append(f"\n(total: {len(decorators)})")
    _print("\n".join(lines))
    return 0


def cmd_preview(args: list[str]) -> int:
    if not args:
        _print("Usage: /decorate preview <Name>[(params)]")
        return 2
    sigil = args[0]
    if "(" not in sigil and len(args) > 1:
        # accept `/decorate preview Name key=value ...`
        sigil = f"{sigil}({','.join(args[1:])})"
    bare_name = sigil.split("(")[0]
    if not _decorator_exists(bare_name):
        _print(f"Decorator '{bare_name}' not found in registry.")
        return 1
    ensure_engine_on_path()
    try:
        from prompt_decorators.dynamic_decorators_module import (
            apply_dynamic_decorators,
        )
    except Exception as e:  # noqa: BLE001
        _print(f"Error loading engine: {e}")
        return 1
    sample = f"+++{sigil}\n<user prompt goes here>"
    expanded = apply_dynamic_decorators(sample)
    _print(f"### Expansion of +++{sigil}\n\n{expanded}")
    return 0


def cmd_search(args: list[str]) -> int:
    if not args:
        _print("Usage: /decorate search <term>")
        return 2
    term = " ".join(args).lower()
    matches = [
        d
        for d in registry_decorators()
        if term in d["name"].lower() or term in d["description"].lower()
    ]
    if not matches:
        _print(f"No decorators match '{term}'.")
        return 1
    for d in matches:
        _print(f"  {d['name']:30}  [{d['category']}]  {d['description']}")
    _print(f"\n(matches: {len(matches)})")
    return 0


def _decorator_exists(name: str) -> bool:
    return any(d["name"] == name for d in registry_decorators())


def _toggle_list(
    cfg: dict, key: str, action: str, name: str, verb_on: str, verb_off: str
) -> int:
    current: list[str] = list(cfg.get(key, []))
    bare_name = name.split("(")[0]
    if not _decorator_exists(bare_name):
        _print(f"Unknown decorator '{bare_name}'. Run /decorate list to see options.")
        return 1
    if action == "add":
        if name in current:
            _print(f"'{name}' already in {key} list.")
            return 0
        current.append(name)
        cfg[key] = current
        save_config(cfg)
        _print(f"{verb_on}: {name}")
        return 0
    if action == "remove":
        if name not in current:
            _print(f"'{name}' not in {key} list.")
            return 1
        current.remove(name)
        cfg[key] = current
        save_config(cfg)
        _print(f"{verb_off}: {name}")
        return 0
    _print(f"Unknown action '{action}'. Use add|remove|list.")
    return 2


def cmd_enable(args: list[str]) -> int:
    if not args:
        _print("Usage: /decorate enable <Name>")
        return 2
    cfg = load_config()
    disabled: list[str] = list(cfg.get("disabled", []))
    name = args[0]
    if name not in disabled:
        _print(f"'{name}' is not currently disabled.")
        return 0
    disabled.remove(name)
    cfg["disabled"] = disabled
    save_config(cfg)
    _print(f"Re-enabled: {name}")
    return 0


def cmd_disable(args: list[str]) -> int:
    if not args:
        _print("Usage: /decorate disable <Name>")
        return 2
    cfg = load_config()
    name = args[0]
    if not _decorator_exists(name):
        _print(f"Unknown decorator '{name}'.")
        return 1
    disabled: list[str] = list(cfg.get("disabled", []))
    if name in disabled:
        _print(f"'{name}' already disabled.")
        return 0
    disabled.append(name)
    cfg["disabled"] = disabled
    save_config(cfg)
    _print(f"Disabled: {name}")
    return 0


def cmd_always(args: list[str]) -> int:
    cfg = load_config()
    if not args or args[0] == "list":
        items = cfg.get("always_on", [])
        _print(
            "Always-on decorators:\n  "
            + ("\n  ".join(items) if items else "(none)")
        )
        return 0
    if args[0] in {"add", "remove"} and len(args) >= 2:
        return _toggle_list(
            cfg,
            "always_on",
            args[0],
            args[1],
            verb_on="Added to always-on",
            verb_off="Removed from always-on",
        )
    _print("Usage: /decorate always [list|add <name>|remove <name>]")
    return 2


def cmd_auto(args: list[str]) -> int:
    cfg = load_config()
    auto = cfg.setdefault("auto", {})
    if not args or args[0] == "status":
        _print(
            f"auto.mode={auto.get('mode', 'off')}  "
            f"once_armed={auto.get('once_armed', False)}  "
            f"model={auto.get('model', 'claude-haiku-4-5')}"
        )
        return 0
    action = args[0]
    if action == "on":
        auto["mode"] = "on"
        auto["once_armed"] = False
        save_config(cfg)
        _print("auto-decorate: ON (every prompt will be auto-decorated)")
        return 0
    if action == "off":
        auto["mode"] = "off"
        auto["once_armed"] = False
        save_config(cfg)
        _print("auto-decorate: OFF")
        return 0
    if action == "once":
        auto["once_armed"] = True
        save_config(cfg)
        _print("auto-decorate: armed for ONE next prompt")
        return 0
    if action == "model" and len(args) >= 2:
        auto["model"] = args[1]
        save_config(cfg)
        _print(f"auto-decorate model set to: {args[1]}")
        return 0
    _print("Usage: /decorate auto [on|off|once|status|model <id>]")
    return 2


def cmd_config(_: list[str]) -> int:
    _print(load_config())
    return 0


def cmd_help(_: list[str]) -> int:
    _print(__doc__ or "")
    return 0


DISPATCH: dict[str, callable] = {
    "list": cmd_list,
    "preview": cmd_preview,
    "search": cmd_search,
    "enable": cmd_enable,
    "disable": cmd_disable,
    "always": cmd_always,
    "auto": cmd_auto,
    "config": cmd_config,
    "help": cmd_help,
}


def run(argv: Iterable[str]) -> int:
    argv = list(argv)
    if not argv:
        return cmd_help([])
    cmd, *rest = argv
    handler = DISPATCH.get(cmd)
    if handler is None:
        _print(f"Unknown subcommand '{cmd}'. Run /decorate help.")
        return 2
    return handler(rest)


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
