# Writing for UniacDocs

User-facing documentation for [Uniac](https://uniac.ai), a cloud deployment platform. Built on [Mintlify](https://mintlify.com).

## Workflow

- Pages are `.mdx`. Site config is `docs.json`.
- `mint dev` — preview at `http://localhost:3000`.
- `mint broken-links` — check links before pushing.
- Pushes to the default branch auto-deploy via the Mintlify GitHub app.

For Mintlify components and config reference, install the Mintlify skill: `npx skills add https://mintlify.com/docs`.

## Scope

Document what users can do today. If a feature isn't shipped, it doesn't appear here, even as "coming soon." Internal platform architecture lives in UniacInfra.

## Style

- Active voice, second person.
- Sentence case for headings.
- Bold for UI elements: Click **Settings**.
- Code formatting for commands, paths, file names, code references.
- Apply Uniac's information-cleanness principles: every sentence earns its keep; no derived info; no example lists where each item reduces to the same point; no cross-references that don't pay rent.

## Canonical names

Manifest: `uniac.yaml`. Auth file: `~/.uniac/auth.json`. Link binding: `.uniac/deploy.json`. Resource types: `service`, `stateful`, `deployment`. There is no SDK and no build-from-source: users bring prebuilt OCI images, and the CLI (`init`, `plan`, `link`, `deploy`, `status`, `auth`, `version`) is the whole client surface. See Concepts and CLI reference for definitions.

Verify CLI claims against the released binary before documenting them — `uniac plan` and every error in the manifest page reproduce offline.
