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
