# Playing JSRF Recompiled

## Setup

Download the [Windows x64 beta](https://github.com/mstan/JSRFRecomp/releases/tag/windows-preview-2026.11.02.1),
extract the entire ZIP into a writable folder and open **Start Game.exe**.
The launcher and runtime dependencies are included; no compiler is needed.

Choose **Skip** in the optional console setup for a new local console identity.
New local play needs no kernel dump, EEPROM or HDD image. Select your own
supported `.iso`, `.xiso` or extracted `default.xbe`. An extracted XBE needs its
complete game asset folder beside it. Disc images import once and are reused
from `data/discs`.

The supported inputs are the USA standalone release and NTSC-U certificate
revision 4. The launcher selects the matching native program automatically;
default save profiles are separate for each revision. Other revisions are not
supported. Original game files are not included.

Select your device in **Player 1**, choose **Mods**, then press **Play**.
Pressing Play with a controller selects that controller. Individual button
remapping is not exposed in this beta. **Alt+Enter** toggles borderless
fullscreen, and window placement is remembered.

## Graphics and gameplay options

Fresh settings enable adaptive **Fit to screen** widescreen, Original internal
resolution, 3x supersampling, FXAA and 8x filtering, with sharp original frames.
Saved choices are kept when updating. Higher resolution and supersampling cost
GPU time; reduce them if performance is poor on your hardware.

Fit to screen follows the window's aspect, or choose a fixed aspect through
32:9. Gameplay expands with title-specific HUD placement. Internal height
overrides run up to 2160p; supersampling choices run from 1x through 8x.

**Early Test Runs** is enabled by default. Collect the area's required graffiti
souls to access challenges without finishing the story. It does not award souls
or story progress. Disable it in Mods for the original unlock rule.

**Mods → Manage Graffiti** imports PNG, JPEG and TGA files at native, 2x or 4x
detail. Imports add new designs to your local save/profile. Browse, preview or
delete artwork in the launcher; talk to Roboy and choose **Graffiti → Pick or Edit**
to select a design in-game. RPTK and RAID Discord emblem examples are included
in `extras/graffiti` with suggested settings.

Startup-logo skipping with A/Start is enabled by default. Optional story-scene
skipping is off by default: release Start after a scripted story scene begins,
then hold it for one second. Normal gameplay pause and dialogue controls remain.

Optional blended 60/120 Hz presentation blends existing frames. It can add
double edges and one source frame of latency; it does not increase simulation speed.

## Saves, settings and updates

Keep the complete **`data` folder** when replacing a Windows package, including
console identity, imported discs, settings and native saves. Preserve any
selected external save folder, HDD image and its accompanying `.xboxllr` profile.
An original-console save may need matching signing inputs and console identity.
See [console and save setup](https://github.com/mstan/xboxllr/blob/master/docs/SETUP.md).
Close xemu or other writers before sharing an HDD image. Xbox Live is unavailable.

A Linux AppImage matching the current Windows release is still being prepared.
Existing native Linux packages use an Ubuntu 24.04/glibc baseline and Vulkan 1.3.
Their settings and saves live **outside the AppImage**, at
`${XDG_DATA_HOME:-~/.local/share}/xboxllr/xbox-5345000a/data/`.

For a custom location, use an absolute `XDG_DATA_HOME` path and keep using it
after replacing the application:

```sh
XDG_DATA_HOME="$HOME/Games/xboxllr-data" ./JSRFRecomp-linux-x86_64.AppImage
```

FUSE-less environments can use `--appimage-extract-and-run`. Bounded WSL startup
checks do not qualify full-speed gameplay or the complete campaign.

## Testing scope

This is an early beta. Movement, grinding, graffiti, sampled progression and
native save/load have direct testing, but JSRF has **not been exhaustively
playtested or tested end to end**. Assisted scene coverage does not establish
every mission, encounter or recovery path. See [coverage](CONTENT-COVERAGE.md)
and [reporting bugs](REPORTING-BUGS.md).
