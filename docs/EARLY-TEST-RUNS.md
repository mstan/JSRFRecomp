# Early Test Runs

Tracking: `beads-xbox.2.15`.

The default-on **Early Test Runs** mod removes the finished-story prerequisite
from Roboy's Test Run menu. Each area's original graffiti-soul requirement
remains. A saved OFF selection restores the original story prerequisite.
The mod works without visual enhancements. It changes disposable menu
allocations and the results screen's separate postgame prerequisite; it never
awards souls, advances the chapter or directly edits a save. Earned character
rewards continue through the original rank/area checks and award routine.

The supported original `0x756E0` first requires chapter9 and then builds four
challenge lists using per-area total-souls == collected-souls comparisons.
The authored title registry reproduces those menu lists for earlier chapters,
retaining the original loaded rows, destination IDs and availability values.
Chapter9 is left to the original code. The base CPU translation stays unchanged.

Focused validation on October23:

- Six portable tests pass, including missing-soul locking, completed-area
  unlocking, disabled/postgame behavior, invalid destinations and repeat calls.
- Four soul-bit patterns produce exactly the original postgame routine's menu
  bytes in a bounded Unicorn comparison, with the mod's chapter still early.
  The original XBE and proof tables are hash-checked; none are redistributed.
- Three existing visual contract tests pass. Shared launcher, selection,
  packaging and runtime checks pass: 66 tests, four skipped on this host.
- The optimized native build passes. Original Load Game reaches Chapter2's
  Garage; the native Roboy menu reports Test Run available after a private
  RAM-only soul-completion setup. The source save hashes remain unchanged.

This qualifies the changed unlock predicate and menu availability. The automated
follow-up navigation did not establish entry into a challenge: directional
inputs left the initial submenu selected, and a later retry timed out at the
title. These are recorded limits, not challenge-gameplay passes. Broader original
extra-mode initialization and mechanics remain deferred under `beads-xbox.2.9`.
No release or existing Nextcloud ZIP is replaced by this local feature build.

October26 reward correction: the results constructor independently queried
chapter9 before running any character reward checks. The exact admitted call
site now reports that prerequisite as met when Early Test Runs is on, retaining
all original earned-rank, area and already-unlocked checks. The generic chapter
getter's other callers, chapter RAM and disabled behavior are unchanged. Both
revision contracts pass. The reporter's Garage challenge recording is retained
privately for gameplay validation; no complete earned-reward pass is claimed.
