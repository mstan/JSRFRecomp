/* Asset-only acceleration. Invoke the source-hashed original loader and
 * one-shot mission resource handlers; never repeat CMission::update, its
 * dialogue/script tail, world updates, gameplay state15, or fade timers. */
static unsigned seamless=1;
static struct {unsigned actor,id,last,steps;uint64_t begin,work,native_begin;} loading[2];
static uint64_t loading_native_time;
static unsigned loading_cost_records;
static void loading_cost(unsigned type,uint64_t begin)
{
    uint64_t elapsed=api->monotonic()-begin;
    if(elapsed>=200000 && loading_cost_records++<48)
        fprintf(stderr,"[JSRF LOAD COST] resource_class=%u elapsed_ms=%.3f\n",type,elapsed/10000.0);
}
static void seamless_configure(void)
{
    const char *value=getenv("XLLE_PILOT_TITLE_MOD_SEAMLESS_LOADING");
    if(value && strcmp(value,"0") && strcmp(value,"1"))fail("invalid Seamless Loading selection");
    seamless=!value || !strcmp(value,"1");
    static const char *streams[]={".adx"};
    if(seamless && (!api->resident_media || !api->resident_media(1152,streams,1)))
        fail("JSRF resident preload configuration rejected");
}
static void seamless_step(struct PilotTitleModCall *call)
{
    if(!seamless || call->id!=3 || call->phase!=1 || !api->resident_ready())return;
    unsigned actor=call->entry[1],manager=0,mission=0,pending=0,vtable=0,state=0,id=0,loader=0;
    if(!read_u32(JSRF_VA(0x22fca0),&manager) || !manager ||
       !read_u32(manager+0x98+9*4,&mission) || !read_u32(manager+0x98+10*4,&pending) ||
       (mission!=actor && pending!=actor) ||
       !read_u32(actor,&vtable) || vtable!=JSRF_VA(0x1caa70) ||
       !read_u32(actor+0x5c,&state) || !read_u32(actor+0x58,&id))return;
    unsigned slot=mission==actor?0:1;
    if(loading[slot].actor!=actor || loading[slot].id!=id) {
        loading[slot].actor=actor;loading[slot].id=id;loading[slot].last=~0u;
        loading[slot].steps=0;loading[slot].work=0;loading[slot].begin=api->monotonic();
        loading[slot].native_begin=loading_native_time;
    }
    unsigned start=state,steps=0;
    uint64_t begin=api->monotonic();
    if(!read_u32(manager+0x98+7*4,&loader) || !loader)return;
    /* A bounded quantum permits the OS/audio services to run between turns.
     * Original handlers publish completion only after their real writes. */
    for(;steps<4096 && api->monotonic()-begin<120000;++steps) {
        if(state>12 || state==2)break;
        unsigned busy=0,result=0;
        if(!read_u32(loader+0x44,&busy))break;
        if(busy) {
            unsigned before[0x1920/4],after[0x1920/4];
            /* Each original resource class owns its own progress fields, not
             * just the shared busy/file-I/O prefix. Observe the complete
             * source-bound loader allocation before calling another step. */
            uint64_t cost_begin=api->monotonic();
            if(!api->read(loader,before,sizeof(before)) || !api->invoke(2,loader,NULL,0,&result) ||
               !api->read(loader,after,sizeof(after)))fail("JSRF original loader invocation failed");
            loading_cost(before[0x48/4],cost_begin);
            if(!memcmp(before,after,sizeof(before))) {
                static unsigned waits;
                if(waits++<16) {
                    char name[128]={0};api->read(loader+0x78,name,127);
                    fprintf(stderr,"[JSRF LOAD WAIT] phase=%u busy=%u type=%u asset=%08x io=%u/%u status=%08x class1=%u class11=%u errors=%u file=%s\n",
                    state,after[0x44/4],after[0x48/4],after[0x4c/4],after[0x50/4],after[0x54/4],after[0x64/4],after[0x25c/4],after[0x1590/4],after[0x180/4],name);
                }
                break;
            }
        } else {
            unsigned before[4],after[4];
            if(!api->read(actor+0x64,before,sizeof(before)))break;
            if(!api->invoke(32+state,actor,NULL,0,&result))fail("JSRF original loading phase invocation failed");
            unsigned next=0;if(!read_u32(actor+0x5c,&next))break;
            if(next==state && !read_u32(loader+0x44,&busy))break;
            if(next==state && !busy && state!=8)break;
            if(next==state && !busy && (!api->read(actor+0x64,after,sizeof(after)) || !memcmp(before,after,sizeof(before)))) {
                static unsigned waits;
                if(waits++<16)fprintf(stderr,"[JSRF RESOURCE WAIT] phase=%u queue=%u/%u pending=%u\n",state,after[2],after[1],after[3]);
                break;
            }
            state=next;
        }
    }
    loading[slot].steps+=steps;
    loading[slot].work+=api->monotonic()-begin;
    if(state!=loading[slot].last) {
        fprintf(stderr,"[JSRF LOAD] mission=%08x actor=%u phase=%u->%u steps=%u total_steps=%u elapsed_ms=%.3f work_ms=%.3f native_ms=%.3f quantum_ms=%.3f\n",
            id,slot+9,start,state,steps,loading[slot].steps,(api->monotonic()-loading[slot].begin)/10000.0,
            loading[slot].work/10000.0,(loading_native_time-loading[slot].native_begin)/10000.0,(api->monotonic()-begin)/10000.0);
        loading[slot].last=state;
    }
}
