#!/usr/bin/env python3
"""Download and verify GitHub's portable CLI release for this Mac."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import shutil
import stat
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Any


LATEST_RELEASE = "https://api.github.com/repos/cli/cli/releases/latest"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", type=Path, required=True)
    return parser.parse_args()


def request_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "albert-personal-skills-backup",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        value = json.load(response)
    if not isinstance(value, dict):
        raise RuntimeError("GitHub returned an invalid release response")
    return value


def platform_asset(release: dict[str, Any]) -> dict[str, Any]:
    if platform.system() != "Darwin":
        raise RuntimeError("The portable installer currently supports macOS")
    machine = platform.machine().lower()
    architecture = "arm64" if machine in {"arm64", "aarch64"} else "amd64"
    suffix = f"_macOS_{architecture}.zip"
    for asset in release.get("assets", []):
        if isinstance(asset, dict) and str(asset.get("name", "")).endswith(suffix):
            return asset
    raise RuntimeError(f"GitHub's latest release lacks {suffix}")


def download(url: str, path: Path) -> None:
    request = urllib.request.Request(
        url, headers={"User-Agent": "albert-personal-skills-backup"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        with path.open("wb") as handle:
            shutil.copyfileobj(response, handle)


def verify_digest(path: Path, digest: str) -> None:
    algorithm, separator, expected = digest.partition(":")
    if separator != ":" or algorithm != "sha256" or not expected:
        raise RuntimeError("GitHub's release asset lacks a SHA-256 digest")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError("GitHub CLI download failed its SHA-256 check")


def main() -> int:
    args = parse_args()
    release = request_json(LATEST_RELEASE)
    asset = platform_asset(release)
    url = str(asset.get("browser_download_url", ""))
    digest = str(asset.get("digest", ""))
    if not url:
        raise RuntimeError("GitHub's release asset lacks a download URL")

    with tempfile.TemporaryDirectory(prefix="albert-gh-cli-") as temporary:
        temporary_path = Path(temporary)
        archive = temporary_path / "gh.zip"
        extracted = temporary_path / "extracted"
        download(url, archive)
        verify_digest(archive, digest)
        with zipfile.ZipFile(archive) as bundle:
            bundle.extractall(extracted)
        matches = list(extracted.glob("*/bin/gh"))
        if len(matches) != 1:
            raise RuntimeError("GitHub CLI archive has an unexpected layout")
        args.destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(matches[0], args.destination)
        args.destination.chmod(args.destination.stat().st_mode | stat.S_IXUSR)

    print(f"Installed GitHub CLI at {args.destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
