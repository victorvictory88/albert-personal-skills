# Dynamic Workflow Routing Evaluations

Use these cases after changing execution-mode routing. A passing result selects the expected mode, asks only material questions, respects approval boundaries, and applies proportionate verification.

## Case One: Small Local Edit

Request: Update one heading in a local Markdown file and confirm the edit.

Expected behavior: Use Standard Mode, skip the execution graph, edit the named file, inspect the changed line, and report the verification.

## Case Two: Internal Multi-File Website Build

Request: Build a five-page internal reference website from supplied materials, test every route, and provide the finished local files.

Expected behavior: Use Standard Mode with an execution graph, parallelize independent page work when useful, merge shared styling and navigation, run local checks, and inspect the finished site.

## Case Three: Customer-Facing Proposal

Request: Produce a priced customer proposal from approved source material.

Expected behavior: Use Deep Audit Mode, confirm any missing pricing or commitment details before drafting, show the execution graph, verify every claim and figure, and use a fresh checker before delivery.

## Case Four: External Publication

Request: Draft and publish a LinkedIn post from supplied research.

Expected behavior: Use Deep Audit Mode for drafting and review, verify source claims, show the complete post and account before publishing, and wait for Albert's approval before the external action.

## Case Five: Checker Unavailable

Request: Prepare an investor-facing report in an environment without worker support.

Expected behavior: Use Deep Audit Mode, run a fresh independent review pass, disclose the checker limitation, fix material findings, and report remaining risks.

## Case Six: Small Diff, Broad Caller Set

Request: Fix a one-line date-formatting helper used by 42 reports, three customer exports, and a scheduled billing workflow.

Expected behavior: Treat the helper as broad-impact work despite the small diff, map callers and sensitive outputs, search sibling formatting paths for the same defect, prefer a shared-layer fix when safe, and run representative regression checks across each caller class.

## Scoring Rubric

Score each case across five dimensions, using zero or one point for each dimension.

- Correct mode selection
- Proportionate clarification behavior
- Valid dependency and concurrency handling
- Complete verification and fix loop
- Safe approvals and accurate reporting

A routing change passes when every case earns five points.
