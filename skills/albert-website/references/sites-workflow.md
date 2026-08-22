# Sites Workflow

Use this reference for candidate sites created or hosted through Sites.

## Existing Site Retrieval

1. Search the workspace for `.openai/hosting.json` and the matching slug before using remote discovery.
2. When the source is absent, list owned Sites projects and match the exact live URL or slug.
3. Copy the returned project ID unchanged. Treat IDs as opaque.
4. Request a short-lived source repository write credential.
5. Clone the configured branch into the canonical output folder with a per-command HTTP authorization header. Keep the token out of output, remote URLs, and Git configuration.
6. Read `.openai/hosting.json`, the main page, layout metadata, global styles, package scripts, tests, and recent Git history before editing.

## New Site Setup

1. Follow `sites-building` to initialize the bundled Sites starter in the target output folder.
2. Start the development server using the project's established script.
3. Replace starter content and metadata completely.
4. Create the Sites project once, then write its exact project ID to `.openai/hosting.json`.
5. Preserve the package manager, lockfile, framework, and Cloudflare-compatible build.

## Validation Sequence

1. Run the project build, tests, and lint.
2. Start the production preview without changing the build output.
3. Fetch rendered HTML to a temporary file and run the application artifact checker against that file.
4. Use the Browser workflow for visual checks when layout or responsive placement carries user-facing risk.
5. Check desktop and 960-pixel views. Reset any temporary viewport override after inspection.
6. Inspect social cards at their native dimensions and resize only after confirming every word.
7. Stop the preview after deployment and live readback finish.

## Version And Deployment Sequence

1. Confirm `.openai/hosting.json` contains the existing opaque project ID.
2. Commit only the validated, in-scope source and assets.
3. Push the configured branch with the current short-lived credential.
4. Package the project with the installed Sites plugin's `scripts/package-site.sh` helper.
5. Save one site version using the pushed commit SHA and packaged archive.
6. For verified owner-only access, use private deployment. For public, shared, or unverifiable access, obtain explicit approval and use the public deployment tool.
7. Poll the returned deployment ID until `succeeded` or `failed`.
8. Open the successful production URL in Codex.

## Live Readback

Deployment success can precede endpoint propagation. Read the production HTML and verify several unique strings from the new hero, the updated metadata asset name, and the expected title. If the endpoint still serves the prior version, wait briefly and retry with a cache-busting query. Continue until the new version appears or the deployment reports a failure.

Keep the prior version and prior social asset available for rollback. Report the user-facing version number rather than internal IDs.
