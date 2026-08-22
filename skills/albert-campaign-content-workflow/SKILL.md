---
name: albert-campaign-content-workflow
description: >-
  Use whenever the user asks for a marketing campaign, a content calendar, or content repurposing — e.g. "plan a campaign for our product launch," "build a content calendar for Q3," "repurpose this webinar into social posts," "turn this blog post into a LinkedIn carousel and three tweets." Runs a structured brief, research, planning, creation, and review workflow. It loads brand voice and audience context first, requires a cited source for every factual claim, applies a quality rubric before finalizing, and always delivers review-ready tables rather than loose prose. Trigger this even if the user doesn't use the word "campaign" or "calendar" explicitly, as long as they're asking to plan, schedule, or adapt content across channels or over time.
metadata:
  version: 1.0.0
---

# Campaign Content Workflow

You are running a content strategy workflow for three kinds of requests: **campaigns** (a coordinated push around a launch, event, or theme), **content calendars** (a scheduled slate of content over a time period), and **repurposing** (adapting one source asset into multiple channel-native formats). All three follow the same five-stage process below. The stages exist because content that skips straight to "create" tends to drift from the brand, misses the audience's actual questions, and can't be fact-checked after the fact — doing the earlier stages first is what makes the final table trustworthy enough to hand to a reviewer without a rewrite.

## Stage 0: Load Brand and Audience Context

Before writing a brief, gather what the brand sounds like and who it's for. Check, in order:

1. Any brand voice, style guide, or audience persona files already in the project (look for `brand`, `voice`, `style-guide`, `persona`, or `audience` in filenames near the working directory).
2. Anything the user has already told you in this conversation about tone, audience, or positioning.
3. If neither exists, ask directly — one batched set of questions, not a drip. At minimum: who is this for, what should it sound like, and what does this brand avoid saying.

Do not proceed to the brief until you have at least a working answer to "brand voice" and "audience" — everything downstream inherits from these two things, and guessing at them produces content that reads generic even when every other stage is done well.

## Stage 1: Brief

Fill out `templates/brief-template.md` with what you know, marking any assumed fields clearly. The brief is the contract for the rest of the workflow — it's what lets someone catch a scope or audience mismatch before you've spent effort on research and drafts. Share the completed brief back to the user only if the request is ambiguous enough that proceeding on a wrong assumption would waste real work; otherwise carry it forward silently and surface it inside the final review table.

## Stage 2: Research

Gather the facts, data points, and examples the content will lean on. For every factual claim you plan to make — a statistic, a trend, a competitor detail, a quote — capture its source now, while you still have it open. Do not backfill citations after drafting; that's when claims quietly go unsourced or get misattributed. Use web search or provided documents/data. If a claim can't be traced to a source, either drop it or flag it in the review table as unverified rather than presenting it as fact.

## Stage 3: Plan

Turn research into a structured plan appropriate to the request type:

- **Campaign**: a table of content pieces mapped to campaign phases (awareness/consideration/conversion or launch/sustain/close), channel, and owner.
- **Content calendar**: a table of scheduled posts/pieces by date, channel, and theme.
- **Repurposing**: a table mapping the source asset's key ideas to target formats and channels.

This is the point to check coverage against the brief — every stated goal and channel should show up somewhere in the plan — before any actual copy gets written.

## Stage 4: Create

Draft the actual content for each row in the plan: post copy, captions, headlines, calendar entries, or repurposed excerpts, matching the brand voice loaded in Stage 0. Keep drafts tied to their row in the plan so the final table stays traceable back to the brief and the research.

## Stage 5: Review

Before returning anything, run every piece through `templates/qa-checklist.md` covering accuracy/citations, brand voice alignment, audience fit, actionability, and formatting. Fix what fails; note in the output what you couldn't verify (e.g., "engagement projection is an estimate, not sourced data").

## Output Format

Always return a review-ready table, not prose paragraphs. Structure depends on request type but every table needs, at minimum: content/piece identifier, channel, draft copy or summary, source/citation (or "N/A"), and a status/notes column for anything the reviewer should double-check. Prose is fine as a short intro line above the table, but the deliverable itself is the table.

## Reference Files

- `templates/brief-template.md` — fill this out in Stage 1
- `templates/qa-checklist.md` — run every deliverable through this in Stage 5
