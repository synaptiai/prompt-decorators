---
name: authoring-decorators
description: Use when the user wants to write a new prompt decorator - either a personal one for their repo or a contribution back to the upstream catalogue. Walks through the JSON schema, the extensions/ convention, and how to test a new decorator end-to-end through the hook.
context: fork
agent: general-purpose
---

# Authoring Decorators

This skill guides creation of a new decorator: where the JSON file lives,
what fields it needs, and how to verify it works end-to-end via the
`UserPromptSubmit` hook.

## Prerequisites

- The `prompt-decorators` plugin is installed.
- The user has a concrete behaviour they want a decorator to codify (e.g.,
  "always format output as XML", "always include confidence intervals").
- Write access to `$HOME/.config/prompt-decorators/extensions/` for personal decorators, OR write access to the upstream `synaptiai/prompt-decorators` repo for contributions back.

## Workflow

Use TodoWrite to track these mandatory steps:

<required>
1. Decide whether the decorator is personal (stays local) or a contribution (goes upstream)
2. Pick a name and category
3. Draft the decorator JSON using the schema template
4. Place the file in the correct directory (per step 1's decision)
5. Cover the behaviour with a test — committed test for contributions, Step 6 smoke-test for personal
6. Verify end-to-end via the /decorate CLI
</required>

### Step 1: Decide destination

Two legitimate destinations exist, and choosing wrong loses your work:

| Use case | Destination | Survives vendor sync? |
|---|---|---|
| Personal decorator for your workflow | `$HOME/.config/prompt-decorators/extensions/<your-namespace>/<name>.json` (or set `PROMPT_DECORATORS_USER_REGISTRY` to a path of your choice) | Yes - independent of plugin |
| Contribution back to the shared catalogue | Upstream repo `synaptiai/prompt-decorators/registry/extensions/<namespace>/<name>.json`, open a PR, then re-sync the vendor (see `claude-code-plugin/VENDORING.md`) | Yes - becomes part of upstream |

**Do NOT place personal decorators under
`claude-code-plugin/vendor/prompt_decorators/registry/`.** The vendored
copy is periodically wiped and re-synced from upstream (see
`claude-code-plugin/VENDORING.md`), so anything under `vendor/` that
isn't in the source-of-truth upstream repo gets silently deleted on the
next sync.

### Step 2: Pick a name and category

**Naming rules**
- PascalCase (e.g., `ConfidenceIntervals`, not `confidence_intervals`).
- Single-word preferred; multi-word only when unavoidable.
- Must not collide with an existing decorator - check first.

    From inside an interactive Claude Code session:

        /decorate search <your-candidate-name>

    Equivalent from a terminal (works without Claude Code):

        python3 claude-code-plugin/scripts/dispatch.py search <your-candidate-name>

    Exit code 0 + `(matches: 1)` means a collision. Exit code 1 + `No decorators match '...'` means the name is free.

**Shadowing (intentional but surprising):** a user decorator with the
same name as a vendored core decorator *replaces* the core one. This is
deliberate - it lets you override catalogue behaviour without forking
the upstream repo - but it's a sharp edge. The hook logs a
`user_registry_shadow` event when it happens (visible with
`PROMPT_DECORATORS_LOG_DEBUG=1`). If you didn't mean to shadow a core
name, rename your decorator.

**Category choice**

| Category | What belongs |
|---|---|
| `reasoning` | Changes HOW the model thinks (TreeOfThought, Socratic, FirstPrinciples, RedTeam) |
| `structure` | Changes the shape of the OUTPUT (Outline, TableFormat, Bullet, Summary, Comparison) |
| `tone` | Changes the VOICE of the response (Concise, Detailed, Academic, Professional, ELI5) |
| `verification` | Adds CHECKS to the output (CiteSources, FactCheck, Confidence, Uncertainty) |
| `minimal` | Foundational base-layer decorators — OutputFormat, Reasoning, StepByStep, Tone, Version. Do NOT use for brevity (that's Concise/ELI5 in `tone`). |
| `meta` | About decorators themselves (Override, Chain, Conditional) |

If none of those fit, use an extension category under
`registry/extensions/<your-namespace>/`.

### Step 3: Draft the decorator JSON

Minimal schema:

```json
{
  "decoratorName": "ConfidenceIntervals",
  "version": "1.0.0",
  "description": "Include a confidence range with every quantitative claim.",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "parameters": [
    {
      "name": "style",
      "type": "enum",
      "description": "Numeric range or qualitative label.",
      "default": "numeric",
      "required": false,
      "enum": ["numeric", "qualitative"]
    }
  ],
  "transformationTemplate": {
    "instruction": "For every quantitative claim in your response, include a confidence range. If style is numeric, use ranges like 40-60. If qualitative, use labels like 'high confidence' / 'low confidence'.",
    "parameterMapping": {
      "style": {
        "format": "Style preference: {value}."
      }
    }
  }
}
```

<good-example>
- `decoratorName` is PascalCase and unique.
- `description` is one short sentence readable by the `/decorate list` output.
- `parameters` declare types (`string`, `number`, `boolean`, `enum`, `array`,
  `object`) with defaults where sensible.
- `transformationTemplate.instruction` is the instruction the model will see -
  imperative, specific, under 400 chars.
</good-example>

**`parameterMapping`: pick `format` or `valueMap` per parameter**

- `format` — free-form parameters (`string`, `number`, `boolean`). The
  `{value}` placeholder is substituted with whatever the user passed.

    ```json
    "depth": { "format": "Use depth level {value}." }
    ```

- `valueMap` — enum parameters. Map each declared enum value to a specific
  instruction fragment; the engine selects one at expansion time.

    ```json
    "style": {
      "valueMap": {
        "numeric":     "Use numeric ranges like 40-60.",
        "qualitative": "Use labels like 'high confidence' / 'low confidence'."
      }
    }
    ```

  Every value in the parameter's `enum` list should have a matching
  `valueMap` entry — missing keys fall through to the base `instruction`.

<bad-example>
- Instruction text that says "please think about X" - too vague.
- Parameter with no `default` and `required: false` - confusing.
- Decorator that duplicates an existing one from a different category.
- Instruction longer than ~500 chars - decorators are supposed to be
  compact additions, not essays.
</bad-example>

### Step 4: Place the file

For a **personal** decorator (matches step 1's first row):

```bash
# Create the namespace dir. The hook discovers decorators by scanning this
# tree but does NOT auto-create it; without the mkdir, your JSON goes
# nowhere.
mkdir -p "$HOME/.config/prompt-decorators/extensions/<your-namespace>"

# Write the decorator JSON (replace path with your editor of choice).
$EDITOR "$HOME/.config/prompt-decorators/extensions/<your-namespace>/<decorator-name>.json"
```

Override the base directory with `PROMPT_DECORATORS_USER_REGISTRY=/some/path`
if you want a different location. Once the file lands anywhere under the
user-registry tree, the `UserPromptSubmit` hook and `/decorate preview`
both register it via `DynamicDecorator.register_decorator` at runtime - the
decorator is usable inline (`::YourName`) with no sync step.

For a **contribution** back to the shared catalogue (matches step 1's
second row), open a PR against `synaptiai/prompt-decorators` adding the
file under the appropriate `registry/core/<category>/` directory, and
then re-sync the vendor per `claude-code-plugin/VENDORING.md`.

The `<decorator-name>` in the filename should be lowercase kebab-case
(`confidence-intervals.json`) - the engine reads the `decoratorName` field
from inside, not the filename, but kebab-case filenames match the rest of
the registry.

### Step 5: Unit test

Testing guidance differs by destination.

**Personal decorator** (step 1's first row):

Do **not** add a committed test. A test referencing a JSON file in your
`$HOME/.config/` would fail for every other contributor — the file doesn't
exist on their machine. Rely on the end-to-end smoke test in Step 6 to
prove your decorator expands correctly; that's the canonical verification
for personal decorators.

**Contribution decorator** (step 1's second row):

Add a test under `claude-code-plugin/tests/test_hook.py` proving the hook
expands your sigil. Reuse the shared helpers from `tests/conftest.py`:

```python
import json

from conftest import make_event, run_hook_subprocess


def test_my_new_decorator(tmp_path):
    out, _, rc = run_hook_subprocess(
        make_event("::ConfidenceIntervals(style=qualitative)\nHow many users do we have?"),
        env={"PROMPT_DECORATORS_CONFIG_DIR": str(tmp_path)},
    )
    assert rc == 0
    data = json.loads(out)
    ctx = data["hookSpecificOutput"]["additionalContext"]
    assert "confidence" in ctx.lower()
    assert "qualitative" in ctx.lower()
```

Run the suite:

```bash
cd claude-code-plugin && python3 -m pytest tests/ -q
```

### Step 6: Verify end-to-end

```bash
# Browse the catalogue to confirm registry pickup.
python3 claude-code-plugin/scripts/dispatch.py search "ConfidenceIntervals"

# Preview the expansion your users will see.
python3 claude-code-plugin/scripts/dispatch.py preview ConfidenceIntervals

# Exercise the hook directly.
echo '{"hook_event_name":"UserPromptSubmit","prompt":"::ConfidenceIntervals\nHow many users?"}' | \
  python3 claude-code-plugin/hooks/scripts/decorate_hook.py
```

The last command should print a JSON object whose `additionalContext`
field contains your instruction text.

## User Interaction

Use the **AskUserQuestion tool** when:

### The category is ambiguous

```
Question: "Your decorator affects <aspect>. Which category best fits?"
Options:
- "reasoning (changes how the model thinks)"
- "structure (changes output shape)"
- "tone (changes voice)"
- "verification (adds checks)"
- "Let me specify an extension namespace"
```

### The decorator duplicates an existing one

If `/decorate search` finds a close match, surface it:

```
Question: "<MatchName> already exists with the description '<existing-desc>'.
Your candidate '<your-desc>' overlaps. What do you want to do?"
Options:
- "Extend <MatchName> with a new parameter instead"
- "Ship mine anyway (distinct enough)"
- "Pick a different name"
```

## Failure Conditions

The decorator is not ready to ship if any of these hold:

- `/decorate search <name>` finds an existing decorator with the same name.
- The `transformationTemplate.instruction` text is longer than ~500 chars
  (signals the decorator is doing too many things at once - split it).
- End-to-end expansion is unverified. For a **personal** decorator, Step 6's
  hook smoke-test must produce an `additionalContext` containing the
  instruction text. For a **contribution** decorator, a committed test in
  `claude-code-plugin/tests/test_hook.py` must pass.
- Parameter validation is absent for enum-style params.
- The file is placed under `claude-code-plugin/vendor/...` - the vendored
  copy is wiped on every upstream sync. Put personal decorators in
  `$HOME/.config/prompt-decorators/extensions/`, or open an upstream PR
  against `synaptiai/prompt-decorators` for contributions.

## Output

After a successful authoring session, report:

```markdown
## Decorator Ready: <Name>

**File:** `$HOME/.config/prompt-decorators/extensions/<ns>/<name>.json` (personal) OR `synaptiai/prompt-decorators/registry/extensions/<ns>/<name>.json` (contribution)
**Category:** <category>
**Verification:** Step 6 hook smoke-test output (personal) OR `claude-code-plugin/tests/test_hook.py::test_my_new_decorator` (contribution)

**Preview:**
    /decorate preview <Name>

**Try it:**
    ::<Name>
    <your prompt>
```

## References

- JSON schema: `claude-code-plugin/vendor/prompt_decorators/schemas/decorator_schema.json`
- Sync policy: `claude-code-plugin/VENDORING.md`
- Full decorator spec (upstream):
  https://synaptiai.github.io/prompt-decorators/prompt-decorators-specification-v1.0/
