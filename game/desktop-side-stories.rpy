





screen virtual_desktop_sidestories_app():

    on "show" action Function(clear_notification, "sidestory")

    style_prefix "virtual_desktop"

    use virtual_desktop_app_window("Side Stories", taskbar_icon="desktop_SideStories_H"):

        key ['K_ESCAPE'] action NullAction()

        frame:
            xpadding 30
            viewport id "desktop_popup_canvas":
                draggable True mousewheel True
                xalign 0.5
                has vbox
                spacing 10

                if True in plus_persistent.side_stories_unlocked:
                    null height 50
                else:
                    null height 200

                text "The Side Stories are stories of friendship that are unrelated to the events of the main game. To get all six Side Stories, try writing poems for different characters and viewing their special scenes in DDLC.":
                    text_align 0.5




                if plus_persistent.side_stories_unlocked[0]:
                    grid 2 1:
                        style_prefix "sidestory"
                        align (0.5, 1)

                        button:
                            if plus_persistent.side_stories_unlocked[0]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "sm1"), Hide())]
                                use sidestory_image("TRUST", "sideStory_trust_UL", 1)
                            else:
                                action NullAction()
                                use sidestory_image("TRUST", "sideStory_trust_L", 1)
                        button:
                            if plus_persistent.side_stories_unlocked[1]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "sm3"), Hide())]
                                use sidestory_image("TRUST", "sideStory_trust_UL", 2)
                            else:
                                action NullAction()
                                use sidestory_image("TRUST", "sideStory_trust_L", 2)


                if plus_persistent.side_stories_unlocked[2]:
                    grid 2 1:
                        style_prefix "sidestory"
                        align (0.5, 1)

                        button:
                            if plus_persistent.side_stories_unlocked[2]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "sy1"), Hide())]
                                use sidestory_image("UNDERSTANDING", "sideStory_understanding_UL", 1)
                            else:
                                action NullAction()
                                use sidestory_image("UNDERSTANDING", "sideStory_understanding_L", 1)
                        button:
                            if plus_persistent.side_stories_unlocked[3]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "sy3"), Hide())]
                                use sidestory_image("UNDERSTANDING", "sideStory_understanding_UL", 2)
                            else:
                                action NullAction()
                                use sidestory_image("UNDERSTANDING", "sideStory_understanding_L", 2)


                if plus_persistent.side_stories_unlocked[4]:
                    grid 2 1:
                        style_prefix "sidestory"
                        align (0.5, 1)

                        button:
                            if plus_persistent.side_stories_unlocked[4]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "nm1"), Hide())]
                                use sidestory_image("RESPECT", "sideStory_respect_UL", 1)
                            else:
                                action NullAction()
                                use sidestory_image("RESPECT", "sideStory_respect_L", 1)
                        button:
                            if plus_persistent.side_stories_unlocked[5]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "nm3"), Hide())]
                                use sidestory_image("RESPECT", "sideStory_respect_UL", 2)
                            else:
                                action NullAction()
                                use sidestory_image("RESPECT", "sideStory_respect_L", 2)


                if plus_persistent.side_stories_unlocked[6]:
                    grid 2 1:
                        style_prefix "sidestory"
                        align (0.5, 1)

                        button:
                            if plus_persistent.side_stories_unlocked[6]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "sn1"), Hide())]
                                use sidestory_image("BALANCE", "sideStory_balance_UL", 1)
                            else:
                                action NullAction()
                                use sidestory_image("BALANCE", "sideStory_balance_L", 1)
                        button:
                            if plus_persistent.side_stories_unlocked[7]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "sn3"), Hide())]
                                use sidestory_image("BALANCE", "sideStory_balance_UL", 2)
                            else:
                                action NullAction()
                                use sidestory_image("BALANCE", "sideStory_balance_L", 2)


                if plus_persistent.side_stories_unlocked[8]:
                    grid 2 1:
                        style_prefix "sidestory"
                        align (0.5, 1)

                        button:
                            if plus_persistent.side_stories_unlocked[8]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "ym1"), Hide())]
                                use sidestory_image("REFLECTION", "sideStory_reflection_UL", 1)
                            else:
                                action NullAction()
                                use sidestory_image("REFLECTION", "sideStory_reflection_L", 1)
                        button:
                            if plus_persistent.side_stories_unlocked[9]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "ym3"), Hide())]
                                use sidestory_image("REFLECTION", "sideStory_reflection_UL", 2)
                            else:
                                action NullAction()
                                use sidestory_image("REFLECTION", "sideStory_reflection_L", 2)


                if plus_persistent.side_stories_unlocked[10]:
                    grid 2 1:
                        style_prefix "sidestory"
                        align (0.5, 1)

                        button:
                            if plus_persistent.side_stories_unlocked[10]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "ny1"), Hide())]
                                use sidestory_image("SELF-LOVE", "sideStory_selfLove_UL", 1)
                            else:
                                action NullAction()
                                use sidestory_image("SELF-LOVE", "sideStory_selfLove_L", 1)
                        button:
                            if plus_persistent.side_stories_unlocked[11]:
                                action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "ny4"), Hide())]
                                use sidestory_image("SELF-LOVE", "sideStory_selfLove_UL", 2)
                            else:
                                action NullAction()
                                use sidestory_image("SELF-LOVE", "sideStory_selfLove_L", 2)


                if "epilogue" in plus_persistent.all_unlocked:
                    button style "sidestory_button_wide":
                        xalign 0.5
                        if False not in plus_persistent.side_stories_unlocked:
                            action [SetVariable("confirm_title_message", "Open Side Story"), Confirm("Begin this Side Story?", Call("start_side_story", "epilogue"), Hide())]
                        else:
                            action NullAction()

                        frame:
                            xysize (760, 210)
                            align (0.5,0.5)
                            if False not in plus_persistent.side_stories_unlocked:
                                background Frame("sideStory_equals_UL")
                            else:
                                background Frame("sideStory_equals_L")
                            text "EQUALS" style "sidestory_title_text":
                                align (0.5,0.5)


                if "email_9" in plus_persistent.read_mails:
                    button style "sidestory_button_wide":
                        xalign 0.5
                        if "email_9" in plus_persistent.read_mails:
                            action Call("start_side_story", "test_vm")
                        else:
                            action NullAction()
                        frame:
                            xysize (760, 210)
                            align (0.5,0.5)
                            background Frame("sideStory_testVM")
                            text "TEST VM" style "virtual_desktop_text":
                                align (0.5,0.5)
                                color "#fff"

                null height 10

            vbar value YScrollValue("desktop_popup_canvas") xpos 1.0 xoffset 20

label start_side_story(side_story_name):

    if side_story_name is "test_vm":
        $ desktop_window_animation_multi = 0
        $ unlock("testvm_open")
    else:
        play sound "sfx/DLCP_sfx/i3.wav"

    hide screen virtual_desktop_sidestories_app

    hide screen virtual_desktop_start_menu

    pause(0.3)


    scene black onlayer master

    hide screen virtual_desktop_wallpaper
    hide screen virtual_desktop

    $ in_side_story = True
    $ enable_autofocus = True


    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"


    python:
        renpy.context()._main_menu = False
        main_menu = False
        _history_list = []
        renpy.store._history = True
        renpy.store.suppress_overlay = False

    if renpy.mobile:
        if renpy.ios:
            $ jukebox_function_ios_stop()
        else:
            $ jukebox_function_android_stop()

    jump expression side_story_name

style sidestory_button:
    hover_background "sidestory_button_highlight"
    xysize (398, 247)

style sidestory_button_wide is sidestory_button:
    xysize (802, 250)
    hover_background "sidestory_button_highlight"

image sidestory_button_highlight:
    Frame(Image("gui/virtual_desktop/sidestory_highlight.png",oversample=2), 44, 44)

screen sidestory_image(title, base_img, part):




    $ title_text_style = "sidestory_title_text" if int(Text(title, style="sidestory_title_text").size()[0]) < 300 else "sidestory_title_text_small"
    frame:

        xysize (360,210)
        align (0.55,0.55)
        background Frame(base_img)


        text "[title!t]":
            xanchor 0.7
            align (0.65, 0.65)
            style title_text_style


        if part > 0:

            $ part_bg_color = "#FFFFFF" if part == 1 else gui.virtual_desktop_accent_color
            $ part_text_color = gui.virtual_desktop_accent_color if part == 1 else "#FFFFFF"
            $ part_text = _("PART") + " {b}" + str(part) + "{/b}"
            frame:
                xysize (69, 20)
                align (0.78,0.8)
                background part_bg_color
                text "[part_text!t]":
                    style "sidestory_part_text"
                    color part_text_color

style sidestory_title_text:
    font gui.virtual_desktop_black_text_font
    size 48
    color "FFFFFF"
    outlines []
style sidestory_title_text_small is sidestory_title_text:
    size 36
style sidestory_part_text:
    font gui.virtual_desktop_bold_text_font
    align (0.5, 0.5)
    xycenter (0.5, 0.5)
    size 15
    outlines []
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
