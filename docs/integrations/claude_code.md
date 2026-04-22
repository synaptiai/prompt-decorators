# Claude Code Plugin

The `claude-code-plugin/` subdirectory ships prompt-decorators as an
installable [Claude Code](https://claude.com/claude-code) plugin. Users
prepend a `::Name(params)` or `+++Name(params)` line to any prompt and the
plugin's `UserPromptSubmit` hook expands it into precise instructions using
the prompt-decorators engine **before** the model sees the prompt.

> **This page is a pointer.** The canonical reference for the plugin — full
> subcommand list, config schema, security posture, vendoring, sync policy —
> lives next to the plugin source at
> [`claude-code-plugin/README.md`](https://github.com/synaptiai/prompt-decorators/blob/main/claude-code-plugin/README.md).
> This page summarises and links; that README is the source of truth. The
> authoring guide (how to write a new decorator) and the usage guide (when to
> suggest one) live as installable skills under
> [`claude-code-plugin/skills/`](https://github.com/synaptiai/prompt-decorators/tree/main/claude-code-plugin/skills).

## What the plugin does (short version)

- **Inline syntax**: `::Name` or `+++Name` at the start of a prompt line.
  Mid-line occurrences are ignored (so Rust/C++ paths like
  `std::collections::HashMap;` don't false-trigger).
- **`/decorate` slash command**: browse, preview, search, toggle always-on
  list, control auto-decorate mode.
- **Auto-decorate** (opt-in): a two-pass selector picks 0-3 decorators per
  prompt. Can be one-shot, stateful, or off.
- **User registry override**: personal decorators under
  `$HOME/.config/prompt-decorators/extensions/` survive vendor re-syncs.
- **Self-contained**: the engine and decorator registry are vendored into
  the plugin directory, so no `pip install` is required by end users.

## Install

From Claude Code:

```bash
/plugin marketplace add synaptiai/synapti-marketplace
/plugin install prompt-decorators
```

## Further reading

- **Plugin reference**: [`claude-code-plugin/README.md`](https://github.com/synaptiai/prompt-decorators/blob/main/claude-code-plugin/README.md)
  — inline syntax, `/decorate` subcommands, auto-decorate internals,
  configuration, security, full how-it-works.
- **Usage guidance skill**:
  [`skills/prompt-decorators-usage/SKILL.md`](https://github.com/synaptiai/prompt-decorators/blob/main/claude-code-plugin/skills/prompt-decorators-usage/SKILL.md)
  — when and how to suggest decorators for a given prompt.
- **Authoring skill**:
  [`skills/authoring-decorators/SKILL.md`](https://github.com/synaptiai/prompt-decorators/blob/main/claude-code-plugin/skills/authoring-decorators/SKILL.md)
  — how to write a new decorator (naming, schema, testing).
- **Vendoring and sync policy**:
  [`claude-code-plugin/VENDORING.md`](https://github.com/synaptiai/prompt-decorators/blob/main/claude-code-plugin/VENDORING.md).
- **Marketplace entry**: the companion
  [synapti-marketplace](https://github.com/synaptiai/synapti-marketplace)
  repo points at this directory via a `git-subdir` source, so plugin
  updates flow through automatically.
