/* Authored title UI mod. Original CPU code, chapter and soul flags stay intact.
 * Source-bound facts: config/revisions/ntsc-u/challenge-unlock.json.
 * Rebuild only the transient Roboy Test Run menu the original 756E0 builds
 * after chapter9, using its same area/soul comparisons and loaded menu rows.
 */
static unsigned early_test_runs=1,challenge_cached,challenge_notified;
static uint32_t challenge_key[16],challenge_root;

static void challenge_configure(void)
{
    const char *value=getenv("XLLE_PILOT_TITLE_MOD_EARLY_TEST_RUNS");
    if(value && strcmp(value,"0") && strcmp(value,"1"))fail("invalid Early Test Runs selection");
    early_test_runs=!value || !strcmp(value,"1");
}
static int challenge_read(uint32_t at,void *out,uint32_t bytes)
{return api->read(at,out,bytes);}
static int challenge_heap(uint32_t at,uint32_t bytes)
{
    /* The original image ends at2885E0. UI allocations cannot alias original
     * static data (including the save manager), code or the hardware aperture. */
    return at>=0x2885e0u && at<0x04000000u && !(at&3) && bytes<=0x04000000u-at;
}
static int challenge_overlap(uint32_t a,uint32_t an,uint32_t b,uint32_t bn)
{return a<b+bn && b<a+an;}
static void challenge_refresh(void)
{
    if(!early_test_runs)return;
    uint32_t manager=0,owner=0,vtable=0,chapter=0,pointers[20],key[16],root;
    if(!read_u32(0x22fca0,&manager) || !manager ||
       !read_u32(manager+0x98+0x128a*4,&owner) || !owner ||
       !challenge_heap(owner,0x17c) || !read_u32(owner,&vtable) || vtable!=0x1ccc98) {
        challenge_cached=0;return;
    }
    if(!read_u32(0x1eff74,&chapter))fail("Test Run chapter data unavailable");
    if(chapter==9){challenge_cached=0;return;} /* Original post-game behavior. */
    if(chapter>9)fail("unexpected Test Run chapter");
    if(!challenge_read(owner+0xb0,pointers,sizeof(pointers)))fail("Test Run menu owner unavailable");
    uint32_t main=pointers[1],modes=pointers[7],source=pointers[18];
    uint32_t destinations[5]={modes,pointers[9],pointers[10],pointers[11],pointers[12]};
    const uint32_t sizes[5]={64,208,208,96,112};
    if(!main || !modes || !source)return; /* Constructor has not published its data. */
    for(unsigned i=0;i<5;++i)if(!destinations[i])return;
    if(!challenge_heap(main,96) || !challenge_heap(source,0x270))fail("invalid Test Run menu allocation");
    if(challenge_overlap(main,96,owner,0x17c) || challenge_overlap(source,0x270,owner,0x17c) ||
       challenge_overlap(main,96,source,0x270))fail("aliased Test Run source allocation");
    for(unsigned i=0;i<5;++i) {
        if(!challenge_heap(destinations[i],sizes[i]) ||
           challenge_overlap(destinations[i],sizes[i],owner,0x17c) ||
           challenge_overlap(destinations[i],sizes[i],main,96) ||
           challenge_overlap(destinations[i],sizes[i],source,0x270))fail("aliased Test Run menu allocation");
        for(unsigned j=0;j<i;++j)
            if(challenge_overlap(destinations[i],sizes[i],destinations[j],sizes[j]))fail("overlapping Test Run lists");
    }
    key[0]=owner;key[1]=main;key[2]=source;
    memcpy(key+3,destinations,sizeof(destinations));
    if(!challenge_read(0x1f0088,key+8,32) || !read_u32(main+0x58,&root))
        fail("Test Run soul data unavailable");
    if(challenge_cached && root==challenge_root && !memcmp(key,challenge_key,sizeof(key)))return;
    uint32_t area_ids[14],zone_map[100],soul_zones[256],source_rows[0x270/4];
    if(!challenge_read(0x21c058,area_ids,sizeof(area_ids)) ||
       !challenge_read(0x1efc48,zone_map,sizeof(zone_map)) ||
       !challenge_read(0x1f8bf8,soul_zones,sizeof(soul_zones)) ||
       !challenge_read(source,source_rows,sizeof(source_rows)))fail("Test Run source tables unavailable");
    uint32_t complete[14];
    for(unsigned area=0;area<14;++area) {
        uint32_t zone=zone_map[((area_ids[area]>>16)%10)*10+(area_ids[area]&0xffff)%10];
        unsigned total=0,collected=0;
        for(unsigned soul=0;soul<256;++soul)if(soul_zones[soul]==zone) {
            ++total;if(key[8+soul/32]&(1u<<(soul%32)))++collected;
        }
        complete[area]=total==collected; /* Same comparison as original3A0A0/3A130. */
    }
    uint32_t mode_rows[16],lists[4][52],any=0;
    const unsigned offsets[4]={4,0xd4,0x1a4,0x204},counts[4]={13,13,6,7};
    for(unsigned mode=0;mode<4;++mode) {
        uint32_t available=0;
        for(unsigned row=0;row<counts[mode];++row) {
            const uint32_t *original=source_rows+offsets[mode]/4+row*4;
            if(original[0]>=14)fail("invalid Test Run area index");
            uint32_t *entry=lists[mode]+row*4;
            entry[0]=original[0];entry[1]=original[2];entry[2]=complete[original[0]];entry[3]=original[1];
            available|=entry[2];
        }
        mode_rows[mode*4]=mode;mode_rows[mode*4+1]=mode+8;
        mode_rows[mode*4+2]=available;mode_rows[mode*4+3]=0xffffffffu;any|=available;
    }
    /* These are the only writes: disposable menu allocations, never soul,
     * chapter, mission-completion or save bytes. Original launch flow consumes
     * the same rows/IDs it uses after story completion. */
    for(unsigned mode=0;mode<4;++mode)
        if(!api->write_data(destinations[mode+1],lists[mode],counts[mode]*16))fail("Test Run list is not writable");
    if(!api->write_data(modes,mode_rows,sizeof(mode_rows)) ||
       !api->write_data(main+0x58,&any,4))fail("Test Run menu is not writable");
    memcpy(challenge_key,key,sizeof(key));challenge_root=any;challenge_cached=1;
    if(!challenge_notified) {
        fprintf(stderr,"[MOD] early-test-runs=1 chapter=%u menu-only=1 soul-requirement=original\n",chapter);
        challenge_notified=1;
    }
}
