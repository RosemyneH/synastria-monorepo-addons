# Why submodules can look “invisible” on GitHub

They **are** there, but the GitHub web UI does **not** show the same thing as a normal folder with files inside the parent repository.

## What to open

1. **Full list in plain text (always works)**  
   [`.gitmodules` on `main`](https://github.com/RosemyneH/synastria-monorepo-addons/blob/main/.gitmodules)  
   Every `url =` line is a linked upstream add-on.

2. **The submodule directories**  
   [Browse `addons/upstream/`](https://github.com/RosemyneH/synastria-monorepo-addons/tree/main/addons/upstream)  

   On the web, each add-on is a **gitlink** (pinned commit in another repo), not the whole tree inlined here. You should see:
   - One row per add-on (e.g. `weakauras-wotlk`)
   - Often a **commit short SHA** and/or a **“Submodule”** / link that jumps to the **other** repository at that commit  
   - Clicking the name or link opens the **upstream** project on GitHub, not a nested file list inside *this* repo.

3. **Raw list from git** (API-style)  
   [Repository contents API path](https://api.github.com/repos/RosemyneH/synastria-monorepo-addons/contents/addons/upstream?ref=main) — `type: "file"` is wrong; items should be `type: "submodule"` with a `submodule_git_url` in some responses, or the tree shows as gitlinks in git directly.

## If you see nothing

- Confirm the branch is **`main`** and the path is **`addons/upstream`**, not an old fork or a branch without commit `9919f2b` or later.
- Try an incognito window or hard refresh (cache can show an old tree).
- The mobile GitHub app sometimes hides metadata; use the full site for `addons/upstream/`.

**Bottom line:** submodules = **pointers** to other repos. [`.gitmodules`](https://github.com/RosemyneH/synastria-monorepo-addons/blob/main/.gitmodules) is the file that always proves every link exists from GitHub’s UI.
