---
name: albert-research-synthesis
description: Source-grounded research, market or competitor analysis, vendor evaluation, and evidence synthesis. Use automatically when Albert asks to compare sources, resolve conflicting evidence, investigate a current or niche topic, produce a research report, or ground a recommendation in current facts. This skill owns evidence gathering and synthesis. Add `albert-decision-work` only when Albert also needs a consequential choice or commitment.
---

# Albert Research Synthesis

## Core Standard

Produce source-grounded synthesis rather than a pile of notes. Separate facts, source-backed claims, inferences, contradictions, blind spots, recommendations, and open questions whenever mixing them could confuse the answer.

For quick factual lookups, answer directly and name the source. For research reports, market maps, competitor analysis, vendor evaluation, or source-dependent recommendations, run the full workflow.

## Workflow

1. Define the question, audience, expected output, and evidence standard.
2. Gather current source-grounded perspectives. Prefer primary sources, official documentation, filings, transcripts, direct product pages, and named experts.
3. Compare definitions, incentives, time windows, and source quality.
4. Map conflicts, missing evidence, stale data, source bias, and association risk.
5. Synthesize the answer with confidence levels and source support for important claims.
6. State the evidence that would change the conclusion.

## Evidence Rules

- Browse or use connected sources when information could have changed, the topic is niche, the user asks for current information, spending or reputation is involved, or source attribution improves trust.
- Pull private connector content before making claims about it. Never infer messages, meetings, documents, or records from memory.
- Cite web sources in the final answer unless Albert requests an internal format without citations.
- Make uncertainty visible when the available evidence cannot support a firm conclusion.

## Decision Boundary

Use `albert-decision-work` alongside this skill only when the research must support a consequential choice. Hand the evidence, conflicts, and uncertainty into the decision process rather than repeating both workflows.

## Output Shape

Lead with the answer or recommendation. Present facts and evidence next, followed by inferences and tradeoffs. End with open questions, risks, and what would change the conclusion. Use `albert-writing-style` for substantive prose.
