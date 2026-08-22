# Candidate Site Design Spec

Load this file after the role brief is established. It carries the design system, page structure, responsive behavior, and metadata requirements.

## Design System

**Font:** Inter (weights 300-900) from Google Fonts.

**Brand colors:** Use CSS variables in `:root`. Derive colors from the company's verified brand palette.
```css
:root {
  --brand-primary: /* main accent */;
  --brand-dark:    /* darker variant for hover */;
  --brand-light:   /* very light tint for card backgrounds */;
  --brand-navy:    /* dark background, use #1A1A1A if no navy */;
}
```

Brand color reference:
- Groupon: #53A318
- Nutanix: navy #0D1B36, green #6CC04A
- Sprinklr: #7B2FBE
- Meta: #0866FF
- Salesforce: #00A1E0
- Anthropic: #CC785C
- Google: use the dominant color of the specific product mentioned in the job description

**Contrast rule:** never place gray text on a dark or gray background. On dark backgrounds,
body text is white or near-white. This has been corrected before; do not repeat it.

**Typography:**
- Hero name: 62px, weight 800, letter-spacing -0.03em
- Section titles: clamp(28px, 3vw, 42px), weight 800
- Body: 14-17px, weight 400-500, line-height 1.6-1.7
- Tags/labels: 11-12px, weight 600-700, letter-spacing 0.08-0.12em, uppercase

**Interactions:**
- Cards: translateY(-4px) on hover + box-shadow + brand-colored top border slides in
- Buttons: darken background on hover + slight lift
- Nav links: color transition on hover
- Pedigree companies: faded gray to near-black on hover

**Responsive breakpoint at 960px:** stack hero columns vertically, place the strongest positioning before the photo, simplify stats to a 2-column grid, and linearize the timeline.

---

## Page Sections (build in this order)

### 1. Sticky Nav
- Small SVG mark in brand color + text "Albert Chan x [Company]"
- Nav links: Why Me, Experience, Impact, Contact
- CTA button: "Let's Connect" linking to mailto:albert@rowland.ai
- White background, subtle drop shadow, fixed at top of viewport

### 2. Hero
Two-column CSS grid. Left: headshot. Right: content.

Headshot:
- `src="headshot.jpg"`, rounded frame with brand-colored border and soft glow, ~420px wide
- Add an `onerror` handler that swaps the image for a brand-colored monogram block ("AC")
  so the page never shows a broken-image icon before the user drops in the photo

Right column:
- Eyebrow badge: "Candidate Application" with a brand-colored dot
- Name: 62px, weight 800. First name dark, "Chan" in brand accent color
- Role title: [Job Title] at [Company]
- Headline (2-3 sentences): The first sentence names the single most differentiating credential for this role. If the role needs AI expertise, open with the Rowland AI Claude/OpenAI deployment work. If it needs platform or partnerships depth, open with Google or Meta.
- When Albert's current industry or customer focus strengthens the fit, display it directly above the opening paragraph in a compact proof block or tag group.
- Two buttons: "See the Fit" (primary, smooth scroll to #fit) and "Get in Touch" (outlined, mailto)

Background: soft gradient using light tints of brand color, with subtle dot grid SVG overlay.

### 3. Stats Strip
- Background: #1A1A1A or company dark color
- Large bold number + short uppercase label, 5 stats total
- Thin vertical borders between each stat, numbers in brand accent color
- Select the 5 stats MOST relevant to this specific role. An AI role should surface the pilot-to-production and 20+ use case metrics. A partnership role should surface Google tenure and the eBay JBP. A revenue role should surface $30B+ book and 3X ARR. Never default to the same 5 stats every time.

### 4. Why Me / Fit Section (id="fit")
- Background: light off-white
- Section tag: "Why Albert", title: "Built for this role"
- 6 cards in a 3-column grid

Each card:
- Emoji in a brand-colored rounded box
- "Role Requirement" label in brand accent, uppercase, small
- Bold title stating the specific requirement this card addresses
- Body: explain what the role needs and why this quality is hard to find
- Proof block (separated by horizontal divider): a specific Albert achievement proving he meets this requirement. Every proof block MUST include at least one specific metric (dollar amount, percentage, headcount, or time period). "Led a large team" is not acceptable.

Read the job description carefully. Each card should address an actual requirement from the posting.

### 5. Career Timeline (id="experience")
- Background: white
- Vertical line on the left in brand color, fades out at the bottom
- No dot elements on the timeline. No `.timeline-dot` class. No circular markers.
- Two columns: left has company name + date range (right-aligned), right has role title, description, tags
- Entries in reverse chronological order, starting with Rowland AI (2026-present)
- Each description must include at least one sentence connecting that role to the company's current need.
- Tags: pill-shaped badges, brand light background, brand accent text

### 6. Impact Section (id="impact")
- Background: off-white
- Two-column layout

Left column: numbered list of 6 items
- Each item: dark square badge with brand accent digit, bold title, and 2-3 sentences connecting the impact to this role and company

Right column (dark panel, #1A1A1A or brand navy):
- Title: "Why [Company], why this role"
- 3 paragraphs making the unfair advantage argument. What does Albert know or have that no other candidate can claim? Be bold and specific. Write it like the most honest, confident cover letter ever written, not a list of qualifications.
- 5 bullet points prefixed with green arrow (→): the 5 sharpest differentiators that make Albert the only logical choice

### 7. Company Pedigree
- Background: white, centered
- Companies: Procter and Gamble, Google, Meta, Tickr, Harvard
- Company names in faded gray, darken to near-black on hover

### 8. Quote Section
- Background: dark (brand navy or #1A1A1A), centered
- Large faded decorative opening quotation mark
- One sentence quote: why does Albert want THIS role at THIS company? Personal and ambitious, not generic. One key phrase in brand accent color.
- Attribution: use the location confirmed for this application.

### 9. Footer (id="contact")
- Background: light off-white
- Left column: Albert Chan name with email and phone links
- Right column: LinkedIn and "Let's Connect" primary CTA buttons
- Omit any executive-profile link or button from candidate sites

---

## Metadata Requirements

- Title: `Albert Chan: [Job Title] | [Company]`
- Description: one role-specific sentence grounded in Albert's strongest proof
- Open Graph and X titles, descriptions, and image references
- Absolute metadata base using the production Sites URL
- Versioned 1200 by 630 social-preview image with inspected text
- Site-specific favicon and accessible image alt text
