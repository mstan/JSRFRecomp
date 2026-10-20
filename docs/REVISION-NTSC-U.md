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
