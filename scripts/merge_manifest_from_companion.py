#!/usr/bin/env python3
import json
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_COMPANION_MANIFEST = Path(__file__).resolve().parents[2] / "AttuneHelperCompanion" / "manifest" / "addons.json"
OUT = _REPO_ROOT / "manifest" / "addons.json"

NEW_ADDONS = [
    {
        "id": "raajik-warp-alias",
        "name": "RaajikWarpAlias",
        "author": "Synastria",
        "category": "Utility",
        "folder": "RaajikWarpAlias",
        "source_subdir": "addons/RaajikWarpAlias",
        "description": "Vendored in synastria-monorepo-addons; populate addons/RaajikWarpAlias from your local Interface folder.",
        "repo": "https://github.com/RosemyneH/synastria-monorepo-addons.git",
        "install": {"type": "git", "url": "https://github.com/RosemyneH/synastria-monorepo-addons.git"},
        "github_release": {
            "owner": "RosemyneH",
            "repo": "synastria-monorepo-addons",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/RosemyneH.png?size=96",
        "version": "main",
        "page_url": "https://github.com/RosemyneH/synastria-monorepo-addons",
        "categories": ["Utility", "Quality of Life"],
    },
    {
        "id": "scoots-ui-tweaks",
        "name": "Scoots' UI Tweaks",
        "author": "Scoots",
        "category": "Quality of Life",
        "folder": "ScootsUITweaks",
        "description": "UI tweaks from the Scoots library.",
        "repo": "https://github.com/SynScoots/ScootsUITweaks.git",
        "install": {"type": "git", "url": "https://github.com/SynScoots/ScootsUITweaks.git"},
        "github_release": {
            "owner": "SynScoots",
            "repo": "ScootsUITweaks",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/SynScoots.png?size=96",
        "version": "main",
        "categories": ["Quality of Life", "Community Favorites"],
    },
    {
        "id": "scoots-warp-map",
        "name": "Scoots' Warp Map",
        "author": "Scoots",
        "category": "Map",
        "folder": "ScootsWarpMap",
        "description": "Warp map helper from the Scoots library.",
        "repo": "https://github.com/SynScoots/ScootsWarpMap.git",
        "install": {"type": "git", "url": "https://github.com/SynScoots/ScootsWarpMap.git"},
        "github_release": {
            "owner": "SynScoots",
            "repo": "ScootsWarpMap",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/SynScoots.png?size=96",
        "version": "main",
        "categories": ["Map", "Quality of Life"],
    },
    {
        "id": "cdf-synastria",
        "name": "cDF Synastria",
        "author": "RosemyneH",
        "category": "Attunement",
        "folder": "cDF_Synastria",
        "description": "Synastria cDF package (verify in-game folder name from repo).",
        "repo": "https://github.com/RosemyneH/cDF---Synastria.git",
        "install": {"type": "git", "url": "https://github.com/RosemyneH/cDF---Synastria.git"},
        "github_release": {
            "owner": "RosemyneH",
            "repo": "cDF---Synastria",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/RosemyneH.png?size=96",
        "version": "main",
        "categories": ["Attunement", "Quality of Life"],
    },
    {
        "id": "resource-bank-viewer",
        "name": "Resource Bank Viewer",
        "author": "RosemyneH",
        "category": "Inventory",
        "folder": "ResourceBankViewer",
        "description": "View resource bank contents in-game.",
        "repo": "https://github.com/RosemyneH/ResourceBankViewer.git",
        "install": {"type": "git", "url": "https://github.com/RosemyneH/ResourceBankViewer.git"},
        "github_release": {
            "owner": "RosemyneH",
            "repo": "ResourceBankViewer",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/RosemyneH.png?size=96",
        "version": "main",
        "categories": ["Inventory", "Quality of Life"],
    },
    {
        "id": "talented-synastria",
        "name": "Talented (Synastria)",
        "author": "RosemyneH",
        "category": "Class",
        "folder": "Talented",
        "description": "Talents UI fork for Synastria.",
        "repo": "https://github.com/RosemyneH/talented-synastria.git",
        "install": {"type": "git", "url": "https://github.com/RosemyneH/talented-synastria.git"},
        "github_release": {
            "owner": "RosemyneH",
            "repo": "talented-synastria",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/RosemyneH.png?size=96",
        "version": "main",
        "categories": ["Class", "Quality of Life"],
    },
    {
        "id": "qt-ui-tweaks",
        "name": "qtUITweaks",
        "author": "Qt",
        "category": "Quality of Life",
        "folder": "qtUITweaks",
        "description": "UI tweaks and automation helpers.",
        "repo": "https://github.com/RosemyneH/qtUITweaks.git",
        "install": {"type": "git", "url": "https://github.com/RosemyneH/qtUITweaks.git"},
        "github_release": {
            "owner": "RosemyneH",
            "repo": "qtUITweaks",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/RosemyneH.png?size=96",
        "version": "main",
        "categories": ["Quality of Life", "Utility"],
    },
    {
        "id": "elvui-attune",
        "name": "ElvUI Attune",
        "author": "RosemyneH",
        "category": "Attunement",
        "folder": "ElvUI_Attune",
        "description": "Attunement integration for ElvUI.",
        "repo": "https://github.com/RosemyneH/ElvUI_Attune.git",
        "install": {"type": "git", "url": "https://github.com/RosemyneH/ElvUI_Attune.git"},
        "github_release": {
            "owner": "RosemyneH",
            "repo": "ElvUI_Attune",
            "asset_pattern": "*.zip",
            "enabled": False,
        },
        "direct_zip": None,
        "avatar_url": "https://github.com/RosemyneH.png?size=96",
        "version": "main",
        "categories": ["Attunement", "Utility"],
    },
]


def main() -> int:
    import sys

    if _COMPANION_MANIFEST.is_file():
        data = json.loads(_COMPANION_MANIFEST.read_text(encoding="utf-8"))
    elif OUT.is_file():
        data = json.loads(OUT.read_text(encoding="utf-8"))
    else:
        print("merge_manifest_from_companion: need", _COMPANION_MANIFEST, "or existing", OUT, file=sys.stderr)
        return 1
    addons: list[dict] = data["addons"]
    seen = {a["id"] for a in addons}
    for entry in NEW_ADDONS:
        if entry["id"] not in seen:
            addons.append(entry)
            seen.add(entry["id"])
    data["addons"] = addons
    data["updated_at"] = "2026-04-27"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    src = "companion" if _COMPANION_MANIFEST.is_file() else "hub"
    print(f"Wrote {len(addons)} addons to {OUT} (base={src})")
    print("Next: python scripts/bootstrap_upstream_submodules.py", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
