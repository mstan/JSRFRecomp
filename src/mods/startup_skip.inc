/* Source-bound startup presentation: original logo actor 1DDA, vtable
 * 1CCF78 (rev4), update 7E330. Original A/Start latch +A0 controls logo
 * fades; warning phase13 ignores it until counter +9C exceeds420.
 * Let the original code perform its fade, teardown and resource lifetime.
 */
static unsigned skip_startup=1;
static void startup_configure(void)
{
    const char *value=getenv("XLLE_PILOT_TITLE_MOD_SKIP_STARTUP");
    if(value && strcmp(value,"0") && strcmp(value,"1"))fail("invalid startup skip selection");
    skip_startup=!value || !strcmp(value,"1");
}
static void startup_refresh(void)
{
    if(!skip_startup)return;
    unsigned manager=0,owner=0,vtable=0,phase=0,pulse=0;
    if(!read_u32(JSRF_VA(0x22fca0),&manager) || !manager ||
       !read_u32(manager+0x98+0x1dda*4,&owner) || !challenge_heap(owner,0xbc) ||
       !read_u32(owner,&vtable) || vtable!=JSRF_VA(0x1ccf78) ||
       !read_u32(owner+0x98,&phase) || phase>13)return;
    for(unsigned port=0;port<4;++port) {
        unsigned value=0;
        if(read_u32(JSRF_VA(0x251da8)+port*0x40,&value))pulse|=value;
    }
    if(!(pulse&5))return;
    const unsigned pending=1;
    if(!api->write_data(owner+0xa0,&pending,4))fail("startup input latch unavailable");
    if(phase==13) {
        const unsigned elapsed=421;
        if(!api->write_data(owner+0x9c,&elapsed,4))fail("startup warning timer unavailable");
    }
}
