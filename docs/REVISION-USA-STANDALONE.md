# USA standalone admission

Tracking: beads-xbox.2.17; shared package work: beads-xbox.1.198.

The USA standalone retail executable has SHA-256
`fd19055756719893c466302809b433b785ecf5732df0441286f3f605f0f3ef9c`,
MD5 `f4e366bfdceee551a09f42219c90d84e`, title ID `5345000A`,
certificate revision 1 and XDK 4134. Its 2,281,472-byte file is distinct from
the existing revision-4 input. Its entry point is `0x148023`; most static data
and SDK sections are 64 bytes later. Game-code differences prevent treating
the second full-file hash as an alias for the first native program.

`native-title-usa.toml` owns separate generation and bindings. Its profiles
record exact original body/table hashes and independently pass the existing
cache, input, classic D3D and audio binders, including their decoding, stack
cleanup and data-reference checks. One previously recovered cleanup entry is
already discovered normally in this input; the remaining recoveries retain
their own exact-image plans. No original XBE or asset is patched or bundled.

Both compiled title registries share the authored implementation with explicit
revision-specific mod sites. The new source-block and menu/table hashes live
under `config/revisions/usa-standalone/`. This mapping applies to those reviewed
sites, not arbitrary addresses in another release.

October 24 validation:

- Both native executables build. Both revisions pass disabled, fixed-aspect and
  adaptive visual contracts. Both Early Test Runs fixtures pass six checks,
  including four soul-bitmap comparisons with each original postgame x86 menu
  routine. The mod preserves chapter/soul bytes and existing menu ownership.
- Standalone New Game reaches the original Garage introduction and controllable
  gameplay. Ordinary stick input moves the player about 87 game units. Live
  4:3, 16:9, 21:9 and 32:9 resizing gives projection m0 values 1, .75, .5714286
  and .375 while m5 remains 4/3. Captures show additional world geometry and
  consistent health/can HUD placement. 1080p, FXAA, 8x filtering and blended
  60 Hz presentation are active in these samples.
- An explicit same-chapter mission handover and resource refill bypass travel
  and collection prerequisites. Real RT input paints Shibuya save target 576;
  no paint/completion fields are written. The original menu reports Done saving
  and creates a 41,088-byte JSRFDATA.SAV. A fresh process uses original Load Game,
  restores mission 10014 and the painted target, and responds to movement
  by about 68 game units. No signature override or save conversion is used.
- Revision 4 still loads a private Chapter-2 checkpoint into playable Chuo
  gameplay. Source checkpoint files remain separate from all writable QA state.
- A matched New Game Garage comparison uses the same player position and
  story/camera state, 1080p, 2x2 supersampling, FXAA, 8x filtering and adaptive
  16:9 with blended 60 Hz presentation. Two eight-second intervals per revision,
  sampled in ABBA order with the other process suspended, average 59.9902 Hz
  for each. This capped, short sample does not qualify campaign-wide performance.
- The authored routing/preservation checks, compiled launcher round trips,
  package integrity and embedded-Python standalone first-profile setup pass.
  Unknown identities and mismatched revision build receipts remain rejected.

This is revision admission with representative gameplay/save/mod coverage.
It does not expand the campaign or extra-mode qualification recorded in the
existing gameplay/content ledgers. Original disc-pressing provenance for the
revision-4 development input remains unconfirmed.

Private logs, RAM observations, screenshots, save fingerprints and exact build
receipts are retained under `local/usa-revision-20261024` and the task scratch
directory. Original game, console and save bytes remain private.
