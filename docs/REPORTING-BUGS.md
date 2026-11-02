# Reporting JSRF bugs

JSRF is an early beta and has not been exhaustively playtested or tested end to end.
[Open a GitHub issue](https://github.com/mstan/JSRFRecomp/issues/new) with:

- Release version and supported game revision.
- Operating system, CPU, GPU and controller.
- Area or mission, selected mods, steps to reproduce, expected behavior and actual behavior.
- A screenshot or short recording when useful, plus the diagnostic report below.

## If the game crashes

In the Windows crash report dialog, select **Copy diagnostic ZIP** or
**Open report folder**, then attach that ZIP to the issue.

The shareable ZIP is saved under **`data/diagnostics/crash-reports/`**. It
contains selected diagnostic logs, build information, your description and
validated controller inputs where available. The export excludes native saves,
console signing secrets and raw private logs.

## If the problem does not crash

Close the game normally and attach the latest session's **`report.json`** from
**`data/diagnostics/<session>/`**. Include the reproduction steps and a screenshot
or recording. Keep the local private session in case further investigation is needed.

On Linux, find `data/diagnostics` under the external application-data directory
described in the [save and configuration guide](PLAYING.md#saves-settings-and-updates).

## What not to upload

Do not upload **`PRIVATE-DO-NOT-SHARE`**, the complete `data` folder, original
game files, console keys or EEPROMs. The private directory may contain original
saves, console identity/signing material and raw logs. Use the crash dialog's
shareable export rather than zipping the complete diagnostic session yourself.
