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
from typing import Callable

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from pd_common import (  # noqa: E402
    AUTO_MODE,
    AUTO_MODEL,
    AUTO_ONCE,
    CFG_ALWAYS_ON,
    CFG_AUTO,
    CFG_DISABLED,
    DEFAULT_MODEL,
    MODE_OFF,
    MODE_ON,
    bare_name,
    ensure_engine_on_path,
    load_config,
    registry_decorators,
    registry_names,
    save_config,
)


def _print(obj: str | dict | list) -> None:
    if isinstance(obj, str):
        sys.stdout.write(obj.rstrip() + "\n")
    else:
        sys.stdout.write(json.dumps(obj, indent=2) + "\n")


def _require_decorator(name: str) -> bool:
    if name not in registry_names():
        _print(f"Unknown decorator '{name}'. Run /decorate list to see options.")
        return False
    return True


def _mutate_list(
    cfg_key: str, action: str, name: str, *, verb_add: str, verb_remove: str
) -> int:
    """Shared add/remove logic for always_on and disabled lists."""
    cfg = load_config()
    current: list[str] = list(cfg.get(cfg_key, []))
    if action == "add":
        if not _require_decorator(bare_name(name)):
            return 1
        if name in current:
            _print(f"'{name}' already in {cfg_key} list.")
            return 0
        current.append(name)
        cfg[cfg_key] = current
        save_config(cfg)
        _print(f"{verb_add}: {name}")
        return 0
    if action == "remove":
        if name not in current:
            _print(f"'{name}' not in {cfg_key} list.")
            return 1
        current.remove(name)
        cfg[cfg_key] = current
        save_config(cfg)
        _print(f"{verb_remove}: {name}")
        return 0
    _print(f"Unknown action '{action}'. Use add|remove|list.")
    return 2


def cmd_list(args: list[str]) -> int:
    category_filter = args[0].lower() if args else None
    decorators = registry_decorators()
    if category_filter:
        decorators = [d for d in decorators if d["category"].lower() == category_filter]
        if not decorators:
            _print(f"No decorators found in category '{category_filter}'.")
            return 1
    lines: list[str] = []
    current_cat = None
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
        sigil = f"{sigil}({','.join(args[1:])})"
    if not _require_decorator(bare_name(sigil)):
        return 1
    ensure_engine_on_path()
    try:
        from prompt_decorators.dynamic_decorators_module import apply_dynamic_decorators
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


def cmd_enable(args: list[str]) -> int:
    if not args:
        _print("Usage: /decorate enable <Name>")
        return 2
    name = args[0]
    if not _require_decorator(bare_name(name)):
        return 1
    cfg = load_config()
    disabled: list[str] = list(cfg.get(CFG_DISABLED, []))
    if name not in disabled:
        _print(f"'{name}' is not currently disabled.")
        return 0
    disabled.remove(name)
    cfg[CFG_DISABLED] = disabled
    save_config(cfg)
    _print(f"Re-enabled: {name}")
    return 0


def cmd_disable(args: list[str]) -> int:
    if not args:
        _print("Usage: /decorate disable <Name>")
        return 2
    return _mutate_list(
        CFG_DISABLED,
        "add",
        args[0],
        verb_add="Disabled",
        verb_remove="Re-enabled",
    )


def cmd_always(args: list[str]) -> int:
    cfg = load_config()
    if not args or args[0] == "list":
        items = cfg.get(CFG_ALWAYS_ON, [])
        body = "\n  ".join(items) if items else "(none)"
        _print(f"Always-on decorators:\n  {body}")
        return 0
    if args[0] in {"add", "remove"} and len(args) >= 2:
        return _mutate_list(
            CFG_ALWAYS_ON,
            args[0],
            args[1],
            verb_add="Added to always-on",
            verb_remove="Removed from always-on",
        )
    _print("Usage: /decorate always [list|add <name>|remove <name>]")
    return 2


_AUTO_ACTIONS: dict[str, Callable[[dict, list[str]], int]] = {}


def _auto_status(cfg: dict, _args: list[str]) -> int:
    auto = cfg.get(CFG_AUTO, {})
    _print(
        f"auto.mode={auto.get(AUTO_MODE, MODE_OFF)}  "
        f"once_armed={auto.get(AUTO_ONCE, False)}  "
        f"model={auto.get(AUTO_MODEL, DEFAULT_MODEL)}"
    )
    return 0


def _auto_on(cfg: dict, _args: list[str]) -> int:
    cfg[CFG_AUTO][AUTO_MODE] = MODE_ON
    cfg[CFG_AUTO][AUTO_ONCE] = False
    save_config(cfg)
    _print("auto-decorate: ON (every prompt will be auto-decorated)")
    return 0


def _auto_off(cfg: dict, _args: list[str]) -> int:
    cfg[CFG_AUTO][AUTO_MODE] = MODE_OFF
    cfg[CFG_AUTO][AUTO_ONCE] = False
    save_config(cfg)
    _print("auto-decorate: OFF")
    return 0


def _auto_once(cfg: dict, _args: list[str]) -> int:
    cfg[CFG_AUTO][AUTO_ONCE] = True
    save_config(cfg)
    _print("auto-decorate: armed for ONE next prompt")
    return 0


def _auto_model(cfg: dict, args: list[str]) -> int:
    if not args:
        _print("Usage: /decorate auto model <model-id>")
        return 2
    cfg[CFG_AUTO][AUTO_MODEL] = args[0]
    save_config(cfg)
    _print(f"auto-decorate model set to: {args[0]}")
    return 0


_AUTO_ACTIONS.update(
    {
        "status": _auto_status,
        "on": _auto_on,
        "off": _auto_off,
        "once": _auto_once,
        "model": _auto_model,
    }
)


def cmd_auto(args: list[str]) -> int:
    cfg = load_config()
    cfg.setdefault(CFG_AUTO, {})
    if not args:
        return _auto_status(cfg, [])
    handler = _AUTO_ACTIONS.get(args[0])
    if handler is None:
        _print("Usage: /decorate auto [on|off|once|status|model <id>]")
        return 2
    return handler(cfg, args[1:])


def cmd_config(_: list[str]) -> int:
    _print(load_config())
    return 0


def cmd_help(_: list[str]) -> int:
    _print(__doc__ or "")
    return 0


DISPATCH: dict[str, Callable[[list[str]], int]] = {
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


def run(argv: list[str]) -> int:
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
