# Windows preview — 2026.10.26.3

Both supported NTSC-U revisions are included; the launcher selects the matching
native executable from the original game hash. This release includes the
combined graffiti, portrait, crash-report and optional story-skip work.

- **Manage Graffiti** in Mods imports external images as new native save designs.
  It shows free slots/storage automatically, browses saved thumbnails, opens
  full-size previews and deletes a selected design after confirmation. Images
  can retain native,2x or4x detail through a content-bound companion; native
  in-game edits fall back to the game's edited artwork. Size labels show aspect
  ratios and original dimensions. Existing unrelated saves are preserved.
- Only the **RPTK mascot** and **RAID Discord emblem** source PNGs and import
  instructions are bundled under `extras/graffiti`. They are available for
  importing through Manage Graffiti, not automatically installed into saves.
  No personal artwork, saved progress or console identity is distributed.
- Graffiti menu import/preview/back navigation receives allocation, file-path,
  texture-format and viewport-clear corrections. Multiplayer portrait/name
  atlas transforms now select distinct characters rather than repeating Beat.
- Early Test Runs now let the original results code evaluate earned character
  rewards before story completion. Original area/rank requirements still apply;
  the mod does not directly award characters or change the chapter.
- Startup logos and the graffiti warning can be dismissed with A/Start through
  their original fades. This title enhancement is enabled by default.
- **Hold Start to skip cutscenes** is an optional, default-off mod under
  Presentation. Release Start after a story scene begins, then hold it for one
  second. It requests the original scripted-event cleanup; ordinary gameplay
  pause and dialogue controls retain their existing behavior.
- Unexpected stops open a crash-report window with the recorded reason and a
  **Copy diagnostic ZIP** action. Shareable reports exclude keys and native
  saves; private reproduction material remains on the player's computer.

Both optimized revisions and20 title mod contracts pass. Actual USA validation
includes custom graffiti, distinct multiplayer portraits and six unseen
scripted scenes skipped into normal gameplay. The final chapter, next mission
and viewed-scene flags match watching that intro normally; short Start presses
do not skip it. This is representative scene coverage, not an all-cutscene audit.
The exact Dogenzaka corner-flicker angle and earned Test Run/post-run preview
remain pending human checks, despite the underlying renderer/reward fixes.

Close the old build before updating, and keep its complete `data` folder,
external save folder or HDD profile. Existing native saves, personal graffiti,
console identity, controller choices and imported-disc caches are not replaced
by a fresh release ZIP. Original game and optional console files remain
user-supplied.
