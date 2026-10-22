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
| Image quality | Optional FXAA, 2x2 or 3x3 supersampling, and anisotropic texture filtering. |
| Smoother presentation | Optional blended 60/120 Hz presentation while gameplay keeps its original timing. |
| Controller selection | The shared recomp-ui Player 1 card detects connected controllers and remembers the selected device. Keyboard input is also available. |
| Original saves | Real in-game saving and fresh-process Load Game, character selection and movement. |

Enhancements are individually selectable mods. Fresh launchers default to
adaptive Fit to screen, a 16:9 starting window, 1080p internal height, 2x2
supersampling, FXAA, 8x filtering and blended 60 FPS presentation. Gameplay
keeps its original timing. Interpolation can show double edges and adds one
source frame of latency. Actual higher-rate gameplay is unavailable.

## Getting started

**[Download the GPL source/tooling preview](https://github.com/mstan/JSRFRecomp/releases/tag/preview-2026-10-22).**
This release contains build tools, title metadata/mods and the pinned framework.
It does not contain a precompiled game or original game code. Use the
[developer setup guide](docs/DEVELOPMENT.md) to build locally with your own game.
The tested native host is Windows x64; Linux releases are deferred.

The local owner-use Windows candidate includes the launcher, Python and native
dependencies. Its setup flow is described below for locally prepared packages.

You supply your own **Jet Set Radio Future (NTSC-U)** files. Open **Start Game.cmd**,
choose **Skip** in the optional first-launch console setup, and select the
supported extracted `default.xbe` on the main screen. Keep the complete game
asset folder beside that XBE. Direct ISO import and other revisions are not
supported yet. Original game files are not included in this repository.

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
does not affect new single-player play. Fresh virtual-profile save/restart/load
and the full image-backed per-title save matrix remain qualification work.
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
The source/tooling release excludes original and generated game code; local
precompiled owner candidates are not included.
