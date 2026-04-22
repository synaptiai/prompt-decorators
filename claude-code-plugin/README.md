# prompt-decorators (Claude Code plugin)

Automatically enhance prompts with composable, categorized prompt decorators
before they reach the model - via a `UserPromptSubmit` hook, a `/decorate`
slash command, and an opt-in Haiku-powered auto-selector.

Bundles the [`prompt-decorators`](https://github.com/synaptiai/prompt-decorators)
engine (vendored) and its full 143-decorator catalogue across 14 categories.

## What it does

- **Inline syntax.** Prepend a `::Name(params)` line to any prompt and the hook
  expands it into precise instructions that are fed to the model as a
  `<system-reminder>` block adjacent to your prompt. `+++Name(params)` also
  works for parity with the upstream library.
- **Always-on decorators.** Put a list of decorators in your config and every
  prompt gets them prepended automatically.
- **Stateful auto-decorate.** Turn it on and every prompt gets 0-3 decorators
  chosen by a small model based on what your prompt seems to need. Or arm it
  for a single prompt at a time.
- **Self-contained.** No `pip install` required; the engine and registry are
  vendored in `vendor/`. Python 3.11+ only.

## Quick start

```bash
# Inline - most direct
::Concise
::StepByStep(numbered=true)
Explain how a CPU works.
```

```bash
# Slash-command driven
/decorate list                      # browse the catalogue
/decorate search reasoning          # find by keyword
/decorate preview Concise           # show the instruction text
/decorate always add Concise        # apply to every prompt
/decorate auto on                   # pick decorators automatically
/decorate auto once                 # auto, only next prompt
/decorate auto off                  # disable
```

## Syntax

Decorators are recognised only when they appear at the start of a line:

```
::Name                              # no parameters
::Name(key=value)                   # single parameter
::Name(key1=val1, key2="string")    # multiple parameters
+++Name                             # upstream library syntax - same behaviour
```

Mid-line occurrences (e.g. `use std::collections::HashMap;` in Rust code) are
ignored. `@` and `/` are reserved by Claude Code for file references and slash
commands and are not used by this plugin.

## Auto-decorate

When `auto.mode = on` (or `once_armed = true`), the hook runs a two-pass
selector before calling the engine:

1. A cheap keyword-based pre-filter narrows the 143-decorator catalogue to
   ~20 candidates based on which categories the prompt seems to need
   (`reasoning`, `structure`, `verification`, `tone`, etc.).
2. A small model (Haiku 4.5 by default) picks 0-3 decorator names from the
   narrowed set.

The picks are prepended as `+++Name` lines and the main hook expands them via
the same engine used for explicit sigils. The expanded context starts with a
visible header so you can see what was applied:

```
[auto-decorate: +Outline +Precision +Alternatives]

...expanded instructions here...
```

The selector prefers direct Anthropic SDK calls (with prompt caching on the
catalogue manifest) when `ANTHROPIC_API_KEY` is set, and falls back to
`claude --print` otherwise.

## Configuration

Persistent config lives at
`~/.config/prompt-decorators/config.json` by default (override with
`PROMPT_DECORATORS_CONFIG_DIR`).

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

All fields are managed via `/decorate` subcommands - you rarely need to edit
this file directly.

## Categories

- `reasoning` (16) - ToT, Socratic, First-Principles, Red-Team, ...
- `structure` (14) - Outline, Summary, Table-Format, Comparison, ...
- `tone` (14) - Concise, Detailed, Academic, Casual, ...
- `verification` (13) - FactCheck, Cite, Confidence, ...
- `minimal` (5) - Short, TL;DR, ...
- `meta` (10) - Meta-reasoning, decorator introspection
- `architecture_and_design` (8) - APIDesign, Scalability, Tradeoffs, ...
- `code_generation` (8) - CodeStandards, ImplementationGuide, ...
- `developer_education` (8), `developer_workflow` (8),
  `devops_and_infrastructure` (8), `implementation-focused` (13),
  `systematic_debugging` (10), `testing_and_debugging` (8)

Run `/decorate list` or `/decorate list <category>` to browse.

## Extensions

The plugin loads any decorators placed under
`vendor/prompt_decorators/registry/extensions/`. To author your own decorator,
follow the schema documented in
[`prompt-decorators`](https://github.com/synaptiai/prompt-decorators).

## How the hook works (for the curious)

The `UserPromptSubmit` hook reads a JSON event on stdin:

```json
{
  "session_id": "...",
  "prompt": "::Concise\nExplain recursion",
  "cwd": "...",
  "hook_event_name": "UserPromptSubmit"
}
```

...and emits:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Please provide a concise, to-the-point response...\n\nExplain recursion"
  }
}
```

Claude Code injects `additionalContext` as a `<system-reminder>` adjacent to
(not replacing) the user's original prompt. Your `::Concise` line stays in
the transcript; Claude ignores it and follows the expanded instructions.

Failures in the hook (parse errors, unknown decorators, engine exceptions)
all fail open - the prompt passes through unchanged and an entry is written
to `$PROMPT_DECORATORS_LOG` (default
`$HOME/.cache/prompt-decorators/hook.log`, mode `0o600`, `O_NOFOLLOW`).

## Development

```bash
cd claude-code-plugin
pip install pytest pydantic jsonschema importlib-metadata markdown
python3 -m pytest tests/ -v
```

The test suite covers the hook parser, dispatcher subcommands, auto-decorate
selector logic, and config read/write. No network calls in tests.

## Roadmap

- **v2 learning loop.** Track which decorators users keep vs. remove and use
  that as implicit feedback for the auto-selector. Design outlined in
  `ideas/intent_to_decorator.md` of the upstream repo.
- **MCP server integration.** Expose decorator discovery as MCP tools for
  Claude Desktop.
- **Cross-session auto-decorate caching.** Cache shortlist results by prompt
  hash to eliminate selector latency for repeat-pattern prompts.
