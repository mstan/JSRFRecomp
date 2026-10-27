/* Source-bound CCamera::draw calls to CPlayer's boost predicate. The original
 * predicate still runs for every caller. Only the two camera rendering tests
 * select its ordinary full-resolution scene path; boost physics, inventory,
 * animation, audio and all other predicate callers retain the real result. */
static unsigned boost_pending;
static unsigned boost_passes;
static void boost_composite(void)
{
    if(!boost_pending)return;
    boost_pending=0;
    if(!api->radial_blur || !api->radial_blur(.032f))fail("JSRF native boost scene is unavailable");
    if(!boost_passes++)fprintf(stderr,"[JSRF BOOST] full-resolution native scene; one radial pass before original overlays\n");
}
static int title_function(struct PilotTitleModCall *call)
{
    cutscene_function(call);
    if(!call->phase) {
        if(call->id==2 && seamless) {
            unsigned kind=63;read_u32(call->entry[1]+0x48,&kind);
            call->scratch=(api->monotonic()<<6)|(kind&63);
        }
        return 0;
    }
    if(call->id==2 && call->scratch) {
        loading_native_time+=api->monotonic()-(call->scratch>>6);
        loading_cost((unsigned)(call->scratch&63),call->scratch>>6);
    }
    seamless_step(call);
    challenge_result(call);
    if(call->id==1 && (call->caller==JSRF_VA(0xa299f) || call->caller==JSRF_VA(0xa30fc))) {
        if(call->caller==JSRF_VA(0xa299f) && call->gpr[0])boost_pending=1;
        call->gpr[0]=0;
    }
    return 0;
}
