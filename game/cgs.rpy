image y_cg2_bg:
    Transform("images/cg/y_cg2_bg1.png", zoom=res_ratio)
    6.0
    Transform("images/cg/y_cg2_bg2.png", zoom=res_ratio) with Dissolve(1)
    2
    Transform("images/cg/y_cg2_bg1.png", zoom=res_ratio) with Dissolve(1)
    1
    repeat
image y_cg2_base:
    Transform("images/cg/y_cg2_base.png", zoom=res_ratio)
image y_cg2_nochoc:
    Transform("images/cg/y_cg2_nochoc.png", zoom=res_ratio)
    on hide:
        linear 0.5 alpha 0
image y_cg2_details:
    Transform("images/cg/y_cg2_details.png", zoom=res_ratio)
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

image y_cg2_exp2:
    Transform("images/cg/y_cg2_exp2.png", zoom=res_ratio)
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0
image y_cg2_exp3:
    Transform("images/cg/y_cg2_exp3.png", zoom=res_ratio)
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_dust1:
    Transform("images/cg/y_cg2_dust1.png", zoom=res_ratio)
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust2:
    Transform("images/cg/y_cg2_dust2.png", zoom=res_ratio)
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust3:
    Transform("images/cg/y_cg2_dust3.png", zoom=res_ratio)
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    Transform("images/cg/y_cg2_dust4.png", zoom=res_ratio)
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

image n_cg1_bg:
    Transform("images/cg/n_cg1_bg.png", zoom=res_ratio)
image n_cg1_base:
    Transform("images/cg/n_cg1_base.png", zoom=res_ratio)

image n_cg1_exp1:
    Transform("images/cg/n_cg1_exp1.png", zoom=res_ratio)
image n_cg1_exp2:
    Transform("images/cg/n_cg1_exp2.png", zoom=res_ratio)
image n_cg1_exp3:
    Transform("images/cg/n_cg1_exp3.png", zoom=res_ratio)
image n_cg1_exp4:
    Transform("images/cg/n_cg1_exp4.png", zoom=res_ratio)
image n_cg1_exp5:
    Transform("images/cg/n_cg1_exp5.png", zoom=res_ratio)

image n_cg1b = LiveComposite((1280,720), (0,0), Transform("images/cg/n_cg1b.png", zoom=res_ratio), (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    size (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    size (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    size (30, 20)

image n_cg2_bg:
    Transform("images/cg/n_cg2_bg.png", zoom=res_ratio)
image n_cg2_base:
    Transform("images/cg/n_cg2_base.png", zoom=res_ratio)
image n_cg2_exp1:
    Transform("images/cg/n_cg2_exp1.png", zoom=res_ratio)
image n_cg2_exp2:
    Transform("images/cg/n_cg2_exp2.png", zoom=res_ratio)

image n_cg3_base:
    Transform("images/cg/n_cg3_base.png", zoom=res_ratio)
image n_cg3_cake:
    Transform("images/cg/n_cg3_cake.png", zoom=res_ratio)
image n_cg3_exp1:
    Transform("images/cg/n_cg3_exp1.png", zoom=res_ratio)
image n_cg3_exp2:
    Transform("images/cg/n_cg3_exp2.png", zoom=res_ratio)

image y_cg1_base:
    Transform("images/cg/y_cg1_base.png", zoom=res_ratio)
image y_cg1_exp1:
    Transform("images/cg/y_cg1_exp1.png", zoom=res_ratio)
image y_cg1_exp2:
    Transform("images/cg/y_cg1_exp2.png", zoom=res_ratio)
image y_cg1_exp3:
    Transform("images/cg/y_cg1_exp3.png", zoom=res_ratio)

image y_cg3_base:
    Transform("images/cg/y_cg3_base.png", zoom=res_ratio)
image y_cg3_exp1:
    Transform("images/cg/y_cg3_exp1.png", zoom=res_ratio)

image s_cg1:
    Transform("images/cg/s_cg1.png", zoom=res_ratio)

image s_cg2_base1:
    Transform("images/cg/s_cg2_base1.png", zoom=res_ratio)
image s_cg2_base2:
    Transform("images/cg/s_cg2_base2.png", zoom=res_ratio)
image s_cg2_exp1:
    Transform("images/cg/s_cg2_exp1.png", zoom=res_ratio)
image s_cg2_exp2:
    Transform("images/cg/s_cg2_exp2.png", zoom=res_ratio)
image s_cg2_exp3:
    Transform("images/cg/s_cg2_exp3.png", zoom=res_ratio)

image s_cg3:
    Transform("images/cg/s_cg3.png", zoom=res_ratio)

image s_kill_bg:
    subpixel True
    Transform("images/cg/s_kill_bg.png", zoom=res_ratio)

image s_kill:
    subpixel True
    "images/cg/s_kill.png"

image s_kill_bg2:
    subpixel True
    Transform("images/cg/s_kill_bg2.png", zoom=res_ratio)

image s_kill2:
    subpixel True
    "images/cg/s_kill2.png"

image y_kill = ConditionSwitch(
    "persistent.yuri_kill >= 1380", Transform("images/cg/y_kill/3a.png", zoom=res_ratio),
    "persistent.yuri_kill >= 1180", Transform("images/cg/y_kill/3c.png", zoom=res_ratio),
    "persistent.yuri_kill >= 1120", Transform("images/cg/y_kill/3b.png", zoom=res_ratio),
    "persistent.yuri_kill >= 920", Transform("images/cg/y_kill/3a.png", zoom=res_ratio),
    "persistent.yuri_kill >= 720", Transform("images/cg/y_kill/2c.png", zoom=res_ratio),
    "persistent.yuri_kill >= 660", Transform("images/cg/y_kill/2b.png", zoom=res_ratio),
    "persistent.yuri_kill >= 460", Transform("images/cg/y_kill/2a.png", zoom=res_ratio),
    "persistent.yuri_kill >= 260", Transform("images/cg/y_kill/1c.png", zoom=res_ratio),
    "persistent.yuri_kill >= 200", Transform("images/cg/y_kill/1b.png", zoom=res_ratio),
    "True", Transform("images/cg/y_kill/1a.png", zoom=res_ratio),

    )

transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        xalign 0.2 yalign 0.3 zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
