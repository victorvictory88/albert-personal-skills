---
name: albert-prompt-optimization
description: Primary eval-driven workflow for recurring prompts, global instruction systems, classifiers, extractors, routers, agent workflows, and automations with measurable outcomes. Use automatically when Albert asks to improve, debug, compare, audit, or systematize a prompt or instruction set that will run repeatedly. Add `albert-instruction-maintenance` when durable instruction edits will be applied. Do not use the full loop for one-off creative prompts.
---

# Albert Prompt Optimization

## Operating Rules

1. Define the job the prompt or instruction system performs and the expected output contract.
2. Gather representative examples, failure cases, edge cases, and accepted outputs.
3. Build a small evaluation set before rewriting when quality can be measured.
4. Change the smallest coherent set of variables needed to test the hypothesis.
5. Score outputs against the rubric before editing again.
6. Preserve eval cases, prompt versions, and durable lessons near the workflow when they will be reused.
7. For a new reusable prompt, deliver the prompt, consequential assumptions, evaluation rubric, and representative cases unless Albert requests a different format.

## Prompt Contract

Normalize each prompt into a working brief with only the fields needed for the task:

- Intended outcome or decision
- Relevant context and audience
- Hard constraints and approval boundaries
- Required evidence or source standard
- Success criteria and material failure modes
- Output format, length, and concrete tone choices

Resolve recoverable gaps from available sources. Ask one batched set of questions only when a missing or conflicting detail could materially change the result. Otherwise use sensible defaults, record consequential assumptions, and proceed.

When the prompt itself is the deliverable, rewrite it around outcomes instead of prescribing hidden reasoning or every execution step. State each requirement once. Keep process instructions only when the process is a requirement, safety boundary, or measured source of quality.

## Lean Prompt And Configuration Pass

- Remove one redundant instruction group, example set, or tool at a time, then rerun the same evals.
- Keep examples and style rules that encode a requirement or fix a measured gap.
- Treat model choice, reasoning effort or mode, and verbosity as configuration variables rather than prompt language. For difficult quality-first workflows, compare stronger settings when available instead of adding phrases such as "think harder."
- Preserve required facts, evidence, caveats, decisions, and next actions before trimming background or repetition.

## Evaluation Dimensions

Choose dimensions that match the job, such as:

- Correct skill or tool selection
- Instruction compliance
- Factual accuracy and source grounding
- Writing quality and audience fit
- Appropriate clarification behavior
- Verification quality
- Latency and unnecessary context loading
- Safe handling of external actions

## Output Shape

Report:

- What was weak in the prior version
- What changed and why
- How the new version was checked
- Remaining failure modes
- Eval cases to add next

Optimize for the measurable target first, then polish wording.

For audits of task-intake behavior, read and run [references/prompt-intake-evals.md](references/prompt-intake-evals.md). Add cases only when they represent a recurring or costly failure.
