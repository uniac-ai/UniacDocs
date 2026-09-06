#!/usr/bin/env python3
"""Generate docs from the pinned public source, or an explicit local source tree."""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROVENANCE = ROOT / "docs-source.json"
REPOSITORY = "uniac-ai/agent-skills"


def generate(source: Path, check: bool) -> None:
    command = [sys.executable, str(source / "tools/export_docs.py"), "--output", str(ROOT)]
    if check:
        command.append("--check")
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--source-dir", type=Path, help="use a local public-repository working tree without changing the pin")
    selection.add_argument("--revision", help="generate from this full public commit SHA and update docs-source.json")
    parser.add_argument("--check", action="store_true", help="verify generated pages without modifying the docs repository")
    args = parser.parse_args()
    if args.revision and args.check:
        parser.error("--revision updates the pin; use --check to verify the current pin")
    try:
        if args.source_dir:
            generate(args.source_dir.resolve(), args.check)
        else:
            pin = {"repository": REPOSITORY, "commit": args.revision} if args.revision else json.loads(PROVENANCE.read_text())
            if pin.get("repository") != REPOSITORY or not re.fullmatch(r"[0-9a-f]{40}", pin.get("commit") or ""):
                raise ValueError("docs-source.json must name uniac-ai/agent-skills and a full commit SHA; run --revision <sha>")
            with tempfile.TemporaryDirectory(prefix="uniac-docs-") as directory:
                source = Path(directory)
                for command in (
                    ["git", "init", "--quiet", directory],
                    ["git", "-C", directory, "fetch", "--quiet", "--depth=1", f"https://github.com/{REPOSITORY}.git", pin["commit"]],
                    ["git", "-C", directory, "checkout", "--quiet", "--detach", "FETCH_HEAD"],
                ):
                    subprocess.run(command, check=True, capture_output=True, text=True)
                generate(source, args.check)
            if args.revision:
                PROVENANCE.write_text(json.dumps(pin, indent=2) + "\n")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"{getattr(error, 'stderr', None) or error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
