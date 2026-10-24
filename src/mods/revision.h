/* Revision-specific title facts. Never changes original executable bytes. */
#ifndef JSRF_REVISION_H
#define JSRF_REVISION_H
#ifdef JSRF_USA_STANDALONE
#define JSRF_SHA "fd19055756719893c466302809b433b785ecf5732df0441286f3f605f0f3ef9c"
/* Reviewed mod sites below 76800 retain their addresses; the referenced
 * later code sites move by 30h, and SDK/data sections move by 40h.
 * This is a mapping of these mod sites, not every game instruction.
 * config/revisions/usa-standalone records exact source-block hashes. */
#define JSRF_VA(value) ((value) + ((value) >= 0x18cb00u ? 0x40u : ((value) >= 0x76800u ? 0x30u : 0u)))
#else
#define JSRF_SHA "f4441696fdd007c31a712815cdde967836fbc3ab97fcb2f58e1db56974644219"
#define JSRF_VA(value) (value)
#endif
#endif
