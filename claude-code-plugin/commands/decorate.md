---
description: Use to browse the decorator catalogue, preview an expansion, manage the always-on list, or toggle auto-decorate mode.
argument-hint: "[list|preview|search|enable|disable|always|auto|config|help] [...]"
allowed-tools: Bash
context: fork
agent: Explore
---

# /decorate

Manage the prompt-decorators catalogue, always-on list, and auto-decorate
mode. The actual work happens in a Python dispatcher; this command is a
thin shell around it.

The user invoked: `/decorate $ARGUMENTS`

## Contract

**GOAL:** Show the user the exact, unmodified output of the dispatcher so
they can act on it (e.g., see the decorator list, copy a sigil, confirm an
auto mode change). Testable: the output in the fenced block matches what
`scripts/dispatch.py` prints verbatim.

**CONSTRAINTS:**
- Command is read-mostly. The only writes are to
  `~/.config/prompt-decorators/config.json` via
  `enable`/`disable`/`always`/`auto` subcommands - never to project files.
- `$ARGUMENTS` must reach the dispatcher as tokenised argv, NOT as a shell
  command string. The heredoc below uses a quoted delimiter
  (`'PD_ARGS_EOF'`) so user-supplied metacharacters cannot escape; the
  dispatcher then uses `shlex.split` inside Python for safe tokenisation.
- Do not interpret or summarise the output unless the user explicitly
  asks. Relay verbatim.

**FORMAT:** A fenced code block containing the dispatcher's stdout. If the
dispatcher exits non-zero, include the exit code and any stderr.

**FAILURE CONDITIONS:**
- Output is paraphrased rather than verbatim.
- `$ARGUMENTS` is interpolated into a shell command string (reintroduces
  the injection vector).
- The user's `config.json` is written outside the subcommand's intent
  (e.g., running `list` leaves the config modified).

## Process

1. Invoke the dispatcher via a quoted heredoc so shell metacharacters in
   the user's input can't be executed:

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/dispatch.py" --args-from-stdin <<'PD_ARGS_EOF'
   $ARGUMENTS
   PD_ARGS_EOF
   ```

2. Wrap the output in a fenced code block and return it to the user
   without edits.

3. If the user's query is "what decorator should I use for X?" rather than
   a subcommand, invoke the `prompt-decorators-usage` skill instead of
   running this dispatcher - it's better suited to that kind of judgement
   call.

4. If the user wants to create a new decorator, invoke the
   `authoring-decorators` skill instead.

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

## Related skills

- `prompt-decorators-usage` - choose which decorators to suggest for a given prompt.
- `authoring-decorators` - walk through writing a new decorator end-to-end.
