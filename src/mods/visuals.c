/* Trusted title registry. Raster/AA/filtering implementations live in XboxLLR;
 * data-only packages select them without changing original code or descriptors.
 */
#include "title_mod.h"
#include "visual_mod_plan.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define JSRF_SHA "f4441696fdd007c31a712815cdde967836fbc3ab97fcb2f58e1db56974644219"
static const struct PilotTitleModHost *api;
static FILE *trace;
static const char *trace_trigger;
static unsigned trace_armed,transform_count,draw_count;
static unsigned numerator=4,denominator=3,adaptive,wide,frame_mode;
static unsigned frame_aspect[2]={4,3},projection_seen,scope_dirty=1,scene,scope;
static unsigned scene_manager,scene_camera;
static float prior_scale=1,prior_offset;
static void fail(const char *reason)
{fprintf(stderr,"[TITLE MOD STOP] %s\n",reason);fflush(stderr);exit(2);}

static int read_u32(unsigned address,unsigned *value)
{return api->read(address,value,4);}
static void write_float(unsigned address,float value)
{if(!api->write_data(address,&value,4))fail("JSRF visual mod data is not writable");}
static void update_scope(void)
{
    if(!scope_dirty)return;
    scope_dirty=0;scene=scope=scene_manager=scene_camera=0;
    unsigned manager,mission,camera,vtable,state,id,flags[4];
    /* Original CActMan::getAct(9), not a heap scan or a cached actor lifetime.
     * Camera 0 is actor4C. Slot owners and CMission state are checked before
     * using this scope; missing actors during loading mean original output. */
    if(!read_u32(0x22fca0,&manager) || !manager ||
       !read_u32(manager+0x98+9*4,&mission) || !mission ||
       !read_u32(mission,&vtable) || vtable!=0x1caa70 ||
       !read_u32(mission+0x58,&id) || !read_u32(mission+0x5c,&state) ||
       (state!=15 && state!=19) ||
       !read_u32(manager+0x98+0x4c*4,&camera) || !camera ||
       !read_u32(camera,&vtable) || vtable!=0x1cd4d8)return;
    scene=1;scene_manager=manager;scene_camera=camera;
    /* Covered pause, event, frozen camera, uncovered pause. Only ordinary
     * gameplay enables synthetic presentation; a scope cut clears history. */
    if(state==15 && api->read(manager+0x40,flags,sizeof(flags)) &&
       !flags[0] && !flags[1] && !flags[2] && !flags[3])scope=id+1;
}
static void aspect(unsigned *n,unsigned *d)
{
    *n=numerator;*d=denominator;
    unsigned size[2];
    if(adaptive && api->client_size(size) && size[1]) {
        if((unsigned long long)size[0]*3<(unsigned long long)size[1]*4){*n=4;*d=3;}
        else if((unsigned long long)size[0]*9>(unsigned long long)size[1]*32){*n=32;*d=9;}
        else {*n=size[0];*d=size[1];}
    }
}
static void camera_transform(unsigned state,unsigned address,unsigned caller)
{
    if(!wide || state!=1 || address!=0x22e678 || caller!=0x153fa9)return;
    scope_dirty=1;update_scope();
    float matrix[16];
    if(!api->read(address,matrix,sizeof(matrix)))fail("JSRF projection is unavailable");
    if(!isfinite(matrix[0]) || (fabsf(matrix[0]-1)>.00001f && fabsf(matrix[0]-prior_scale)>.00001f) ||
       !isfinite(matrix[5]) || fabsf(matrix[5]-4.0f/3.0f)>.0001f ||
       !isfinite(matrix[8]) || (fabsf(matrix[8])>.000001f && fabsf(matrix[8]-prior_offset)>.000001f) ||
       !isfinite(matrix[11]) || matrix[11]<=0 || matrix[11]>32)
        fail("unexpected original JSRF perspective data");
    unsigned n=4,d=3;if(scene)aspect(&n,&d);
    float scale=4.0f*d/(3.0f*n),tangent=matrix[11]/scale;
    /* 153E90 builds m0=1, m5=4/3 and m11=tan(horizontalFov/2), and copies
     * that matrix to264EB8 before SetTransform. Update both copies. The
     * original builder retains m0, so assign from its source invariant each
     * time instead of repeatedly multiplying an already modified matrix. */
    write_float(address,scale);write_float(0x264eb8,scale);prior_scale=scale;
    /* The camera's HUD pass uses the original0x222-angle miniature 3D
     * projection (spray-can model), then screen-space health/counter quads.
     * Move that model to the same right anchor with an off-axis projection;
     * changing m8 adds a constant clip-X offset without stretching the model.
     * Other actors using this UI projection and world/cutscene cameras keep
     * their own placement. Original builders retain m8: restore it each call. */
    unsigned owner=0;
    float offset=0;
    if(scope && fabsf(matrix[11]-.0260835867f)<.000001f &&
       read_u32(scene_manager+0x87ec,&owner) && owner==scene_camera)
        offset=(1-scale)*matrix[11];
    write_float(address+32,offset);write_float(0x264eb8+32,offset);prior_offset=offset;
    /* 153A60 builds the two CPU horizontal clipping planes from this same
     * tangent: (+/-1,0,tan) and the sphere-radius factor sec(halfFov).
     * Keep original vertical/near/far planes. This preserves geometry/entity
     * admission in the added camera margins instead of widening only GPU X. */
    if(scale<1) {
        float secant=sqrtf(1+tangent*tangent);
        write_float(0x264e40,secant);write_float(0x264e44,-tangent);
        write_float(0x264e48,secant);write_float(0x264e4c,tangent);
    }
    /* Original CPU point projection uses inverse horizontal pixel focal
     * length at264EA8; vertical projection has an independent owner264EB0. */
    unsigned width;
    if(!read_u32(0x264e98,&width) || width!=640)fail("unexpected JSRF logical viewport width");
    if(scale<1)write_float(0x264ea8,tangent/320.0f);
    frame_aspect[0]=n;frame_aspect[1]=d;projection_seen=scene;
}

/* Bounded, explicitly enabled diagnostics for deriving the title camera/HUD
 * contract. No rendering or guest data changes, and no per-draw work by default.
 * Arm after loading gameplay so startup/menu draws cannot consume the budget. */
static void transform(unsigned state,unsigned address,unsigned caller)
{
    camera_transform(state,address,caller);
    if(!trace_armed || transform_count>=128 || (state!=1 && transform_count>=16))return;
    float matrix[16];
    if(!api->read(address,matrix,sizeof(matrix)))return;
    unsigned manager=0,actor=0,id=0,vtable=0;
    if(read_u32(0x22fca0,&manager) && manager) {
        read_u32(manager+0x87ec,&actor);read_u32(manager+0x87f0,&id);
        if(actor)read_u32(actor,&vtable);
    }
    fprintf(trace,"transform %u state=%u address=%08x caller=%08x owner=%x/%08x matrix=",transform_count++,state,address,caller,id,vtable);
    for(unsigned i=0;i<16;++i)fprintf(trace,"%.9g%c",matrix[i],i==15?'\n':',');
    fflush(trace);
}
static void draw(struct PilotTitleModDraw *draw)
{
    /* FVF XYZRHW draws carry authored screen pixels. Keep their shape while
     * moving ordinary gameplay HUD to its nearest original edge. 3D draws,
     * full-screen passes and offscreen producers keep their own transforms. */
    if(wide && projection_seen && draw->default_target && draw->position_type==0x42 && draw->positions &&
       draw->count<=4096 && draw->stride>=16) {
        float lo[2]={1e20f,1e20f},hi[2]={-1e20f,-1e20f};int valid=1;
        for(unsigned i=0;i<draw->count;++i) {
            float xy[2];memcpy(xy,draw->positions+i*draw->stride,8);
            for(unsigned j=0;j<2;++j) {
                if(!isfinite(xy[j]))valid=0;
                if(xy[j]<lo[j])lo[j]=xy[j];if(xy[j]>hi[j])hi[j]=xy[j];
            }
        }
        if(valid && !(lo[0]<=1 && hi[0]>=639 && lo[1]<=1 && hi[1]>=479)) {
            draw->x_scale=4.0f*frame_aspect[1]/(3.0f*frame_aspect[0]);draw->x_anchor=320;
            update_scope();
            if(scope && (hi[1]<=160 || lo[1]>=320)) {
                if(hi[0]<=270)draw->x_anchor=0;
                else if(lo[0]>=390)draw->x_anchor=640;
            }
        }
    }
    if(!trace_armed || draw_count>=512 || !draw->positions || draw->count>4096 || draw->stride<8)return;
    float lo[2]={1e20f,1e20f},hi[2]={-1e20f,-1e20f};
    for(unsigned i=0;i<draw->count;++i) {
        float xy[2];memcpy(xy,draw->positions+i*draw->stride,8);
        for(unsigned j=0;j<2;++j) {
            if(!isfinite(xy[j]))return;
            if(xy[j]<lo[j])lo[j]=xy[j];if(xy[j]>hi[j])hi[j]=xy[j];
        }
    }
    unsigned manager=0,actor=0,id=0,vtable=0;
    if(read_u32(0x22fca0,&manager) && manager) {
        read_u32(manager+0x87ec,&actor);read_u32(manager+0x87f0,&id);
        if(actor)read_u32(actor,&vtable);
    }
    fprintf(trace,"draw %u caller=%08x shader=%08x type=%u count=%u xy=%.9g,%.9g,%.9g,%.9g depth=%u/%u target=%u owner=%x/%08x\n",
        draw_count++,draw->caller,draw->shader,draw->position_type,draw->count,
        lo[0],lo[1],hi[0],hi[1],draw->depth_test,draw->depth_write,draw->default_target,id,vtable);
    fflush(trace);
}
static void present(void)
{
    scope_dirty=1;update_scope();
    if(frame_mode)api->frame_scope(scope);
    if(wide && !api->frame_shape(projection_seen?frame_aspect[0]:4,projection_seen?frame_aspect[1]:3))
        fail("unsupported JSRF frame shape");
    projection_seen=0;scope_dirty=1;
    if(trace && !trace_armed) {
        FILE *trigger=fopen(trace_trigger,"rb");
        if(trigger){fclose(trigger);trace_armed=1;}
    }
}

const struct PilotTitleMod *pilot_title_mod_open(const struct PilotTitleModHost *host)
{
    const char *path=getenv("XLLE_PILOT_MOD_PLAN");
    if(!path || !*path)return NULL;
    if(!host || host->abi!=PILOT_TITLE_MOD_ABI || strcmp(host->xbe_sha256,JSRF_SHA))
        fail("JSRF visual mod identity mismatch");
    api=host;
    FILE *file=fopen(path,"rb");
    if(!file)fail("resolved visual mod plan is unavailable");
    struct PilotVisualPlan plan;
    int valid=pilot_visual_plan_read(file,&plan);fclose(file);
    if(!valid || strcmp(plan.identity,JSRF_SHA))fail("invalid JSRF visual mod plan");
    wide=(plan.operations&PILOT_MOD_ASPECT)!=0;
    if(wide && strcmp(plan.aspect_plugin,"jsrf.widescreen"))fail("JSRF aspect plugin identity mismatch");
    frame_mode=plan.options.frame_mode;
    if(frame_mode && (!host->frame_scope || frame_mode!=PILOT_FRAMES_INTERPOLATED))
        fail("JSRF actual faster simulation is not qualified");
    if(!host->visual_mods || !host->visual_mods(&plan.options))
        fail("visual options are unsupported by this build");
    numerator=plan.options.aspect_numerator;denominator=plan.options.aspect_denominator;adaptive=plan.adaptive;
    if(wide && !host->presentation(numerator,denominator,720))fail("unsupported JSRF initial presentation");
    fprintf(stderr,"[MOD] visual-plan=2 operations=%u height=%u ssaa=%u aa=%u aniso=%u aspect=%u:%u adaptive=%u frames=%u/%u original-image=unchanged\n",
        plan.operations,plan.options.internal_height,plan.options.supersample,
        plan.options.antialiasing,plan.options.anisotropy,numerator,denominator,adaptive,frame_mode,plan.options.frame_rate);
    const char *path_trace=getenv("JSRF_MOD_TRACE");
    if(path_trace && *path_trace) {
        trace_trigger=getenv("JSRF_MOD_TRACE_TRIGGER");
        if(!trace_trigger || !*trace_trigger)fail("JSRF mod trace requires an explicit arm file");
        trace=fopen(path_trace,"wb");if(!trace)fail("JSRF mod trace cannot be opened");
    }
    static struct PilotTitleMod result;
    result=(struct PilotTitleMod){PILOT_TITLE_MOD_ABI,(wide||trace)?transform:NULL,(wide||trace)?draw:NULL,
        (wide||frame_mode||trace)?present:NULL};
    return &result;
}
