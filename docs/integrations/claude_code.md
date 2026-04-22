# Claude Code Plugin

The `claude-code-plugin/` subdirectory ships prompt-decorators as an installable
[Claude Code](https://claude.com/claude-code) plugin. Users prepend a
`::Name(params)` or `+++Name(params)` line to any prompt and the plugin's
`UserPromptSubmit` hook expands it into precise instructions using the
prompt-decorators engine **before** the model sees the prompt.

## Install

From Claude Code:

```bash
/plugin marketplace add synaptiai/synapti-marketplace
/plugin install prompt-decorators
```

## Inline syntax

```text
::Concise
::StepByStep(numbered=true)
Explain how a CPU works.
```

Both `::Name` (recommended, modern) and `+++Name` (the library's native
syntax) are recognised **at the start of a line only**. Mid-line occurrences
— e.g. `use std::collections::HashMap;` in Rust code — are ignored to avoid
false triggers.

## `/decorate` slash command

| Subcommand | What it does |
|---|---|
| `list [category]` | Show the catalogue, optionally filtered |
| `preview <Name>[(params)]` | Show the instruction text a decorator expands to |
| `search <term>` | Find decorators by name or description |
| `enable <Name>` / `disable <Name>` | Toggle a decorator for auto-select eligibility |
| `always add <Name>` / `always remove <Name>` | Manage the always-on list |
| `always list` | Show decorators currently applied to every prompt |
| `auto on` / `auto off` / `auto once` | Control stateful auto-decorate mode |
| `auto status` / `auto model <id>` | Inspect or change the selector model |
| `config` / `help` | Print current config or help |

## Auto-decorate

When auto mode is on (or armed for the next prompt via `/decorate auto
once`), a two-pass selector picks 0-3 decorators:

1. A keyword/category pre-filter narrows the 143-decorator catalogue to ~20
   candidates.
2. A fast model (Haiku 4.5 by default) picks from the narrowed list and
   returns a JSON array of names.

The picks are prepended and expanded via the same engine used for explicit
sigils. A visible header shows what was applied:

```text
[auto-decorate: +Outline +Precision +Alternatives]

...expanded instructions here...
```

The selector calls the Anthropic SDK directly when `ANTHROPIC_API_KEY` is
set (with prompt caching on the catalogue manifest), and falls back to
`claude --print` otherwise so the plugin works out of the box.

## Configuration

Persistent config lives at `~/.config/prompt-decorators/config.json` by
default (override with `PROMPT_DECORATORS_CONFIG_DIR`):

```json
{
  "version": 1,
  "always_on": ["Concise"],
  "disabled": [],
  "auto": {
    "mode": "off",
    "once_armed": false,
    "model": "claude-haiku-4-5"
  }
}
```

All fields are managed via `/decorate` subcommands; editing the file
directly is rarely needed.

## Security & privacy notes

- Logs default to `~/.cache/prompt-decorators/hook.log` with `0o600` perms
  and `O_NOFOLLOW` to block symlink attacks. Never `/tmp` by default.
- Prompt content is **not** logged by default. Opt in for debugging with
  `PROMPT_DECORATORS_LOG_DEBUG=1`.
- Plain prompts (no sigils, no always-on, no auto) hit a fast path that
  does zero disk I/O.
- Config writes are atomic (`tempfile` + `os.replace`) - safe under
  concurrent `/decorate` invocations.

## How the hook works

The `UserPromptSubmit` hook reads a JSON event on stdin and emits
`hookSpecificOutput.additionalContext`. Claude Code injects that as a
`<system-reminder>` adjacent to the user's original prompt - so the
`::Concise` sigil line stays in the transcript while Claude follows the
expanded instructions.

Failures (parse errors, unknown decorators, engine exceptions) all fail
open - the prompt passes through unchanged and an entry is written to the
log.

## Source and repository layout

The plugin source lives at [`claude-code-plugin/`](https://github.com/synaptiai/prompt-decorators/tree/main/claude-code-plugin)
in this repo. It vendors the engine and registry into `vendor/` so the
plugin is self-contained - no `pip install` required by the end user.

The [Synapti marketplace](https://github.com/synaptiai/synapti-marketplace)
references this directory remotely via a `git-subdir` source entry, so
plugin updates flow through automatically without duplicating code.
