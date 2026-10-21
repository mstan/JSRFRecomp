# Native gameplay and content coverage

Tracking: `beads-xbox.2.6`. The owner accepted the Dashboard preview on
October 20 and authorized this phase after its source commit `52eb13c`.
The qualified [idle attract](NATIVE-ATTRACT-BURNDOWN.md) stays complete within
its recorded scope; it does not establish interactive gameplay.

Work from the first unfinished row. Use short, muted native runs to expose
the next required boundary, then test that boundary and retry the same route.
Preserve the normal owner builds and saves. Generated code, original content,
state copies and evidence stay private on non-C: storage.

Owner priority, October 20: get through JSRF first. Supporting validation that
does not block the actual route is deferred below. Fix crashes, missing output
and broken gameplay as they are reached; do not expand qualification before
retrying the game. Preserve cheats/teleports as QA tools and record bypasses.

| ID | Work | Status | Completion evidence |
| --- | --- | --- | --- |
| GP01 | Build the current shared runtime with the verified native CPU inventory | Passed | Framework `52eb13c`, optimized/ITERATIVE executable `6cbf353b...`, verified original generation reused; actual native startup/title frames |
| GP02 | Start or load a game through the original menus | Passed: New Game enters the Garage introduction | `new-game-003`: real Start/release/Start/A reaches Corn's original GG's Garage dialogue with active positional audio; no direct-menu bypass; Load Game remains GP08 |
| GP03 | Reach controllable gameplay | Passed for initial Garage movement, camera, jump/landing, rail grinding and NPC talk | Initial routes pass movement/jump/Corn talk. Run023 triggers Gum's original conversation, satisfies her three-jump and grind lessons, and reaches “Collect 10 Spray Cans.” Teleports bypass travel and approach to the rail; original input/collision/counters establish the actions. Remaining tutorial and campaign mechanics remain GP07 |
| GP04 | Implement newly reached shared contracts | Reached boost failure fixed; continue with the next gameplay consumer | Shared `bc4d290` models the original standalone depth surface used by boost. Targeted actual GPU depth/stencil/ownership checks pass; run028 performs two original boosts with expected can consumption and visible effects, then loads3003c and revisits20028. No broad campaign qualification implied |
| GP05 | Derive the area/mission/mechanic inventory | Content inventory derived; behavioral mapping open | `tools/qa_inventory.py` parses all 311 owned mission/script pairs and their setup/trigger operation inventories, grouped under 33 scene keys. Scene keys are not automatically area names. Filename numbers alias modulo 100, so canonical runtime IDs still require original-flow evidence |
| GP06 | Add reusable cheat-assisted QA controls through title mods | Teleport, original handover, explicit event bypass and bounded can/health refill working; further controls open | Shared private RAM transport plus revision-bound `tools/qa.py` and `gameplay-qa.json`. Refills respect original character capacities and reject over-capacity requests without a write. Run034 validates health65 ->110 with the maximum unchanged. Run038 uses explicit private health protection and admits live-player lock/spray/look camera modes while retaining guards; refills do not pass pickup or damage checks |
| GP07 | Rapid stage/boss coverage with explicit cheats | Owner-clarified campaign sweep complete; extra-mode setups deferred | All19 campaign/gameplay and nine story-event scene groups have entry evidence. Thirteen additional encounter files reached, with live groups or rendered introductions. Final boss corrected spawn and original post-fight flow reached using the defeated-condition cheat. Off-camera model visibility, fair mechanics and full routes are not passed; see CONTENT-COVERAGE.md |
| GP08 | Validate save/reload and representative progression boundaries | Original save/fresh-process reload and reached Chapter2 progression save/load passed; wider recovery open | Run032 creates a same-chapter save at10014; independent run033 uses original Load Game and character selection, returns to playable10014, retains the painted save-point target and responds to movement. Run037 then completes the reached Shibuya cop fight and original Chapter2 transition, saves through Roboy; fresh038 loads the Chapter2 Garage and moves. Wider recovery/content remains GP07 work; owner originals are protected |

Cheats can position/protect the player and bypass prerequisites. A forced
mission-complete flag is recorded as a bypass; it cannot pass the real
completion trigger it replaced. Entering an area or capturing a still does
not pass its interactions, collision, enemies, mission behavior or audio.
Batch compatible routes in a single run and stop a run at its first required
unsupported boundary. Do not repeat the long attract observation for each fix.

The [content coverage ledger](CONTENT-COVERAGE.md) lists all 33 source-derived
scene keys and the remaining mechanics. These include event scenes and extra
modes; neither 33 keys nor 311 script pairs is a qualification denominator.

After gameplay coverage, add adaptive widescreen through 32:9, HUD anchoring,
higher internal resolution and the generic frame-rate mods. Real faster
simulation and frame interpolation remain separate, mutually exclusive modes.
Owner visual/performance review is the appropriate acceptance step for those
enhancements; gameplay timing must remain correct.

## Owner scope clarification: rapid coverage, 2026-10-21

The owner explicitly requests the bare minimum to load every stage and boss and
attempt coverage, using blatant cheats, instant kills and forced end sequences.
Do not spend the pass playing routes, reproducing combat input or qualifying each
repeated mechanic. Target a30-45 minute wall-clock sweep. Load each distinct scene
and boss setup, take a brief visual/input observation, force progression as needed,
and record reached failures and explicit bypasses. A forced victory is coverage of
the reached setup/end sequence, not a passed combat mechanic. Earlier mechanics
qualification language below is historical scope; exhaustive mission/mechanic
validation is deferred under this owner clarification. Visual enhancement work and
Blinx/Dashboard preservation/final owner review remain required after this sweep.

## Full end-to-end completion scope

The October21 owner goal (beads-xbox.2.6 and beads-xbox.2.7) includes gameplay coverage first, followed by visual
mods and final delivery. The goal remains open until each row has direct evidence;
scene entry, source registration and a successful build do not close these rows.

| Work | Status | Required evidence |
| --- | --- | --- |
| Areas and bosses; extra-mode setup deferred | Rapid campaign coverage recorded | All19 campaign/gameplay scene groups entered;13 encounter files reached. Original extra-mode initialization and mechanics remain deferred under the owner clarification |
| Recovery and audiovisual behavior | Original save/load and reached race failure/retry passed | Carry scoped evidence forward; deeper death/recovery and audiovisual permutations deferred unless a reached failure requires them |
| Adaptive widescreen and HUD | Sampled world/basic HUD and reported text cases pass | Actual 4:3/16:9/21:9/32:9 changes retain original vertical FOV and widen GPU/CPU projection/clipping. Owner-reported score/dialogue/prompt defects repaired with source-owned anchors and original pixel canvas. Actual rail scoring, centered talk prompt, right stock icon/count and bottom portrait dialogue inspected through32:9; broader effects remain sampled/reviewable |
| Internal resolution and fidelity | Implemented; representative gameplay passes | Actual2520x1080,5040x2160 and1920x1440 with3x3 supersampling, FXAA and8x/16x filtering; original movement/pause/resume. Intermediate resolution choices share the tested resolver/raster path. Owner performance review remains |
| Higher FPS and interpolation | Optional interpolated presentation implemented; gameplay simulation retained | Actual120Hz plan in controllable Garage with title gameplay scope and pause/resume cuts; original/interpolated modes are exclusive. Blended double edges are expected. Actual faster simulation remains unavailable without a qualified timing adapter |
| Compatibility and final handoff | Compatibility smoke passes; owner handoff delivered | Dashboard Home/Memory/Music/Settings and Blinx boot/cinematics rendered with frameworkb5e3b8e; three Blinx visual contracts pass. Coherent title pin, normal windowed Player1/mod launcher and100% volume delivered. Owner selected options and started the immutable native build; protected source saves and existing Blinx/Dashboard builds remain untouched |

Supporting precision/hardware SV01-SV08 and full runtime snapshots stay deferred;
actual reached crashes or broken output remain required fixes.

### Owner Load Game crash fixed, October21

`beads-xbox.2.12`: the enhanced preview stopped at the title mod's perspective
guard during original Load Game. A private copy of the owner's save reproduced
exit2 in run20261021-152856-98irjwxr: the original camera builder also creates a
512x512 offscreen view with m5=1 during mission state12. The mod incorrectly
required the gameplay4:3 matrix there. Save decoding and native CPU execution
were not the failing boundary.

Adaptation now requires the reviewed640x480 gameplay viewport. Other producers
retain their original projection, with only the mod's previous retained m0/m8
edits restored. Loading and in-game offscreen regression cases pass alongside
the disabled/fixed/adaptive contracts. Actual retest20261021-153157-yr297v14,
executable0cc19142..., uses the same adaptive1080p/2x supersampling/FXAA/8x
filtering/interpolated60 plan and the original Load/character-selection menus.
It reaches saved Chuo200e6/state15 and responds to ordinary movement. Captures
were inspected; the test then stops intentionally (exit15), not at a crash or
deadline. Owner source saves remain unchanged. Broader visual checks retain
their recorded sampled scope.

Current private work/evidence root:
`G:/Temp/Codex/JSRFRecomp/gameplay-20261020`.
The original native generation is copied intact from the prior qualified
input; generated output and state remain isolated from owner previews.

### Visual implementation checkpoint, October21

The shared native-title driver now builds the existing Xbox recomp-ui launcher
and resolves trusted, image-bound v2 mod plans. The launcher uses the same Player1
controller selection and saved feature controls as Blinx. Its compiled catalog
roundtrip agrees with CLI resolution for1080p/FXAA/8x filtering. Generic controls
include1080/1440/1800/2160, supersampling, AA and filtering; each defaults off.
Title registry source and declared fact inputs are included in build identity.

Original New Game reaches controllable Garage and movement with actual1440x1080
rendering in run20261021-133731-fxe7ruwb. Initial observer mistakes were attaching
before image mapping and choosing New Game while attempting Load; neither was a
native crash. The same live run completed introduction dialogue and movement.
Its300sec bounded process ended at the explicit deadline. Original owner saves
were never used as writable state.

The camera mod keeps the original vertical field of view, widens GPU X,
updates the original CPU projection copy and horizontal clipping planes, and
preserves shape/placement of screen-space HUD. Exact-image facts and source-block
hashes are in config/revisions/ntsc-u/visuals.json. No original code is patched.
Authored contract checks cover disabled behavior, repeated-frame stability,
adaptive4:3/21:9/32:9, pause/history scope and loading restoration. They do not
establish actual entity visibility or complete HUD coverage.

A bounded opt-in native TCP resize command lets one running title exercise
multiple live window aspects. Window operations remain on the graphics owner;
background tests stay hidden/muted. Runs20261021-141432-1ah6l0c_,141748-mx6w27lk
and141901-433japq_ pass original NewGame, movement, four live aspects, pause/resume
and sampled margin/HUD review. The first uses1080p/FXAA/8x/120Hz interpolation;
the other two exercise2160p/16x and3x3 supersampling. Evidence is private below
`host-001/runs/`; screenshots and read-only projection/CPU clipping observations
are retained per run. Processes are intentionally stopped after the checks.
No isolated performance or entire-game visual acceptance is claimed.
Actual faster simulation is unavailable: a
higher presentation rate alone does not qualify game timers or physics.

A retained comparison of those three native runs also checks coarse gameplay
pacing: the same800ms LY20000 lease from identical Garage coordinates produces
28.03 units of settled travel with120Hz interpolation, versus28.67 and28.54
with original presentation. That is about98% of the original-run displacement,
consistent with input/frame scheduling variation and no2x/4x simulation speedup.
It is a smoke comparison across different raster settings/host runs, not a
deterministic physics or bit-identical timing qualification. The observations,
input durations and source-evidence hashes are in the private
`visual-mods/timing-comparison.aot-private.json`.

Frameworkb5e3b8e is clean and pinned with the title gitlink/framework.json. Its
launcher catalog roundtrip, driver/visual resolver, native recovery and TCP
contracts pass. Title fixed/adaptive/disabled contracts pass. Later title mod
edits rebuild only the registry and link (about8sec), reusing generated CPU.
Compatibility evidence is `visual-mods/dashboard-latest-143748` (three menus,
749 presented frames) and `visual-mods/blinx-latest-143812` (3481 presented frames,
boot/cinematics); this is a smoke check, not repeated campaign qualification.
Dashboard attempts using a different private baseline or stale content did not
pass and are retained separately. The verified QA content/private owner-state
copy passes; no native behavior was changed to hide those attempts.

Nonessential follow-ups remain explicit: deeper stage-specific HUD/effects and
isolated performance sampling; an actual higher-simulation-rate adapter; the
Dashboard private-baseline launch difference; and an existing Blinx generated
CPU C4293 shift-count warning (`beads-xbox.1.7.14`). None is a claim of a passed
unreached operation. Current-build snapshots may break across builds; native
in-game saves remain a separate protected contract.

Visual follow-ups are tracked in `beads-xbox.2.11`. The owner launcher is built
under `host-001/launcher/Release/` and was visually inspected as a normal window
with Player1 selection, Mods/Settings and a verified owned XBE. Private owner
paths/preferences and a separate copy of the original post-Chuo-race in-game save
are under `owner-visual-preview-20261021/`. The protected41088-byte save retains
SHA256`5e07983ef9f5d57a1f58a8a9465b0d5b508d5bc3959b2fbd917bcce2b298c6f3`.
The owner then selected adaptive1080p/2x supersampling/FXAA/8x/60Hz interpolation
and launched native executable`85b4de49...` (run20261021-144406-z0qhclk7).
That owner-facing process has no QA deadline and is left alone. Playback feel
and performance remain the owner's review; this is not a claim of that review.

### Owner HUD review and repair, October21

The owner reports gameplay feels solid, but the initial enhanced build splits
score and dialogue glyphs across different anchors and misplaces the talk prompt.
The earlier health/spray-only Garage sample did not cover those components.
The fix groups original camera score digits with the shared text actor's trick
name/multiplier rows, while NPC and radio dialogue retain one centered canvas.
The original pixel focal is preserved: source-bound154100 projects into authored
640x480 coordinates, which are mapped once by the raster callback. The stock
pass at79C41 uses depth bias-24.9 and anchors right; other miniature producers,
including the talk prompt, retain their original placement. Original code,
generated CPU and shared frameworkb5e3b8e are unchanged.

Three authored disabled/fixed/adaptive contracts pass, including dialogue glyphs
crossing the former per-draw edge thresholds, score group ownership, unchanged
pixel focal, and separation of miniature stock/prompt passes. Runtime calibration
in run20261021-151448-bcge1jyr separates the original0/24/24.9/25 bias producers;
the calibration switch is removed from the delivered source. Final native run
20261021-151709-lf8_39pj uses executable055c3af6... and retains rail-score, talk
prompt, stock, tutorial text and bottom portrait-dialogue captures at21:9/32:9.
Score and portrait text/frame alignment are visually inspected. Its first marker
and Corn captures occur in original state31 introduction, so those particular
frames establish centered4:3 UI rather than adaptive gameplay. The later original
state15 Gum/radio frames establish the wide talk-prompt/stock/portrait placement.
The process exits15 only after the explicit private QA stop, with no runtime guard.
Teleports bypass approach; no fair tutorial/combat claim is added. This repairs
the reported samples, not every possible stage-specific HUD combination.

### Historical progress notes

The dated/run-numbered notes below preserve earlier frontiers. The current
scope and delivery table above supersede their then-open status.

The current input investigation establishes that TCP input reaches original
`XInputGetState` successfully, the original input wrapper converts Start to
its internal `0x80` button, and the game publishes a real Start press edge
in its port and active-input state. This does not establish menu acceptance.
Packed state/capability layouts and Controller S identity remain unchanged.
Bounded, opt-in observations are a diagnostic source change; there is no
input correctness fix yet. Its incremental rebuild reused every generated
CPU object and took 12.9 seconds. Render-triggered runs avoid sending input
before variable-duration startup finishes; screenshots can time out during
asset loading without that proving a crash.

The title-state observer now confirms real Start moves the original object
from state 1 to 3; the original dispatch table selects `0x7DAB0` for state 3.
A fresh second Start edge moves it to state 4 and renders the original
New Game / Load Game / JS Mode menu (`title-state-003`). Earlier automation
sent A after the initial animation skip, while state 3 specifically tests
Start. This was an automation sequence error, not a demonstrated input ABI
bug. The native state sequence 1 -> 3 -> 4 required no correctness patch.

xemu 0.8.136 is installed and now has a private portable diagnostic setup
under the evidence root. QMP/GDB respond; the disc is mounted read-only,
EEPROM uses a private G: copy and HDD writes use a G: qcow2 overlay with the
existing raw disk as its backing file. This setup has not yet reached JSRF,
so no xemu gameplay or transition comparison is claimed. Its diagnostic process was stopped after setup checks
while native gameplay diagnosis proceeds.

The next run `new-game-001` used real Start/release/Start/A and exited at
`spatial audio output owner unqualified` (`d00b0fa4`). This is the required
active-output frontier already tracked by `beads-xbox.1.152`, not an input
failure. The read-only observer then lost its process handle because the
runtime had stopped; its Python assertion is not a separate game crash.
Controllable gameplay and New Game completion remain unverified.

Spatial playback implementation now has a bounded native CPU service with
stack arguments and a source-bound arithmetic profile: 17 roots, 26 helpers
and seven original default-data blocks. Sixteen position/HRTF/distance/cone/
Doppler vectors match all 76 result bytes between generated native C and
original x86 execution in Unicorn 2.1.4. The HRTF lookup needs its original
SDK function-pointer initializer; that dependency is now explicit. This is
arithmetic evidence, not complete playback or gameplay qualification.
The native consumer now publishes original calculated gains, Doppler/pitch,
HRTF data, direct/room filters and effect sends through a per-voice submix.
Mono source cursors, notifications and deferred state retain their owners.

## Practical QA batching and sampling

Carry forward completed shared-behavior evidence; do not replay a passed fight,
painted area or save boundary solely to prepare another check when a consistent
private checkpoint is available. Use short batches with actual game triggers and
terminal observations, retaining explicit position/resource/prerequisite bypasses.
Inspect representative repeated visuals and ordinary interactions; expand a sample
when a reached failure or a distinct implementation justifies it. The current owner gate is stage/boss setup coverage, with forced progression
explicitly recorded; deeper mechanic and recovery qualification is deferred.

Sampling a common behavior does not pass an unexercised mission or its completion.
The owner now requests rapid stage/boss coverage; detailed mission/mechanic
entries stay unverified or deferred rather than blocking this sweep. Optional repetitions, precision/stress matrices and
subjective presentation checks may be sampled or deferred only with that scope
visible. Owner visual/audio review can settle subjective appearance and feel;
original counters, transitions and save/load establish progression and persistence.

## Supporting validation deferred until after game coverage

Owner-directed deferrals, tracked with `beads-xbox.1.152` and
`beads-xbox.2.6`. These do not authorize fabricated output or bypassing a
required service. If a deferred case is actually exercised and fails during
coverage, promote that failure immediately.

| ID | Deferred work | Revisit trigger |
| --- | --- | --- |
| SV01 | Exhaustive spatial arithmetic vectors for all distances, cone boundaries, orientations and exceptional floats | A reached mismatch, or post-coverage qualification; the existing 16 exact vectors remain evidence |
| SV02 | Exact hardware HRTF coefficient scaling, quantization, delay and smoothing precision | Final hardware phase or a concrete audible discrepancy; implement functional native positional output now |
| SV03 | Exhaustive combinations of immediate/deferred listener/source updates and all mode transitions | A combination reached by JSRF fails, or post-coverage qualification; working live updates remain required |
| SV04 | Additional host/compiler/platform coverage beyond the completed MSVC/MinGW CPU-service checks | Portability work after campaign coverage; preserve portable interfaces and explicit unsupported paths now |
| SV05 | Long audio stress runs, broad lifecycle permutations and performance benchmarking | A reached leak/stutter/corruption, or post-coverage qualification; use short targeted checks for fixes |
| SV06 | Repairing the complete xemu firmware/game boot setup and conducting broad oracle comparisons | A specific native mismatch needs that reference, or final qualification; do not block native gameplay on emulator setup |
| SV07 | Hardware/oracle precision and projection/depth-policy comparison for native pretransformed fog | A reached visual mismatch or post-coverage qualification; real native fog output and reached crashes remain required now |
| SV08 | Exact NV2A point-size quantization, subpixel edge rules and attenuation reciprocal precision | A reached visual mismatch or post-coverage qualification; real scaled/textured point output is implemented and tested |
| SV09 | Exhaustive campaign mission variants, fair combat/traversal, unique-mechanic completion and recovery permutations | Owner explicitly requests later gameplay qualification, or a reached failure blocks stage/boss coverage; the current pass permits instant kills and forced end sequences |

Runtime save states and rewind remain a separate workflow improvement under
`beads-xbox.1.131`. Existing generic native-continuation diagnostics are not a
title snapshot. The PSX recomp-net/rbengine model is the intended reusable
foundation, but full native waits/stacks and graphics/audio/storage state need
additional work. On October 20 the owner explicitly prioritized finishing JSRF
over this larger detour. Continue batching original scene handovers now.

For short boost/spray retries, `python tools/qa.py --run <private-run> cans 12`
uses the original character's current capacity. The field facts are bound to
the exact image and original consumption/pickup-clamp code identities. This
changes only a private run's resource count and records a prerequisite bypass;
it does not write mission flags or qualify collection. Actual collection in
run024 remains independently established by original pickups and lesson output.

`python tools/qa.py --run <private-run> health <count>` provides a bounded
private health refill for encounter coverage. Original pickup/clamp code at
8e670 binds current health at player+f98 and its maximum at player+f9c;
the reverse interpretation would overwrite the maximum. Only positive values
within the existing character capacity are accepted, under the same original
camera-owner and frozen-write checks as can refills. Run034 rejects a request
above110 without changing either field, then refills actual health65 ->110
with maximum 110 retained. This is an explicit resource bypass, not evidence
of a health pickup, damage behavior or invincibility.

The rebuilt `new-game-002` route reaches the same required spatial Play in
57.1 seconds. It uses CTRL3D mode 0, with two current mix routes and genuinely
deferred position values. This is a real positional playback consumer, not
a mode-2 disabled-spatial voice that could use ordinary mono output.
This established the need for real positional output rather than a mono bypass.

`new-game-003` uses the completed native positional consumer and reaches
Corn's rendered introduction in the GG's Garage. No unsupported boundary or
audio backend failure occurred before the planned bounded stop at 104.9 s.
This passes menu-to-New-Game entry, not controllable gameplay or campaign
coverage. The next run advances original dialogue and exercises movement.
The revised profile also binds original 3D mix defaults (five sends) and the
native frequency-to-pitch helper; 3D headroom follows the original zero default.

The SV01-SV06 decision and this functional milestone are recorded locally in
Beads. The remote sync attempt hit Beads' five-minute integrity-check deadline;
its push is pending and the central database was preserved.

`gameplay-entry-001` advances the original conversation, enters the playable
Garage and responds to movement. `adaptive-04` shows the initial floor position;
`adaptive-32` and `route-94` show movement onto a ramp with camera follow.
Original controller inputs also exercise jump requests, but these stills do not
prove a complete jump/landing or a mission interaction. The run ended at its
planned bound (228.1 s), with no unsupported stop or backend failure. The next
coverage work is an explicit interaction and revision-checked QA controls.

The existing MIT JSRF Unleashed implementation is a useful behavioral reference,
not an address map for this older image. Its mission-queue entry `0x30490` and
flow dispatcher `0x51fc0` have matching roles here, but the flow step-table
address differs and its cited player/camera functions do not all match. Bind
cheat/observation facts to this exact image before using them; do not install
the other revision's offsets blindly. No added xemu/hardware work is required.

## Current gameplay coverage checkpoint

Run028 also performs an original three-part spray at Rokkaku-dai Heights.
Actual RT input spends three cans (30 ->27), paints descriptor592 and activates
the Graffiti Stop save point. Resource refill and the area prerequisite are
explicit bypasses; no paint or completion flags are written. This establishes
one save-point graffiti interaction, not the regular wall-tag mission.
The original save menu then creates Game File1, Chapter1, play time00:20 and
reports Done saving. The new private JSRFDATA.SAV is41088bytes, accompanied by
SaveMeta.xbx. Run028 is intentionally stopped after that completed save so an
independent process can test original loading. This first forced cross-chapter
save is subsequently rejected as usable QA setup: the handover did not update
the persistent story chapter. Run031 accepts the file and character selection,
then requests nonexistent mssn0140 instead of the forced area's mssn0240.
The real missing-file statuses are preserved. No runtime failure is inferred
from this inconsistent prerequisite bypass, and no filename alias or fake
success is added to the base runtime.

Run032 starts fresh, uses an explicitly bypassed same-chapter handover10014,
and paints its original Graffiti Stop target576 with real RT input, cans30 ->27.
Original saving writes JSRFDATA.SAV41088bytes. Independent process run033 loads
that file through the actual Load Game confirmation and character selection,
then reaches mission10014/state15 with the original player/camera. Target576
is still painted (unpainted0, designsfffffe00), its save-point effect is active,
and ordinary stick input moves the player. No paint, completion or signature
validation override is used. The private save identity and before/after memory
observations are retained in fresh-load-proof.aot-private.json. This passes
the reached save/create/reload interaction; wider progression and recovery
boundaries remain open. A game save is not a runtime snapshot.

QA handovers leave persistent story progression unchanged. Use a consistent
chapter/area setup for save, mission-chain and extra-mode checks, and continue
recording bypassed prerequisites. A rendered forced scene alone does not prove
its persistent story state is suitable for those checks.

| Route | Result | Scope and bypasses |
| --- | --- | --- |
| Initial Garage (`0x10001`) | Movement, follow camera, jump/landing and Corn conversation passed | `mission-qa-001`: ordinary jump and interaction inputs; teleport bypasses travel to Corn, not the conversation trigger. Tutorial completion remains unverified |
| Shibuya Terminal (`0x10014`) | All 35 regular graffiti and save point painted, map100%, original save/load and a story encounter observed | Run034/035 uses actual RT, including one/three/six-part targets; no paint/completion writes. Original30-target checkpoint reloads in fresh035, then remaining six pass and full progress saves. Travel/resources/story prerequisites bypassed. Original NPC/exit progression and mission clear remain unverified |
| Post-tutorial scene (`0x100c4`) | Cutscene entry, animation and subtitles observed | Original handover loads the scene; tutorial prerequisite bypassed. Natural scene completion and exit unverified |
| Mission `0x1000a` / `mssn0110`, Stage 12 assets | Loads, movement and original story conversation passed | `mission-qa-004` advances past both graphics failures, renders the reached FVF102, movement triggers the original story dialogue in state31, real A advances it back to15 and movement resumes. Tutorial prerequisite bypassed; full area mechanics remain unverified |
| Mission `0x10014` / `mssn0120`, scene key `0x10000` | Loads; movement and camera input exercised | Same live location batch, inspected position changes; prerequisites bypassed. Area-wide mechanics/completion unverified |
| Mission `0x2001e` / `mssn0230`, scene key `0x10001` | Event entry observed | Original flow reaches state19. Event completion bypassed for the next handover; ordinary movement not established during the event |
| Mission `0x20028` / `mssn0240`, Rokkaku-dai Heights, scene key `0x20000` | Original introduction renders past the fog failure | `mission-qa-007` renders original animated introduction/subtitles with typed and immediate XYZRHW fog. Event completion is bypassed for the next handover; ordinary gameplay and area-wide mechanics unverified |
| Mission `0x20032` / `mssn0250`, 99th Street, scene key `0x30000` | Original introduction renders | Same live batch renders original area introduction/subtitles. Event completion bypassed; ordinary movement and area-wide mechanics unverified |
| Mission `0x3003c` / `mssn0360`, scene key `0x20001` | Forward sequence, entry and movement passed | `mission-qa-010` clears the exact `20028 -> 20032 -> 3003c` sequence after admitting screen-space unit points, shared commit `bc3a6a6`; independent full-image point/fog/offset tests pass. Full area mechanics unverified |
| Further mid/late-game locations | Entries observed; some movement passed | Run010 reaches `30046`, `40032`, `4003c`, `40046`, `40050`, `5000a`, `6003c`, `70032`; the original `40032` introduction returns naturally from19 to15. The separate content ledger distinguishes movement from event entry |
| Late-game scene types | Four introductions captured; reached scaled sprites fixed | Run014 repeats `8000b -> 8000c -> 80050 -> 8005a`, renders past the previous scaled-point stop, and the original introduction naturally returns to state15. Independent full-image size/attenuation/UV/fog checks pass. Forced entry leaves the player outside the final arena; boss setup/mechanics/completion remain open |
| Extra-mode setup | City Rush briefing and countdown reached; race setup incomplete | Run012 requests `14000a`, reaches the original City Rush briefing, and real A starts countdown. World/player setup is not established after this direct story handover. Use proper original extra-mode setup before qualifying races |
| Reverse handover `0x3003c -> 0x20028` | Reached crash fixed; repeated loading and movement passed | Shared `eb180a4` corrects native vertex-header allocation ownership. Fresh run022 passes the original failing route, then `20032 -> 3003c -> 20028`, with playable state15 and movement on the final revisit. Mission prerequisites are bypassed; this does not qualify the complete missions |

The enabled normal-normalization fix uses the existing real lighting consumer,
with three targeted initializer/lighting tests passing. The actual retry now
gets past its previous rejection; it does not establish all lighting or area
coverage. Missing-array normals now use the existing retained GPU input owner,
with analytic pixels for updates, packet setters, explicit-array precedence
and normalization. Both reached lighting fixes are committed as `3e1835b`.
Shared spatial playback implementation is committed as `c383fd3`; reusable
private QA transport as `e40eec8`. Native pretransformed fog is committed as
`2d02e7c`, with ten independent GPU cases across three device lifetimes plus
fixed-declaration/lighting regressions (3.07 s), followed by the original route
advancing through two introductions. Range fog remains guarded; precision and
projection/depth-policy comparisons remain SV07 supporting validation.
Screen-space unit points are committed as `bc3a6a6`, with complete-image tests
covering source offsets/counts, screen placement and fog; original forward
handover now passes its earlier failure. Native scaled sprites now pass the
same late-game route and targeted GPU checks; exact precision remains SV08.
The scaled-point implementation is committed as `4a56ca4`; targeted points,
fixed-declaration and fog checks pass in 1.46s. Run014 additionally captures
eight previously unobserved story-event scene groups in one running process.
The fresh reverse-handover failure is now resolved under `beads-xbox.1.181`.
Allocation tracing and a private debugger watch establish a graphics-header
allocation mismatch: the bridge placed an opaque driver header in a recycled
raw user-VM reservation, whereas the original SDK allocates a small heap
object. Shared `eb180a4` uses the maintained header pool, preserving physical
data and reference/binding/waiter ownership. A targeted actual VM reuse,
CPU/GPU byte, binding-retention and final-cleanup regression passes across
three device lifetimes. Fresh run022 passes the previously failing route and
repeats the forward/reverse sequence with movement. Broad ABI/capacity/scheduler
fixtures explicitly skip unavailable boundaries in this older SDK profile;
those skips are not counted as passes.
Campaign-wide behavioral mapping, mechanics, mission completion and save/reload remain
open. No overall campaign percentage is established. SV01-SV08 remain deferred.

Generate the private content inventory without copying game content into Git:

```powershell
python tools/qa_inventory.py --media-root <owned-media-root> --output G:/Temp/Codex/JSRFRecomp/content-inventory.aot-private.json
```

This emits filenames, hashes, scene keys and command counts/opcode counts for
all four command arrays. Inventory v2 also separates individual enemy definitions
from the original group sets that spawn/despawn/listen commands reference.
Placement-record counts are not claimed as live actor or encounter counts.
It neither runs commands nor establishes their behavior. For example,
`mssn0196` is reached with runtime ID `0x100c4` (low word196), so the naive
filename candidate with low word96 must not be treated as a proven ID.

The original Shibuya story route now advances beyond graffiti: run036 passes four
Poison Jam recordings/returns and Combo's real two-grind/air-trick challenge,
then enters the cop fight and disables one cop through normal dash/spray input.
No action/counter/completion fields are written. Run037 repeats the four routes
and saves an original C31/C50 story checkpoint (chapter1, return mission120,
events10/21/23). Its lane checks pass and the save reports Done saving; independent
reload of this newer story checkpoint remains open. The checkpoint excludes only
the rebuildable locked native cache. The per-consumer evidence and explicit repeat
prerequisite bypass are recorded in CONTENT-COVERAGE.md and private traces.

Run037 now completes the reached20-cop fight through actual knockdown/tagging.
The original defeat listener, event and exit advance to native20060/Chapter2.
The repeated Combo prerequisite is explicitly bypassed after its actual run036
pass; no enemy/completion/chapter fields are written. Chapter2 entry is direct
progression evidence, not a claim that all Chapter1 side content is covered.

Original Chapter2 progression save/load now passes: after its introduction and
character selection, run037 enters Garage200c8, talks to Roboy and uses the original
save menus. The chapter2/return mission0 file is saved with original validation
active. Fresh038 loads it into native20000/state15 and ordinary movement responds.
The earlier Shibuya checkpoint and the new Garage checkpoint are preserved privately.

Run038 completes the first Chuo tank phase through real RT spraying: all six
original Tank groups reach remaining0 and the mission despawns them, then spawns
Hayashi for its second phase. Group-set parsing distinguishes initial block5
set0 (six tanks/barricades) from set1 (Hayashi/barricades); the initial absence of
Hayashi is expected. Teleports/refills/protection bypass approach and survival,
with no enemy, target or completion writes. The second-phase LT/B and RT batch also defeats
Hayashi and the original mission returns to playable Chuo. A subsequent graffiti
approach unexpectedly reenters0231, so stable post-fight story progression and
the ten-part targets remain open; no broad Chuo completion claim is made. Details and source ownership are in the content
ledger; no native runtime change or rebuild is required for these QA controls.

Fresh039 repeats the fight and original return with a read-only data watch.
Original C11 clears and C13/C19 set; the same XL approach stays in0230/state15.
The earlier reentry is not reproduced and no native behavior change is justified.
Ten-part painting, post-fight save and Chuo's next real story interaction remain
next. The diagnostic run is deliberately stopped for debugger-input cleanup;
its terminal status is not a game crash. Immutable Garage restart state remains
available. Enemy/group-set inventory v2 passes all311 owned mission pairs.

Run040 adds a post-tank original save through Roboy. Chapter2/return0 and
C10/C13/C19/C270 decode with valid lane checks; the immutable checkpoint retains
the identical41088-byte file. Original return travel is bypassed, not passed.
Two ten-part murals have six accepted pieces each; full painting remains open.
Private instant teleports now synchronize the original current/previous position
samples, retaining an explicit sweep option. Actual frozen-byte/resource checks
pass. Earlier region-coordinate handovers do not independently qualify portal
identity; see the content ledger's clarification. Original player actions still
need a valid approach/grounding setup before spray acceptance.

Fresh independent041 loads the post-tank checkpoint through the original menus,
reaches native20000/state15, moves and retains C10/C13/C19 with C11 clear. This
checkpoint is the new restart source for Chuo; the fight does not need repeating
for each remaining mural/story approach. Full Chuo progression/ten-part painting,
other missions/bosses/extra modes/recovery and subsequent visual mods stay open.

Run041 completes Chuo's actual graffiti consumer: all25 registered targets and
front/back layers pass, original map24 (100%), with natural C13 ->C14/C200 story
progress. Original per-piece volumes replace unreliable whole-mural/reference
positions; public read-only `qa.py tags` exposes source-bound metadata for further
area batches. Actual RT, not paint/completion writes, establishes the pass.
The same-area save point and original Save menu create a chapter2/return230
checkpoint (SHA8c5fbc08...,41088bytes, lane checks valid). Fresh independent042
accepts original Load Game/character selection, returns playable200e6/state15,
moves and restores all25 painted targets. The following Chuo story/challenge is
next; wider campaign/extra-mode and final visual-mod/handoff requirements remain
unchanged.


Run042 accepts the original Poison Jam race after full Chuo graffiti. The first
attempt reaches actual You Lose; original Retry/briefing/A returns to a running
race. An adjusted217-plane travel batch makes the native race manager complete
lap1 and enter victory29; the original return to playable Chuo advances to
C16/C23. Positions/sweeps bypass skating, without lap/completion/chapter writes.
A new original Chuo save is retained (SHA5e07983e...,41088bytes, valid lane checks,
chapter2/return230/C10/C16/C23/C200/C270); this exact file has not been freshly
reloaded. Chuo's reached graffiti/race progression is passed. Rokkaku-dai story
coverage is next, with inter-area travel explicitly bypassed; full campaign and
later enhancements remain open. Race failure/retry does not establish death.


Run042 also completes four original Rokkaku-dai Poison Jam recordings/returns,
advancing C23->C27, then clears the first reached three-cop police zone through
actual lock/dash/spray and original return. A second zone's five ordinary cops
are disabled, but its type4 group remains. An instant escape teleport then
reaches a native unmapped-read stop in sub_00011D00 (exit2). This is an open
reached failure, not a passed encounter; focused reproduction is next. The
Chuo post-race save protects earlier progress. Rokkaku-dai full graffiti and
later campaign/visual requirements remain open.


The owner-clarified rapid sweep reaches13 additional encounter files in runs043/044,
including the final boss. The corrected original arena start prevents the carried-
over fall. The public `force-encounter-end` cheat bypasses native defeated tests;
original final-boss flow advances into its rendered post-fight sequence. This is
coverage with explicit cheats, not fair combat or whole-campaign qualification.
The two unusual travel/setup failures and five extra-mode setup scenes remain
recorded as deferred follow-ups; per-model visibility gaps are explicit in the
coverage table. Proceed to reusable visual mods rather than expanding mechanics
validation again. Shared frameworkbc4d290 and native CPU execution are unchanged.
