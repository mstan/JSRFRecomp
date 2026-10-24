/* Authored fake-memory transport for the title plugin, with no original code. */
#include "title_mod.h"
#include "../src/mods/revision.h"
#include <setjmp.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif
static unsigned char *ram;
static uint32_t ram_size,writes;
static jmp_buf rejected;
static const char *error;
static void fail(const char *reason){error=reason;longjmp(rejected,1);}
static int read_memory(uint32_t at,void *out,uint32_t bytes)
{if(at>ram_size || bytes>ram_size-at)return 0;memcpy(out,ram+at,bytes);return 1;}
static int write_memory(uint32_t at,const void *in,uint32_t bytes)
{if(at>ram_size || bytes>ram_size-at)return 0;++writes;memcpy(ram+at,in,bytes);return 1;}
static int read_u32(unsigned at,unsigned *out){return read_memory(at,out,4);}
static const struct PilotTitleModHost transport={PILOT_TITLE_MOD_ABI,"fixture",read_memory,write_memory};
static const struct PilotTitleModHost *api=&transport;
#include "../src/mods/challenge_unlock.inc"
EXPORT int jsrf_challenge_fixture(void *memory,unsigned bytes,unsigned enabled,unsigned reset)
{
    ram=memory;ram_size=bytes;writes=0;error=NULL;early_test_runs=enabled;
    if(reset){challenge_cached=0;challenge_notified=0;}
    if(setjmp(rejected))return -1;
    challenge_refresh();return (int)writes;
}
EXPORT const char *jsrf_challenge_error(void){return error?error:"";}
