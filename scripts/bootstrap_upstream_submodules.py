#!/usr/bin/env python3
"""
Register each manifest GitHub clone URL as a git submodule under addons/upstream/<id>/.

Meta-repo layout: each catalog row with a public GitHub URL becomes a submodule pointer.
Vendored-only rows (this monorepo as repo) stay as real trees under addons/<Name>/.

    python scripts/bootstrap_upstream_submodules.py

Re-run after adding manifest rows. Idempotent.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest" / "addons.json"
HUB_MARKERS = ("synastria-monorepo-addons",)


def clone_url(entry: dict) -> str | None:
    inst = entry.get("install")
    if isinstance(inst, dict):
        u = inst.get("url")
        if isinstance(u, str) and u.strip():
            return u.strip().rstrip("/")
    r = entry.get("repo")
    if isinstance(r, str) and r.strip():
        return r.strip().rstrip("/")
    return None


def should_skip(url: str) -> bool:
    if not url.startswith(("https://github.com/", "http://github.com/")):
        return True
    return any(m in url for m in HUB_MARKERS)


def normalize_git_url(url: str) -> str:
    if url.endswith(".git"):
        return url
    return f"{url}.git"


def submodule_path_registered(rel_posix: str) -> bool:
    gm = ROOT / ".gitmodules"
    if not gm.is_file():
        return False
    return f"path = {rel_posix}" in gm.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    if not MANIFEST.is_file():
        print("bootstrap_upstream_submodules: missing", MANIFEST, file=sys.stderr)
        return 1
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    addons = data.get("addons")
    if not isinstance(addons, list):
        return 1

    added = 0
    skipped = 0
    for entry in addons:
        if not isinstance(entry, dict):
            continue
        aid = entry.get("id")
        if not isinstance(aid, str) or not aid.strip():
            continue
        url = clone_url(entry)
        if not url or should_skip(url):
            skipped += 1
            continue
        url = normalize_git_url(url)
        rel = Path("addons") / "upstream" / aid
        rel_posix = rel.as_posix()
        if submodule_path_registered(rel_posix):
            continue
        abs_path = ROOT / rel
        if abs_path.is_dir() and (abs_path / ".git").exists():
            continue
        print(f"Adding submodule {rel_posix} <- {url}")
        p = subprocess.run(
            ["git", "submodule", "add", url, rel_posix],
            cwd=ROOT,
            text=True,
        )
        if p.returncode != 0:
            print(f"  skip {aid} (git returned {p.returncode})", file=sys.stderr)
            continue
        added += 1

    print(f"Done. Added {added} submodule(s); skipped {skipped} non-GitHub or hub rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
