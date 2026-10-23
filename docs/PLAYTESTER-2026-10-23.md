# October 23 playtester update

Framework pin: `da5b9b2af7cc142d57d59d16be695106e73bf428`.
This refresh retains the optimized native gameplay profile and existing
generated CPU code. The shared launcher includes independent horizontal and
vertical camera inversion, both off by default. Optional native startup remains
off by default for this game and uses compatible original startup inputs
supplied separately by the player.

The focused regression passed original Load Game from a private checkpoint
copy, measured player movement and a 15-second active rendering/audio-pipeline
stability interval. The source saves remained unchanged. Retained captures
show Chuo gameplay geometry, player/NPCs and HUD. This does not claim subjective
audio quality, performance qualification or new campaign/mechanics coverage.
A bright radial foreground effect appears in both this checkpoint run and its
earlier accepted reference; its original-game accuracy was not evaluated.

The existing [gameplay burndown](NATIVE-GAMEPLAY-BURNDOWN.md) retains the broader
coverage limits. The clean Windows ZIP includes matching project/framework and
prepared dependency source locally; original media, console inputs, saves,
used profiles and private diagnostic receipts are excluded.
