# Add-ons in this monorepo

## Upstream (git submodules)

Each **subfolder** named `addons/<id>/` that is a **git submodule** points at the canonical GitHub repository for that catalog row (`manifest/addons.json` → same `id`).

**On GitHub you do not get a full file tree in the parent repo** for each of these: Git shows them as a **link / pinned commit** to the *other* repository. The full list of URLs is always visible in the root [**`.gitmodules`**](https://github.com/RosemyneH/synastria-monorepo-addons/blob/main/.gitmodules) file. See **[docs/GitHub_submodules.md](../docs/GitHub_submodules.md)**.

**Clone this monorepo with submodules:**

```bash
git clone --recurse-submodules https://github.com/RosemyneH/synastria-monorepo-addons.git
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

**Vendored-only** add-ons (no separate public repo) live as normal trees here too — e.g. `RaajikWarpAlias/`.

Regenerate submodule registrations after manifest changes:

```bash
python scripts/bootstrap_upstream_submodules.py
```

Some catalog rows point at upstreams that are **not** registered as submodules here (for example [TrinityCore/wow_335a_addons](https://github.com/TrinityCore/wow_335a_addons) cannot be checked out on Windows NTFS); the companion still installs from `install.url` when the client can clone the tree.
