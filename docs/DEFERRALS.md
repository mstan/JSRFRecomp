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
| Unknown original listener defaults and 3D voice transforms | Known masks distinguish explicitly supplied listener values. Only qualified 2D buffers are admitted; no spatial voice capability is invented. | A reached 3D consumer needs defaults, distance/doppler/HRTF or transformed output. |

Required boundaries remain explicit: spatial audio consumers, immediate gamma,
active fixed-function lighting and
extended COPY Reset have not been qualified. Owning-thread file APCs and deferred
nonidentity gamma and I3DL2 conversion/application are implemented; these are no
longer open boundaries. Replacing an installed effects image after listener
reverb settings have been applied still guards until replacement ownership is
qualified.
If the attract sequence reaches any of them, they are required work, not a
precision waiver. Full campaign play and later gameplay enhancements are outside
the current attract goal.
