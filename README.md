# Jet Set Radio Future

A separate original Xbox title project using the pinned XboxLLR framework.
The current target is the original NTSC-U attract demo running entirely through generated native CPU and shared native services. Actual execution now renders the title and animated city/skating demo, then returns through the original logos and title into the demo again. Audio routing acceptance and interactive gameplay remain unverified; this is a development preview.

Provide your own game under ignored local paths. Original game files, console inputs and generated code are never included in this repository. The private development image is SHA256 `f4441696fdd007c31a712815cdde967836fbc3ab97fcb2f58e1db56974644219` (title ID `5345000A`, XDK 4134).

The [native attract burndown](docs/NATIVE-ATTRACT-BURNDOWN.md) records reached behavior, failures and deferred precision. Framework code is reusable across this title, Blinx and the dashboard; title-specific profiles supply reviewed interfaces and layouts.

CPU translation references phobos665/xboxrecomp and sp00nz/sp00nznet/xboxrecomp. Additional exact source/license attribution follows each borrowed implementation through the framework notices; this project does not grant rights to original game assets.

The reviewed [native function recovery plan](config/revisions/ntsc-u/native-function-recovery.json)
contains image-bound extent facts, rather than original code. After the normal
`prepare` step, apply it before `configure`/`build`:

```powershell
python tools/game.py recover --paths local/paths.json --recovery config/revisions/ntsc-u/native-function-recovery.json
```

This uses the shared transactional native compiler path. Generated original
code and recovery history stay in the private build directory.
