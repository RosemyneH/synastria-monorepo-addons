# Add-ons in this catalog

This folder only contains **vendored** add-on trees (full files checked into **this** repo). Everything else is installed from **its own GitHub repository** — the companion clones that URL directly. The table below is the same list as [manifest/addons.json](../manifest/addons.json), so you can browse links from here.

| Name | In-game folder | Where to get it |
| --- | --- | --- |
| Addon Control Panel | ACP-Zero | [GitHub](https://github.com/DivideByZeroToDeleteWorld/ACP-Zero) |
| ArkInventory | ArkInventory | [GitHub](https://github.com/SynScoots/ArkInventory-modified-for-attunements-) |
| AtlasLoot Mythic | AtlasLoot_Mythic | [GitHub](https://github.com/imevul/AtlasLoot_Mythic) |
| Attune Helper | AttuneHelper | [GitHub](https://github.com/RosemyneH/AttuneHelperHosting) |
| AttuneProgress | AttuneProgress | [GitHub](https://github.com/RosemyneH/AttuneProgress) |
| cDF Synastria | cDF_Synastria | [GitHub](https://github.com/RosemyneH/cDF---Synastria) |
| ElvUI Attune | ElvUI_Attune | [GitHub](https://github.com/RosemyneH/ElvUI_Attune) |
| LizardDMP | LizardDMP | [GitHub](https://github.com/Versicoloris/LizardDMP) |
| LizardKTS | LizardKTS | [GitHub](https://github.com/Versicoloris/LizardKTS) |
| LizardMMU | LizardMMU | [GitHub](https://github.com/Versicoloris/LizardMMU) |
| LizardSTB | LizardSTB | [GitHub](https://github.com/Versicoloris/LizardSTB) |
| LizardTMO | LizardTMO | [GitHub](https://github.com/Versicoloris/LizardTMO) |
| LizardWWG | LizardWWG | [GitHub](https://github.com/Versicoloris/LizardWWG) |
| Mapster | Mapster | [GitHub](https://github.com/RosemyneH/MapsterSynastriaHosting) |
| MehTrajectory | MehTrajectory | [GitHub](https://github.com/SynScoots/MehTrajectory) |
| OmniInventory Syn | OmniInventory | [GitHub](https://github.com/RosemyneH/OmniInv-Syn) |
| Postal | Postal | [GitHub](https://github.com/binnesman/Postal) |
| Qt's Auto-Roller | qtRoll | [GitHub](https://github.com/RosemyneH/qtRoll) |
| qtRunner | qtRunner | [GitHub](https://github.com/RosemyneH/qtRunner) |
| qtUITweaks | qtUITweaks | [GitHub](https://github.com/RosemyneH/qtUITweaks) |
| Questie 3.3.5 | Questie-335 | [GitHub](https://github.com/Netrinil/Questie-335) |
| RaajikWarpAlias | RaajikWarpAlias | [tree in this repo](https://github.com/RosemyneH/synastria-monorepo-addons/tree/main/addons/RaajikWarpAlias) |
| Resource Bank Viewer | ResourceBankViewer | [GitHub](https://github.com/RosemyneH/ResourceBankViewer) |
| Scoots' Combat Attune Watch | ScootsCombatAttuneWatch | [GitHub](https://github.com/SynScoots/ScootsCombatAttuneWatch) |
| Scoots' Confirmation Skip | ScootsConfirmationSkip | [GitHub](https://github.com/SynScoots/ScootsConfirmationSkip) |
| Scoots' Craft | ScootsCraft | [GitHub](https://github.com/SynScoots/ScootsCraft) |
| Scoots' Quick Auction | ScootsQuickAuction | [GitHub](https://github.com/SynScoots/ScootsQuickAuction) |
| Scoots' Rares | ScootsRares | [GitHub](https://github.com/SynScoots/ScootsRares) |
| Scoots' Speedrun | ScootsSpeedrun | [GitHub](https://github.com/SynScoots/ScootsSpeedrun) |
| Scoots' Stats | ScootsStats | [GitHub](https://github.com/SynScoots/ScootsStats) |
| Scoots' UI Tweaks | ScootsUITweaks | [GitHub](https://github.com/SynScoots/ScootsUITweaks) |
| Scoots' Vendor | ScootsVendor | [GitHub](https://github.com/SynScoots/ScootsVendor) |
| Scoots' Warp Map | ScootsWarpMap | [GitHub](https://github.com/SynScoots/ScootsWarpMap) |
| Synastria Build Manager | SynastriaBuildManager | [GitHub](https://github.com/Lubricated/SynastriaBuildManager) |
| SynastriaQuestieHelper | SynastriaQuestieHelper | [GitHub](https://github.com/Elmegaard/SynastriaQuestieHelper) |
| Talented (Synastria) | Talented | [GitHub](https://github.com/RosemyneH/talented-synastria) |
| The Journal | TheJournal | [GitHub](https://github.com/RosemyneH/TheJournal) |
| TrufiGCD | TrufiGCD | [GitHub](https://github.com/robgha01/TrufiGCD) |
| VendorForgeList | VendorForgeList | [GitHub](https://github.com/APLiquid/VendorForgeList) |
| WeakAuras | WeakAuras | [GitHub](https://github.com/Bunny67/WeakAuras-WotLK) |

## Why most rows are not subfolders here

We use an **upstream-first** policy: public projects stay on their authors’ GitHub accounts. That keeps updates, issues, and credit with the original maintainer. Only add-ons **without** a suitable public repo are vendored under `addons/<Name>/`.

## Regenerate this file

```bash
python scripts/generate_addons_index.py
```

