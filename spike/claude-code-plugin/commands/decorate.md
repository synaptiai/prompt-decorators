---
description: Browse, preview, and manage prompt decorators
argument-hint: "[list|preview|enable|disable|always] [name]"
---

# /decorate

Browse and manage the prompt-decorators catalog.

## Subcommands (spike — not yet wired to a backing script)

- `list` — show available decorators grouped by category
- `preview <name>` — show the instruction text a decorator expands to
- `search <term>` — find decorators by keyword
- `enable <name>` / `disable <name>` — toggle individual decorators
- `always add <name>` / `always remove <name>` — manage always-on list
- `auto` — run Haiku-based selector on the next prompt

## Inline syntax

Prepend a `::Name` line to any prompt:

```
::Concise
::StepByStep(numbered=true)
Explain how a CPU works.
```

The `+++Name` syntax (native to the upstream library) also works.
