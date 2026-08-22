---
name: albert-instruction-maintenance
description: Apply and route durable changes to Albert's instruction and preference system. Use automatically when Albert says to remember a preference, corrects recurring assistant behavior, states how he wants future work handled, asks to update global instructions or a skill, or when a repeated workflow lesson should be stored. For an instruction audit or optimization, use `albert-prompt-optimization` as the primary workflow and add this skill only when edits will be applied. Do not trigger for one-off task feedback that has no future value.
---

# Albert Instruction Maintenance

## Decide Whether The Signal Is Durable

- Treat an explicit future-facing preference or instruction as durable.
- Treat a repeated correction or repeated acceptance pattern as durable when the pattern is clear.
- Keep one-off requests, temporary context, and task-specific constraints inside the current task.
- Ask Albert only when the intended scope or permanence would materially change where the rule belongs.

## Route To The Narrowest Source

- Shared behavior across tools and workspaces: `/Users/albertchan/Desktop/AI/About Me/Global Instructions.md`
- Stable personal facts, biography, family, career, or personal priorities: `/Users/albertchan/Desktop/AI/About Me/About Me.md`
- Repeatable procedure, rubric, tool workflow, or artifact standard: the relevant skill or a focused new skill under `/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/Skills`
- Shared skill discovery: link the canonical skill source into `~/.agents/skills`, `~/.codex/skills`, and `~/.claude/skills`; keep product-specific skills isolated to their product
- Retired skill: after creating a rollback snapshot, move the canonical skill under a dated folder in `/Users/albertchan/Desktop/AI/Outputs/_archive` and remove its discovery symlinks
- Project-specific commands, paths, constraints, or verification rules: the nearest `AGENTS.md` or `CLAUDE.md`
- Changing day-to-day context: the Daily Brain Dump, only when Albert authorizes an external edit
- Mechanical product settings: the relevant configuration file, never prose instructions

## Update Process

1. Inspect the current source and nearby rules before editing.
2. Look for an existing rule to revise or consolidate.
3. Before a substantial instruction-system refactor, run `python3 /Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/instruction_doctor.py snapshot --label <short-label>`.
4. Make the smallest change that captures the durable lesson.
5. Remove or reconcile any contradiction introduced by the change.
6. Keep skill trigger conditions in frontmatter descriptions rather than a global routing catalog.
7. Run targeted routing evaluations, validate changed skills, then run `python3 /Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/instruction_doctor.py check`.
8. Inspect the final instruction chain, verify discovery from Codex and Claude, and repair every failed check.
9. Tell Albert what changed, where it changed, and why.

## Size And Quality Guardrails

- Treat the global file as a fixed budget of 1,650 words rather than a growing document. At the ceiling, every new rule requires removing or relocating an equal amount, usually by moving repair guidance into the owning skill. The instruction doctor enforces the ceiling.
- Keep personal context conditional and stable. Move changing priorities out of the personal profile.
- Keep each skill focused on one job and use progressive disclosure for detailed references or scripts. Review any `SKILL.md` above roughly 1,500 words for a split, and move the parts that only some routes need into `references/`. Keep material that every run consumes inside `SKILL.md`, because a split that hides an always-needed rule trades quality for tokens and quality ranks first.
- Do not duplicate platform safeguards, skill catalogs, or workflow steps across several files. When two skills carry the same facts or rules, extract one shared reference and point both at it.
- Keep rule text in one canonical place. A memory file should hold the origin and rationale that the canonical file omits, rather than restating the rule.
- Preserve a versioned rollback snapshot with file hashes before substantial instruction-system refactors.
- Run the instruction doctor and targeted evaluations when the global file, personal profile, routing, or skill set changes substantially.
