# Test Cases

## Test 1: Campaign

**Input:**
"We're launching a new project-management app for freelancers on September 15. Plan a 3-week campaign across LinkedIn, X, and email to build awareness and drive signups. Brand voice: direct, no corporate jargon, a little irreverent."

**Expected output shape:**
- Brand voice loaded from the prompt (direct, no jargon, irreverent) — no separate question needed since it's already stated.
- Brief filled with goal (awareness + signups), audience (freelancers), channels (LinkedIn/X/email), timeline (3 weeks ending/around Sept 15).
- Research stage cites at least one real, sourced data point relevant to freelancer pain points or PM tool market (e.g., a survey or industry stat), with a link or named source.
- Plan table mapping pieces to campaign phase (awareness -> consideration -> conversion), channel, and rough date.
- Create stage produces draft copy per row matching the stated voice.
- Final deliverable is a table with columns: piece/day, channel, phase, draft copy, source/citation, notes.
- QA checklist applied — any unsourced claims flagged, not stated as fact.

## Test 2: Content Calendar

**Input:**
"Build me a content calendar for October for our SaaS company's LinkedIn page. We post 3x/week. Audience is mid-market IT directors. Keep it consistent with our normal brand voice — check the style guide in this repo if there is one."

**Expected output shape:**
- Stage 0 attempts to locate a brand/style guide file in the working directory before asking the user; if none found, asks a batched question rather than guessing silently.
- Brief captures cadence (3x/week), channel (LinkedIn), audience (mid-market IT directors), month (October).
- Plan is a full month table: date, theme/topic, channel, status/notes — covering all posting days per the stated cadence.
- Any factual/industry claims embedded in post topics are cited; where a claim can't be sourced it's marked as an idea/opinion, not a stat.
- Output is a single scannable table (by week or by date), not prose describing each week.
- QA checklist catches any gaps (e.g., missing week, uneven cadence) before final delivery.

## Test 3: Repurposing

**Input:**
"Here's our webinar transcript on remote team management [transcript text/link]. Turn it into a LinkedIn carousel outline, 3 tweets, and a short email teaser."

**Expected output shape:**
- Stage 0 confirms or asks for brand voice/audience if not already established in the session.
- Brief identifies the source (webinar transcript) and target formats (carousel, tweets, email teaser).
- Research/extraction stage pulls specific claims, quotes, or stats directly from the transcript and cites them as "from webinar transcript, [timestamp/speaker if available]" rather than paraphrasing loosely.
- Plan maps key transcript ideas to each target format (which idea becomes which tweet/slide).
- Create stage drafts actual copy for each format, channel-native (carousel slide text is different from a tweet, is different from an email teaser).
- Final table: format, channel, draft copy, source excerpt/citation from the transcript, notes.
- QA checklist confirms no claim exceeds what's actually in the transcript.
