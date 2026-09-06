# UniacDocs

Mintlify publication of the Markdown documentation authored in
[uniac-ai/agent-skills](https://github.com/uniac-ai/agent-skills).
The source repository and commit are recorded in `docs-source.json`.

## Update documentation

Make content changes in the public repository, then generate from its
published commit and verify the result:

```sh
python3 tools/sync_docs.py --revision <full-public-commit-sha>
python3 tools/sync_docs.py --check
mint broken-links
mint validate
```

The sync command fetches that exact commit and runs its exporter. A normal
`python3 tools/sync_docs.py` regenerates from the existing pin; `--check`
reports changed, missing, or extra MDX pages without modifying them. CI runs
the pinned-source check on every pull request and push to `main`.

To preview uncommitted public-source changes, explicitly select that worktree:

```sh
python3 tools/sync_docs.py --source-dir /absolute/path/to/public-source-worktree
python3 tools/sync_docs.py --source-dir /absolute/path/to/public-source-worktree --check
```

These local commands leave the commit pin unchanged. Pin the resulting public
commit before publishing the docs update.

## Preview the website

```sh
npm install -g mint
mint dev
```

Preview at `http://localhost:3000`. Website navigation and styling are owned
here; all MDX pages are generated. See [AGENTS.md](AGENTS.md) for ownership.
