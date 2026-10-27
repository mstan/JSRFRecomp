/* Optional hold-Start request at the original scripted-event update boundary.
 * Original 23790 calls 1E8C0 both at natural completion and for a previously
 * viewed event's A/Start skip. That routine records viewing, releases actor,
 * animation/voice resources and resumes the original mission. Never jump the
 * mission, advance its timer, fabricate completion flags or modify input.
 * Source identities and layout proofs: config/revisions/.../cutscene-skip.json.
 */
static unsigned skip_cutscenes;
static struct {
    unsigned actor,script,event,armed,fired;
    uint64_t begin,last;
} cutscene_hold;
static void cutscene_configure(void)
{
    const char *value=getenv("XLLE_PILOT_TITLE_MOD_HOLD_SKIP_CUTSCENES");
    if(value && strcmp(value,"0") && strcmp(value,"1"))fail("invalid Hold Start to Skip selection");
    skip_cutscenes=value && !strcmp(value,"1");
    if(skip_cutscenes && (!api->invoke || !api->monotonic))fail("cutscene completion service unavailable");
}
static int cutscene_context(unsigned actor,unsigned *script,unsigned *event)
{
    unsigned manager=0,owner=0,wrapper=0,mission=0,vtable=0,flags=0,state=0,id=0;
    if(!challenge_heap(actor,0x108) ||
       !read_u32(JSRF_VA(0x22fca0),&manager) || !manager ||
       !read_u32(manager+0x98+0x1ddd*4,&owner) || owner!=actor ||
       !read_u32(actor,&vtable) || vtable!=JSRF_VA(0x1c4b68) ||
       !read_u32(actor+4,&flags) || (flags&0x80000000u) ||
       !read_u32(actor+0x88,&state) || state!=2 ||
       !read_u32(actor+0x24,&wrapper) || !challenge_heap(wrapper,0x64) ||
       !read_u32(manager+0x98+0x1ddb*4,&owner) || owner!=wrapper ||
       !read_u32(wrapper,&vtable) || vtable!=JSRF_VA(0x1c4c90) ||
       !read_u32(wrapper+0x24,&mission) || !challenge_heap(mission,0xfbc) ||
       !read_u32(manager+0x98+9*4,&owner) || owner!=mission ||
       !read_u32(mission,&vtable) || vtable!=JSRF_VA(0x1caa70) ||
       !read_u32(mission+0x5c,&state) || state!=19 ||
       !read_u32(actor+0x8c,event) || !read_u32(wrapper+0x48,&id) || id!=*event ||
       !read_u32(actor+0xdc,script) || !challenge_heap(*script,0x1a0))return 0;
    return 1;
}
static void cutscene_function(struct PilotTitleModCall *call)
{
    if(!skip_cutscenes || call->id!=11)return;
    unsigned actor=call->entry[1],script=0,event=0;
    if(!cutscene_context(actor,&script,&event)) {
        memset(&cutscene_hold,0,sizeof(cutscene_hold));return;
    }
    if(call->phase) {
        if(call->scratch!=1)return;
        /* The ordinary update just ran. Revalidation above prevents a second
         * teardown if it naturally finished (or the vanilla repeat skip won).
         * invoke preserves the complete original CPU/register/stack state. */
        unsigned result=0;
        if(!api->invoke(12,actor,NULL,0,&result))fail("original cutscene completion invocation failed");
        fprintf(stderr,"[JSRF CUTSCENE] held-start event=%u original-cleanup=1\n",event);
        return;
    }
    if(cutscene_hold.actor!=actor || cutscene_hold.script!=script || cutscene_hold.event!=event) {
        memset(&cutscene_hold,0,sizeof(cutscene_hold));
        cutscene_hold.actor=actor;cutscene_hold.script=script;cutscene_hold.event=event;
    }
    unsigned held=0;
    if(!read_u32(JSRF_VA(0x251da4),&held))return;
    uint64_t now=api->monotonic();
    /* Only time observed while this event updates counts. A suspended window
     * or long CPU stall cannot turn an old press into an immediate skip. */
    if(now<cutscene_hold.last || now-cutscene_hold.last>2500000)cutscene_hold.begin=0;
    cutscene_hold.last=now;
    if(!(held&1)) { /* Original logical Start=1, A=4 (not raw XINPUT bits). */
        cutscene_hold.begin=0;cutscene_hold.armed=1;return;
    }
    /* Require release after scene entry, so holding Start through a transition
     * cannot also skip the following scene. Player 1 owns this convenience. */
    if(!cutscene_hold.armed || cutscene_hold.fired)return;
    if(!cutscene_hold.begin){cutscene_hold.begin=now;return;}
    if(now-cutscene_hold.begin<10000000)return;
    cutscene_hold.fired=1;call->scratch=1;
}
