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
| GP07 | Exercise every inventoried location and meaningful mechanic | In progress: 28/33 scene groups entered; Shibuya graffiti and reached Combo challenge passed | Run034/035 paints all regular tags and save point with actual RT, original map 35 (100%), with original saves and a fresh-process30-target persistence check. Run036 also completes four original Poison Jam route returns and Combo's actual grind/air-trick challenge; run037 completes the reached 20-cop fight through real lock-dash/spray and original Chapter2 transition; other content remains open. Entry count is not a campaign qualification denominator |
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

## Full end-to-end completion scope

The October21 owner goal (beads-xbox.2.6 and beads-xbox.2.7) includes gameplay coverage first, followed by visual
mods and final delivery. The goal remains open until each row has direct evidence;
scene entry, source registration and a successful build do not close these rows.

| Work | Status | Required evidence |
| --- | --- | --- |
| Areas, missions, bosses and extra modes | Open under beads-xbox.2.6 | Per-content real mechanics, completion and next-area/progression observations; explicit travel/prerequisite bypasses |
| Recovery and audiovisual behavior | Save/load passed in reached scope; wider checks open | Death/retry, representative progression reloads, interaction audio and animation during actual content coverage |
| Adaptive widescreen and HUD | Pending gameplay coverage | Window/aspect changes through 32:9, real margin content, visible entities, correctly shaped indicators and anchored HUD |
| Internal resolution and fidelity | Pending gameplay coverage | 1080p through 4K, AA and supersampling options through reusable mod controls and inspected output |
| Higher FPS and interpolation | Pending gameplay coverage | Separate mutually exclusive modes; measured gameplay timers/movement retain intended pacing |
| Compatibility and final handoff | Open | Blinx/Dashboard regression evidence, committed coherent framework pins, windowed launcher and normal audio for owner review |

Supporting precision/hardware SV01-SV08 and full runtime snapshots stay deferred;
actual reached crashes or broken output remain required fixes.

Current private work/evidence root:
`G:/Temp/Codex/JSRFRecomp/gameplay-20261020`.
The original native generation is copied intact from the prior qualified
input; generated output and state remain isolated from owner previews.

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
