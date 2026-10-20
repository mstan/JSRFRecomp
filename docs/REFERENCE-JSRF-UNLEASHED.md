# JSRF Unleashed reference review

Reviewed [JuMatt/JetSetRadioFuture-Unleashed](https://github.com/JuMatt/JetSetRadioFuture-Unleashed)
at commit `36828c4d2d80bf8cd1b4962579a2cdb10f4f05a9`, 2026-10-20.
Tracking: `beads-xbox.2.1`, shared texture generation `beads-xbox.1.160`,
spatial output `beads-xbox.1.152`. This is source-reference evidence, not
qualification of our executable or a replacement for the LLE contract.

## Licensing and provenance

The root [LICENSE](https://github.com/JuMatt/JetSetRadioFuture-Unleashed/blob/36828c4d2d80bf8cd1b4962579a2cdb10f4f05a9/LICENSE)
is MIT, copyright 2026 sp00nz. Its
[NOTICE](https://github.com/JuMatt/JetSetRadioFuture-Unleashed/blob/36828c4d2d80bf8cd1b4962579a2cdb10f4f05a9/NOTICE)
separately identifies xemu-derived APU sources and NV2A register definitions
as LGPL-2.1-or-later. Review the particular file's header and provenance before
adopting code; the repository's root license is not a blanket license for every
component. Preserve applicable notices and include adopted components in the
release attribution/source obligations review. No implementation body or game
data was copied during this assessment.

## Useful behavior and limits

| Area | Pinned reference | Our action |
| --- | --- | --- |
| Camera-space normal texture generation | `src/d3d/d3d8_shaders.c`: `gen_tex`, camera-normal transform and per-stage constant upload | Confirms that TEXCOORDINDEX `0x10000` uses the camera-space normal and then the texture matrix. Independent GPU expectations exposed an inverse-transpose packing error in our prepared renderer; framework `83a2b35` fixes it and admits the shared state encoding. No title address or special-case success value. |
| Immediate vertices | No XDK `D3DDevice_Begin/End/SetVertexData*` implementation; interpolation Begin/End hooks serve another purpose | Do not treat its host DrawPrimitiveUP support as this API's contract. Original API bodies and retained LLE packets establish latching, flags and ordering. The separately licensed Phobos shadow implementation is a design reference, but its fixed 4096-vertex capacity and silent dropping are unsuitable. No implementation body copied. |
| HRTF | `src/apu/apu_state.h`: filter state/processing; `src/apu/apu_vp.c`: target coefficients and 3D selection | Useful comparison for 31-tap ears, bounded interaural delay and history. This is LGPL code; our active spatial output still requires original parameter ownership, meaningful output and lifecycle tests. Never substitute guessed coefficients or ship original tables. |
| APU completeness | `src/apu/README.md`, `src/apu/apu_shim.h` | GP/EP functionality and the default-disabled HRTF path do not establish our required effects or active spatial output. Keep the existing source-native DSP work. |
| File EOF/sector padding and capacity | `src/kernel/kernel_file.c` | Diagnostic leads for JSRF's cache parser and capacity arithmetic. Establish original file/device semantics before changing shared behavior; do not introduce game-name branches or arbitrary capacity caps. |
| Threads and interrupt callbacks | `src/kernel/kernel_bridge.c` | Audit leads for real idle-priority work, invalid handles and callback coverage. Retain original ABI/status/scheduling boundaries; do not inherit a caller-specific handle workaround or accept an unmodeled callback. |

The texture-generation behavior also matches
[Microsoft's API description](https://learn.microsoft.com/en-us/windows/win32/direct3d9/automatically-generated-texture-coordinates).
That describes API semantics; exact Xbox raster/normalization precision remains
part of the retained graphics qualification and deferral ledger.

The reference can reduce reverse-engineering time and suggest a fast native
consumer. Each adopted change still belongs in the reusable XboxLLR service,
preserves the original state and ownership interface, and needs evidence in
our actual title. Reference screenshots, advertised playability and source
coverage do not establish this project's complete repeating attract.
