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

## Reaching Roboy for private menu QA

`tools/qa_roboy.py --run <private-run> --port <TCP-port>` drives the original
USA standalone menus from an isolated endgame save (slot 2 by default),
positions the character beside Roboy, and talks to him through normal RT/A
input. It retains TCP screenshots and action observations at each checkpoint.
The position shortcut is an explicit travel bypass; it sets no success flags.
The launch receipt, process lifetime and exact original image are checked.
Use `--from-checkpoint` to continue after observing the current screen instead
of replaying an unsuitable prefix. Physical controller presence is unnecessary
while the native debug listener supplies P1. Do not interrupt an owner playtest.

Graffiti options use horizontal D-pad navigation: Pick, Create, Edit. Create
selects a size, then A on Spray opens its palette. RT paints while the left
stick moves the cursor; B closes the palette. Save is the seventh toolbar
item. Confirmations start on Cancel: D-pad Left selects OK. Use one navigation
source per press; do not combine D-pad and stick. Observe each transition
before the next command. The helper waits for the actual size controls after
the scene's camera easing, rather than treating the first frame as readiness.

The October 26 private USA audit verified all five prefab preview regions,
actual RT strokes, repeated backing out/re-entry, original custom-design file
writing and editor reopening. It also exposed and fixed redundant separators
in original save paths and the thumbnail copy's system-memory allocation/free
calls. Thumbnail bytes were independently compared with the original asset.
System save/settings and character selection were sampled. Practice tutorial
entry was reached; complete Practice exit/re-entry, Music/Test Run menu sweeps
and billboard camera flicker remain unverified in that audit. Both revision
builds and focused GPU/input/memory/storage tests pass; this is not a claim
that every original workshop or Roboy operation has been tested.

## Early Test Runs mod

`src/mods/challenge_unlock.inc` rebuilds the transient Roboy challenge
menu for the supported original revision. Original `0x756E0` requires chapter9
before comparing each area's total and collected graffiti souls. This mod
retains that comparison and the original loaded challenge rows while allowing
earlier chapters. It does not change chapter, collected souls, missions or
saved progress. A caller-filtered chapter query in the results constructor
also removes its separate postgame reward prerequisite. The original rank,
area, already-unlocked and character-award routines still decide the reward.
No chapter, score or earned flag is written by the mod. Chapter9 retains the
original behavior. Both revision contracts pass; a complete earned-reward
gameplay check remains pending.

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

## Native graffiti image import

`tools/graffiti_native.py` authors native `save.dat` blocks and signatures from
RGBA pixels; no original artwork, templates or keys are in the codec. Recomp-ui
uses its bounded private stb_image decoder and a polled local handoff to the
verified title codec. The shared release path admits the selected revision and
console identity, holds the normal storage writer lease, checks free slots and
bytes, verifies new file readback, and publishes a new canonical save directory.
Existing directories reserve their slot even with damaged metadata.

Original USA functions 12CB40, 12CCB0, 12D6C0, 12DFC0 and 12E240 establish the
name, six raw payloads and HMAC-SHA1 layout. XAPI 146C6C hashes each UTF-16 unit
as `(hash * 65536 + unit) mod 0xFFFFFFFFFFC5`, rendered as twelve hex digits.
The original game probes these paths directly rather than enumerating arbitrary
directory names. Editable pixels are linear BGRA, previews use RGB565 with
C618 transparency, and display art is BC2. M uses a padded allocation. Imported
raster art has fifteen inactive editor objects and normal paint defaults.
The static slot thumbnail is read from the owner's verified original media.

`src/mods/startup_skip.inc` only sets the original A/Start latch on the live
logo actor and removes the warning's 420-frame minimum after an input pulse.
Original fades, cleanup and subsequent startup flow still execute. Both
revision registries have default-on launcher selections and an off switch.

Manage Graffiti is an always-available Mods action supplied by the title's image
import capability, rather than a persisted runtime switch. It has no checkbox;
Disable all leaves it available. Opening it inspects free slots/storage
asynchronously through the same handoff, and every successful import returns
updated capacity. Its browser is the existing in-app picker so the render/event
loop never waits inside a blocking Windows file dialog. UTF-8 paths are retained
through filtering, selection, decode and the native save handoff.

Saved designs shows thumbnails decoded from the actual signed native saves.
Full-size view uses a valid high-resolution companion when present, with an
actual-size scrolling option. Deletion requires a matching canonical name,
native graffiti header, selected save digest and a known file set. Unrelated
progress and changed saves are preserved. Successful deletion refreshes the
gallery and capacity through the same exclusive storage lease. Folder and
actual FATX delete/reopen checks use disposable authored saves.

Imports accept native, 2x or 4x detail. A content-bound `xboxllr-hd.bin` companion
retains sharper RGBA pixels while the normal signed save remains game-readable.
Native editor changes invalidate the companion. The shared renderer matches
exact native texture content, preserving guest dimensions, UVs and readback.
It supports BC2/RGB565 display resources and the game's shared BGRA preview
atlas; GPU fixtures qualify detail, unchanged native pixels and edited-save
fallback. An actual USA Roboy preview displays the 4x mascot; the owner has
also passed custom graffiti in gameplay. Title release manifests explicitly
list only the RPTK and RAID source PNGs and their instructions as extras.
Packaging never enumerates a player's artwork or save/profile folders.

The all-Beat multiplayer roster came from a separate fixed-function texture
matrix defect: FLOAT2 inputs omitted the homogeneous third component used by
the original atlas offsets. The shared fix passes authored GPU tests, and an
actual USA two-player roster now displays distinct portraits and names.

The Dogenzaka corner investigation also found different viewport treatment
between XYZ fixed geometry and original programs. Both now use the original
sample-space screen offset and four-bit window rounding, retaining ordinary
depth tests. GPU tests cover exact fixed/program pixels and coplanar decal
coverage, offset viewports, 2x samples and perspective W. The exact owner-reported
flicker angle still needs a human check; successful tag painting or a still
image alone does not establish that it is resolved. Earned Test Run rewards
and the reported post-run single-player preview also retain separate checks.

## Optional hold-Start story skipping

`jsrf.enhancement.cutscenes/hold-start` defaults off. The source-hashed original
scripted-event update at23790 already calls1E8C0 for normal completion and the
vanilla previously-viewed A/Start skip. The opt-in requests that same cleanup
after one second of Player1's original logical Start input. It requires the
registered live1DDD actor, ready phase2, its1DDB wrapper and CMission state19;
ordinary gameplay pause and dialogue are outside the scope. It never changes
input, mission/chapter/completion bytes or script clocks. Original cleanup
records viewing, releases resources and resumes the original mission tail.

Release Start after each scene starts to arm the hold. Actor/script/event
identity changes, release and long update gaps reset the timer. The post-update
check revalidates ownership so a natural finish or vanilla skip cannot cause a
second teardown. Disabled selection performs no mod-side RAM reads. Both
revision identities and function hashes are in `cutscene-skip.json`; both
optimized builds and the20 combined mod contracts pass.

Actual muted USA validation compared a natural chapter1 intro with an unseen
run using held Start. Short200ms and650ms presses left event201 playing;
six one-second holds skipped events201 through206 through original cleanup.
The resulting chapter, mission10064/state15 and all64 viewed-scene bytes
matched the natural run. Native player movement then resumed. Private inputs,
RAM observations and screenshots are retained outside the repository under
`jsrf-content-20261026/cutscene-hold-002` and `cutscene-hold-004`. This is a
representative scripted-story check, not an all-cutscene or FMV audit. The
unpublished pristine `cutscene-skip-stage` candidate verifies the launcher
selection reaches the runtime and remains disabled on a fresh profile. The
owner's currently open build has not been interrupted or replaced.
