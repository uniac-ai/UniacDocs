# UniacDocs publication

The [public agent repository](https://github.com/uniac-ai/agent-skills) owns
the authored documentation. This repository publishes generated Mintlify
pages; `docs-source.json` identifies their source commit.

## Ownership

- Change product facts, examples, headings, and links in the public repository.
- Change the website navigation and theme in `docs.json`; its groups provide
  website navigation independently of the authored documents' links.
- Change the visual skin in `custom.css`, with assets in `logo/` and `images/`.
- Every `.mdx` page is generated. The public repository's `tools/export_docs.py`
  owns route mapping and conversion; `tools/sync_docs.py` selects its source.

The public setup guide becomes `/setup`, quickstart becomes `/quickstart`,
and Concepts becomes `/`. Other references keep their source-relative paths.
The exporter derives frontmatter, preserves code, and converts documentation
links to website routes. Links to the installable skill itself stay external.

## Verification and publication

Use the commands in [README.md](README.md) to regenerate and check pages.
Local source previews leave the published commit pin unchanged. Before
submitting the website update, pin the public commit and run the default
source check, `mint broken-links`, and `mint validate`.

CI verifies every page against the pinned source. Pushes to the default branch
auto-deploy through the Mintlify GitHub app. Changes use a worktree and PR;
the Uniac engineering skills own that workflow.
