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
5. Add a unit test proving the hook expands it correctly
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
- Must not collide with an existing decorator - check first:

    /decorate search <your-candidate-name>

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
| `reasoning` | Changes HOW the model thinks (ToT, Socratic, FirstPrinciples) |
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

<bad-example>
- Instruction text that says "please think about X" - too vague.
- Parameter with no `default` and `required: false` - confusing.
- Decorator that duplicates an existing one from a different category.
- Instruction longer than ~500 chars - decorators are supposed to be
  compact additions, not essays.
</bad-example>

### Step 4: Place the file

For a **personal** decorator (matches step 1's first row):

```
$HOME/.config/prompt-decorators/extensions/<your-namespace>/<decorator-name>.json
```

(override the base with `PROMPT_DECORATORS_USER_REGISTRY=/some/path`).

The plugin's `UserPromptSubmit` hook injects every JSON file found under
this directory into the engine at runtime via
`DynamicDecorator.register_decorator`, so the decorator is immediately
usable inline (`::YourName`) without any sync step.

For a **contribution** back to the shared catalogue (matches step 1's
second row), open a PR against `synaptiai/prompt-decorators` adding the
file under the appropriate `registry/core/<category>/` directory, and
then re-sync the vendor per `claude-code-plugin/VENDORING.md`.

The `<decorator-name>` in the filename should be lowercase kebab-case
(`confidence-intervals.json`) - the engine reads the `decoratorName` field
from inside, not the filename, but kebab-case filenames match the rest of
the registry.

### Step 5: Unit test

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
- No unit test proves end-to-end expansion.
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
**Test coverage:** `claude-code-plugin/tests/test_hook.py::test_my_new_decorator`

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
