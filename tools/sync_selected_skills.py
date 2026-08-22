#!/usr/bin/env python3
"""Copy selected skills into the managed GitHub-ready repository."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from pathlib import Path
from typing import Any


IGNORE = shutil.ignore_patterns(
    ".DS_Store", ".git", ".env", ".env.*", "__pycache__", "*.pyc", "*.pyo"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--usage", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    return parser.parse_args()


def load_usage(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict) or not isinstance(value.get("skills"), list):
        raise ValueError(f"invalid usage audit: {path}")
    return value


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = ["skill", "uses", "codex_uses", "claude_uses", "included"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: row[field] for field in fields} for row in rows)


def markdown_report(data: dict[str, Any]) -> str:
    rows = data["skills"]
    included = [row for row in rows if row["included"]]
    excluded = [row for row in rows if not row["included"]]
    cutoff = str(data["cutoff"])[:10]
    generated = str(data["generated_at"])[:10]
    minimum = data["minimum_uses"]
    window = data["window_days"]

    lines = [
        "# Skill Selection Report",
        "",
        f"This report was generated on {generated}. The audit covers {window} days beginning {cutoff}.",
        "",
        "Recorded use means a distinct Codex turn or Claude prompt where the assistant loaded the skill. Catalog listings and ordinary text mentions receive zero credit. Deleted or unavailable sessions remain outside these totals.",
        "",
        f"The repository includes every personal skill with at least {minimum} recorded uses.",
        "",
        f"## Included skills ({len(included)})",
        "",
        "| Skill | Total | Codex | Claude |",
        "|---|---:|---:|---:|",
    ]
    lines.extend(
        f"| `{row['skill']}` | {row['uses']} | {row['codex_uses']} | {row['claude_uses']} |"
        for row in included
    )
    lines.extend(
        [
            "",
            f"## Excluded skills ({len(excluded)})",
            "",
            "| Skill | Total | Reason |",
            "|---|---:|---|",
        ]
    )
    lines.extend(
        f"| `{row['skill']}` | {row['uses']} | Fewer than {minimum} recorded uses |"
        for row in excluded
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    marker = repo / ".skill-repo-marker"
    if not marker.is_file():
        print(f"refusing to manage an unmarked directory: {repo}", file=sys.stderr)
        return 2
    if not args.source.is_dir():
        print(f"skill source is missing: {args.source}", file=sys.stderr)
        return 2

    data = load_usage(args.usage)
    included = {row["skill"] for row in data["skills"] if row["included"]}
    destination = repo / "skills"
    destination.mkdir(exist_ok=True)

    for current in destination.iterdir():
        if current.is_dir() and current.name not in included:
            shutil.rmtree(current)

    for skill in sorted(included):
        source = args.source / skill
        if not (source / "SKILL.md").is_file():
            print(f"selected skill is missing SKILL.md: {source}", file=sys.stderr)
            return 2
        target = destination / skill
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target, ignore=IGNORE)

    (repo / "SELECTED_SKILLS.md").write_text(markdown_report(data), encoding="utf-8")
    write_csv(repo / "usage.csv", data["skills"])
    print(f"Exported {len(included)} skills into {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
