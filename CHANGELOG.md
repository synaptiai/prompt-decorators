# Changelog

All notable changes to the Prompt Decorators project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.10.0] - 2026-04-23

### Added

- **Claude Code plugin** under `claude-code-plugin/` (#148). Installs via
  the Synapti marketplace and expands inline `::Name(params)` /
  `+++Name(params)` sigils into precise instructions through a
  `UserPromptSubmit` hook, before the model sees the prompt. Includes:
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
  - 108 plugin tests covering hook parsing, dispatcher subcommands,
    selector logic, config read/write, vendor-patch regressions, and
    security edge cases (log symlink refusal, atomic config writes,
    prompt-content redaction, fd-ownership race, non-finite float
    rejection, SystemExit fail-open, KeyboardInterrupt propagation).
  - Full documentation under `docs/integrations/claude_code.md`.
  - `authoring-decorators` and `prompt-decorators-usage` skills bundled
    with the plugin for in-context help.

### Security

Six-cycle adversarial self-review hardened the plugin's trust boundary:

- `transformFunction` / `transform_function` fields in user-supplied
  decorator JSON are rejected at registration (would otherwise `exec()`
  arbitrary Python in the hook process).
- `parameterMapping` keys and values are validated against a safe
  template-string grammar; triple-quote and backslash-escape breakouts
  are blocked before they reach the engine's `exec()` path.
- Slash-command arguments are passed via quoted heredoc +
  `--args-from-stdin` + `shlex.split`, neutralising shell-metachar
  injection.
- Log files open with `O_NOFOLLOW` and mode `0o600`; default log path
  is `$HOME/.cache/prompt-decorators/hook.log`, never `/tmp`.
- Prompt content is not logged by default (set
  `PROMPT_DECORATORS_LOG_DEBUG=1` to opt in).
- Secrets (`sk-ant-*`, `sk-*`, `Bearer ...`, `Authorization:`, common
  env keys) are redacted from log entries.
- Atomic config writes use `tempfile.mkstemp` + `os.replace` with an
  fd-ownership guard so `os.close(fd)` never races with fd reuse.
- Hook outer guard is scoped to `(Exception, SystemExit)` — fail-open
  against buggy decorator imports while preserving `KeyboardInterrupt`
  for Ctrl-C.
- Vendor patch: `parse_decorator` rejects non-finite floats
  (`nan` / `inf` / `-inf`) that would silently bypass numeric validators.

### Dependencies

- 34 dependabot updates covering `anthropic`, `openai`, `mcp`,
  `pydantic`, `jsonschema`, `typing-extensions`, `mkdocs-material`,
  `mypy`, `pre-commit`, `starlette`, `langchain`, `python-dotenv`, and
  related tooling.
