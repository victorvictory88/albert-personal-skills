---
name: albert-remotion-video
description: "Create and edit short video clips for LinkedIn and other feeds using the Remotion studio at Outputs/_workspace-maintenance/remotion-studio. Use when Albert asks for a video, clip, reel, short, animated quote card, captioned cutdown, or talking-points video, when he says 'make a video', 'turn this post into a clip', 'add captions to this footage', 'trim this video', 'reframe this for portrait', or when he supplies footage and wants it posted. Also use to repurpose a written post, article, or transcript into video. Do not use for slide decks, static images, carousels, or GIFs."
metadata:
  version: 1.0.0
  created: 2026-08-09
---

# Remotion Video

Albert's clip factory lives at
`/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/remotion-studio`.
Read its `README.md` before the first render in a session.

## What this skill owns

Short feed video, made from copy or cut from existing footage. Every clip is
React rendered to MP4, so the wording, timing, and branding are all editable
text rather than a timeline nobody can reproduce.

## Route the request

| Albert asks for | Kind | Composition |
| --- | --- | --- |
| A point, an opinion, a list, a lesson | `text` | TextClip |
| Captions on footage he supplies, a trim, a reframe | `video` | CaptionedVideo |
| One number, one line, a pull quote | `quote` | QuoteCard |

Default to `portrait` unless he names a format. It takes the most feed space on
mobile and desktop alike.

## Workflow

1. **Write the copy first.** Apply `albert-writing-style` to every word that
   lands on screen, including the hook, the beats, the closing line, and any
   caption text you generate. Screen copy is a deliverable, so the four-word
   floor, the banned vocabulary, and the em dash ban all apply.
2. **Earn the first two seconds.** The hook carries the clip. Lead with the
   sharpest claim, never with a greeting or a title card that says what the
   video will cover.
3. **Set the props.** Write a JSON file under `props/`. Keep beats near three
   and a half seconds, which is long enough to read a line twice.
4. **Render.** Use the script rather than raw Remotion flags.

   ```bash
   python3 scripts/make_clip.py --kind text --format portrait --name topic-slug --props props/topic.json
   ```

5. **Verify visually.** Render a still at a mid-clip frame, read it, and check
   it at thumbnail size. Confirm no text collides with the caption band, no
   line overflows the safe area, and the hook is legible small.

   ```bash
   npx remotion still src/index.ts TextClip-portrait out/check.png --frame=60
   ```

6. **Report** the output path, the duration, the file size, and the format.

## Editing footage Albert supplies

Copy the source into `public/`, never edit it in place. Set `trimStart` and
`trimEnd` in seconds. When cutting landscape footage to portrait, use
`fit: "cover"` and move `focusX` off centre to keep the subject framed.

Captions come from an SRT or WebVTT file through `subtitleFile`. When Albert has
no transcript, say so and offer the Whisper install rather than inventing
timings. Guessed caption timing drifts within a few seconds and looks broken.

## Rules that hold

- Burn captions in. LinkedIn plays the feed muted, so an untitled clip is a
  silent clip.
- Keep clips under ninety seconds unless Albert asks otherwise, and never past
  the ten-minute feed limit.
- Save finished clips to `Outputs` with the dated filename the script builds.
  Working renders and stills stay in the studio's `out/` folder.
- Change branding in `src/theme.ts`, never inline in a composition.
- Pin TypeScript below version 7. Remotion's bundler calls `typescript.sys`,
  which version 7 removed.

## When Albert wants a post to go with the clip

Hand the caption and post copy to `albert-social-content` with
`albert-writing-style` as the overlay. This skill stops at the rendered file.
