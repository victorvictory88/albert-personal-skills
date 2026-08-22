#!/usr/bin/env python3
"""Audit personal skill activations in local Codex and Claude histories."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable


DEFAULT_SOURCE = Path(
    "/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/Skills"
)
DEFAULT_CODEX = Path.home() / ".codex"
DEFAULT_CLAUDE = Path.home() / ".claude"
SKILL_PATH_RE = re.compile(
    r"(?:/|\\)(?:skills|Skills)(?:/|\\)(albert-[a-z0-9-]+)(?:/|\\)SKILL\.md"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--codex-root", type=Path, default=DEFAULT_CODEX)
    parser.add_argument("--claude-root", type=Path, default=DEFAULT_CLAUDE)
    parser.add_argument("--days", type=int, default=120)
    parser.add_argument("--minimum-uses", type=int, default=3)
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        help="maximum included skills; 0 includes every skill meeting the minimum",
    )
    parser.add_argument("--csv", type=Path)
    parser.add_argument("--json", type=Path)
    return parser.parse_args()


def parse_timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def walk_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for nested in value.values():
            yield from walk_strings(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from walk_strings(nested)


def read_json_lines(path: Path) -> Iterable[dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(record, dict):
                    yield record
    except OSError:
        return


def canonical_skills(source: Path) -> list[str]:
    return sorted(
        child.name
        for child in source.iterdir()
        if child.is_dir()
        and child.name.startswith("albert-")
        and (child / "SKILL.md").is_file()
    )


def record_use(
    uses: dict[str, set[tuple[str, str, str]]],
    skill: str,
    platform: str,
    session: str,
    turn: str,
    allowed: set[str],
) -> None:
    if skill in allowed:
        uses[skill].add((platform, session, turn))


def audit_codex(
    root: Path,
    cutoff: datetime,
    allowed: set[str],
    uses: dict[str, set[tuple[str, str, str]]],
) -> int:
    paths: set[Path] = set()
    for folder in (root / "sessions", root / "archived_sessions"):
        if folder.exists():
            paths.update(folder.rglob("*.jsonl"))

    scanned = 0
    for path in sorted(paths):
        session = path.stem
        session_recent = False
        session_events: list[tuple[datetime, dict[str, Any]]] = []
        for record in read_json_lines(path):
            stamp = parse_timestamp(record.get("timestamp"))
            if stamp is None or stamp < cutoff:
                continue
            session_recent = True
            session_events.append((stamp, record))
        if not session_recent:
            continue
        scanned += 1

        for _, record in session_events:
            kind = record.get("type")
            payload = record.get("payload")
            if not isinstance(payload, dict):
                continue

            candidate: Any = None
            turn = session
            if kind == "response_item" and payload.get("type") in {
                "custom_tool_call",
                "function_call",
                "local_shell_call",
            }:
                candidate = payload
                metadata = payload.get("internal_chat_message_metadata_passthrough")
                if isinstance(metadata, dict):
                    turn = str(metadata.get("turn_id") or turn)
            elif kind == "event_msg" and payload.get("type") == "item_completed":
                item = payload.get("item")
                if isinstance(item, dict) and item.get("type") == "CommandExecution":
                    candidate = item
                    turn = str(payload.get("turn_id") or turn)

            if candidate is None:
                continue
            for text in walk_strings(candidate):
                for match in SKILL_PATH_RE.finditer(text):
                    record_use(uses, match.group(1), "codex", session, turn, allowed)
    return scanned


def find_claude_skill_uses(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        if value.get("type") == "tool_use" and value.get("name") == "Skill":
            tool_input = value.get("input")
            if isinstance(tool_input, dict) and isinstance(tool_input.get("skill"), str):
                yield tool_input["skill"]
        for nested in value.values():
            yield from find_claude_skill_uses(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from find_claude_skill_uses(nested)


def audit_claude(
    root: Path,
    cutoff: datetime,
    allowed: set[str],
    uses: dict[str, set[tuple[str, str, str]]],
) -> int:
    paths: set[Path] = set()
    for folder in (root / "projects", root / "sessions"):
        if folder.exists():
            paths.update(folder.rglob("*.jsonl"))

    scanned = 0
    seen_files: set[tuple[str, str]] = set()
    for path in sorted(paths):
        file_recent = False
        file_records: list[dict[str, Any]] = []
        for record in read_json_lines(path):
            stamp = parse_timestamp(record.get("timestamp"))
            if stamp is None or stamp < cutoff:
                continue
            file_recent = True
            file_records.append(record)
        if not file_recent:
            continue

        first = file_records[0] if file_records else {}
        session = str(first.get("sessionId") or path.stem)
        dedupe_key = (session, str(path.resolve()))
        if dedupe_key in seen_files:
            continue
        seen_files.add(dedupe_key)
        scanned += 1

        for record in file_records:
            session = str(record.get("sessionId") or session)
            turn = str(record.get("promptId") or record.get("uuid") or session)
            for skill in find_claude_skill_uses(record):
                record_use(uses, skill, "claude", session, turn, allowed)
    return scanned


def rows_for(
    skills: list[str], uses: dict[str, set[tuple[str, str, str]]]
) -> list[dict[str, Any]]:
    rows = []
    for skill in skills:
        events = uses.get(skill, set())
        codex = sum(1 for platform, _, _ in events if platform == "codex")
        claude = sum(1 for platform, _, _ in events if platform == "claude")
        rows.append(
            {
                "skill": skill,
                "uses": len(events),
                "codex_uses": codex,
                "claude_uses": claude,
            }
        )
    return sorted(rows, key=lambda row: (-row["uses"], row["skill"]))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    if args.days < 1 or args.minimum_uses < 1 or args.top < 0:
        print("days and minimum uses must be positive; top cannot be negative", file=sys.stderr)
        return 2
    if not args.source.is_dir():
        print(f"skill source is missing: {args.source}", file=sys.stderr)
        return 2

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=args.days)
    skills = canonical_skills(args.source)
    allowed = set(skills)
    uses: dict[str, set[tuple[str, str, str]]] = defaultdict(set)
    codex_files = audit_codex(args.codex_root, cutoff, allowed, uses)
    claude_files = audit_claude(args.claude_root, cutoff, allowed, uses)
    rows = rows_for(skills, uses)
    qualified = [row for row in rows if row["uses"] >= args.minimum_uses]
    included = qualified[: args.top] if args.top else qualified
    included_names = {row["skill"] for row in included}
    for row in rows:
        row["included"] = row["skill"] in included_names

    result = {
        "generated_at": now.isoformat(),
        "window_days": args.days,
        "cutoff": cutoff.isoformat(),
        "minimum_uses": args.minimum_uses,
        "top_limit": args.top,
        "codex_files_scanned": codex_files,
        "claude_files_scanned": claude_files,
        "skills": rows,
    }
    if args.csv:
        write_csv(args.csv, rows)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
