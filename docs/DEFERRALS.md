# Scoped deferrals and unreached boundaries

Tracking: beads-xbox.2.1. An item below never waives a failure required to finish
the actual native attract cycle.

| Item | Current treatment | Reopen when |
|---|---|---|
| Exact RGB565 framebuffer quantization and console dither | Native RGBA8 render precision; original RGB565 surface descriptors and two-byte pitch retained. Exact console pixel identity is unqualified. | Pixel comparison or a readback-dependent effect needs this precision. |
| 10:11 pixel-aspect presentation calibration | Original presentation flag retained and queryable. Desktop framing/calibration remains to be compared with the actual scene. | First complete frames expose an aspect discrepancy, or final presentation QA. |
| Physical encoder/scanout timing | Software capability query is source referenced; physical hardware remains deferred. | Final hardware phase, if required by a concrete discrepancy. |

Required boundaries remain explicit: audio is not yet bound; nonidentity gamma,
active fixed-function lighting and extended COPY Reset have not been qualified.
If the attract sequence reaches any of them, they are required work, not a
precision waiver. Full campaign play and later gameplay enhancements are outside
the current attract goal.
