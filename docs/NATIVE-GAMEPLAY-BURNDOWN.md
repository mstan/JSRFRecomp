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
| GP03 | Reach controllable gameplay | Passed for initial Garage movement, camera, jump/landing and NPC talk | `gameplay-entry-001` movement/follow camera; `mission-qa-001` real A input raises player Y from 0 to 16.5 and returns to 0; teleport near Corn then real RT triggers original conversation. Travel is bypassed; conversation trigger is not |
| GP04 | Implement newly reached shared contracts | In progress | Active positional playback now runs through shared native HRTF/filter/send output, tracked by `beads-xbox.1.152`; fix the next concrete boundary found during gameplay |
| GP05 | Derive the area/mission/mechanic inventory | Content inventory derived; behavioral mapping open | `tools/qa_inventory.py` parses all 311 owned mission/script pairs and their setup/trigger operation inventories, grouped under 33 scene keys. Scene keys are not automatically area names. Filename numbers alias modulo 100, so canonical runtime IDs still require original-flow evidence |
| GP06 | Add reusable cheat-assisted QA controls through title mods | Teleport and original mission handover working; further controls open | Shared development RAM transport plus revision-bound `tools/qa.py` and `gameplay-qa.json`; public controls exercised in `mission-qa-002/003`, unfrozen writes rejected; no game addresses in shared transport. Protection/resource controls and event cancellation remain unverified |
| GP07 | Exercise every inventoried location and meaningful mechanic | Unverified | Per-location passed/failed/unverified/bypassed ledger, original transitions, interactions, mission triggers, unique actions and relevant audio |
| GP08 | Validate save/reload and representative progression boundaries | Unverified | Original save writes and authenticated fresh-process reload, with protected owner originals |

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

| Route | Result | Scope and bypasses |
| --- | --- | --- |
| Initial Garage (`0x10001`) | Movement, follow camera, jump/landing and Corn conversation passed | `mission-qa-001`: ordinary jump and interaction inputs; teleport bypasses travel to Corn, not the conversation trigger. Tutorial completion remains unverified |
| Post-tutorial scene (`0x100c4`) | Cutscene entry, animation and subtitles observed | Original handover loads the scene; tutorial prerequisite bypassed. Natural scene completion and exit unverified |
| Mission `0x1000a` / `mssn0110`, Stage 12 assets | Loads, movement and original story conversation passed | `mission-qa-004` advances past both graphics failures, renders the reached FVF102, movement triggers the original story dialogue in state31, real A advances it back to15 and movement resumes. Tutorial prerequisite bypassed; full area mechanics remain unverified |
| Mission `0x10014` / `mssn0120`, scene key `0x10000` | Loads; movement and camera input exercised | Same live location batch, inspected position changes; prerequisites bypassed. Area-wide mechanics/completion unverified |
| Mission `0x2001e` / `mssn0230`, scene key `0x10001` | Event entry observed | Original flow reaches state19. Event completion bypassed for the next handover; ordinary movement not established during the event |
| Mission `0x20028` / `mssn0240`, Rokkaku-dai Heights, scene key `0x20000` | Original introduction renders past the fog failure | `mission-qa-007` renders original animated introduction/subtitles with typed and immediate XYZRHW fog. Event completion is bypassed for the next handover; ordinary gameplay and area-wide mechanics unverified |
| Mission `0x20032` / `mssn0250`, 99th Street, scene key `0x30000` | Original introduction renders | Same live batch renders original area introduction/subtitles. Event completion bypassed; ordinary movement and area-wide mechanics unverified |
| Mission `0x3003c` / `mssn0360`, scene key `0x20001` | Forward sequence, entry and movement passed | `mission-qa-010` clears the exact `20028 -> 20032 -> 3003c` sequence after admitting screen-space unit points, shared commit `bc3a6a6`; independent full-image point/fog/offset tests pass. Full area mechanics unverified |
| Further mid/late-game locations | Entries observed; some movement passed | Run010 reaches `30046`, `40032`, `4003c`, `40046`, `40050`, `5000a`, `6003c`, `70032`; the original `40032` introduction returns naturally from19 to15. The separate content ledger distinguishes movement from event entry |
| Late-game scene types | Three introductions captured; scaled sprites blocked | Run011 captures `8000b`, `8000c`, `80050`. The `8005a` request reaches scaled XYZ point sprites (size0.3, sprite/scale enabled), requiring real output under `beads-xbox.1.182`; this is distinct from the completed unit-point fix |
| Reverse handover `0x3003c -> 0x20028` | Failed; investigation required | `mission-qa-008` reads unmapped guest address `0x05ec0000` during the handover. Repeated-transition correctness remains required; no assumption that this is automation-only and no pass claimed |

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
handover now passes its earlier failure. Scaled point sprites remain required.
Campaign-wide inventory, mechanics, mission completion and save/reload remain
open. No overall campaign percentage is established. SV01-SV07 remain deferred.

Generate the private content inventory without copying game content into Git:

```powershell
python tools/qa_inventory.py --media-root <owned-media-root> --output G:/Temp/Codex/JSRFRecomp/content-inventory.aot-private.json
```

This emits filenames, hashes, scene keys and command counts/opcode counts.
It neither runs commands nor establishes their behavior. For example,
`mssn0196` is reached with runtime ID `0x100c4` (low word196), so the naive
filename candidate with low word96 must not be treated as a proven ID.
