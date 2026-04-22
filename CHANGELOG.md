# Changelog

All notable changes to the Prompt Decorators project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Claude Code plugin** under `claude-code-plugin/`. Installs via the
  Synapti marketplace and expands inline `::Name(params)` / `+++Name(params)`
  sigils into precise instructions through a `UserPromptSubmit` hook,
  before the model sees the prompt. Includes:
  - A `/decorate` slash command with `list`, `preview`, `search`, `enable`,
    `disable`, `always`, and `auto` subcommands.
  - A persistent config at `~/.config/prompt-decorators/config.json` for
    always-on decorators and auto-decorate mode (on / off / once).
  - A two-pass auto-selector (keyword/category pre-filter, then Haiku 4.5)
    that picks 0-3 decorators per prompt when enabled. Uses the Anthropic
    SDK with prompt caching when `ANTHROPIC_API_KEY` is set, falls back
    to `claude --print`.
  - Self-contained vendored engine and registry (~1.6 MB) so the plugin
    works without `pip install`.
  - 51 unit tests covering hook parsing, dispatcher subcommands, selector
    logic, config read/write, and security edge cases (log symlink
    refusal, atomic config writes, prompt-content redaction).
  - Full documentation under `docs/integrations/claude_code.md`.
