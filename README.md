# UniacDocs

The documentation for [Uniac](https://uniac.ai), a cloud deployment platform,
published at [docs.uniac.ai](https://docs.uniac.ai) by Mintlify from this
repository's `main`. Every public product fact is written here, once.

## Edit

The `.mdx` files are the pages; `docs.json` holds navigation and theme;
`custom.css`, `logo/` and `favicon.png` are the visual skin. Preview and
check locally (Mintlify's CLI needs Node 20.17+):

```sh
npm install -g mint
mint dev            # http://localhost:3000
mint validate
mint broken-links
```

CI runs the two checks on every pull request and push to `main`. Merging to
`main` publishes: the Mintlify GitHub app deploys the commit and reports the
result as its "Mintlify Deployment" check.

Beside the pages, Mintlify serves their Markdown versions (`/<route>.md`),
`llms.txt`, `llms-full.txt` and a `skill.md` it generates itself. The
public `uniac` agent skill in [uniac-ai/agent-skills](https://github.com/uniac-ai/agent-skills)
compresses these pages and links to them; nothing here is written for it.

[AGENTS.md](AGENTS.md) covers ownership and how the pages are written.
