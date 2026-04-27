# Contributing

## What belongs here

- Updates to [manifest/addons.json](manifest/addons.json) (install sources the Attune Helper Companion can use).
- Updates to [ADDONS.md](ADDONS.md) (human-readable index and notes).
- Vendored add-on trees under [addons/](addons/) when there is no public upstream to point at.

## What belongs elsewhere

- **Bugs in the Attune Helper app** (UI, installs, crashes): [AttuneHelperCompanion Issues](https://github.com/RosemyneH/AttuneHelperCompanion/issues).

## How to propose a change

1. Open an **Issue** using the templates, or a **Pull Request** with a short description of the add-on row or doc fix.
2. For new git sources, include the public clone URL and confirm the add-on layout (`.toc` path, `source_subdir` if not repo root).
3. Regenerate the browsable list: `python scripts/generate_addons_index.py` and commit `addons/README.md` with your manifest change.
4. Run validation from a clone of AttuneHelperCompanion (sibling directory):

   `python scripts/generate_addon_catalog.py --check --input ../synastria-monorepo-addons/manifest/addons.json`

Maintainers merge when the JSON is valid and policy in [docs/CURATION.md](docs/CURATION.md) is satisfied.

## Approve who?

Repository write access is limited to maintainers; small doc and list fixes are welcome via PR for review.
