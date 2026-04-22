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
- Write access to `claude-code-plugin/vendor/prompt_decorators/registry/extensions/`.

## Workflow

Use TodoWrite to track these mandatory steps:

<required>
1. Pick a name and category for the new decorator
2. Draft the decorator JSON using the schema template
3. Place the file under the correct extensions subdirectory
4. Add a unit test proving the hook expands it correctly
5. Verify end-to-end via the /decorate CLI
</required>

### Step 1: Pick a name and category

**Naming rules**
- PascalCase (e.g., `ConfidenceIntervals`, not `confidence_intervals`).
- Single-word preferred; multi-word only when unavoidable.
- Must not collide with an existing decorator - check first:

```bash
/decorate search <your-candidate-name>
```

**Category choice**

| Category | What belongs |
|---|---|
| `reasoning` | Changes HOW the model thinks (ToT, Socratic, FirstPrinciples) |
| `structure` | Changes the shape of the OUTPUT (Outline, Table, Bullet) |
| `tone` | Changes the VOICE of the response (Concise, Detailed, Formal) |
| `verification` | Adds CHECKS to the output (Cite, FactCheck, Confidence) |
| `minimal` | Extreme brevity (Short, TLDR) |
| `meta` | About decorators themselves (Override, Chain, Conditional) |

If none of those fit, use an extension category under
`registry/extensions/<your-namespace>/`.

### Step 2: Draft the decorator JSON

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

### Step 3: Place the file

For a personal/experimental decorator:

```
claude-code-plugin/vendor/prompt_decorators/registry/extensions/<your-namespace>/<decorator-name>.json
```

The `<decorator-name>` in the filename should be lowercase kebab-case
(`confidence-intervals.json`) - the engine reads the `decoratorName` field
from inside, not the filename, but kebab-case filenames match the rest of
the registry.

For a contribution back to the upstream catalogue, **do not edit
`vendor/`** directly - open a PR against `synaptiai/prompt-decorators`
adding the file to the appropriate `registry/core/<category>/` directory,
then re-sync the vendor (see `claude-code-plugin/VENDORING.md`).

### Step 4: Unit test

Add a test under `claude-code-plugin/tests/test_hook.py` proving the hook
expands your sigil:

```python
def test_my_new_decorator(tmp_path):
    out, rc = _run_hook(
        _event("::ConfidenceIntervals(style=qualitative)\nHow many users do we have?"),
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

### Step 5: Verify end-to-end

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
- The file is placed under `registry/core/<category>/` in the vendored
  copy (edit `synaptiai/prompt-decorators` upstream and re-sync instead).

## Output

After a successful authoring session, report:

```markdown
## Decorator Ready: <Name>

**File:** `claude-code-plugin/vendor/prompt_decorators/registry/extensions/<ns>/<name>.json`
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
