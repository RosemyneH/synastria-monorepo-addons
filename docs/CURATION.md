# Curation policy

- **Upstream-first:** If a add-on has a public GitHub repository, the catalog points at that URL. Do not fork or mirror here unless intentional.
- **ACP:** Only [ACP-Zero](https://github.com/DivideByZeroToDeleteWorld/ACP-Zero) is listed for the “Addon Control Panel” line.
- **SynastriaQuestieHelper:** The catalog uses [Elmegaard/SynastriaQuestieHelper](https://github.com/Elmegaard/SynastriaQuestieHelper) as the install target; other forks may be noted in [ADDONS.md](../ADDONS.md).
- **Felbite** is not a default source for bulk rows; the companion may support opt-in imports for maintenance only.
- **Edits:** Change [manifest/addons.json](../manifest/addons.json) in this repo first, then rebuild the Attune Helper Companion so the baked catalog updates.
- **Browsing `addons/` on GitHub:** Run `python scripts/generate_addons_index.py` so [addons/README.md](../addons/README.md) lists every row with links. Upstream add-ons are **not** duplicated as subfolders here (see below).

## If you want every add-on as a real folder under `addons/`

| Approach | What users see | Trade-off |
|----------|----------------|-----------|
| **Current (recommended)** | [addons/README.md](../addons/README.md) = generated table → links to each upstream GitHub repo; only true vendored trees (e.g. RaajikWarpAlias) are folders. | Small repo; companion clones each upstream URL from the manifest. |
| **Git submodule per add-on** | One folder per add-on under `addons/`, each a submodule to upstream. | `git clone --depth 1` on the monorepo **does not** fetch submodule contents unless you add `--recurse-submodules` and change the installer — easy to ship empty folders by mistake. |
| **Vendor / mirror copies** | Full file trees under `addons/`. | Huge repo; you must merge or re-sync from upstream manually. |

## Verify after editing the manifest

From a clone of [AttuneHelperCompanion](https://github.com/RosemyneH/AttuneHelperCompanion) with this repo beside it:

```bash
python scripts/generate_addon_catalog.py --check --input ../synastria-monorepo-addons/manifest/addons.json
cmake --build build
ctest --test-dir build
```

## Regenerate manifest from companion (one-time seed)

```bash
python scripts/merge_manifest_from_companion.py
```

(requires `../AttuneHelperCompanion/manifest/addons.json` — used when bootstrapping; day-to-day edits happen in this repo.)

## Regenerate the add-ons index (under `addons/`)

```bash
python scripts/generate_addons_index.py
```

Commit `addons/README.md` together with `manifest/addons.json` when you change the catalog.
