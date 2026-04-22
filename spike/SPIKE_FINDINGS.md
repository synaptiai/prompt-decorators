# Spike: prompt-decorators as a Claude Code plugin

This spike validates whether prompt-decorators can be repackaged as a Claude Code
plugin that transforms user prompts before they reach the model. It includes a
minimal working plugin, end-to-end tests against a real Claude Code session, and
notes on the design decisions that need user sign-off before building further.

Branch: `claude/refactor-prompt-decorators-hVtwW`
Scope: `spike/claude-code-plugin/` only. Nothing outside the `spike/` directory
was modified.

## TL;DR

- **Architecture works.** A `UserPromptSubmit` hook calls the existing Python
  engine (`apply_dynamic_decorators`) and injects the expanded instructions. In
  end-to-end tests, Claude received the instructions and changed its behaviour
  accordingly.
- **The hook augments, does not replace.** The user's literal prompt stays in
  the conversation; the expansion arrives as a `<system-reminder>` tag labelled
  "UserPromptSubmit hook". Claude sees both and follows the injected guidance.
- **`::` is a viable modern sigil.** With a start-of-line anchor, it does not
  collide with Rust/C++ paths (`std::collections::HashMap`) or common prose.
  `@` is unusable (file references), `/` is unusable (slash commands); `::`
  and `+++` are both safe. Recommendation: support both — `::` as the preferred
  modern form, `+++` for continuity with the existing library.
- **Auto-decorate path works.** A thin selector calls a fast model (Haiku
  shown via `claude --print`, production will use the Anthropic SDK with
  prompt caching on the catalog manifest), returns 0-3 decorator names, and
  prepends them for the main hook to expand.

## How the hook actually works (empirically verified)

Claude Code's `UserPromptSubmit` hook receives this on stdin:

```json
{
  "session_id": "...",
  "transcript_path": "...",
  "cwd": "...",
  "permission_mode": "...",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "<raw user input>"
}
```

Emitting this on stdout:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "<text>"
  }
}
```

...causes `<text>` to appear in Claude's context as a `<system-reminder>` block
tagged with the hook name, **adjacent to** the user's original message.

**Meta-test evidence.** When asked "how many times does the string
SENTINEL_X_42 appear in any message visible to you right now?", Claude
replied:

> The string `SENTINEL_X_42` appears **2** times.
> 1. In the `<system-reminder>` (UserPromptSubmit hook): ...
> 2. In your user message: ...

So the original `::Concise` sigil line remains in the transcript. Claude is
smart enough to ignore the sigil and follow the expanded instruction, but this
does mean the transcript will contain the sigil lines — a small UX cost, not
a blocker.

## Syntax decision

Verified with unit tests and an end-to-end session:

| Candidate | Collides with | Verdict |
|---|---|---|
| `@name`          | Claude Code file references (mid-line) | ❌ out |
| `/name`          | Slash commands (prompt-start)          | ❌ out |
| `#name`          | Memory-write convention in some tools  | ⚠️ avoid |
| `+++name`        | None (library-native syntax)           | ✅ ship |
| `::name` (BOL)   | None when anchored to start-of-line    | ✅ ship |
| `[[name]]`       | None                                   | ✅ alternative |
| YAML frontmatter | None                                   | ✅ alternative |

The hook translates `::Name(params)` → `+++Name(params)` internally before
calling the library, so the upstream regex doesn't need to change.

**Collision test that passed.** The prompt
`Look at my Rust code: use std::collections::HashMap;` correctly does NOT
trigger expansion — `(?m)^::` only matches at start-of-line.

## Unknown-decorator gotcha (fixed)

The engine silently drops unresolved decorator names and returns the clean
prompt body. The hook now compares the expanded output against the
sigil-stripped prompt and passes through unchanged when nothing was added,
so an unknown sigil does not become an injected message that the model
misinterprets.

## Auto-decorate path

`hooks/scripts/auto_decorate.py` demonstrates the pattern. Given
"Help me write a bash script to backup my home directory", Haiku returned:

```
+++Outline
+++Precision
+++Alternatives
Help me write a bash script to backup my home directory
```

...which the main hook then expands via the same engine. Latency in the spike
is ~2s because of the shelled-out `claude --print`. Production would:

- Call the Anthropic SDK directly.
- Cache the catalog manifest with prompt caching (the manifest is a fixed
  prefix; only the user prompt varies).
- Use `claude-haiku-4-5` which makes <400ms round-trips realistic.

## Open questions for the user

1. **Two commands or one sentinel?**
   - `/decorate auto` as a stateful toggle ("auto for next N prompts")
   - `::auto` sigil as a per-prompt opt-in
   - Config flag `autodecorate: always` for unconditional auto
   - My lean: support `::auto` + config flag; skip the slash-command state
     machine in v1.

2. **How aggressive should the default catalog be?**
   - All 142 decorators loaded (current behaviour)
   - Curated ~25 for coding workflows, opt-in for the rest via
     `/decorate enable <category>`
   - My lean: curate for v1, everything else gated behind a config toggle.

3. **Transcript noise.**
   - Accept the sigil lines staying in user messages (simpler, works today)
   - Add Claude-facing instruction "treat lines starting with `::` as metadata
     and ignore them" to the additionalContext (belt-and-suspenders)
   - My lean: ship without the extra instruction, add only if users report
     confusion.

4. **Learning loop (from `ideas/intent_to_decorator.md`).**
   - Skip for v1
   - Wire it in behind a `PROMPT_DECORATORS_LEARN=1` opt-in
   - My lean: skip for v1. The learning loop is a separate product decision.

## What this spike did NOT cover

- Packaging for distribution via the Synapti marketplace (`marketplace.json`
  entry, plugin install testing). The `.claude-plugin/plugin.json` is a
  stub — keywords and version are placeholder.
- Multi-OS testing. Only run on Linux.
- Python environment strategy for end users — the spike assumes the hook can
  `sys.path` into the repo. A shippable plugin needs to either vendor the
  engine or pin a pip install path.
- MCP server integration. The existing `prompt_decorators/integrations/mcp/`
  path is an alternative entry point worth evaluating if we decide we want
  Claude Code Desktop support as well.
- Windows path handling in `hooks.json` (`${CLAUDE_PLUGIN_ROOT}` vs. raw
  paths).
- Conflict-matrix enforcement. The library validates parameters but does not
  enforce decorator-pair conflicts at apply time. Deferred.

## Files in the spike

```
spike/
├── SPIKE_FINDINGS.md                     (this file)
└── claude-code-plugin/
    ├── .claude-plugin/
    │   └── plugin.json                    plugin manifest (stub)
    ├── hooks/
    │   ├── hooks.json                     UserPromptSubmit wiring
    │   └── scripts/
    │       ├── decorate_hook.py           the hook itself
    │       └── auto_decorate.py           auto-select prototype
    ├── commands/
    │   └── decorate.md                    slash-command stub
    └── tests/
        └── (empty — unit tests ran inline)
```

## Recommended next steps

1. Confirm direction on the four open questions above.
2. Wire a proper Anthropic SDK call into `auto_decorate.py` (with prompt
   caching) and measure real latency.
3. Decide packaging strategy (vendor vs. pip) and update `plugin.json`.
4. Add a curated catalog manifest so the auto-selector doesn't have to read
   all 142 decorators per call.
5. Add the plugin entry to the Synapti marketplace repo.
