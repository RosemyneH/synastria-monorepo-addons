# Curation policy

- **Upstream-first:** Each public GitHub add-on has its own repository. The manifest lists the clone URL the **Attune Helper Companion** uses for installs.
- **Meta-repo links:** The same URLs are registered as **git submodules** under [`addons/upstream/<id>/`](../addons/upstream/README.md) so this monorepo is multi-linked to every upstream (browse on GitHub or clone with `--recurse-submodules`).
- **Vendored-only:** Add-ons without a suitable public repo (e.g. **RaajikWarpAlias**) stay as a normal folder under `addons/<FolderName>/`, not a submodule.
- **ACP:** Only [ACP-Zero](https://github.com/DivideByZeroToDeleteWorld/ACP-Zero) for the “Addon Control Panel” line.
- **SynastriaQuestieHelper:** [Elmegaard/SynastriaQuestieHelper](https://github.com/Elmegaard/SynastriaQuestieHelper) as the install target; other forks in [ADDONS.md](../ADDONS.md) if needed.
- **Felbite** is not a default bulk source.

## After you change `manifest/addons.json`

1. Register new GitHub rows as submodules (idempotent):

   ```bash
   python scripts/bootstrap_upstream_submodules.py
   ```

2. Commit `.gitmodules`, submodule gitlinks, and the manifest.

3. Validate the catalog from [AttuneHelperCompanion](https://github.com/RosemyneH/AttuneHelperCompanion):

   ```bash
   python scripts/generate_addon_catalog.py --check --input ../synastria-monorepo-addons/manifest/addons.json
   ```

## Clone this monorepo with all upstream checkouts

```bash
git clone --recurse-submodules https://github.com/RosemyneH/synastria-monorepo-addons.git
# or, if already cloned:
git submodule update --init --recursive
```

## Regenerate manifest from companion (bootstrap)

```bash
python scripts/merge_manifest_from_companion.py
python scripts/bootstrap_upstream_submodules.py
```
