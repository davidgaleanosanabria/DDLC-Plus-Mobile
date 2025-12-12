init python:
    menu_trans_time = 1
    splash_message_default = "This game is not suitable for children\nor those who are easily disturbed."
    splash_messages = [
"You are my sunshine,\nMy only sunshine",
"I missed you.",
"Play with me",
"It's just a game, mostly.",
"This game is not suitable for children\nor those who are easily disturbed?",
"sdfasdklfgsdfgsgoinrfoenlvbd",
"null",
"I have granted kids to hell",
"PM died for this.",
"It was only partially your fault.",
"This game is not suitable for children\nor those who are easily dismembered.",
"Don't forget to backup Monika's character file."
]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:

    topleft
    Transform("gui/menu_bg.png", zoom=res_ratio)
    menu_bg_move

image game_menu_bg:

    topleft
    Transform("gui/menu_bg.png", zoom=res_ratio)
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    Transform("gui/menu_art_m.png", zoom=res_ratio)
    xcenter 1000
    ycenter 640
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    Transform("gui/menu_art_m_ghost.png", zoom=res_ratio)
    xcenter 1000
    ycenter 640
    menu_art_move(1.00, 1000, 1.00)

image menu_art_m_ghost_single = "gui/menu_art_m_ghost.png"

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    Transform("gui/overlay/main_menu.png", zoom=res_ratio)
    menu_nav_move

image game_nav:
    Transform("gui/overlay/game_menu.png", zoom=res_ratio)

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:

    pause 2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleTimeOffset=2.481, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft

    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset (0 if persistent.reduce_motion else -100) yoffset (0 if persistent.reduce_motion else -100)
        repeat
    parallel:
        on show:
            ypos 0
            time 0.65
            ease_cubic 2.5 ypos -500

transform menu_bg_loop:

    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset (0 if persistent.reduce_motion else -100) yoffset (0 if persistent.reduce_motion else -100)
        repeat

transform menu_logo_move:
    subpixel True
    on show:
        yoffset -300
        time 1.925
        easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    on show:
        xoffset -500
        time 1.5
        easein_quint 1 xoffset 0

transform menu_fadeout:
    on show:
        easeout 0.75 alpha 0
        time 2.481
        alpha 0.4
        linear 0.5 alpha 0
    on replace:
        alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    on show:
        yoffset 0 + (1200 * z)
        xoffset (740 - x) * z * 0.5
        zoom z2 * 0.75
        time 1.0
        parallel:
            ease 1.75 yoffset 0
        parallel:
            pause 0.75
            ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    Transform("bg/splash-comp.png", zoom=res_ratio) with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = Transform("bg/warning.png", zoom=res_ratio)
image tos2 = Transform("bg/warning2.png", zoom=res_ratio)

label splashscreen:
    $ startup_settings_apply()
    $ copy_old_seen()
    $ check_reapply_preferences()

    $ gui.SetPreference("text_scale", preferences.text_scale)

    if renpy.mobile:
        $ apply_plus_content_purchase()

    if _return == "DDLC" or persistent.first_boot == True:
        $ persistent.first_boot = False
        jump DDLC_splashscreen
    else:
        call desktop_start

label DDLC_splashscreen:

    if renpy.mobile:
        if renpy.ios:
            $ jukebox_function_ios_stop()
        else:
            $ jukebox_function_android_stop()


    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().decode("utf-8").replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:





        persistent.stream_check_override = None

        if "-stream" in sys.argv:
            persistent.stream_check_override = True
        elif "-nostream" in sys.argv:
            persistent.stream_check_override = False      

    $ in_side_story = False
    $ enable_autofocus = False


    if not renpy.mobile:
        python:
            firstrun = ""
            try:
                firstrun = renpy.file("firstrun").read(1)
            except:
                with open(config.basedir + "/game/firstrun", "wb") as f:
                    pass
        if not firstrun:
            if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
                $ quick_menu = False
                scene black
                menu:
                    "A previous save file has been found. Would you like to delete your save data and start over?"
                    "Yes, delete my existing data.":
                        "Deleting save data...{nw}"
                        python:
                            delete_all_saves()
                            renpy.loadsave.location.unlink_persistent()
                            renpy.persistent.should_save_persistent = False
                            save_preferences_to_external()
                            renpy.utter_restart()
                    "No, continue where I left off.":
                        $ restore_relevant_characters()

            python:
                if not firstrun:
                    try:
                        with open(config.basedir + "/game/firstrun", "w") as f:
                            f.write("1")
                    except:
                        renpy.jump("readonly")

        if config.version != persistent.oldversion:
            $ restore_relevant_characters()
            $ persistent.oldversion = config.version
            $ renpy.save_persistent()

    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "This game is not suitable for children or those who are easily disturbed."
        "{i}Doki Doki Literature Club{/i} features sensitive content and themes that may be disturbing for some players and should be approached with caution."
        "In-game content warnings for such material can be enabled in the Settings menu at any time."
        "The Settings menu also contains a link to an external webpage that lists all content warnings."
        menu:
            "Would you like a brief, categorical overview of those content warnings now? (Contains moderate thematic spoilers.)"
            "Yes (contains spoilers)":
                "Thank you for your interest in {i}Doki Doki Literature Club{/i}."
                "{i}Doki Doki Literature Club{/i} is a horror game. Please do not take this lightly."
                "Here are some of the themes that are prominently featured in this game:"
                "Mental Illness: Symptoms of depression (hopelessness, isolation, self-blame), anxiety, disordered eating"
                "Death/Suicide: Depictions of hanging, stabbing, murder, self-harm, suicidal thoughts"
                "Abuse: Parental abuse, emotional abuse (gaslighting, guilting/shaming/blaming the player)"
                "Gore: Blood, body damage, decomposition, vomit, eye manipulation"
                "Sensory Horror: Unsettling audio (wet, squelching sounds) and visual disruptions (glitching, flickering, flashing, color changes)"
                "These themes are portrayed realistically and may be too distressing for some players to comfortably tolerate."
                "For more information on how these topics are included in the game, please view the Full Content Warnings link in the Settings menu."
                "You may review the Full Content Warnings before you play, or keep it as a resource alongside enabling the in-game content warnings."
                "Thank you for considering these extra steps to enjoy {i}DDLC{/i} in a way that is right for you."
                pause 1.0
            "No":
                pause 1.0
        menu:
            "By playing {i}Doki Doki Literature Club{/i}, you agree that you have noted the game's age rating in your region, and you consent to your exposure of highly disturbing content."
            "I agree.":
                pass
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white


    python:
        s_kill_early = None
        if persistent.playthrough == 0:
            if renpy.mobile:
                if "characters/sayori.chr" not in plus_persistent.real_file_path_names:
                    s_kill_early = True
            else:
                try: renpy.file("../characters/sayori.chr")
                except: s_kill_early = True
        if not s_kill_early:
            if persistent.playthrough <= 2 and persistent.playthrough != 0:
                if renpy.mobile:
                    if "characters/monika.chr" not in plus_persistent.real_file_path_names:
                        plus_persistent.real_file_path_names.append("characters/monika.chr")
                else:
                    try: renpy.file("../characters/monika.chr")
                    except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 2 or persistent.playthrough == 4:
                if renpy.mobile:
                    if "characters/natsuki.chr" not in plus_persistent.real_file_path_names:
                        plus_persistent.real_file_path_names.append("characters/natsuki.chr")
                    if "characters/yuri.chr" not in plus_persistent.real_file_path_names:
                        plus_persistent.real_file_path_names.append("characters/yuri.chr")
                else:
                    try: renpy.file("../characters/natsuki.chr")
                    except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                    try: renpy.file("../characters/yuri.chr")
                    except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 4:
                if renpy.mobile:
                    if "characters/sayori.chr" not in plus_persistent.real_file_path_names:
                        plus_persistent.real_file_path_names.append("characters/sayori.chr")
                else:
                    try: renpy.file("../characters/sayori.chr")
                    except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ unlock("special_ghost")
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return


    if s_kill_early:
        show black
        play music "bgm/s_kill_early.ogg"
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        scene white
        show expression Transform("images/cg/s_kill_early.png", zoom=res_ratio):
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Now everyone can be happy.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            600
            linear 60 alpha 0.5
        pause
        $ renpy.quit()


    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message!t]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

label after_load:
    $ renpy.block_rollback()
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ increment_yuri_kill()
        jump expression persistent.autoload

    elif anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"
        $ m_name = "Monika"
        show monika 1 at t11
        if persistent.playername == "":
            m "You're so funny."
        else:
            m "You're so funny, [persistent.playername]."
        $ save_preferences_to_external()
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label autoload_yurikill:
    $ increment_yuri_kill()
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show menu_art_m_ghost_single:
            xpos -100 ypos -100 zoom 3.5 * res_ratio
        pause 0.01

    if renpy.mobile:
        pause 0.2
        hide menu_art_m_ghost_single
        jump desktop
    else:
        return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.quit()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
