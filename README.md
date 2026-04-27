# synastria-monorepo-addons

## For players

If you play on a **World of Warcraft 3.3.5**–style server (for example Synastria) and use **Attune Helper Companion** to install add-ons, this repository is the **official home** for the **list of add-ons** the helper can install from Git: names, links to authors’ projects, and a few add-on folders that ship **only** here because they are not published as separate projects.

You do **not** need to understand Git or builds. Browse **[ADDONS.md](ADDONS.md)** for a readable table. To suggest a fix or a new add-on, open an **[Issue](https://github.com/RosemyneH/synastria-monorepo-addons/issues)** (see [CONTRIBUTING.md](CONTRIBUTING.md)). Problems with the **app itself** (crashes, buttons, installs) belong on **[AttuneHelperCompanion](https://github.com/RosemyneH/AttuneHelperCompanion/issues)**.

**Upstream-first:** when an add-on already has its own public GitHub project, we **link to it** instead of copying it here, so updates stay with the original author.

---

## For developers and maintainers

This repo holds:

| Path | Purpose |
|------|---------|
| [manifest/addons.json](manifest/addons.json) | Machine-readable catalog consumed by Attune Helper Companion (built into the app). **Edit this file here first** when changing install sources. |
| [ADDONS.md](ADDONS.md) | Human index (names, paths, upstream notes). |
| [addons/](addons/) | **[addons/upstream/](addons/upstream/README.md)** — git **submodules** to every upstream (see [docs/GitHub_submodules.md](docs/GitHub_submodules.md) for how this appears on **GitHub**). Vendored trees (e.g. RaajikWarpAlias) sit beside `upstream/`. On GitHub, open [`.gitmodules`](https://github.com/RosemyneH/synastria-monorepo-addons/blob/main/.gitmodules) for the full list of links. |
| [docs/CURATION.md](docs/CURATION.md) | Policy and verification commands. |

The companion app clones this layout from **[RosemyneH/synastria-monorepo-addons](https://github.com/RosemyneH/synastria-monorepo-addons)** (or a sibling checkout during development). See [docs/CURATION.md](docs/CURATION.md) for `generate_addon_catalog.py --check` after edits.

**Related repositories**

- **[AttuneHelperCompanion](https://github.com/RosemyneH/AttuneHelperCompanion)** — desktop/mobile helper that **bakes** this JSON at build time and can refresh from the copy on GitHub.

Do **not** use git submodules inside `addons/`. The installer uses `git clone --depth 1`; optional `source_subdir` in each manifest row selects a subfolder after clone.

## First-time publish

```bash
git remote add origin https://github.com/RosemyneH/synastria-monorepo-addons.git
git branch -M main
git push -u origin main
```

Replace the org/repo if yours differs.

## Community

[Code of conduct](CODE_OF_CONDUCT.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Support](SUPPORT.md)
