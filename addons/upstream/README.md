# Upstream add-ons (git submodules)

Each **subfolder** under `addons/upstream/` is a **git submodule** pointing at the canonical GitHub repository for that catalog row (`manifest/addons.json` → same `id`).

**On GitHub you do not get a full file tree in the parent repo** for each of these: Git shows them as a **link / pinned commit** to the *other* repository. The full list of URLs is always visible in the root [**`.gitmodules`**](https://github.com/RosemyneH/synastria-monorepo-addons/blob/main/.gitmodules) file. See **[docs/GitHub_submodules.md](../../docs/GitHub_submodules.md)**.

**Clone this monorepo with submodules:**

```bash
git clone --recurse-submodules https://github.com/RosemyneH/synastria-monorepo-addons.git
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

**Vendored-only** add-ons (no separate public repo) live as normal folders under [`addons/`](../) next to this directory — for example `addons/RaajikWarpAlias/`.

Regenerate submodule registrations after manifest changes:

```bash
python scripts/bootstrap_upstream_submodules.py
```
