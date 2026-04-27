# Curation policy

- **Upstream-first:** If a add-on has a public GitHub repository, the catalog points at that URL. Do not fork or mirror here unless intentional.
- **ACP:** Only [ACP-Zero](https://github.com/DivideByZeroToDeleteWorld/ACP-Zero) is listed for the “Addon Control Panel” line.
- **SynastriaQuestieHelper:** The catalog uses [Elmegaard/SynastriaQuestieHelper](https://github.com/Elmegaard/SynastriaQuestieHelper) as the install target; other forks may be noted in [ADDONS.md](../ADDONS.md).
- **Felbite** is not a default source for bulk rows; the companion may support opt-in imports for maintenance only.
- **Edits:** Change [manifest/addons.json](../manifest/addons.json) in this repo first, then rebuild the Attune Helper Companion so the baked catalog updates.

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
