# 2026.10.25.4

- Full-resolution boost presentation preserves the wide scene and avoids the original low-resolution feedback effect. Boost and spray rendering passed the owner's playtest.
- Adaptive Fit to screen remains active through outgoing scene transitions and dialogue. Original cinematic bars span the output width. The owner validated these framing changes.
- Preloaded Area Assets is enabled by default, caching non-ADX files and accelerating original resource preparation. Music and voices continue to stream. Uses approximately1GB additional host memory.
- Normal loading screens remain visible while resources are prepared. This release does not implement instantaneous area transitions or freeze the previous frame to conceal loading. A true prepared-resource handoff remains experimental work.
- Crash reports and input logs remain enabled by default under Diagnostics. Input playback does not restore host clocks or thread scheduling.

Both supported USA executable revisions are included. Blinx receives the tested shared framework update. Native saves and settings are preserved. No GitHub publication is part of this release.
