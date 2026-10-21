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
| `0x00000000` | 52 | `10001` | Movement, camera, jump/landing, Corn talk | Open |
| `0x00000008` | 1 | `100c4` | Cutscene entry/motion; end unverified | Open |
| `0x00000009` | 1 | Not observed | Unverified | Open |
| `0x00010000` | 16 | `10014` | Entry and movement | Open |
| `0x00010001` | 18 | `2001e` | Introduction entry | Open |
| `0x00010002` | 17 | `1000a` | Movement and original story conversation/return | Open |
| `0x00010003` | 12 | `40032` | Introduction naturally returns to gameplay | Open |
| `0x00010008` | 1 | Not observed | Unverified | Open |
| `0x00010009` | 1 | Not observed | Unverified | Open |
| `0x00020000` | 21 | `20028` | Rokkaku-dai Heights introduction | Open |
| `0x00020001` | 10 | `3003c` | Entry/movement; point failure fixed | Open |
| `0x00020002` | 20 | `4003c` | Introduction entry | Open |
| `0x00020003` | 15 | `30046` | Entry/movement; story text observed | Open |
| `0x00020004` | 8 | `70032` | Introduction entry | Open |
| `0x00020008` | 1 | Not observed | Unverified | Open |
| `0x00020009` | 1 | Not observed | Unverified | Open |
| `0x00030000` | 15 | `20032` | 99th Street introduction | Open |
| `0x00030001` | 8 | `6003c` | Introduction entry | Open |
| `0x00030002` | 21 | `5000a` | Entry and movement | Open |
| `0x00030003` | 17 | `40050` | Introduction entry | Open |
| `0x00030004` | 14 | `40046` | Introduction entry | Open |
| `0x00030008` | 1 | Not observed | Unverified | Open |
| `0x00030009` | 1 | Not observed | Unverified | Open |
| `0x00040000` | 1 | `8037a` | Original flow15 observed; visuals unverified | Open |
| `0x00040001` | 1 | `80050` | Original introduction captured in run011 | Open |
| `0x00040002` | 1 | `8000c` | Original introduction captured in run011 | Open |
| `0x00040003` | 2 | `8000b` | Original introduction captured in run011 | Open |
| `0x00040008` | 2 | Not observed | Unverified | Open |
| `0x00050000` | 6 | Not observed | Unverified | Open |
| `0x00050001` | 6 | Not observed | Unverified | Open |
| `0x00050002` | 6 | Not observed | Unverified | Open |
| `0x00050003` | 7 | Not observed | Unverified | Open |
| `0x00050004` | 7 | Not observed | Unverified | Open |

Initial evidence: `mission-qa-001/004/007/008/010`. Current captures and raw state
stay private under `G:/Temp/Codex/JSRFRecomp/gameplay-20261020` and
`F:/Temp/Codex/JSRFRecomp/gameplay-20261020`. In run010, the 40032 event returned
from19 to15 without a completion write or further A input. The late-game 0811
request loaded its file and the original scripts later loaded0890 and returned
to the title/attract. This does not pass the final boss or establish the exact
0811 scene path in run010. Run011 subsequently captures that introduction and
the next two late-game scene types, then stops at scaled point sprites while
entering0890 (`beads-xbox.1.182`). The run010 observer timed out before its asynchronous progression;
the process remained alive and was observed rather than restarted.

The reverse handover3003c ->20028 failed with an unmapped read and remains required
work under `beads-xbox.1.181`. The screen-space unit-point failure in the forward
sequence is fixed by shared commit `bc3a6a6` (`beads-xbox.1.180`).

## Mechanics that still need coverage

| Behavior | Current scope |
| --- | --- |
| Movement, camera and jump/landing | Initial Garage passed; movement observed in several additional areas |
| NPC interaction | Corn conversation trigger passed after teleport bypassed travel |
| Graffiti/spraying, pickups and resource limits | Unverified |
| Boost, grinding, tricks, jumps and traversal routes | Unverified beyond initial movement/jump |
| Enemies, police encounters and bosses | Unverified |
| Real mission completion and next-mission triggers | Unverified; forced handovers do not count |
| Death/retry, checkpoint handling and game-over | Unverified |
| Save and authenticated fresh-process reload | Unverified |
| All remaining script variants and scene exits | Unverified; inventory presence does not prove execution |

Supporting precision/oracle validation remains in the SV01-SV07 deferral list of
[the gameplay burndown](NATIVE-GAMEPLAY-BURNDOWN.md). Reached crashes and missing
output remain required fixes.
