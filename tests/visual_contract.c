/* Authored RAM and matrices only. No original executable or generated CPU. */
#include "title_mod.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SHA "f4441696fdd007c31a712815cdde967836fbc3ab97fcb2f58e1db56974644219"
#define CHECK(x) do{if(!(x)){fprintf(stderr,"line%d: %s\n",__LINE__,#x);return 1;}}while(0)
static unsigned char ram[0x4000000];
static unsigned reads,writes,client[2]={1680,720},shape[2],frame_scope;
static int read_data(unsigned a,void *p,unsigned n)
{if(a>=sizeof(ram) || n>sizeof(ram)-a)return 0;++reads;memcpy(p,ram+a,n);return 1;}
static int write_data(unsigned a,const void *p,unsigned n)
{if(a>=sizeof(ram) || n>sizeof(ram)-a)return 0;++writes;memcpy(ram+a,p,n);return 1;}
static void u32(unsigned a,unsigned n){memcpy(ram+a,&n,4);}
static void f32(unsigned a,float n){memcpy(ram+a,&n,4);}
static float getf(unsigned a){float n;memcpy(&n,ram+a,4);return n;}
static int presentation(unsigned n,unsigned d,unsigned h){return n && d && h==720;}
static int client_size(unsigned size[2]){memcpy(size,client,sizeof(client));return 1;}
static int frame_shape(unsigned n,unsigned d){shape[0]=n;shape[1]=d;return 1;}
static int visuals(const struct PilotVisualMods *p){return pilot_visual_mods_validate(p);}
static void set_scope(unsigned scope){frame_scope=scope;}
static void env(const char *key,const char *value)
{
#ifdef _WIN32
    _putenv_s(key,value);
#else
    if(*value)setenv(key,value,1);else unsetenv(key);
#endif
}
static void original_projection(void)
{
    f32(0x22e68c,4.0f/3);f32(0x22e6a4,.75f);u32(0x264e98,640);u32(0x264e9c,480);
    f32(0x264e40,1.25f);f32(0x264e44,-.75f);f32(0x264e48,1.25f);f32(0x264e4c,.75f);
    f32(0x264ea8,320.0f/.75f);
}
int main(int argc,char **argv)
{
    CHECK(argc==3);env("JSRF_MOD_TRACE","");env("XLLE_PILOT_MOD_PLAN","");
    struct PilotTitleModHost host={PILOT_TITLE_MOD_ABI,SHA,read_data,write_data,
        presentation,client_size,frame_shape,visuals,set_scope};
    if(!strcmp(argv[2],"disabled")) {
        CHECK(!pilot_title_mod_open(&host));CHECK(!reads && !writes);return 0;
    }
    unsigned adaptive=!strcmp(argv[2],"adaptive");
    FILE *out=fopen(argv[1],"wb");CHECK(out);
    fprintf(out,"xlle-mod-plan 2\nidentity %s\noperation aspect 1 jsrf.widescreen 7 3 %u\noperation frame-rate 1 1 60\nend\n",SHA,adaptive);
    fclose(out);env("XLLE_PILOT_MOD_PLAN",argv[1]);
    u32(0x22fca0,0x300000);u32(0x300000+0x98+9*4,0x310000);
    u32(0x310000,0x1caa70);u32(0x310058,0x10001);u32(0x31005c,15);
    u32(0x300000+0x98+0x4c*4,0x320000);u32(0x320000,0x1cd4d8);
    f32(0x22e678,1);original_projection();
    const struct PilotTitleMod *mod=pilot_title_mod_open(&host);CHECK(mod && mod->transform && mod->draw && mod->present);
    /* Original Load Game creates a square offscreen projection before the
     * gameplay camera. It must neither trip the gameplay guard nor change. */
    u32(0x31005c,12);u32(0x264e98,512);u32(0x264e9c,512);f32(0x22e68c,1);
    unsigned before=writes;mod->transform(1,0x22e678,0x153fa9);
    CHECK(writes==before && getf(0x22e68c)==1);mod->present();CHECK(shape[0]==4 && shape[1]==3);
    u32(0x31005c,15);original_projection();
    mod->transform(1,0x22e678,0x153fa9);
    CHECK(fabsf(getf(0x22e678)-4.0f/7)<.000001f);
    CHECK(getf(0x22e678)==getf(0x264eb8));
    CHECK(fabsf(getf(0x264e4c)-1.3125f)<.000001f);
    CHECK(fabsf(getf(0x264e40)-sqrtf(1+1.3125f*1.3125f))<.000001f);
    CHECK(getf(0x264e40)==getf(0x264e48));CHECK(getf(0x264e44)==-getf(0x264e4c));
    /* World-to-canvas points and authored glyphs use the same original pixel
     * focal. Raster compression, not a second CPU focal change, maps them to
     * the wide display. A point at the original right edge must still be640. */
    CHECK(fabsf(.75f*getf(0x264ea8)+320-640)<.0001f);
    /* The miniature 3D spray icon shares the right anchor with its 2D count;
     * a following ordinary camera restores zero off-axis translation. */
    u32(0x300000+0x87ec,0x320000);f32(0x22e6a4,.0260835867f);
    f32(0x22e6a0,.02609f);f32(0x22e6b0,-.02609f);
    /* The unbiased miniature pass owns the centered talk prompt. */
    mod->transform(1,0x22e678,0x153fa9);CHECK(getf(0x22e698)==0);
    f32(0x22e6b0,-24.92609f);
    mod->transform(1,0x22e678,0x153fa9);
    CHECK(fabsf(getf(0x22e698)-(1-4.0f/7)*.0260835867f)<.000001f);
    CHECK(getf(0x22e698)==getf(0x264ed8));
    /* Offscreen passes can also occur during gameplay. Undo retained mod
     * elements without imposing the gameplay aspect or miniature HUD bias. */
    u32(0x264e98,512);u32(0x264e9c,512);f32(0x22e68c,1);
    mod->transform(1,0x22e678,0x153fa9);
    CHECK(getf(0x22e678)==1 && getf(0x264eb8)==1 && getf(0x22e698)==0 && getf(0x264ed8)==0);
    CHECK(getf(0x22e68c)==1);original_projection();f32(0x22e6a4,.0260835867f);
    /* A following unbiased prompt must not inherit the can's right anchor. */
    f32(0x22e6b0,-.02609f);mod->transform(1,0x22e678,0x153fa9);CHECK(getf(0x22e698)==0);
    f32(0x22e6b0,-24.02609f);mod->transform(1,0x22e678,0x153fa9);CHECK(getf(0x22e698)==0);
    f32(0x22e6b0,-25.02609f);mod->transform(1,0x22e678,0x153fa9);CHECK(getf(0x22e698)==0);
    original_projection();mod->transform(1,0x22e678,0x153fa9);CHECK(getf(0x22e698)==0);
    /* Repeated frames retain original m0; never compound the prior scale. */
    mod->transform(1,0x22e678,0x153fa9);CHECK(fabsf(getf(0x22e678)-4.0f/7)<.000001f);
    float quad[4][4]={{393,40,0,1},{588,40,0,1},{393,60,0,1},{588,60,0,1}};
    struct PilotTitleModDraw draw={0};draw.positions=(const unsigned char*)quad;
    draw.count=4;draw.stride=16;draw.position_type=0x42;draw.default_target=1;draw.x_scale=1;
    mod->draw(&draw);CHECK(draw.x_anchor==640 && fabsf(draw.x_scale-4.0f/7)<.000001f);
    /* One original dialogue actor owns all text pieces. Moving a glyph over
     * the old left/right heuristic boundaries cannot move it to another edge. */
    u32(0x300000+0x87ec,0x330000);u32(0x330000,0x1c4540);
    for(unsigned glyph=0;glyph<3;++glyph) {
        float x=110+glyph*170.0f;
        quad[0][0]=quad[2][0]=x;quad[1][0]=quad[3][0]=x+16;
        quad[0][1]=quad[1][1]=60;quad[2][1]=quad[3][1]=86;
        mod->draw(&draw);CHECK(draw.x_anchor==320);
        quad[0][1]=quad[1][1]=360;quad[2][1]=quad[3][1]=386;
        mod->draw(&draw);CHECK(draw.x_anchor==320);
    }
    u32(0x300000+0x87ec,0x320000);
    quad[0][0]=quad[2][0]=260;quad[1][0]=quad[3][0]=280;
    quad[0][1]=quad[1][1]=130;quad[2][1]=quad[3][1]=156;
    mod->draw(&draw);CHECK(draw.x_anchor==0);
    /* Score digits and the shared text actor's X/name use one left anchor. */
    u32(0x320208,5);u32(0x300000+0x87ec,0x330000);
    quad[0][1]=quad[1][1]=134;quad[2][1]=quad[3][1]=152;
    mod->draw(&draw);CHECK(draw.x_anchor==0);
    quad[0][1]=quad[1][1]=78;quad[2][1]=quad[3][1]=103.84f;
    mod->draw(&draw);CHECK(draw.x_anchor==0);
    u32(0x320208,9);mod->draw(&draw);CHECK(draw.x_anchor==320);
    mod->present();CHECK(frame_scope==0x10002 && shape[0]*3==shape[1]*7);
    /* Pause cuts interpolation history while retaining the wide world. */
    u32(0x300040,1);original_projection();mod->transform(1,0x22e678,0x153fa9);mod->present();CHECK(!frame_scope);
    u32(0x300040,0);
    if(adaptive) {
        client[0]=2560;client[1]=720;original_projection();mod->transform(1,0x22e678,0x153fa9);
        CHECK(fabsf(getf(0x22e678)-.375f)<.000001f);mod->present();CHECK(shape[0]*9==shape[1]*32);
        client[0]=640;client[1]=480;original_projection();mod->transform(1,0x22e678,0x153fa9);
        CHECK(getf(0x22e678)==1 && getf(0x264e40)==1.25f);mod->present();
    }
    /* Loading restores original shape/projection and cuts synthetic frames. */
    u32(0x31005c,93);original_projection();mod->transform(1,0x22e678,0x153fa9);mod->present();
    CHECK(getf(0x22e678)==1 && shape[0]==4 && shape[1]==3 && !frame_scope);
    return 0;
}
