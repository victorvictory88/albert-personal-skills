# Albert's Personal Skills Backup

This private GitHub repository keeps the personal skills that Albert has used repeatedly during the last 120 days. The default rule includes every skill with at least three recorded uses across Codex and Claude.

## Publish this repository once

Double-click the file `Publish to GitHub.command` in Finder. The script downloads GitHub's portable command-line client when needed, opens browser authorization, creates a private GitHub repository named `albert-personal-skills`, and pushes this local repository.

You can run the terminal version instead.

```bash
cd "/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/personal-skills-repo"
./publish.sh
```

## Update the backup later

Double-click the file `Update GitHub Backup.command` in Finder. The script audits recent usage, refreshes the selected skill copies, commits any changes, and pushes them to GitHub.

You can run the terminal version instead.

```bash
cd "/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/personal-skills-repo"
./update.sh --push
```

Run `./update.sh` without `--push` when you want a local preview.

## Change the selection rule

This example uses a 180-day window and requires four recorded uses.

```bash
./update.sh --days 180 --minimum-uses 4 --push
```

The [selection report](SELECTED_SKILLS.md) lists every included and excluded skill with its recorded count. The audit stores aggregate counts only, so prompts and session content stay outside this repository.

## Privacy

Keep this GitHub repository private because selected skills contain personal workflow and candidate context. The export excludes environment files, private keys, cache files, and Git metadata.
