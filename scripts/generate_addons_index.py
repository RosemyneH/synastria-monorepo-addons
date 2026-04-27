#!/usr/bin/env python3
"""Write addons/README.md — browsable index of every catalog row with GitHub (or in-repo) links."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest" / "addons.json"
OUT = ROOT / "addons" / "README.md"

HUB_REPO_MARKERS = ("synastria-monorepo-addons", "RosemyneH/synastria-monorepo-addons")


def web_url_for_addon(entry: dict) -> tuple[str, str]:
    """Return (label, url) for markdown link."""
    repo = entry.get("repo") or ""
    if isinstance(repo, str) and repo.strip():
        r0 = repo.strip()
        if any(m in r0 for m in HUB_REPO_MARKERS):
            base = r0.removesuffix(".git").rstrip("/")
            sub = entry.get("source_subdir")
            if isinstance(sub, str) and sub.strip():
                return ("tree in this repo", f"{base}/tree/main/{sub.strip('/')}")
            return ("this repository (vendored)", base)
    page = entry.get("page_url")
    if isinstance(page, str) and page.strip():
        return ("project page", page.strip())
    if not isinstance(repo, str) or not repo.strip():
        return ("—", "")
    r = repo.strip()
    if r.endswith(".git"):
        r = r[: -len(".git")]
    if "github.com" in r:
        return ("GitHub", r)
    return ("clone URL", r)


def main() -> int:
    if not MANIFEST.is_file():
        print("generate_addons_index: missing", MANIFEST, file=sys.stderr)
        return 1
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    addons = data.get("addons")
    if not isinstance(addons, list):
        print("generate_addons_index: invalid manifest", file=sys.stderr)
        return 1

    lines: list[str] = [
        "# Add-ons in this catalog",
        "",
        "This folder only contains **vendored** add-on trees (full files checked into **this** repo). "
        "Everything else is installed from **its own GitHub repository** — the companion clones that URL directly. "
        "The table below is the same list as [manifest/addons.json](../manifest/addons.json), so you can browse links from here.",
        "",
        "| Name | In-game folder | Where to get it |",
        "| --- | --- | --- |",
    ]

    for a in sorted(addons, key=lambda x: (x.get("name") or "").lower()):
        if not isinstance(a, dict):
            continue
        name = (a.get("name") or a.get("id") or "?").replace("|", "\\|")
        folder = (a.get("folder") or "—").replace("|", "\\|")
        label, url = web_url_for_addon(a)
        if url.startswith("http"):
            cell = f"[{label}]({url})"
        elif url:
            cell = f"**{label}** — {url}"
        else:
            cell = label
        lines.append(f"| {name} | {folder} | {cell} |")

    lines.extend(
        [
            "",
            "## Why most rows are not subfolders here",
            "",
            "We use an **upstream-first** policy: public projects stay on their authors’ GitHub accounts. "
            "That keeps updates, issues, and credit with the original maintainer. "
            "Only add-ons **without** a suitable public repo are vendored under `addons/<Name>/`.",
            "",
            "## Regenerate this file",
            "",
            "```bash",
            "python scripts/generate_addons_index.py",
            "```",
            "",
        ]
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {len(addons)} rows to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
