# Developer setup and validation notes

A separate original Xbox title project using the pinned XboxLLR framework.
The original NTSC-U attract and interactive gameplay use generated native CPU
and shared native services. A rapid cheat-assisted campaign sweep has rendered
entry evidence for all19 campaign/gameplay areas and nine story-event groups;
13 additional encounter files and the final post-fight sequence were reached.
Forced victories and prerequisite bypasses are explicit, and do not qualify
fair combat or full routes. Original save/fresh-process loading and sampled
movement, grinding, graffiti and progression have direct evidence. Extra-mode
initialization and deeper mechanics remain deferred. This is a development preview.

Provide your own game under ignored local paths. Original game files, console inputs and generated code are never included in this repository. The private development image is SHA256 `f4441696fdd007c31a712815cdde967836fbc3ab97fcb2f58e1db56974644219` (title ID `5345000A`, XDK 4134).

The USA standalone input is independently described by `native-title-usa.toml`
and `config/revisions/usa-standalone/`. Use `tools/game.py --revision usa-standalone`
with separate private paths, generated output and host build directories.
Prepare and recover with that revision's `native-function-recovery.json`, then
configure/build normally. Its native executable is `JSRFRecompUSA`; both windows
retain the clean game name. `tools/qa.py --revision usa-standalone` selects its
own process-memory facts. Mod fixtures support both address layouts; select
`JSRF_TEST_REVISION=usa-standalone` and the USA fixture DLL for the original-code
Early Test Runs comparison.

Package both native builds through the shared stager, supplying
`--revision usa-standalone <USA-runtime.exe> <USA-build/CMakeCache.txt>`.
The stager rejects an omitted declared revision. Its exact XBE hash selects the
runtime, mod identity and private console/save directory; unknown XBEs remain
rejected. Keep `data/console` and `data/state` for existing revision-4 users;
standalone defaults live under `data/revisions/usa-standalone/`.

The [native attract burndown](NATIVE-ATTRACT-BURNDOWN.md) records reached behavior, failures and deferred precision. Framework code is reusable across this title, Blinx and the dashboard; title-specific profiles supply reviewed interfaces and layouts.

Interactive gameplay, explicit coverage bypasses and visual enhancements are
tracked in the [gameplay burndown](NATIVE-GAMEPLAY-BURNDOWN.md).

Visual mods use the shared Xbox launcher: adaptive widescreen through 32:9,
internal resolution through 2160p, AA, supersampling, filtering and optional
60/120Hz interpolated presentation. Live 4:3, 16:9, 21:9 and 32:9 resizing,
GPU/CPU projection and clipping, HUD anchoring, 1080p/2160p rendering and 3x3
supersampling have sampled gameplay evidence. These enhancements are optional
and disabled by default. Final visual/performance review belongs to the owner;
the samples do not qualify every stage-specific effect. Frame interpolation preserves original
simulation and can produce blended double edges. Actual faster game simulation
is unavailable until a title timing adapter is qualified.

The development driver accepts `build-launcher`, and `run --launcher` opens the
shared Player1/mod controls after it is built. `run --no-launcher` uses explicit
CLI choices such as `--widescreen adaptive --internal-resolution 1080
--antialiasing fxaa --anisotropy 8 --frame-mode interpolated --frame-rate 120`.
Use the declared private paths and tested framework pin, or explicitly select a
development worktree. Automated runs require a bounded duration and stay muted;
owner-facing runs are windowed with normal audio by default.

CPU translation references phobos665/xboxrecomp and sp00nz/sp00nznet/xboxrecomp. Additional exact source/license attribution follows each borrowed implementation through the framework notices; this project does not grant rights to original game assets.

The reviewed [native function recovery plan](../config/revisions/ntsc-u/native-function-recovery.json)
contains image-bound extent facts, rather than original code. After the normal
`prepare` step, apply it before `configure`/`build`:

```powershell
python tools/game.py recover --paths local/paths.json --recovery config/revisions/ntsc-u/native-function-recovery.json
```

This uses the shared transactional native compiler path. Generated original
code and recovery history stay in the private build directory.


Return to the [player overview](../README.md).

## Early Test Runs mod

`src/mods/challenge_unlock.inc` rebuilds only the transient Roboy challenge
menu for the supported original revision. Original `0x756E0` requires chapter9
before comparing each area's total and collected graffiti souls. This mod
retains that comparison and the original loaded challenge rows while allowing
earlier chapters. It does not change chapter, collected souls, missions or
saved progress. Chapter9 remains entirely under the original routine.

The default is ON in `native-title.toml`; Mods can save OFF. It works without
visual enhancements. Revision facts and bounded function/table hashes are in
`config/revisions/ntsc-u/challenge-unlock.json`, with no original code bodies.

Build the portable C fixtures with `cmake -S tests -B build/mod-contracts
-DXBOXLLR_ROOT=<framework>`, then run CTest. For the unlock tests, set
`JSRF_CHALLENGE_FIXTURE` to the resulting `jsrf_challenge_contract` shared
library and run `python -m unittest discover -s tests -p test_challenge_unlock.py`.
Setting `JSRF_ORIGINAL_XBE` to your supported original image also enables the
bounded Unicorn comparison: four soul bitmaps must produce identical menu
bytes to the original postgame x86 routine while the mod's chapter stays early.
Capstone/Unicorn are development references only; production remains native.
