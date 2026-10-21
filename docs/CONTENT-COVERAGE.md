# JSRF content coverage

Tracking: `beads-xbox.2.6`. This is a coverage ledger, not a qualification percentage.
The owned content inventory has 311 mission/script file pairs under 33 scene keys.
These keys include event scenes and extra modes; they are not 33 proven playable areas.
A filename number aliases modulo 100, so runtime IDs below come from observations
rather than treating every filename as a canonical mission ID.

All area prerequisites reached through forced handover are bypassed. A loaded scene,
a screenshot or movement alone does not pass its enemies, collision, unique mechanics
or completion trigger. Inputs sent during an event do not establish controllable movement.

| Scene key | Files | Observed runtime ID | Evidence so far | Mechanics/completion |
| --- | --- | --- | --- | --- |
| `0x00000000` | 52 | `10001` | Movement, camera, NPC talk, original jump/grind lessons, real pickups and two original boosts through shared bc4d290 | Open: spraying and later tutorial/progression |
| `0x00000008` | 1 | `100c4` | Cutscene entry/motion; end unverified | Open |
| `0x00000009` | 1 | `200c4` | Story event entry/animation captured in run014 | Open |
| `0x00010000` | 16 | `10014` | Shibuya Terminal: movement, original story encounter, all 35 regular graffiti plus save point painted; original map 35 (100%); progress saved; fresh036 restores all36 targets; four Poison Jam routes and Combo challenge complete through original flow | Passed: reached police-fight completion and original Chapter2 transition; other chapter variants open |
| `0x00010001` | 18 | `2001e` | Introduction entry | Open |
| `0x00010002` | 17 | `1000a` | Movement and original story conversation/return | Open |
| `0x00010003` | 12 | `40032` | Introduction naturally returns to gameplay | Open |
| `0x00010008` | 1 | `300c4` | Story event entry/animation captured in run014 | Open |
| `0x00010009` | 1 | `400c4` | Story event entry/animation captured in run014 | Open |
| `0x00020000` | 21 | `20028` | Introduction, repeated revisits/movement, one real three-part Graffiti Stop spray and original save creation in run028 | Open: regular graffiti mission, encounters and completion |
| `0x00020001` | 10 | `3003c` | Entry/movement; point failure fixed | Open |
| `0x00020002` | 20 | `4003c` | Introduction entry | Open |
| `0x00020003` | 15 | `30046` | Entry/movement; story text observed | Open |
| `0x00020004` | 8 | `70032` | Introduction entry | Open |
| `0x00020008` | 1 | `500c4` | Story event entry/animation captured in run014 | Open |
| `0x00020009` | 1 | `600c4` | Story event entry/animation captured in run014 | Open |
| `0x00030000` | 15 | `20032` | 99th Street introduction | Open |
| `0x00030001` | 8 | `6003c` | Introduction entry | Open |
| `0x00030002` | 21 | `5000a` | Entry and movement | Open |
| `0x00030003` | 17 | `40050` | Introduction entry | Open |
| `0x00030004` | 14 | `40046` | Introduction entry | Open |
| `0x00030008` | 1 | `700c4` | Story event entry/animation captured in run014 | Open |
| `0x00030009` | 1 | `800c4` | Story event entry/animation captured in run014 | Open |
| `0x00040000` | 1 | `8005a`, `8037a` | Run014 introduction renders past scaled-point failure and naturally returns to15; forced-entry arena spawn remains open | Open |
| `0x00040001` | 1 | `80050` | Original introduction captured in run011 | Open |
| `0x00040002` | 1 | `8000c` | Original introduction captured in run011 | Open |
| `0x00040003` | 2 | `8000b` | Original introduction captured in run011 | Open |
| `0x00040008` | 2 | `800c6` | Original story event entry/animation captured in run014; alternate file variant unverified | Open |
| `0x00050000` | 6 | Not observed | Unverified | Open |
| `0x00050001` | 6 | Not observed | Unverified | Open |
| `0x00050002` | 6 | Not observed | Unverified | Open |
| `0x00050003` | 7 | Not observed | Unverified | Open |
| `0x00050004` | 7 | `14000a` | City Rush briefing/countdown only; direct handover misses proper race/player setup | Open |

Initial evidence: `mission-qa-001/004/007/008/010`. Current captures and raw state
stay private under `G:/Temp/Codex/JSRFRecomp/gameplay-20261020` and
`F:/Temp/Codex/JSRFRecomp/gameplay-20261020`. In run010, the 40032 event returned
from19 to15 without a completion write or further A input. The late-game 0811
request loaded its file and the original scripts later loaded0890 and returned
to the title/attract. This does not pass the final boss or establish the exact
0811 scene path in run010. Run011 subsequently captures that introduction and
the next two late-game scene types, then stops at scaled point sprites while
entering0890 (`beads-xbox.1.182`). Run014 repeats the sequence after the shared
point-sprite implementation: the introduction renders and returns naturally
to15. The carried-over player position falls outside the final arena after
forced handover, so boss gameplay is still unverified. Run012 also reaches a
City Rush briefing; it does not establish a properly initialized race.
The run010 observer timed out before its asynchronous progression;
the process remained alive and was observed rather than restarted.

Run014 additionally batches all eight remaining story-event scene keys in one
live process. The original scene-key values and entry frames are observed;
natural ends and their outgoing progression are unverified. In total 28 of33
scene groups now have visually inspected rendered entries. This count includes
introductions and studio events, not 28 fully tested playable areas. The five
extra-mode scene groups still need proper initialization and world coverage.

The reverse handover3003c ->20028 unmapped read is fixed by shared `eb180a4`
under `beads-xbox.1.181`. Fresh run022 passes that route, then repeats
20032 ->3003c ->20028 with playable movement on the final revisit. This closes
the reached allocation failure, not the bypassed missions or their mechanics.
The screen-space unit-point failure in the forward
sequence is fixed by shared commit `bc3a6a6` (`beads-xbox.1.180`).

## Mechanics that still need coverage

| Behavior | Current scope |
| --- | --- |
| Movement, camera and jump/landing | Initial Garage passed; movement observed in several additional areas |
| NPC interaction | Corn/Gum passed; run036 triggers Poison Jam and Combo through original RT/A dialogue, including original Yes/No selection |
| Graffiti/spraying, pickups and resource limits | Real can pickups and original collection lesson passed in run024. Run034/035 paints every Shibuya Terminal target through actual RT, including one/three/six-part wall tags and its save point; original map 35 (100%). Ten-part tags, other areas, limits and other pickup types remain open |
| Boost, grinding, tricks, jumps and traversal routes | Garage jump/grind lessons passed; rail movement, sparks and scoring rendered. Run028 performs two boosts with cans12 ->2 and blur/fire effects. Requested trick combinations and other traversal remain open |
| Enemies, police encounters and bosses | Run036/037 real lock-on/dash knockdown plus close RT spray disables the reached20-cop fight, with original completion/Chapter2 transition; bosses and other enemy families open |
| Real mission completion and next-mission triggers | Four Poison Jam recordings return through original exits; Combo street challenge reaches original success and next story conversation, then cop-fight entry. Travel bypassed, no completion/action-field writes. Run037 cop-fight terminal transition enters original Chapter2 introduction. Wider progression open |
| Death/retry, checkpoint handling and game-over | Unverified |
| Save and authenticated fresh-process reload | Passed for the reached same-chapter10014 save: run032 saves, fresh run033 loads through original menus, restores the painted save-point target and responds to movement; no validation bypass |
| All remaining script variants and scene exits | Unverified; inventory presence does not prove execution |

Supporting precision/oracle validation remains in the SV01-SV08 deferral list of
[the gameplay burndown](NATIVE-GAMEPLAY-BURNDOWN.md). Reached crashes and missing
output remain required fixes.

Run023 reaches Gum through a position-only teleport near `(-140,-9,285)` and
the original RT conversation trigger. Original A inputs finish her instructions,
and ordinary jump inputs satisfy her three-jump counter. Teleports above the
visible Garage rail bypass travel; the original fall/rail collision starts a
grind, with follow-camera mode5, constrained rail height, automatic movement,
sparks and scoring. The original lesson advances through “Grind one more time”
to “Collect 10 Spray Cans.” No lesson or completion flag is written. The run
then ends at its planned bound; pickup/spray and the rest of the tutorial remain
open. A private replay batch now reproduces these inputs/teleports in one route,
so future runs need not repeat the exploratory menu and positioning steps.

Run024 repeats the tutorial using original actions and position-only teleports.
The pickup sweep raises the visible can count from0 to8 to12, and the original
lesson acknowledges collection. This establishes real pickups rather than a
resource-count write. The following B/stick boost attempt reaches an explicit
caller-owned texture-layout stop, tracked by `beads-xbox.1.183`; boost and spray
are not yet passed. The private executable, symbols, receipt and captures are
retained. The next action is to fix and retry this reached native boundary.

That stop is now fixed by shared `bc4d290`: the resource is a standalone depth
surface used during SetRenderTarget, not a texture. The shared implementation
retains caller storage and supplies a native depth/stencil target. Actual GPU
bytes, retained GPU contents across rebind, references and teardown pass across
three device lifetimes. Run028 performs two boosts (each cans12 ->2), renders
the blur/fire trail, then loads3003c with movement and revisits20028. Refill and
travel prerequisites are bypassed explicitly; exact effect pixels and campaign
completion are not established. Run028 subsequently paints the original
three-part Graffiti Stop target592 using actual RT input, with cans30 ->27 and
unpainted1 ->0, and activates its save point. The original menu creates
Game File1 and reports Done saving, with new private JSRFDATA.SAV and
SaveMeta.xbx files. Prerequisite refill and area entry are bypassed; ordinary
wall-tag mission completion remains open. The first cross-chapter forced save
is unsuitable for reload: its unchanged persistent Chapter1 requests missing
mssn0140, while the forced area was mssn0240. No fake alias or load pass is
claimed for run031. Same-chapter run032 paints target576 at10014 and saves;
fresh run033 accepts that file through original Load Game/character selection,
returns to playable10014/state15, retains target576 painted and moves normally.
This closes the reached save/reload check while campaign progression remains
open. QA handovers do not update persistent story flags.

## Shibuya Terminal graffiti checkpoint

Run034 uses the original Load Game path, then batches revision-bound position
candidates and actual RT spraying. Small wall tags and a six-part mural pass;
the Poison Jam story encounter renders and returns naturally to gameplay.
Several initial position candidates are below terrain or inside collision,
so displacement and return-to-save-point behavior are recorded separately.
The first attempt eventually returns to the original title; no mission-clear
or complete game-over qualification is inferred. Same-process reentry is
separate from the independent-process reload evidence.

Above-floor candidates and bounded health refills retain the next batch's
progress. Run034 paints 30/36 registered targets and saves normally. Fresh
process035 loads that exact checkpoint and independently observes all 30
painted targets retained. The remaining six are painted using position
candidates offset toward the descriptor's normal; no paint flags are written.
All 36 descriptors are painted, and the game's map reports 35 (100%) regular
graffiti, excluding the save point. Actual RT can use, original spray
animations and one/three/six-part designs are observed. The fully painted
state is saved normally; the final private save is41088bytes, SHA256
e73a248b47612848d009cf4f078af56207c5375a03e11b7923ac4c899b652d76.
Travel, resource collection and some story prerequisites are bypassed.

At the run035 save checkpoint, the original flow remains10014/state15. The
100% graffiti display does not establish a complete mission or its exit.
Original NPC/exit-triggered progression, encounters and other unique actions
remain open. The parsed0120 mission lists exits to0121/0122; those are route
candidates until an actual transition is observed.

Descriptor IDs are assigned again when a world loads. Repeated same-process
loads can change IDs even for the same target. Compare scene and geometry
when checking persistence, rather than assuming an earlier ID is stable.

Read-only save/mission format inspection uses
[andeecollard/jsrf-recomp's MIT-licensed QA tools](https://github.com/andeecollard/jsrf-recomp/tree/4242eb69694c8752ca42550ca3765e56288d4535/diagnostics/jsrf_first_fault/gametools).
The private saved slot decodes with valid lane popcounts and records the
actual original chapter flags 21/22/23 and events 10/23. Its 64 painted
marks match the sum of the 36 registered target sizes. The upstream editor's
zero-key signature assumption does not match this runtime's save, so its
writer is not used. Original game save validation stays active. Reference
tools, decoded game state and captures remain private; no upstream runtime
code or original content is added to this repository.
## Shibuya original story chain and combat

Fresh process036 loads the final graffiti checkpoint and observes all36 painted
targets retained. Original talk regions parsed from owned0120 supply the four
Poison Jam approach positions. Actual RT/A input triggers each conversation,
mission0121 (observed runtime10079), its recorded skating route, and the original
return to0120 (runtime10078). The game advances chapter flags itself; none are
written by the QA controls. Four routes and their returns pass in this scope.

Combo's original conversation, explicit Yes selection and demonstration then
reach playable0123 (runtime1007b). Simply teleporting to its endpoint does not
complete the challenge. The original challenge manager observes two real grinds
and an actual X air trick in the required regions, advances stages0 ->1 ->2 ->3,
and sets its own success state. Original progression clearsC31, setsC32 and
returns through event22 and Combo's following conversation. Teleports bypass
travel between action regions; completion, action-kind, counters and story flags
are never written. This passes the reached challenge's action consumers and
terminal transition; it does not qualify skating the whole route without cheats.

The next original conversation enters0122 (runtime1007a), with its cop introduction
and playable fight. Actual LT lock-on/B dash knocks an original cop down; close RT
spray consumes cans, enters the original tagging animation and disables the cop
(original state26/removal flag). Only player positions and bounded resources are
changed by QA. Full fight completion and outgoing chapter transition remain open.
Run036 ends at its planned time bound, rather than an unsupported native stop.
The known route is now a single batch for replay and checkpoint creation in037.

Format/name references for locating these original consumers are
[KeybadeBlox/GG-Notebook](https://codeberg.org/KeybadeBlox/GG-Notebook)
(WTFPL2, mission layout blob7aa51fa8c69abfa2f85fae9a11f7581dcb114365) and
[KeybadeBlox/JSRF-Decompilation](https://codeberg.org/KeybadeBlox/JSRF-Decompilation)
(CC0, listing blob247094a23b3ce182c92ed211b6f919050f5468e8).
Addresses/layouts are checked against this owned revision; upstream data addresses
are shifted and cannot be copied blindly. These remain private read-only references;
no original code or game content is shipped.

Run037 preserves an original story checkpoint after all four Poison Jam routes:
41088bytes, SHA256271de43150134f0472ae0ed86ec68431ee90443a7877419d8a332c99c582e59a,
chapter1/return mission120, C31/C50 and events10/21/23, with valid decoded lane
checks. The original save menu reports Done saving. The independent private
checkpoint omits the locked rebuildable native cache and retains identical save
bytes; an independent reload of this newer checkpoint remains open.

A repeat Combo attempt's teleport candidates touch its original retry conditions;
that is a QA route miss, not a demonstrated game failure. Run036 remains its actual
success evidence. To avoid re-proving that completed check, run037 explicitly
bypasses the repeat prerequisite through original handover0122. It then uses actual
LT/B lock-dash and RT spraying for the entire20-cop fight, with bounded can/health
refills and close-approach teleports. No enemy-health, action, mission-completion
or chapter flags are written. Several original hits disable more than one nearby
cop. The game retires disabled actor allocations, so the read-only observer treats
those lifetimes as retired rather than reading freed memory. The terminal proof
is the original mission itself: after its defeat listener/event/exit, native flow
enters20060 and persistent chapter advances to2. This passes the reached fight's
completion and outgoing progression; it does not establish the bypassed repeat
prerequisite or the remaining Chapter1 Dogenzaka content.

Chapter2 introduction ends through the original post-cutscene character selection
(runtime20126), then native Garage gameplay (200c8). The original Roboy interaction
opens its Garage/System/Save menus and saves normally. That save is41088bytes,
SHA2564322d791cb7ef0c52865586b81af9be062d98e5ac05e9b84e4b46fbd43d7a2b9,
chapter2/return mission0 with reset chapter flags and retained prior graffiti.
Fresh independent process038 accepts it through original Load Game and character
selection, returns to20000/state15 and responds to movement. This passes the
reached mission/chapter progression save/load boundary; other recoveries remain
open. Immutable private checkpoints retain both the earlier Shibuya story state
and this Chapter2 Garage state.

Run038 crosses the owned Garage plane1 using position-only travel bypasses; the
original exit loads0210 (runtime200d2), finishes its entrance camera and restores
ordinary movement. Crossing0210 plane2 similarly loads0230 (runtime200e6), with
its original introduction and playable Chuo Street. No handover/exit/completion
fields are written for either transition. Chuo registers25 graffiti targets,
including three10-part targets. The first XL approach triggers the original0231
(runtime200e7) tank encounter before spraying; the area-specific batch stops at
that real mission change. Tank completion and10-part spraying remain open.
Private run038 remains live, hidden/muted, at the reached tank encounter; the
Chapter2 Garage checkpoint is the independent restart source.
