---
name: prompt-decorators-usage
description: Use when a user's prompt would clearly benefit from a reasoning, structure, tone, or verification decorator - or when they ask "what decorators should I use?". Teaches when and how to suggest inline `::Name(params)` sigils instead of repeating verbose prompt-engineering instructions manually.
context: fork
agent: general-purpose
---

# Prompt Decorators Usage

This skill teaches when to suggest prompt decorators to the user and how to
apply them - either as inline sigils, always-on config, or by switching on
auto-decorate mode.

## Prerequisites

- The `prompt-decorators` plugin is installed (the user installed it from
  the Synapti marketplace).
- The `UserPromptSubmit` hook is wired and active.
- The 143-decorator catalogue is available - browse with `/decorate list`
  or `/decorate search <term>`.

## Workflow

Use TodoWrite to track these steps when invoked from another workflow:

<required>
1. Identify the decoration intent (reasoning / structure / tone / verification / minimal / meta)
2. Pick 1-3 decorators from the catalogue that match the intent
3. Decide the delivery method (inline, always-on, or auto mode)
4. Communicate the suggestion to the user with exact syntax
</required>

### Step 1: Identify the decoration intent

Match the user's prompt to one of the catalogue's six core categories:

| Category | Trigger phrases in the prompt | Typical decorators |
|---|---|---|
| **reasoning** | "why", "explain", "analyze", "compare", "pros/cons", "trade-offs" | `Reasoning`, `StepByStep`, `TreeOfThought`, `FirstPrinciples`, `RedTeam` |
| **structure** | "list", "outline", "summarize", "table", "bullet", "organize" | `Outline`, `Summary`, `TableFormat`, `Comparison`, `Bullet` |
| **tone** | "concise", "brief", "detailed", "academic", "casual" | `Concise`, `Detailed`, `Academic`, `Casual` |
| **verification** | "verify", "fact-check", "cite", "sources", "evidence" | `FactCheck`, `Cite`, `Confidence` |
| **minimal** | "short", "one sentence", "quick", "tl;dr" | `Short`, `TLDR` |
| **meta** | asking about decorators themselves | `Override`, `Chain`, `Conditional` |

<good-example>
**User prompt:** "Compare REST and GraphQL, including pros and cons in a table."
**Intent:** reasoning + structure.
**Suggestion:** `::Comparison` + `::TableFormat`.
</good-example>

<bad-example>
**User prompt:** "What's 2+2?"
**Intent:** none. Don't suggest decorators for trivial prompts - the decoration overhead outweighs the benefit.
</bad-example>

### Step 2: Pick 1-3 decorators

Use `/decorate search <term>` to confirm the decorator exists and to read
its one-line description. Use `/decorate preview <Name>` to see the exact
instruction text it expands into.

Rules of thumb:

- **Never more than 3** decorators stacked - they start to contradict each
  other.
- **Never stack two from the same category** unless the category is explicitly
  combinable (e.g., `Concise` + `StepByStep` is fine; `Detailed` + `Concise`
  is not).
- **Prefer concrete decorators over meta ones.** `+++StepByStep` usually
  beats `+++Chain(steps=5)`.

### Step 3: Decide the delivery method

| Pattern | When to recommend |
|---|---|
| **Inline** (`::Name` at start of prompt) | One-off use, or when the user is already thinking about this specific prompt |
| **Always-on** (`/decorate always add <Name>`) | User indicates a persistent preference ("always be concise", "always show me the reasoning") |
| **Auto mode** (`/decorate auto on`) | User is exploring and wants the model to pick decorators for them |
| **Auto one-shot** (`/decorate auto once`) | User wants the selector to try, just for the next prompt, without committing |

### Step 4: Communicate the suggestion

Show the user the exact syntax they should type. Example output:

```
For this prompt, try:

    ::Comparison
    ::TableFormat
    Compare REST and GraphQL, including pros and cons.

The hook will expand those sigils into precise instructions before the
model sees the prompt.
```

If the user has never used decorators before, include a one-line pointer
to `/decorate help` so they can discover the rest of the surface.

## User Interaction

Use the **AskUserQuestion tool** when:

### The intent is ambiguous

```
Question: "Your prompt could benefit from different decorator families. Which
flavour do you want?"
Options:
- "Concise + Structured (short, in a table)"
- "Detailed reasoning (why this is the right answer)"
- "Verification (cite sources, flag uncertainty)"
- "Let me pick from the catalogue"
```

### The user asks "what decorators exist?"

Run `/decorate list` and relay the output. Do not try to memorise the
catalogue - it's 143 entries across 14 categories and it changes.

### The user wants auto-decorate but is worried about cost/latency

```
Question: "Auto-decorate adds ~400ms per prompt (Haiku round-trip). You
can pick per-prompt or session-wide."
Options:
- "Enable it for this one prompt only (/decorate auto once)"
- "Enable it for the whole session (/decorate auto on)"
- "Skip it - I'll pick decorators manually"
```

## Failure Conditions

The suggestion is unacceptable if any of these hold:

- The decorator name doesn't exist in the registry (always verify with
  `/decorate list` first).
- More than 3 decorators are suggested.
- Two decorators from the same narrow subcategory are stacked (e.g., two
  tone decorators).
- The suggestion ignores the user's stated preference in their always-on
  config (check `/decorate config` before suggesting additions).

## Output

When suggesting decorators, use this format:

```markdown
**Suggested decorators:** `::Concise` + `::StepByStep(numbered=true)`

Rationale: your prompt asks for a short, structured walkthrough - those
two compose cleanly without contradicting each other.

Try:

    ::Concise
    ::StepByStep(numbered=true)
    <your original prompt>
```

## References

- Full catalogue: `/decorate list` (143 decorators across 14 categories)
- Preview a decorator: `/decorate preview <Name>`
- Search by keyword: `/decorate search <term>`
- Inline syntax reference: `claude-code-plugin/README.md`
