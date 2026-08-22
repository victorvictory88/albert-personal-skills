---
name: albert-website
description: Build, revise, validate, and publish Albert Chan's role-specific candidate application sites. Use when Albert types "/website," provides a job description and asks for a site or candidate page, asks to update an existing application site, or asks to publish a candidate site. This skill owns the complete workflow from job intake and claim grounding through Sites deployment and live readback. Do not use for general websites, resume-only work, or another person's application materials.
---

# Candidate Application Sites

Create a polished, role-specific case that positions Albert as the strongest credible candidate. Default to a deployed Sites project. Deliver a local-only artifact only when Albert asks for one.

Use `albert-writing-style` for every visible word. Use `sites-building` for implementation and validation, then `sites-hosting` for versioning and deployment. Use `imagegen` when a new or materially revised site needs a social-preview card.

## Load Sources Before Writing

Read these sources in order on every run:

1. `/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/resume-builder/job-application-facts.md`
2. `references/candidate-profile.md`
3. `references/page-spec.md`

Read `references/sites-workflow.md` when creating, retrieving, versioning, publishing, or checking a Sites project.

The shared facts file governs claim hierarchy, current employment, Meta and BPO framing, Rowland claims, and lead credentials. Every metric and career claim must trace to an approved source or a fact Albert supplies in the current request. Record newly supplied durable facts in the proper source only when the task includes that update.

## Establish The Brief

For a new site, obtain a job description through pasted text, PDF, or reachable URL. Identify:

- company and exact role title
- hiring manager's primary screening requirements
- Albert's strongest differentiating credential for those requirements
- company palette and visual cues
- requested access level and publishing intent

For an existing site revision, inspect the current source and live page first. Preserve the role, company, design system, architecture, package manager, lockfile, project ID, and source history unless Albert requests a change.

Proceed with grounded assumptions when gaps carry low risk. Pause when missing information would invent a claim, change the target role, create a public commitment, or alter access.

## Select The Project Path

### Existing site

Locate the local project through `.openai/hosting.json` or match the supplied Sites URL through the Sites connector. Retrieve the existing source repository and work inside its established output folder. Preserve user changes and avoid recreating the project.

### New site

Create the project under:

`/Users/albertchan/Desktop/AI/Outputs/[company-slug]-[role-slug]`

Initialize it through `sites-building`, preserve the generated framework, and persist the Sites project ID in `.openai/hosting.json`. Use lowercase hyphenated slugs.

### Explicit local HTML request

Create a self-contained `index.html` only when Albert specifically asks for HTML or local-only delivery. Apply the content, writing, visual, and verification rules from this skill.

## Build The Candidate Case

Design the first viewport around the hiring decision:

- Place Albert's photo and role-specific positioning together on desktop.
- Lead the first paragraph with the strongest current credential.
- Surface current industry or customer focus immediately when it strengthens the role fit.
- At 960 pixels and below, show the strongest positioning before the photo if stacking would bury the message.

Use `references/page-spec.md` for the page structure and visual system. Select proof and stats for the role rather than copying a standard set. Connect every experience entry to the target company's current need. Give every proof card a sourced number. Make the company-specific rationale the sharpest argument on the page.

For an existing site revision, update every affected layer:

- hero and supporting copy
- evidence cards, timeline, and company rationale
- tests and assertions
- title, description, Open Graph, and social metadata
- social-preview image when the positioning changes materially

Create versioned social assets such as `og-v2.png`. Inspect generated text and dimensions before wiring the asset into metadata. Preserve the prior asset for rollback.

## Validate Before Publishing

Complete the full loop:

1. Install existing dependencies only when absent.
2. Run the production build and project tests.
3. Run lint and fix every error. Report non-blocking inherited warnings.
4. Render the actual page HTML and run:

```bash
python3 "/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/resume-builder/scripts/check_application_artifact.py" "<rendered-html-path>"
```

5. Search visible copy for banned wording, placeholders, unsupported claims, incorrect company names, current-tense Meta references, and every use of `400`.
6. Confirm the headshot fallback, link security, metadata, and social image.
7. Visually inspect the opening viewport at desktop width and the 960-pixel breakpoint. Confirm the strongest positioning appears beside the photo on desktop and before buried content on stacked layouts.
8. Fix defects and repeat the failed checks.

The checker must pass against rendered HTML. A source-file false positive does not replace the rendered-page gate.

## Publish And Read Back

Follow `references/sites-workflow.md` and `sites-hosting` after validation.

- Commit the exact validated source with a descriptive message.
- Push with a short-lived per-command credential and keep the token private.
- Package the validated build, save a numbered site version, and retain its version ID.
- For public or shared sites, prepare the reversible source and saved version before review when useful. Albert's approval gates the production deployment.
- Use owner-only deployment when access is verified as private.
- Obtain Albert's explicit approval immediately before a public or shared deployment unless his current request already approves publication.
- Poll the deployment through success or failure.
- Open the successful production URL in Codex.
- Read the live endpoint back and verify the new hero copy, metadata, and social asset. Allow for propagation and keep checking when the deployment succeeds before the endpoint updates.

Stop the local server after hosting finishes. Leave the worktree clean and preserve prior versions for rollback.

## Handoff

Lead with the production URL. Summarize the positioning change, responsive behavior, saved site version, and social-preview update. Report the checks that passed and any inherited warning or remaining risk.

Close with the required `Verified:` and `NOT RUN:` lines.
