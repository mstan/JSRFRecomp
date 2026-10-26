# Resident loading and adaptive transitions

The default title switch `SEAMLESS_LOADING` preloads non-ADX disc assets into a bounded, read-only host cache. The current USA media set retains 2518 files (976,975,369 bytes). The configured limit is 1152 MiB, with at least 1 GiB of additional free host memory required. Music and voice ADX streams remain on the original streaming path. Incomplete preload, budget exhaustion or allocation failure discards the cache and retains original disc I/O.

Resident assets retain real read handles and file identity. Original guest sharing restrictions, independent synchronous cursors, asynchronous IOSB/APC/event completion, EOF and unbuffered I/O behavior remain enforced. Native saves and utility-cache writes use their original writable paths. There is no whole-file loader replacement and no fabricated completion.

Source-hashed bindings retain the original loader at 0x25310 and CMission update at 0x51FC0. After one original mission update, only original resource handlers for phases0..12 (excluding bridge2) may run additional progress-making steps. A quantum is bounded to4096 calls and12ms, but an individual original resource call can exceed that duration. Scripts, dialogue, game logic and fade clocks are not repeatedly stepped.

Loading screens remain visible while real resource work is pending. The owner rejected desktop-frame holding: it froze the outgoing image while retaining the loading wait and buzzing audio. That presentation API and its use have been removed. Suppression is permitted only after destination preparation and installation genuinely complete within a frame.

Native service accounting and indexed pool allocation reduce resource setup cost without changing allocation ownership. One matched title-load measurement improved from about2.35s to1.60s; timings vary with diagnostics and host load. This is not a measurement of every area transition.

Adaptive widescreen now persists across camera teardown and fade-only frames. Cinematic camera viewports preserve their original vertical framing while adapting horizontally; full-width cinematic bars and wipes span the output. Square save-preview render targets retain their original projection. Interpolation remains restricted to ordinary gameplay.

## Validation status, 2026-10-25

Both supported revisions build. Eight title contracts cover adaptive/fixed/disabled presentation, resident resource progression and boundaries that must retain the original script/gameplay behavior. Affected native checks cover resident I/O and sharing, allocation/accounting, source-bound function calls and radial boost rendering.

The owner has accepted boost, spray and adaptive loading/exit/dialogue framing. One-frame seamless loading is NOT implemented or accepted. The actual owner round trip still spent seconds processing area resources after resident I/O; the measured pending Garage preparation was about3.03s with2.39s of resource work. Do not advertise a held image, absent loading text or a passing build as seamless performance.

## Tomba implementation comparison

Read the actual implementation from local TombaRecomp commit `9748193`, rather than the older main-worktree Fast Loading plugin. `src/mods/tomba_seamless_prepare.cpp` prepares a verified resident pack containing both source bytes and decoded GAM output. `src/mods/tomba_seamless.c` preflights a complete resource queue, installs RAM data, texture rectangles and sound-bank data through the shared guest services, publishes real completion, then combines qualified one-shot transition states. It preserves original movement, fade speed, scheduler yields and music commands. Unsupported queues fall back to retail loading. See that revision's `docs/SEAMLESS_TRANSITIONS_SPIKE.md` for its acceptance limits.

JSRF currently retains source files only and runs the original resource parsers, allocators, GPU resource creation and audio setup at the boundary. A real equivalent requires title-specific decoded resource preparation, validated whole-queue installation and a handoff that preserves current inventory/events and native save state. It must qualify both supported XBEs and demonstrate last-outgoing-frame to first-destination-frame time, correct resources and normal audio. Until then the original loading presentation stays in place.
