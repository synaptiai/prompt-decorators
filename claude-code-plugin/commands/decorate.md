---
description: Browse, preview, and manage prompt decorators
argument-hint: "[list|preview|search|enable|disable|always|auto|config|help] [...]"
allowed-tools: Bash
---

# /decorate

Manage the prompt-decorators catalogue, always-on list, and auto-decorate mode.

The user invoked: `/decorate $ARGUMENTS`

Run the dispatcher and relay its output verbatim to the user in a fenced block
so they can see the exact result. Do not interpret or summarize unless they
ask.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/dispatch.py" $ARGUMENTS
```

## Subcommands

- `list [category]` - show available decorators, optionally filtered by category
- `preview <Name>[(params)]` - show the instruction text a decorator expands to
- `search <term>` - find decorators by name or description
- `enable <Name>` / `disable <Name>` - toggle individual decorators
- `always list|add <Name>|remove <Name>` - manage always-on list
- `auto on|off|once|status|model <id>` - control stateful auto-decorate mode
- `config` - dump current plugin config
- `help` - print this help

## Inline syntax (no command needed)

Prepend a `::Name` or `+++Name` line to any prompt and the UserPromptSubmit
hook will expand it automatically:

```
::Concise
::StepByStep(numbered=true)
Explain how a CPU works.
```
