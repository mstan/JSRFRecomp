# Jet Set Radio Future Recompiled

Explore Tokyo-to on PC with adaptive widescreen, higher internal resolution
and controller support through an Xbox-themed launcher. JSRFRecomp uses
[xboxllr](https://github.com/mstan/xboxllr), the shared Xbox Low Level Recompiler.

![Jet Set Radio Future gameplay in Chuo Street with an expanded widescreen view](docs/screenshots/chuo-widescreen.png)

*Chuo Street in the development preview, after loading an original in-game save.
[Image credits](docs/screenshots/NOTICE.md).*

[Features](#features) | [Getting started](#getting-started) |
[Controls and graphics](#controls-and-graphics) | [Credits](CREDITS.md)

## Features

| Feature | Available in the development preview |
| --- | --- |
| Adaptive widescreen | Fit gameplay to the window, or choose fixed aspects through 32:9, with expanded camera visibility and adjusted HUD anchors. |
| Higher resolution | Native internal heights of 1080p, 1440p, 1800p and 2160p. |
| Image quality | Optional FXAA, supersampling from 1x through 8x, and anisotropic texture filtering. |
| Smoother presentation | Optional blended 60/120 Hz presentation while gameplay keeps its original timing. |
| Controller selection | The shared recomp-ui Player 1 card detects connected controllers and remembers the selected device. Keyboard input is also available. |
| Early Test Runs | Collect an area's graffiti souls to unlock its challenges without finishing the story. Enabled by default; switch it off in Mods for the original rule. |
| Custom graffiti images | Import PNG/JPEG/TGA artwork from Mods > Manage Graffiti at native, 2x or 4x detail. Browse saved thumbnails, view full-size artwork, or delete a selected design. Free slots and storage space update automatically; imports add a new design. |
| Skippable startup screens | A/Start dismisses the startup logos and graffiti warning with the original fade. Enabled by default; switch it off in Mods > Presentation for the original timing. |
| Hold Start to skip story cutscenes | Optional, off by default in Mods > Presentation. Release Start after a scripted story scene begins, then hold it for one second to request the game's original scene cleanup. Gameplay pause and ordinary dialogue controls remain unchanged. |
| Original saves | Real in-game saving and fresh-process Load Game, character selection and movement. |

Enhancements are individually selectable mods. Fresh launchers default to
adaptive Fit to screen, a 16:9 starting window, Original internal resolution,
3x supersampling, FXAA, 8x filtering and sharp original frames. Gameplay keeps its
original timing. Optional blended frames add motion blur, double edges and one
source frame of latency. The first update resets the earlier automatically
enabled blending; later explicit opt-ins are remembered. Actual higher-rate
gameplay is unavailable.

Releases include the RPTK and RAID Discord emblem PNGs under `extras/graffiti`,
with recommended SS/XL and 4x import settings. Only these two emblems are bundled;
personal imports remain in each player's local save/profile.

## Getting started

**[Download the Windows x64 preview](https://github.com/mstan/JSRFRecomp/releases/tag/windows-preview-2026.11.02.1).**
The Windows ZIP includes the precompiled native application, launcher, Python
and runtime dependencies. No compiler is needed to play. Matching project and
prepared dependency source is included under source/ and on the release page.
Linux releases remain deferred. The setup flow is described below.

The [October 27 optimization update](docs/RELEASE-NOTES-2026.10.27.1.md)
retains both supported revisions and existing features. Matched performance is
neutral/inconclusive for both revisions; no reproducible regression was found.

The [October 24 update](docs/RELEASE-NOTES-2026-10-24.1.md) adds the USA standalone
retail revision. It also includes the [controller hotfix](docs/RELEASE-NOTES-2026-10-23.2.md)
for connected gamepads that gave no input, Early Test Runs and existing
presentation and save support.

You supply your own **Jet Set Radio Future (NTSC-U)** files. Open **Start Game.cmd**,
choose **Skip** in the optional first-launch console setup, and select the
supported `.iso`, `.xiso` or extracted `default.xbe` on the main screen. Disc
images are imported once with progress and Cancel, then reused from `data/discs`
with the same gameplay file access as an extracted copy. Keep that cache across
updates to avoid importing again. Extracted XBEs still need the complete game
asset folder beside them. This preview supports both the original
development input (certificate revision 4) and the USA standalone retail
release (certificate revision 1). The launcher chooses the matching native
program automatically. Other revisions remain unsupported.
Original game files are not included in this repository.

| Supported NTSC-U executable | `default.xbe` SHA-256 |
| --- | --- |
| USA standalone, certificate revision 1 | `fd19055756719893c466302809b433b785ecf5732df0441286f3f605f0f3ef9c` |
| Existing development input, certificate revision 4 | `f4441696fdd007c31a712815cdde967836fbc3ab97fcb2f58e1db56974644219` |

The October 23 download supports only revision 4; use the October 24 update for
the standalone release. Default console profiles and save folders are separate
for each revision; selecting another revision
preserves the existing profile and progress. Shared or original-console saves
retain their normal identity and signature checks.

No kernel dump, EEPROM or HDD image is needed to create a new local console.
Automatic save storage is private to this game's package; no large disk image
is generated. Advanced **Settings** can import original signing material and
EEPROM, choose a shared save folder, or use an existing raw/QCOW2 FATX HDD image.
An image takes priority over folder storage and requires validated original
signing inputs and matching console identity. Original saves still undergo
normal verification. Close xemu before sharing a disk image.

Keep the package's `data` folder, your selected save storage and any
`<image>.xboxllr` profile when updating. A new virtual identity is not equivalent
to your physical Xbox's save identity. Xbox Live is unavailable; this generally
does not affect new single-player play. Standalone virtual-profile saving and
fresh-process loading pass the representative check described in the
[revision admission notes](docs/REVISION-USA-STANDALONE.md). The full
image-backed per-title save matrix remains qualification work.
See the shared [setup guide](https://github.com/mstan/xboxllr/blob/master/docs/SETUP.md).

For an already prepared checkout, build and open the shared launcher:

```powershell
python tools/game.py build-launcher --paths local/paths.json
python tools/game.py run --paths local/paths.json --launcher
```

See [developer setup](docs/DEVELOPMENT.md), the
[title profile](native-title.toml) and the shared
[native-title driver guide](xboxllr/docs/NATIVE-TITLE-DRIVER.md) for prerequisites,
preparation and builds. The framework's
[release readiness plan](https://github.com/mstan/xboxllr/blob/master/docs/RELEASE-READINESS.md) tracks packaging,
platform support and distribution requirements.

## Controls and graphics

Choose the input device in **Player 1**, select enhancements in **Mods**, then
launch the game. Individual button remapping is not exposed in this preview.
Use `--launcher` to reopen settings if you previously selected Skip launcher.

Pressing Play with a controller selects that controller for gameplay. Friendly
names are retained while disconnected. Alt+Enter toggles borderless desktop
fullscreen; normal window placement, maximized state and borderless state are
remembered across game launches. Keep the package's whole `data` folder.

**Early Test Runs** keeps the game's original soul requirement for each area.
It changes the Roboy menu's availability checks without awarding souls or
changing story progress. Disable it in Mods to require story completion again.

Adaptive widescreen follows the window's aspect. Score text, dialogue portraits,
speech panels and inventory have title-specific placement fixes through 32:9.
Higher resolution and supersampling increase GPU cost; begin with original
presentation timing when comparing performance.

## Current playtest scope

The original title and attract demo run, and gameplay is available. A rapid
cheat-assisted sweep entered all 19 campaign/gameplay scene groups and nine
story-event groups, plus 13 additional encounter files. The final post-fight
sequence was reached with a forced defeat condition. These are coverage checks,
with explicit bypasses; they do not qualify every mission's natural mechanics.

Original save/load, sampled movement, grinding, graffiti and progression have
direct evidence. The owner briefly playtested the visual preview and reported
that it looked good. Extra-mode setup, deeper recovery checks and exhaustive
routes remain deferred. See the [gameplay burndown](docs/NATIVE-GAMEPLAY-BURNDOWN.md)
and [content ledger](docs/CONTENT-COVERAGE.md) for passed checks and limits.

The tested gameplay profile compiles original CPU code ahead of time and uses
shared native services. It has no guest x86 interpreter fallback. Unsupported
paths stop explicitly; scene-entry coverage is not proof that every function
or gameplay path has been exercised.

## Credits and distribution

Development and integration: **Matthew Stanley**. Special thanks to
**sp00nz / sp00nznet**, **Phobos**, **NoRain** and the **xemu contributors** for
the recompiler, renderer, audio and hardware work used or referenced by the
shared framework. [Credits](CREDITS.md) links their projects and the detailed
component inventory.

This repository does not grant rights to Sega's original game files. The
owner-original source uses [GNU GPL version 3 or later](LICENSE), subject to
[license scope](LICENSE-SCOPE.md). Third-party work retains its own terms.
The native application includes ahead-of-time translated execution code; users
supply the original game data/assets. Original-title source bodies are generated
from their own input. See [the original rights notice](RIGHTS-NOTICE.md).
