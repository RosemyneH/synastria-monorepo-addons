# synastria-monorepo-addons
Vendored **World of Warcraft 3.3.5** add-on trees that are not (or not yet)
published as their own GitHub repositories, plus a **human index** of
upstream and vendored sources.

**Attune Helper Companion** uses an *upstream-first* catalog: the in-app
`manifest/addons.json` should point at each add-on’s canonical **public Git**
URL when it exists. This repository exists for:

- Trees you **copy in** under `addons/<AddOnFolder>/` (Interface-style layout
  with a `.toc` at the expected depth).
- A **central table** in [ADDONS.md](ADDONS.md) listing upstream links and
  notes (e.g. ACP-Zero vs legacy ACP).

## Layout

- [ADDONS.md](ADDONS.md) — index (name, path, upstream or “vendored only”).
- `addons/<AddOnFolderName>/` — one vendored add-on per folder; folder name
  should match the in-game add-on directory / manifest `folder` and
  `source_subdir` when the companion points at this repo.

Do **not** use git submodules. The companion runs `git clone --depth 1` only;
use a normal directory tree. Optional `source_subdir` in the app manifest
selects a subfolder after clone.

## Publishing

From this directory (first push):

```bash
git init
git add -A
git commit -m "Initial monorepo layout"
# create empty repo on GitHub, then:
git remote add origin https://github.com/<org>/synastria-monorepo-addons.git
git branch -M main
git push -u origin main
```

Related: [AttuneHelperCompanion](https://github.com/RosemyneH/AttuneHelperCompanion)
(`manifest/addons.json` is the in-app install catalog).
