# Add-on index

Machine-readable install sources: **[manifest/addons.json](manifest/addons.json)** (also baked into Attune Helper Companion). Each GitHub row is also linked as a **git submodule** under **[addons/upstream/](addons/upstream/README.md)** (`git clone --recurse-submodules`). This table summarizes upstreams and notes.

| Add-on (short) | Upstream / note |
|----------------|-----------------|
| ACP | Use **[ACP-Zero](https://github.com/DivideByZeroToDeleteWorld/ACP-Zero)** only (`source_subdir: src`). |
| WeakAuras (WotLK) | [Bunny67/WeakAuras-WotLK](https://github.com/Bunny67/WeakAuras-WotLK) |
| VendorForgeList | [APLiquid/VendorForgeList](https://github.com/APLiquid/VendorForgeList) |
| TrufiGCD | [robgha01/TrufiGCD](https://github.com/robgha01/TrufiGCD) |
| SynastriaQuestieHelper | [Elmegaard/SynastriaQuestieHelper](https://github.com/Elmegaard/SynastriaQuestieHelper) (canonical row in catalog) |
| AtlasLoot Mythic | [imevul/AtlasLoot_Mythic](https://github.com/imevul/AtlasLoot_Mythic) |
| RaajikWarpAlias | **[Vendored](addons/RaajikWarpAlias/)** — copy from your local Interface folder into this repo; manifest uses `source_subdir` under this monorepo. |
| SynScoots line | ScootsCraft, ScootsVendor, ScootsCombatAttuneWatch, ScootsStats, ScootsQuickAuction, ScootsSpeedrun, ArkInventory…, ScootsUITweaks, ScootsRares, ScootsWarpMap, ScootsConfirmationSkip, MehTrajectory — see manifest rows; skip entries with “deprecated” in name/description after review. |
| RosemyneH / Synastria | AttuneHelper (hosting repo), MapsterSynastriaHosting, OmniInv-Syn, qtRunner, qtRoll, AttuneProgress, TheJournal, qtUITweaks, ElvUI_Attune, cDF---Synastria, ResourceBankViewer, talented-synastria — listed in manifest. |
| Lizard (Versicoloris) | LizardDMP, LizardKTS, LizardMMU, LizardSTB, LizardTMO, LizardWWG — see manifest. |

**Not yet in JSON (need public git or confirmed vendored path):** e.g. `!BugGrabber`, `AckisRecipeList`, `ActionBarSaver`, `AdiBags`, `AttunableStarterItems`, `BoESender`, `BugSack`, `Chatter`, `CL_Fix`, `Details`, `GlobalDump`, `IDTip`, `Kui_NamePlates`, `Leatrix Plus`, `LuaBrowser`, `LuaConsole`, `MSBT`, `pretty_lootalert`, `Questie-DemonicCircleModule`, `SuperDuperMacro`, `TomTom`, `WDM`, `WIM`, `WorldDropList` — add rows when a stable public clone URL or vendored tree is available; until then track in issues or PRs.

Update this table when you add or remove manifest rows.

## Felbite

Bulk third-party site scraping is **not** the default catalog source; the companion may support **opt-in** merge scripts for maintenance only.
