define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')

    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if renpy.mobile:
            if name in plus_persistent.real_file_path_names:
                plus_persistent.real_file_path_names.remove(name)
            combo_name = "characters/" + name + ".chr"
            if combo_name in plus_persistent.real_file_path_names:
                plus_persistent.real_file_path_names.remove(combo_name)
        else:
            import os
            try: 
                os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass
        
        if name == "monika":
            if plus_persistent.monika_delete_once == True:
                unlock("second_delete")
            plus_persistent.monika_delete_once = True

    def restore_all_characters():
        if renpy.mobile:
            if "characters/monika.chr" not in plus_persistent.real_file_path_names:
                plus_persistent.real_file_path_names.append("characters/monika.chr")
            if "characters/natsuki.chr" not in plus_persistent.real_file_path_names:
                plus_persistent.real_file_path_names.append("characters/natsuki.chr")
            if "characters/yuri.chr" not in plus_persistent.real_file_path_names:
                plus_persistent.real_file_path_names.append("characters/yuri.chr")
            if "characters/sayori.chr" not in plus_persistent.real_file_path_names:
                plus_persistent.real_file_path_names.append("characters/sayori.chr")
        else:
            try: renpy.file("../characters/monika.chr")
            except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            try: renpy.file("../characters/natsuki.chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
            try: renpy.file("../characters/yuri.chr")
            except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            try: renpy.file("../characters/sayori.chr")
            except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")
    def pause(time=None):
        global _windows_hidden
        skipping_state = config.allow_skipping 
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        config.allow_skipping = False
        renpy.pause(time)
        _windows_hidden = False
        config.allow_skipping = skipping_state
    def increment_yuri_kill():
        print("increment_yuri_kill()")
        if persistent.yuri_kill >= 1380:
            persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            persistent.yuri_kill = 260
        else:
            persistent.yuri_kill = 200



define audio.t1 = "<to 129.79545455 loop 20.70454545>bgm/1.ogg"
define audio.t2 = "<to 80.9579646 loop 4.49778761>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 to 80.9579646 loop 4.49778761>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g3.ogg"
define audio.t3 = "<to 100.343 loop 4.343>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 to 100.343 loop 4.343>bgm/3.ogg"
define audio.t3g3 = "<to 100.343 loop 4.343>bgm/3g2.ogg"
define audio.t3m = "<to 100.343 loop 4.343>bgm/3.ogg"
define audio.t4 = "<to 122.65 loop 19.45>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<to 91.6136364 loop 4.34090909>bgm/5.ogg"
define audio.t5b = "<to 91.6136364 loop 4.34090909>bgm/5.ogg"
define audio.t5c = "<to 91.6136364 loop 4.34090909>bgm/5.ogg"
define audio.t6 = "<to 86.1590909 loop 6.52272727>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<to 71.4364407 loop 2.28389831>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7g2.ogg"
define audio.t7g = "<loop 44.335>bgm/7g2.ogg"
define audio.t8 = "<to 96.0564516 loop 13.4758065>bgm/8.ogg"
define audio.t9 = "<to 70.25 loop 13.5833333>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<to 105.615854 loop 17.2621951>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"


image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = Transform("bg/splash-comp.png", zoom=res_ratio)
image end:
    truecenter
    Transform("gui/end.png", zoom=res_ratio)
image bg residential_day = Transform("bg/residential.png", zoom=res_ratio)
image bg class_day = Transform("bg/class.png", zoom=res_ratio)
image bg corridor = Transform("bg/corridor.png", zoom=res_ratio)
image bg club_day = Transform("bg/club.png", zoom=res_ratio)
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        Transform("bg/club-skill.png", zoom=res_ratio)
image bg closet = Transform("bg/closet.png", zoom=res_ratio)
image bg bedroom = Transform("bg/bedroom.png", zoom=res_ratio)
image bg sayori_bedroom = Transform("bg/sayori_bedroom.png", zoom=res_ratio)
image bg house = Transform("bg/house.png", zoom=res_ratio)
image bg kitchen = Transform("bg/kitchen.png", zoom=res_ratio)

image bg notebook = Transform("bg/notebook.png", zoom=res_ratio)
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0




image sayori 1 = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 1a = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 1b = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 1c = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 1d = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 1e = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 1f = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 1g = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 1h = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 1i = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 1j = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 1k = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 1l = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 1m = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 1n = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 1o = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 1p = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 1q = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 1r = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 1s = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 1t = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 1u = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 1v = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 1w = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 1x = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 1y = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori 2 = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 2a = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 2b = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 2c = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 2d = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 2e = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 2f = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 2g = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 2h = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 2i = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 2j = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 2k = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 2l = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 2m = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 2n = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 2o = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 2p = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 2q = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 2r = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 2s = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 2t = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 2u = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 2v = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 2w = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 2x = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 2y = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori 3 = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 3a = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 3b = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 3c = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 3d = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 3e = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 3f = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 3g = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 3h = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 3i = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 3j = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 3k = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 3l = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 3m = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 3n = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 3o = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 3p = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 3q = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 3r = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 3s = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 3t = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 3u = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 3v = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 3w = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 3x = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 3y = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori 4 = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 4a = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 4b = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 4c = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 4d = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 4e = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 4f = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 4g = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 4h = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 4i = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 4j = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 4k = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 4l = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 4m = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 4n = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 4o = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 4p = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 4q = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 4r = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 4s = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 4t = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 4u = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 4v = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 4w = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 4x = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 4y = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori 5 = Transform(im.Composite((1440, 1440), (0, 0), "sayori/3a.png"), zoom=res_ratio)
image sayori 5a = Transform(im.Composite((1440, 1440), (0, 0), "sayori/3a.png"), zoom=res_ratio)
image sayori 5b = Transform(im.Composite((1440, 1440), (0, 0), "sayori/3b.png"), zoom=res_ratio)
image sayori 5c = Transform(im.Composite((1440, 1440), (0, 0), "sayori/3c.png"), zoom=res_ratio)
image sayori 5d = Transform(im.Composite((1440, 1440), (0, 0), "sayori/3d.png"), zoom=res_ratio)

image sayori 1ba = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 1bb = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 1bc = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 1bd = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 1be = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 1bf = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 1bg = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 1bh = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 1bi = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 1bj = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 1bk = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 1bl = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 1bm = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 1bn = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 1bo = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 1bp = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 1bq = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 1br = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 1bs = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 1bt = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 1bu = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 1bv = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 1bw = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 1bx = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 1by = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori 2ba = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 2bb = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 2bc = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 2bd = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 2be = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 2bf = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 2bg = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 2bh = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 2bi = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 2bj = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 2bk = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 2bl = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 2bm = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 2bn = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 2bo = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 2bp = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 2bq = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 2br = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 2bs = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 2bt = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 2bu = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 2bv = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 2bw = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 2bx = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 2by = Transform(im.Composite((1440, 1440), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori 3ba = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 3bb = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 3bc = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 3bd = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 3be = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 3bf = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 3bg = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 3bh = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 3bi = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 3bj = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 3bk = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 3bl = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 3bm = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 3bn = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 3bo = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 3bp = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 3bq = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 3br = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 3bs = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 3bt = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 3bu = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 3bv = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 3bw = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 3bx = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 3by = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori 4ba = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png"), zoom=res_ratio)
image sayori 4bb = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png"), zoom=res_ratio)
image sayori 4bc = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png"), zoom=res_ratio)
image sayori 4bd = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png"), zoom=res_ratio)
image sayori 4be = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png"), zoom=res_ratio)
image sayori 4bf = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png"), zoom=res_ratio)
image sayori 4bg = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png"), zoom=res_ratio)
image sayori 4bh = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png"), zoom=res_ratio)
image sayori 4bi = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png"), zoom=res_ratio)
image sayori 4bj = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png"), zoom=res_ratio)
image sayori 4bk = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png"), zoom=res_ratio)
image sayori 4bl = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png"), zoom=res_ratio)
image sayori 4bm = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png"), zoom=res_ratio)
image sayori 4bn = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png"), zoom=res_ratio)
image sayori 4bo = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png"), zoom=res_ratio)
image sayori 4bp = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png"), zoom=res_ratio)
image sayori 4bq = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png"), zoom=res_ratio)
image sayori 4br = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png"), zoom=res_ratio)
image sayori 4bs = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png"), zoom=res_ratio)
image sayori 4bt = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png"), zoom=res_ratio)
image sayori 4bu = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png"), zoom=res_ratio)
image sayori 4bv = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png"), zoom=res_ratio)
image sayori 4bw = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png"), zoom=res_ratio)
image sayori 4bx = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png"), zoom=res_ratio)
image sayori 4by = Transform(im.Composite((1440, 1440), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png"), zoom=res_ratio)

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat


image natsuki 11 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 1a = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 1b = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 1c = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 1d = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 1e = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 1f = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 1g = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 1h = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 1i = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 1j = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 1k = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 1l = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 1m = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 1n = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 1o = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 1p = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 1q = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 1r = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 1s = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 1t = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 1u = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 1v = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 1w = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 1x = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 1y = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 1z = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 21 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 2a = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 2b = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 2c = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 2d = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 2e = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 2f = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 2g = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 2h = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 2i = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 2j = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 2k = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 2l = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 2m = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 2n = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 2o = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 2p = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 2q = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 2r = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 2s = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 2t = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 2u = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 2v = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 2w = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 2x = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 2y = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 2z = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 31 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 3a = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 3b = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 3c = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 3d = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 3e = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 3f = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 3g = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 3h = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 3i = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 3j = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 3k = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 3l = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 3m = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 3n = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 3o = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 3p = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 3q = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 3r = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 3s = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 3t = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 3u = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 3v = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 3w = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 3x = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 3y = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 3z = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 41 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 4a = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 4b = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 4c = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 4d = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 4e = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 4f = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 4g = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 4h = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 4i = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 4j = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 4k = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 4l = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 4m = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 4n = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 4o = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 4p = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 4q = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 4r = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 4s = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 4t = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 4u = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 4v = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 4w = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 4x = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 4y = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 4z = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 12 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png"), zoom=res_ratio)
image natsuki 12a = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png"), zoom=res_ratio)
image natsuki 12b = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png"), zoom=res_ratio)
image natsuki 12c = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png"), zoom=res_ratio)
image natsuki 12d = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png"), zoom=res_ratio)
image natsuki 12e = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png"), zoom=res_ratio)
image natsuki 12f = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png"), zoom=res_ratio)
image natsuki 12g = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png"), zoom=res_ratio)
image natsuki 12h = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png"), zoom=res_ratio)
image natsuki 12i = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png"), zoom=res_ratio)

image natsuki 42 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png"), zoom=res_ratio)
image natsuki 42a = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png"), zoom=res_ratio)
image natsuki 42b = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png"), zoom=res_ratio)
image natsuki 42c = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png"), zoom=res_ratio)
image natsuki 42d = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png"), zoom=res_ratio)
image natsuki 42e = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png"), zoom=res_ratio)
image natsuki 42f = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png"), zoom=res_ratio)
image natsuki 42g = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png"), zoom=res_ratio)
image natsuki 42h = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png"), zoom=res_ratio)
image natsuki 42i = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png"), zoom=res_ratio)

image natsuki 51 = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/1t.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5a = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/a.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5b = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/b.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5c = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/c.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5d = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/d.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5e = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/e.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5f = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/f.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5g = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/g.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5h = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/h.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5i = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/i.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5j = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/j.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5k = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/k.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5l = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/l.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5m = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/m.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5n = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/n.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5o = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/o.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5p = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/p.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5q = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/q.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5r = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/r.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5s = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/s.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5t = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/t.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5u = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/u.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5v = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/v.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5w = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/w.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5x = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/x.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5y = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/y.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)
image natsuki 5z = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/z.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)


image natsuki 1ba = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 1bb = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 1bc = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 1bd = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 1be = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 1bf = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 1bg = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 1bh = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 1bi = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 1bj = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 1bk = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 1bl = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 1bm = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 1bn = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 1bo = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 1bp = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 1bq = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 1br = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 1bs = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 1bt = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 1bu = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 1bv = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 1bw = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 1bx = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 1by = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 1bz = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 2ba = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 2bb = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 2bc = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 2bd = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 2be = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 2bf = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 2bg = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 2bh = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 2bi = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 2bj = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 2bk = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 2bl = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 2bm = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 2bn = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 2bo = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 2bp = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 2bq = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 2br = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 2bs = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 2bt = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 2bu = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 2bv = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 2bw = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 2bx = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 2by = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 2bz = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 3ba = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 3bb = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 3bc = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 3bd = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 3be = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 3bf = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 3bg = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 3bh = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 3bi = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 3bj = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 3bk = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 3bl = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 3bm = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 3bn = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 3bo = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 3bp = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 3bq = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 3br = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 3bs = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 3bt = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 3bu = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 3bv = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 3bw = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 3bx = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 3by = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 3bz = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 4ba = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png"), zoom=res_ratio)
image natsuki 4bb = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png"), zoom=res_ratio)
image natsuki 4bc = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png"), zoom=res_ratio)
image natsuki 4bd = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png"), zoom=res_ratio)
image natsuki 4be = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png"), zoom=res_ratio)
image natsuki 4bf = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png"), zoom=res_ratio)
image natsuki 4bg = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png"), zoom=res_ratio)
image natsuki 4bh = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png"), zoom=res_ratio)
image natsuki 4bi = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png"), zoom=res_ratio)
image natsuki 4bj = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png"), zoom=res_ratio)
image natsuki 4bk = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png"), zoom=res_ratio)
image natsuki 4bl = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png"), zoom=res_ratio)
image natsuki 4bm = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png"), zoom=res_ratio)
image natsuki 4bn = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png"), zoom=res_ratio)
image natsuki 4bo = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png"), zoom=res_ratio)
image natsuki 4bp = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png"), zoom=res_ratio)
image natsuki 4bq = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png"), zoom=res_ratio)
image natsuki 4br = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png"), zoom=res_ratio)
image natsuki 4bs = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png"), zoom=res_ratio)
image natsuki 4bt = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png"), zoom=res_ratio)
image natsuki 4bu = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png"), zoom=res_ratio)
image natsuki 4bv = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png"), zoom=res_ratio)
image natsuki 4bw = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png"), zoom=res_ratio)
image natsuki 4bx = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png"), zoom=res_ratio)
image natsuki 4by = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png"), zoom=res_ratio)
image natsuki 4bz = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png"), zoom=res_ratio)

image natsuki 12ba = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png"), zoom=res_ratio)
image natsuki 12bb = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png"), zoom=res_ratio)
image natsuki 12bc = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png"), zoom=res_ratio)
image natsuki 12bd = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png"), zoom=res_ratio)
image natsuki 12be = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png"), zoom=res_ratio)
image natsuki 12bf = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png"), zoom=res_ratio)
image natsuki 12bg = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png"), zoom=res_ratio)
image natsuki 12bh = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png"), zoom=res_ratio)
image natsuki 12bi = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png"), zoom=res_ratio)

image natsuki 42ba = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png"), zoom=res_ratio)
image natsuki 42bb = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png"), zoom=res_ratio)
image natsuki 42bc = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png"), zoom=res_ratio)
image natsuki 42bd = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png"), zoom=res_ratio)
image natsuki 42be = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png"), zoom=res_ratio)
image natsuki 42bf = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png"), zoom=res_ratio)
image natsuki 42bg = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png"), zoom=res_ratio)
image natsuki 42bh = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png"), zoom=res_ratio)
image natsuki 42bi = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png"), zoom=res_ratio)

image natsuki 5ba = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/a.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bb = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/b.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bc = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/c.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bd = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/d.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5be = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/e.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bf = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/f.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bg = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/g.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bh = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/h.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bi = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/i.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bj = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/j.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bk = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/k.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bl = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/l.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bm = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/m.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bn = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/n.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bo = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/o.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bp = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/p.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bq = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/q.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5br = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/r.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bs = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/s.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bt = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/t.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bu = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/u.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bv = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/v.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bw = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/w.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bx = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/x.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5by = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/y.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)
image natsuki 5bz = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/z.png", (0, 0), "natsuki/3b.png"), zoom=res_ratio)


image natsuki 1 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 2 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 3 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 4 = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png"), zoom=res_ratio)
image natsuki 5 = Transform(im.Composite((1440, 1440), (26, 33), "natsuki/1t.png", (0, 0), "natsuki/3.png"), zoom=res_ratio)

image natsuki mouth = LiveComposite((1440, 1440), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    Transform("natsuki/ghost1.png", zoom=res_ratio)
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Transform("natsuki/ghost2.png", zoom=res_ratio)
image natsuki ghost3 = Transform("natsuki/ghost3.png", zoom=res_ratio)
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = Transform(im.Composite((1440, 1440), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png"), zoom=res_ratio)
image natsuki vomit = Transform("natsuki/vomit.png", zoom=res_ratio)

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"


image yuri 1 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png"), zoom=res_ratio)
image yuri 2 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png"), zoom=res_ratio)
image yuri 3 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png"), zoom=res_ratio)
image yuri 4 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png"), zoom=res_ratio)

image yuri 1a = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png"), zoom=res_ratio)
image yuri 1b = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png"), zoom=res_ratio)
image yuri 1c = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png"), zoom=res_ratio)
image yuri 1d = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png"), zoom=res_ratio)
image yuri 1e = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png"), zoom=res_ratio)
image yuri 1f = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png"), zoom=res_ratio)
image yuri 1g = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png"), zoom=res_ratio)
image yuri 1h = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png"), zoom=res_ratio)
image yuri 1i = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png"), zoom=res_ratio)
image yuri 1j = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png"), zoom=res_ratio)
image yuri 1k = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png"), zoom=res_ratio)
image yuri 1l = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png"), zoom=res_ratio)
image yuri 1m = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png"), zoom=res_ratio)
image yuri 1n = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png"), zoom=res_ratio)
image yuri 1o = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png"), zoom=res_ratio)
image yuri 1p = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png"), zoom=res_ratio)
image yuri 1q = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png"), zoom=res_ratio)
image yuri 1r = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png"), zoom=res_ratio)
image yuri 1s = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png"), zoom=res_ratio)
image yuri 1t = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png"), zoom=res_ratio)
image yuri 1u = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png"), zoom=res_ratio)
image yuri 1v = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png"), zoom=res_ratio)
image yuri 1w = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png"), zoom=res_ratio)

image yuri 1y1 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png"), zoom=res_ratio)
image yuri 1y2 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png"), zoom=res_ratio)
image yuri 1y3 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png"), zoom=res_ratio)
image yuri 1y4 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png"), zoom=res_ratio)
image yuri 1y5 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png"), zoom=res_ratio)
image yuri 1y6 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png"), zoom=res_ratio)
image yuri 1y7 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png"), zoom=res_ratio)

image yuri 2a = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png"), zoom=res_ratio)
image yuri 2b = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png"), zoom=res_ratio)
image yuri 2c = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png"), zoom=res_ratio)
image yuri 2d = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png"), zoom=res_ratio)
image yuri 2e = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png"), zoom=res_ratio)
image yuri 2f = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png"), zoom=res_ratio)
image yuri 2g = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png"), zoom=res_ratio)
image yuri 2h = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png"), zoom=res_ratio)
image yuri 2i = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png"), zoom=res_ratio)
image yuri 2j = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png"), zoom=res_ratio)
image yuri 2k = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png"), zoom=res_ratio)
image yuri 2l = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png"), zoom=res_ratio)
image yuri 2m = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png"), zoom=res_ratio)
image yuri 2n = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png"), zoom=res_ratio)
image yuri 2o = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png"), zoom=res_ratio)
image yuri 2p = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png"), zoom=res_ratio)
image yuri 2q = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png"), zoom=res_ratio)
image yuri 2r = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png"), zoom=res_ratio)
image yuri 2s = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png"), zoom=res_ratio)
image yuri 2t = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png"), zoom=res_ratio)
image yuri 2u = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png"), zoom=res_ratio)
image yuri 2v = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png"), zoom=res_ratio)
image yuri 2w = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png"), zoom=res_ratio)

image yuri 2y1 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png"), zoom=res_ratio)
image yuri 2y2 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png"), zoom=res_ratio)
image yuri 2y3 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png"), zoom=res_ratio)
image yuri 2y4 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png"), zoom=res_ratio)
image yuri 2y5 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png"), zoom=res_ratio)
image yuri 2y6 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png"), zoom=res_ratio)
image yuri 2y7 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png"), zoom=res_ratio)

image yuri 3a = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png"), zoom=res_ratio)
image yuri 3b = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png"), zoom=res_ratio)
image yuri 3c = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png"), zoom=res_ratio)
image yuri 3d = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png"), zoom=res_ratio)
image yuri 3e = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png"), zoom=res_ratio)
image yuri 3f = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png"), zoom=res_ratio)
image yuri 3g = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png"), zoom=res_ratio)
image yuri 3h = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png"), zoom=res_ratio)
image yuri 3i = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png"), zoom=res_ratio)
image yuri 3j = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png"), zoom=res_ratio)
image yuri 3k = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png"), zoom=res_ratio)
image yuri 3l = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png"), zoom=res_ratio)
image yuri 3m = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png"), zoom=res_ratio)
image yuri 3n = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png"), zoom=res_ratio)
image yuri 3o = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png"), zoom=res_ratio)
image yuri 3p = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png"), zoom=res_ratio)
image yuri 3q = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png"), zoom=res_ratio)
image yuri 3r = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png"), zoom=res_ratio)
image yuri 3s = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png"), zoom=res_ratio)
image yuri 3t = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png"), zoom=res_ratio)
image yuri 3u = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png"), zoom=res_ratio)
image yuri 3v = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png"), zoom=res_ratio)
image yuri 3w = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png"), zoom=res_ratio)

image yuri 3y1 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png"), zoom=res_ratio)
image yuri 3y2 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png"), zoom=res_ratio)
image yuri 3y3 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png"), zoom=res_ratio)
image yuri 3y4 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png"), zoom=res_ratio)
image yuri 3y5 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png"), zoom=res_ratio)
image yuri 3y6 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png"), zoom=res_ratio)
image yuri 3y7 = Transform(im.Composite((1440, 1440), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png"), zoom=res_ratio)

image yuri 4a = Transform(im.Composite((1440, 1440), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png"), zoom=res_ratio)
image yuri 4b = Transform(im.Composite((1440, 1440), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png"), zoom=res_ratio)
image yuri 4c = Transform(im.Composite((1440, 1440), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png"), zoom=res_ratio)
image yuri 4d = Transform(im.Composite((1440, 1440), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png"), zoom=res_ratio)
image yuri 4e = Transform(im.Composite((1440, 1440), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png"), zoom=res_ratio)

image yuri 1ba = Transform(im.Composite((1440, 1440), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bb = Transform(im.Composite((1440, 1440), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bc = Transform(im.Composite((1440, 1440), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bd = Transform(im.Composite((1440, 1440), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1be = Transform(im.Composite((1440, 1440), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bf = Transform(im.Composite((1440, 1440), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bg = Transform(im.Composite((1440, 1440), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bh = Transform(im.Composite((1440, 1440), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bi = Transform(im.Composite((1440, 1440), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bj = Transform(im.Composite((1440, 1440), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bk = Transform(im.Composite((1440, 1440), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bl = Transform(im.Composite((1440, 1440), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bm = Transform(im.Composite((1440, 1440), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bn = Transform(im.Composite((1440, 1440), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bo = Transform(im.Composite((1440, 1440), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bp = Transform(im.Composite((1440, 1440), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bq = Transform(im.Composite((1440, 1440), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1br = Transform(im.Composite((1440, 1440), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bs = Transform(im.Composite((1440, 1440), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bt = Transform(im.Composite((1440, 1440), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bu = Transform(im.Composite((1440, 1440), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bv = Transform(im.Composite((1440, 1440), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)
image yuri 1bw = Transform(im.Composite((1440, 1440), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png"), zoom=res_ratio)

image yuri 2ba = Transform(im.Composite((1440, 1440), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bb = Transform(im.Composite((1440, 1440), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bc = Transform(im.Composite((1440, 1440), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bd = Transform(im.Composite((1440, 1440), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2be = Transform(im.Composite((1440, 1440), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bf = Transform(im.Composite((1440, 1440), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bg = Transform(im.Composite((1440, 1440), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bh = Transform(im.Composite((1440, 1440), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bi = Transform(im.Composite((1440, 1440), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bj = Transform(im.Composite((1440, 1440), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bk = Transform(im.Composite((1440, 1440), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bl = Transform(im.Composite((1440, 1440), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bm = Transform(im.Composite((1440, 1440), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bn = Transform(im.Composite((1440, 1440), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bo = Transform(im.Composite((1440, 1440), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bp = Transform(im.Composite((1440, 1440), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bq = Transform(im.Composite((1440, 1440), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2br = Transform(im.Composite((1440, 1440), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bs = Transform(im.Composite((1440, 1440), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bt = Transform(im.Composite((1440, 1440), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bu = Transform(im.Composite((1440, 1440), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bv = Transform(im.Composite((1440, 1440), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 2bw = Transform(im.Composite((1440, 1440), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)

image yuri 3ba = Transform(im.Composite((1440, 1440), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bb = Transform(im.Composite((1440, 1440), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bc = Transform(im.Composite((1440, 1440), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bd = Transform(im.Composite((1440, 1440), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3be = Transform(im.Composite((1440, 1440), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bf = Transform(im.Composite((1440, 1440), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bg = Transform(im.Composite((1440, 1440), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bh = Transform(im.Composite((1440, 1440), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bi = Transform(im.Composite((1440, 1440), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bj = Transform(im.Composite((1440, 1440), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bk = Transform(im.Composite((1440, 1440), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bl = Transform(im.Composite((1440, 1440), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bm = Transform(im.Composite((1440, 1440), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bn = Transform(im.Composite((1440, 1440), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bo = Transform(im.Composite((1440, 1440), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bp = Transform(im.Composite((1440, 1440), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bq = Transform(im.Composite((1440, 1440), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3br = Transform(im.Composite((1440, 1440), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bs = Transform(im.Composite((1440, 1440), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bt = Transform(im.Composite((1440, 1440), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bu = Transform(im.Composite((1440, 1440), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bv = Transform(im.Composite((1440, 1440), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)
image yuri 3bw = Transform(im.Composite((1440, 1440), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png"), zoom=res_ratio)

image yuri 4ba = Transform(im.Composite((1440, 1440), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png"), zoom=res_ratio)
image yuri 4bb = Transform(im.Composite((1440, 1440), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png"), zoom=res_ratio)
image yuri 4bc = Transform(im.Composite((1440, 1440), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png"), zoom=res_ratio)
image yuri 4bd = Transform(im.Composite((1440, 1440), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png"), zoom=res_ratio)
image yuri 4be = Transform(im.Composite((1440, 1440), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png"), zoom=res_ratio)

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = Transform("yuri/stab/1.png", zoom=res_ratio)
image yuri stab_2 = Transform("yuri/stab/2.png", zoom=res_ratio)
image yuri stab_3 = Transform("yuri/stab/3.png", zoom=res_ratio)
image yuri stab_4 = Transform("yuri/stab/4.png", zoom=res_ratio)
image yuri stab_5 = Transform("yuri/stab/5.png", zoom=res_ratio)
image yuri stab_6 = Transform(LiveComposite((1440,1440), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png"), zoom=res_ratio)

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = Transform(LiveComposite((1440, 1440), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2"), zoom=res_ratio)
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    Transform("yuri/0a.png", zoom=res_ratio)
    pause 0.1
    Transform("yuri/0b.png", zoom=res_ratio)
    pause 0.5
    Transform("yuri/0a.png", zoom=res_ratio)
    pause 0.3
    Transform("yuri/0b.png", zoom=res_ratio)
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), Transform("yuri/eyes1.png", zoom=res_ratio), (0, 0), "yuripupils")

image yuri eyes_base = Transform("yuri/eyes1.png", zoom=res_ratio)

image yuripupils:
    Transform("yuri/eyes2.png", zoom=res_ratio)
    yuripupils_move

image yuri cuts = Transform("yuri/cuts.png", zoom=res_ratio)

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"


image monika 1 = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 2 = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 3 = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 4 = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 5 = Transform(im.Composite((1440, 1440), (0, 0), "monika/3a.png"), zoom=res_ratio)

image monika 1a = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 1b = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png"), zoom=res_ratio)
image monika 1c = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png"), zoom=res_ratio)
image monika 1d = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png"), zoom=res_ratio)
image monika 1e = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png"), zoom=res_ratio)
image monika 1f = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png"), zoom=res_ratio)
image monika 1g = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png"), zoom=res_ratio)
image monika 1h = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png"), zoom=res_ratio)
image monika 1i = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png"), zoom=res_ratio)
image monika 1j = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png"), zoom=res_ratio)
image monika 1k = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png"), zoom=res_ratio)
image monika 1l = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png"), zoom=res_ratio)
image monika 1m = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png"), zoom=res_ratio)
image monika 1n = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png"), zoom=res_ratio)
image monika 1o = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png"), zoom=res_ratio)
image monika 1p = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png"), zoom=res_ratio)
image monika 1q = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png"), zoom=res_ratio)
image monika 1r = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png"), zoom=res_ratio)

image monika 2a = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 2b = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png"), zoom=res_ratio)
image monika 2c = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png"), zoom=res_ratio)
image monika 2d = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png"), zoom=res_ratio)
image monika 2e = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png"), zoom=res_ratio)
image monika 2f = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png"), zoom=res_ratio)
image monika 2g = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png"), zoom=res_ratio)
image monika 2h = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png"), zoom=res_ratio)
image monika 2i = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png"), zoom=res_ratio)
image monika 2j = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png"), zoom=res_ratio)
image monika 2k = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png"), zoom=res_ratio)
image monika 2l = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png"), zoom=res_ratio)
image monika 2m = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png"), zoom=res_ratio)
image monika 2n = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png"), zoom=res_ratio)
image monika 2o = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png"), zoom=res_ratio)
image monika 2p = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png"), zoom=res_ratio)
image monika 2q = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png"), zoom=res_ratio)
image monika 2r = Transform(im.Composite((1440, 1440), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png"), zoom=res_ratio)

image monika 3a = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 3b = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png"), zoom=res_ratio)
image monika 3c = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png"), zoom=res_ratio)
image monika 3d = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png"), zoom=res_ratio)
image monika 3e = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png"), zoom=res_ratio)
image monika 3f = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png"), zoom=res_ratio)
image monika 3g = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png"), zoom=res_ratio)
image monika 3h = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png"), zoom=res_ratio)
image monika 3i = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png"), zoom=res_ratio)
image monika 3j = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png"), zoom=res_ratio)
image monika 3k = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png"), zoom=res_ratio)
image monika 3l = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png"), zoom=res_ratio)
image monika 3m = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png"), zoom=res_ratio)
image monika 3n = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png"), zoom=res_ratio)
image monika 3o = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png"), zoom=res_ratio)
image monika 3p = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png"), zoom=res_ratio)
image monika 3q = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png"), zoom=res_ratio)
image monika 3r = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png"), zoom=res_ratio)

image monika 4a = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png"), zoom=res_ratio)
image monika 4b = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png"), zoom=res_ratio)
image monika 4c = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png"), zoom=res_ratio)
image monika 4d = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png"), zoom=res_ratio)
image monika 4e = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png"), zoom=res_ratio)
image monika 4f = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png"), zoom=res_ratio)
image monika 4g = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png"), zoom=res_ratio)
image monika 4h = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png"), zoom=res_ratio)
image monika 4i = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png"), zoom=res_ratio)
image monika 4j = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png"), zoom=res_ratio)
image monika 4k = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png"), zoom=res_ratio)
image monika 4l = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png"), zoom=res_ratio)
image monika 4m = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png"), zoom=res_ratio)
image monika 4n = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png"), zoom=res_ratio)
image monika 4o = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png"), zoom=res_ratio)
image monika 4p = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png"), zoom=res_ratio)
image monika 4q = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png"), zoom=res_ratio)
image monika 4r = Transform(im.Composite((1440, 1440), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png"), zoom=res_ratio)

image monika 5a = Transform(im.Composite((1440, 1440), (0, 0), "monika/3a.png"), zoom=res_ratio)
image monika 5b = Transform(im.Composite((1440, 1440), (0, 0), "monika/3b.png"), zoom=res_ratio)

image monika 1q_complete = "monika/1q_complete.png"

image monika g1:
    Transform("monika/g1.png", zoom=res_ratio)
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat


default dialogue_prefix = '"'
default dialogue_suffix = '"'

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None
default persistent.stream_check_override = None
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None
default in_side_story = False
default persistent.first_boot = True
default persistent.seen_bios = False
default hide_quick_skip_and_auto = False

default persistent.reduce_motion = False
default persistent.use_alt_poem_font = False
default persistent.reduce_transparency = False
default persistent.high_contrast = False



default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"



default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]


default poemwinner = ['sayori', 'sayori', 'sayori']


default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False


default n_read3 = False
default y_read3 = False


default n_poemearly = False


default poemsread = 0



default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0



default n_exclusivewatched = False
default y_exclusivewatched = False


default y_gave = False
default y_ranaway = False


default ch1_choice = "sayori"


default help_sayori = None
default help_monika = None


default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
