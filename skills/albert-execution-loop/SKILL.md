---
name: albert-execution-loop
description: End-to-end build, review, fix, and report workflow for implementing or changing code, documents, spreadsheets, presentations, automations, templates, multi-file artifacts, or multi-system workflows that require tests, render checks, visual QA, connector readback, or a durable definition of done. Use automatically when Albert asks for a finished implementation or deliverable with meaningful verification. Do not trigger for advice-only, research-only, decision-only, or instruction-only work unless implementation extends beyond instruction files.
---

# Albert Execution Loop

## Intake And Definition Of Done

Clarify only gaps that materially change the output. For substantial work, establish:

- Required output and location
- Audience and purpose
- Source of truth
- Scope and constraints
- Approval boundaries
- Verification method

Use existing context to answer routine gaps and proceed on safe assumptions.

## Dynamic Workflow Routing

Choose the smallest mode that still protects the result.

### Standard Mode

Use Standard Mode for most bounded implementation and deliverable work.

1. Build a concise working brief from the request and available sources.
2. Ask one batched question set only when missing information could materially change quality, scope, risk, cost, or an external action.
3. For substantial work, show a concise execution graph with major steps, true dependencies, parallel branches, merge points, and verification points. Keep the graph operational and omit hidden reasoning.
4. Run independent branches concurrently when tools and task structure support concurrency.
5. Merge branch outputs, inspect the assembled result, fix material defects, and report verification.

### Deep Audit Mode

Use Deep Audit Mode when Albert requests it or when the work is high-stakes, external-facing, expensive, hard to reverse, multi-system, or structurally complex.

1. Show the execution graph before implementation begins, except when a safety check or approval must come first.
2. Apply the complete build, review, verify, and fix loop.
3. Use a separate checker with fresh context when the available tools support one. Give the checker the request, success criteria, final artifact, and source evidence while withholding the producer's conclusions.
4. When a separate checker is unavailable, perform a fresh independent review pass and disclose that limitation.
5. Audit unnecessary dependency waits, parallel-branch coverage, merge gaps, unsupported claims, approval boundaries, and final-format compliance.
6. Return the finished result, verification summary, checker findings, fixes applied, remaining risks, and consequential assumptions.

Use [references/dynamic-workflow-evals.md](references/dynamic-workflow-evals.md) when changing this routing logic.

## Execution Loop

1. Build: use existing skills, plugins, scripts, templates, and project patterns first.
2. Review: compare the output with every requirement and the definition of done. Inspect the artifact rather than relying on a summary. When a defect may repeat, search sibling instances and related paths before closing it.
3. Verify: run the relevant tests, renders, visual checks, source checks, or connector readbacks.
4. Fix: address defects and repeat review and verification until the work passes or needs Albert's decision.
5. Report: state what changed, what passed, what was verified, and any remaining risk.

## Fix Scope And Review Depth

- Identify the shared layer that affected paths flow through, including helpers, templates, schemas, prompts, configuration, and source data.
- Prefer a shared-layer fix when it removes the cause across affected paths without adding brittle coupling or unnecessary complexity.
- Inspect sibling instances for the same failure pattern. Fix confirmed instances inside the authorized scope, and report any instance that needs separate authority or evidence.
- Set review depth from caller count, user impact, reversibility, external side effects, data sensitivity, and failure detectability. File count and diff size are secondary signals.
- Treat a one-line change in a widely used helper as broad-impact work. Treat a larger isolated change as bounded work when its callers, data, and rollback path stay narrow.

## Coverage And Independent Review

- Use focused parallel workers for broad reading, codebase sweeps, log analysis, source verification, or coverage only when they improve quality or speed.
- Use an independent critic under the Deep Audit Mode rules when it can catch meaningful defects.
- Keep worker scopes narrow and audit important claims against the source material.

## Reusable Workflow Design

When the workflow will recur, identify:

- Inputs
- Standard or rubric
- Producer
- Reviewer and verification
- Fix loop
- Storage location
- Delivery or approval point

Suggest a script, skill, template, automation, or scheduled routine when it improves reliability. Create or schedule it only after Albert approves cadence, permissions, and external effects.
