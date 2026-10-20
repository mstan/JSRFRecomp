# Reviewed native interfaces

Input SHA256: `f4441696fdd007c31a712815cdde967836fbc3ab97fcb2f58e1db56974644219`.
The source-selected XDK 4134 inventory is a discovery hint; decoded original
bodies and their recorded extents/RET cleanup provide the interface evidence.
Original bodies remain retained by the framework binders.

The eight gamepad APIs use the existing shared input contract. Original
XInputGetState copies a four-byte packet number followed by the gamepad table's
18-byte report; the total state is 22 bytes. The capability routine clears six
DWORDs and a final byte (25 bytes). SetState initializes its header at 0x40/0x41
before dispatching the report, placing the two motors at offset 66. XInputOpen's
actual default gamepad polling record is `01 08 00 00`. Each admitted body's
decoded RET matches its declared stack cleanup. SetLastError retains the original
TLS helper. The original keyboard class is a separate twelve-byte zero object
under the explicit absent-peripheral policy; host keyboard mapping can still
supply the gamepad through the shared controller provider.

XMountUtilityDrive accepts one BOOL, selects a real cache partition, formats
when requested/needed, creates Z:, and calls the original XapiSetLastNTError
on failure. Its native owner uses the existing persistent private cache/namespace
contract. The actual JSRF caller passes clean=0 and receives a real partition-3
namespace. This removes its original raw partition-0 metadata access from the
native service route; it does not pretend that a raw disk was emulated.

Actual optimized execution advances from the old twelve-entry native allocation
prototype to 148 entries, then through the cache call to 1087 entries. The next
explicit boundary is a display query through AvSendTVEncoderOption before the
graphics family is bound. No frame or attract completion is established yet.
Input admission is source/component evidence; actual game input remains to be
observed after graphics startup.


The classic D3D profile covers 131 complete original bodies and validates their
actual return cleanup. GetTexture2's original routine consumes two arguments
and writes an output pointer, despite one-argument discovery metadata.
GetAdapterModeCount consumes one argument, despite two-argument discovery
metadata. Three tail routines additionally validate their destination body.
The 146-state original cache maps into the shared renderer's semantic state
numbers; the 89-entry initializer skips original slots 116 and 135.

Actual native startup now passes the read-only AV capability query and creates
the requested 640x480 RGB565 device with two back buffers in COPY mode. Original
CPU-only mode filters and light/material cache routines use their original game
stack, while shared native services own graphics submission. The current guard
is GetGammaRamp after 1198 native entries. This is not first-frame, movie, audio
or attract acceptance. No original media file has been modified.

The source-proved two-bank identity gamma cache now passes its original native
getter. Actual startup then initializes the shared native controller provider
and reaches DirectSound startup at 1525 native entries. The unbound original
audio path stops at KfRaiseIrql; the native audio family is the next required
admission. No full rendered frame or attract sequence is established.

The SDK4134 native audio profile binds 50 public/object entries. Actual startup
creates a 48 kHz native device, uses owned AddRef/GetCaps, automatic XInputPoll
and GetState, creates its initial LIN565 texture, registers and describes real
CPU headers and records its depth tile. It then loads real game data. The next
required shared service is asynchronous file completion APC delivery (2483
native entries). No first complete frame or attract cycle is accepted yet.

Later source checkpoints implement the owning-thread file completion, original
kernel232 status/argument rules, real full-size 20-effect GP graph within the
unchanged 4096-word hardware banks, source-bound deferred gamma presentation and
metadata-derived mounted content capacity. Their meaningful component suites
pass, and actual game startup passes these calls.

The original renderer helper stayed null because the first input enumeration
returned E_FAIL on a prematurely published controller insertion. Native debugger
observations locate the failure before the skipped helper creation. Modeling the
asynchronous initial enumeration fixes the cause. The original game then loads
TNRoman.bin, creates native shaders and uses PBYTE4 declarations (normalized
stored byte order, distinct from D3DCOLOR's BGRA).

The optional listener proof admits all eight public transforms/deferred APIs
only with their exact called internal helper bodies and cleanup. Actual native
audio component playback/ABI/lifetime checks pass with these methods. Actual
startup reaches the separate I3DL2 reverb operation. Its fifteen-function,
2171-byte pure arithmetic closure is being assessed for direct native reuse.
The first captured present remains black; complete rendered scene and attract
behavior are still open.
