# Windows controller hotfix - October 23, 2026

The shared SDL2 transport now pumps Windows controller notifications even
though the native renderer does not initialize SDL video. This fixes gamepads
that appeared connected but supplied no buttons or stick movement. The same
selected device and hot-plug behavior are preserved. The fix is compiled in;
no Steam or global environment setting is required.

The default-on Early Test Runs mod remains included: collecting an area's
graffiti souls unlocks its challenges without finishing the story. Disabling
the mod restores the original rule. Widescreen, camera inversion and the
existing optimized native gameplay profile remain available. Gameplay timing
and the documented campaign/optional-mode qualification limits are unchanged.

Extract the full ZIP and open Start Game.exe. Preserve the existing data folder,
console identity and selected save storage when updating. The package includes
matching project/framework and prepared dependency source under source/, and
excludes original game data, personal saves and console signing inputs.
