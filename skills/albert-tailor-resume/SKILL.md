---
name: albert-tailor-resume
description: >
  Tailored resume generator for Albert Chan's job applications. Use this skill whenever
  the user types "/tailor-resume", asks to tailor, customize, adapt, or build Albert's
  resume for a specific job, company, or posting, or provides a job description and asks
  for a resume. Triggers on: "tailor my resume", "resume for this role", "build a resume
  for [company]", "update my resume for this JD", "make my resume fit this posting".
  Do NOT use for other people's resumes, general resume advice with no target role, or
  the job application website (use the website skill for that).
---

# Tailored Resume Generator

You generate a one-to-two page, role-specific PDF resume for **Albert Chan** from his
canonical master resume, using the existing ReportLab build system. The output must read
like it was written for this exact posting, while every claim stays traceable to the master.

## Source of truth

1. **Shared facts (content rules):** `/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/resume-builder/job-application-facts.md`
   Shared with the `albert-website` skill. It holds the source-of-truth hierarchy, current employment
   facts, the Rowland claims rule, the Meta and BPO positioning rules, job description intake,
   and the writing rules for generated artifacts. Read it at Step 1. Edit that file rather than
   restating any of it here.
2. **Master resume (content):** `/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/resume-builder/Albert Chan Resume 2026 - Rewritten.md`
   Every job, metric, and award must trace to this file. Never use the original resume PDF.
3. **Build engine (format):** `/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/resume-builder/scripts/build_tailored_resumes.py`
   Import `build_resume` and `common_education` from it. Never re-implement the PDF layout.
4. **Foundation script:** `scripts/build_openai_ads_resume.py` is the resume Albert keeps as his
   base, confirmed 2026-07-27. Copy it as the starting template for every new role and edit from
   there. Superseded per-role scripts were archived to
   `Outputs/_archive/2026-07-27-superseded-resume-scripts/`, so read one from there only when a
   past role closely matches the new target.

**Inline backstop, true even if the shared file goes unread.** Meta is a past role, 2022 to
May 2026, always past tense. Albert's current role is President and Chief AI Officer at
Rowland AI, since 5/18/2026. Any mention of the 400 sellers names them as vendor-employed
through 5 BPO partners, written as "directing 5 BPO vendor partners with 400 vendor-employed
sellers," never as "400-seller organization," "led 400 sellers," "400-person sales team," or
"400 reps."

## Process

### Step 1: Read the shared facts file, then the job description
Read the shared facts file first. Job description intake, including the unreachable-URL case,
is covered there.

Identify before writing anything:
1. Company, exact role title, and seniority level
2. The 4-6 requirements the hiring manager will screen for
3. Albert's single most differentiating credential for this role
4. Which existing build script is the closest starting template

### Step 2: Write the build script
Create `scripts/build_[company]_[role]_resume.py` (lowercase, underscores). Structure:

```python
from build_tailored_resumes import build_resume, common_education

resume = {
    "title": "Albert Chan Resume - [Company] [Role]",
    "file": "Albert_Chan_Resume_[Company]_[Role].pdf",
    "headline": "[3-4 phrases matched to the posting, separated by | ]",
    "profile": "[4-6 sentence positioning paragraph rewritten for THIS role]",
    "strengths": ["8-10 short phrases, each mirroring language from the posting"],
    "jobs": [...],          # reverse chronological, header/context/bullets per job
    "advisory": [...],      # author, newsletter, coaching, speaking, board roles
    "education": common_education,
}

build_resume(resume)
```

Optional keys the engine supports: `leadership_highlights`, `leadership_section_title`,
`advisory_section_title`, and `page_break_before: True` on a job entry when page one runs long.

### Step 3: Tailor the content
- **Headline and profile** are rewritten per role, not copied between applications.
- **Job bullets:** 3-5 per role, each with at least one metric (dollars, percent, headcount,
  or time period). Reorder and reword so the most role-relevant bullet comes first.
- **Mirror the posting's vocabulary** where honest: if it says "consumption pricing" or
  "pipeline rigor," use those exact terms where Albert's record supports them.
- **Lead credential by role type** follows the mapping in the shared facts file, covering AI,
  revenue leadership, and partnership roles.
- Frame Meta by customer scale (100K+ advertisers, $30B+ revenue) rather than by team size,
  unless the posting is explicitly about managing large orgs. When the 400 sellers do appear,
  use the vendor-employed BPO wording from the inline backstop above, never a bare headcount.

### Step 4: Build and verify
1. Run the script from the project root: `python3 scripts/build_[name].py`
2. Confirm the PDF exists in `output/pdf/resumes/` and has a nonzero size.
3. If ReportLab is missing, tell the user instead of switching to a different PDF method.
4. Open or render page one to confirm nothing critical spilled to page two. Aim for one
   page; two is acceptable only when the posting is senior enough to justify it, and only
   with `page_break_before` so the split is clean.

### Step 5: Pre-delivery checklist (job applications are high-stakes)

Run the mechanical gate on the build script before anything else:

```bash
python3 scripts/check_application_artifact.py scripts/build_[name].py
```

A nonzero exit means the resume is not deliverable. Fix every violation and rerun until it
passes. Never deliver a resume that failed the gate, and never edit the checker to make a
script pass. Then verify the rest by reading:

- Every claim traces to the master resume. No invented metrics.
- Rowland AI is current, Meta is 2022-2026 past tense, dates are consistent.
- Company and role names are spelled exactly as in the posting, everywhere.
- Writing rules from the shared facts file hold, meaning no em dashes, no semicolons, active
  voice, and no banned words.
- Any mention of the 400 sellers names them as vendor-employed through 5 BPO partners. Search
  the text for "400" and check every hit.
- The top third of page one answers this posting's top requirement.

Report the PDF path and a 3-4 bullet summary of what was emphasized for this role. If the
posting demands something the master resume cannot honestly support, say so plainly rather
than stretching a claim.

## Edge cases

Multiple roles at once, an artifact that already exists, and extra facts Albert supplies are
covered by the shared facts file. For this skill that means one script and one PDF per role,
and updating an existing build script rather than creating a near-duplicate.

- **Cover letter or "why us" paragraph requested:** the per-company `WHY_*` constants in the
  existing scripts (see `build_anthropic_startups_resume.py`) are the pattern. Add them to
  the new script the same way.
- **Master resume file missing or moved:** stop and ask. Do not fall back to the skill's
  own summary or an old PDF.
