# Scoped deferrals and unreached boundaries

Tracking: beads-xbox.2.1. An item below never waives a failure required to finish
the actual native attract cycle.

| Item | Current treatment | Reopen when |
|---|---|---|
| Exact RGB565 framebuffer quantization and console dither | Native RGBA8 render precision; original RGB565 surface descriptors and two-byte pitch retained. Exact console pixel identity is unqualified. | Pixel comparison or a readback-dependent effect needs this precision. |
| 10:11 pixel-aspect presentation calibration | Original presentation flag retained and queryable. Desktop framing/calibration remains to be compared with the actual scene. | First complete frames expose an aspect discrepancy, or final presentation QA. |
| Exact MCPX allocation counters | Native GetCaps reports actual maintained buffer/page ownership; unavailable spatial voices report zero. Hardware counter identity is unqualified. | A concrete decision depends on exact hardware counters. |
| Physical tile/Z-tag byte encodings | Native images hold logical depth/color; source-proved tile descriptors remain queryable. Exact physical compressed bytes are unqualified. | A raw-memory-dependent effect requires their encoding. |
| Physical encoder/scanout timing | Software capability query is source referenced; physical hardware remains deferred. | Final hardware phase, if required by a concrete discrepancy. |
| Exact original DVD padding/physical extent | Mounted-directory volume size comes from actual file/directory metadata in read-only 2048-byte units. It does not invent unprovided disc padding. | An image provider or behavior requires original physical geometry. |
| Exact initial USB enumeration latency | Shared native initialization models the established 500ms asynchronous HLE phase; real discovery and insertion follow completion. Timing is not claimed hardware-exact. | A concrete title timing discrepancy requires an original timing comparison. |
| Unknown original listener and spatial defaults | Known masks distinguish explicitly supplied values. Inactive spatial storage/setters retain state; active spatial playback still guards. No spatial output capability is invented. | The reached 3D output consumer needs original defaults, distance/doppler/HRTF and effect routing. |
| Unmasked x87 exception delivery and full sticky exception modeling | Existing native arithmetic models values/comparison state. Reached FNCLEX clears represented status without changing conditions, TOP, stack or control word. Hardware trap delivery is not claimed. | A concrete reached exception/status consumer requires that additional behavior. |
| Exact SSE sticky-status provenance and portable denormal controls | The reached STMXCSR nearest-rounding consumer passes with the shared native query (framework `4e89b7e`). Native x64 reads the actual CSR; the portable C profile represents standard flags and masked reset controls. Guest writes, trap delivery and portable DAZ/FTZ remain guarded/unqualified. | A reached consumer depends on these additional bits or changes control state. |
| Exact NV2A texture-combiner intermediate rounding | Native COLOROP8..14 component equations pass independent GPU expectations with one final UNORM byte of rounding tolerance. Original state identity and the retained LLE owner remain intact. Exact fixed-point intermediate pixels are unqualified. | A visible discrepancy or readback-dependent effect requires the intermediate precision. |

Required boundaries remain explicit: spatial audio consumers, immediate gamma,
active fixed-function lighting, the reached beta-FVF drawing consumer and
extended COPY Reset have not been qualified. Owning-thread file APCs and deferred
nonidentity gamma and I3DL2 conversion/application are implemented; these are no
longer open boundaries. Replacing an installed effects image after listener
reverb settings have been applied still guards until replacement ownership is
qualified.
If the attract sequence reaches any of them, they are required work, not a
precision waiver. Full campaign play and later gameplay enhancements are outside
the current attract goal.
