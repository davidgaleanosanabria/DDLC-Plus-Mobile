init python:

    import time


    h_hours = 0
    m_minutes = 0
    am_pm = "AM"
    def change_hour():
        t = datetime.datetime.today()
        global am_pm
        global h_hours
        global m_minutes
        
        am_pm = "AM"
        h_hours = t.hour
        if t.hour > 12:
            h_hours = t.hour - 12
            am_pm = "PM"
        
        m_minutes = t.minute
        if t.minute < 10:
            m_minutes = "0" + str(t.minute)
        
        renpy.restart_interaction()



    def set_taskbar_app(taskbar_icon=""):
        global open_taskbar_icon
        global show_taskbar_icon
        
        if renpy.get_registered_image(taskbar_icon) == None:
            return
        open_taskbar_icon = taskbar_icon
        show_taskbar_icon = True
    def clear_taskbar_app():
        global show_taskbar_icon
        show_taskbar_icon = False

    desktop_box_a = (-1,-1)
    desktop_box_b = (-1,-1)
    desktop_box_count = 0

    def desktop_box_set(drags):
        global desktop_box_a
        global desktop_box_b
        
        desktop_box_a = (drags[0].grab_x, drags[0].grab_y)
        desktop_box_b = renpy.get_mouse_pos()
        
        renpy.restart_interaction()

    def desktop_box_skip():
        global desktop_box_a
        global desktop_box_b
        
        desktop_box_a = (-1, -1)
        desktop_box_b = (-1, -1)

    def desktop_box_end(drags, drop):
        desktop_box_skip()
        
        global desktop_box_count
        
        plus_persistent.desktop_boxes_drawn += 1
        if (plus_persistent.desktop_boxes_drawn == 50):
            unlock("draw_boxes")
        plus_persistent.save()

transform bios_top_right:
    anchor (0,0)
    pos (65,44)
transform bios_under_small_logo:
    anchor (0,0)
    pos (65,144)

style bios_text:
    font "Perfect DOS VGA 437 Win.ttf"
    color "#b5b5b5"
    size 23




translate spanish style bios_text font "ModernDOS8x16.ttf"
translate spanish_latin_america style bios_text font "ModernDOS8x16.ttf"
translate russian style bios_text font "unifont-17.0.03.otf"
translate korean style bios_text font "unifont-17.0.03.otf"
translate japanese style bios_text font "unifont-17.0.03.otf"
translate chinese_simplified style bios_text font "unifont-17.0.03.otf"
translate chinese_traditional style bios_text font "unifont-17.0.03.otf"

image bios_output_text = ParameterizedText(style="bios_text")

image mes_logo_large:
    "gui/virtual_desktop/MES Logo bios.png"
    zoom 0.6
    align (0.5, 0.5)

image mes_logo_small:
    "gui/virtual_desktop/MES Logo bios 2.png"
    zoom 0.7
    align (0.05, 0.1)

image virtual_desktop_button_outline = Frame("/gui/virtual_desktop/settings/button outline.png", 12, 12)
image virtual_desktop_button_highlight = Frame(Transform("/gui/virtual_desktop/settings/button highlight.png", zoom=0.6), 16, 16)

default open_taskbar_icon = "desktop_DDLC_I"
default show_taskbar_icon = False
default show_side_stories_this_desktop = False





define config.detached_layers += [ "bios" ]
image bios_layer = Layer("bios")

transform bios_glow_shader:


    blur 2





label desktop_start:

    call boot_into_desktop

    call login_sequence

    call desktop











label boot_into_desktop:

    play music bios_buzz

    show bios_layer at bios_glow_shader
    scene black onlayer bios


    show mes_logo_large onlayer bios

    $ newline_nonlocalized = "\n"

    $ b1 = "MEMORY OK"
    $ b2 = "Press HELP key to enter SETUP"
    $ bios_output = (
        "8:33" + "\n" +
        "3,4,4" + "\n" + 
        "[b1!t]" + 
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" +
        "[b2!t]")
    show bios_output_text bios_output onlayer bios at bios_top_right

    pause(2.0)

    hide mes_logo_large
    hide bios_output_initial


    show mes_logo_small onlayer bios at bios_top_right

    $ bios_string_line_1 = "Commander Legacy BIOS v2d rev4"
    $ bios_string_line_2 = "Type: Binary Thin Client"
    $ bios_string_line_3 = "68030 @40MHz"
    $ bios_string_line_4 = "Chip RAM: 2MB"
    $ bios_string_line_5 = "Fast RAM: 8MB"
    $ bios_string_line_6 = "Extended RAM: 4194304MB"
    $ bios_string_press_help = "Press HELP key to enter SETUP"

    $ bios_output = (
        "[bios_string_line_1!t]" + "\n\n" +
        "[bios_string_line_2!t]" + newline_nonlocalized + 
        "[bios_string_line_3!t]" + "\n" + 
        "[bios_string_line_4!t]" + newline_nonlocalized +
        "[bios_string_line_5!t]" + newline_nonlocalized +
        "[bios_string_line_6!t]" + newline_nonlocalized +
        newline_nonlocalized + newline_nonlocalized +

        "[bios_string_press_help!t]")
    show bios_output_text bios_output at bios_under_small_logo

    pause(1.0)

    $ bios_string_wait = "WAIT..."
    $ bios_string_physical_address = "PHYSICAL ADDRESS: 4E 6F 45 67 67 73"

    $ bios_output = (
        "[bios_string_line_1!t]" + "\n\n" +
        "[bios_string_line_2!t]" + newline_nonlocalized + 
        "[bios_string_line_3!t]" + "\n" + 
        "[bios_string_line_4!t]" + newline_nonlocalized +
        "[bios_string_line_5!t]" + newline_nonlocalized +
        "[bios_string_line_6!t]" + newline_nonlocalized +
        newline_nonlocalized + newline_nonlocalized +

        "[bios_string_wait!t]" + newline_nonlocalized + 
        "[bios_string_physical_address!t]")
    show bios_output_text bios_output

    pause(1.0)

    $ bios_string_guid = "GUID: 4D6F6E69-6B61-6451-7734-77395767586351"
    $ bios_output += "\n" + "[bios_string_guid!t]"
    show bios_output_text bios_output

    pause(1.0)

    $ bios_string_link = "LINK:"
    $ bios_output += newline_nonlocalized + "[bios_string_link!t]" + " "


    $ spinner_chars = ['\\','|','/','-']
    $ dots = ""
    $ spinner = ""
    $ spinner_step = 0
    $ dot_step = 0
    while dot_step < 3:
        while spinner_step < 8:
            $ spinner = spinner_chars[spinner_step % len(spinner_chars)]
            show bios_output_text bios_output + "[dots]" + "[spinner]"
            $ spinner_step += 1
            pause(0.05)
        $ dots += '.'
        $ dot_step += 1
        $ spinner_step = 0


    $ bios_output += dots
    $ bios_string_connection_established = "Connection Established"
    $ bios_output += "[bios_string_connection_established!t]"
    show bios_output_text bios_output

    $ persistent.seen_bios = True
    $ renpy.save_persistent()

    pause(0.05)

    hide bios_layer
    stop music
    play sound bios_boot

    return

label login_sequence:
    show black
    pause(2.0)

    call screen bootup_login_pre_click with fade 
    return






label desktop(sidestory=False):

    stop music
    $ suppress_overlay = True
    scene black
    $ in_side_story = False
    $ print(sidestory)
    $ open_taskbar_icon = "desktop_DDLC_I"
    $ show_side_stories_this_desktop = sidestory
    call screen virtual_desktop()

label desktop_from_main:
    hide screen main_menu
    hide screen game_menu
    call desktop (False)

label desktop_from_side_stories:
    hide screen main_menu
    hide screen game_menu
    $ config.skipping = False

    call desktop (True)







label desktop_to_ddlc:

    play sound "sfx/DLCP_sfx/i5.wav"
    hide screen virtual_desktop_start_menu
    hide screen virtual_desktop_wallpaper
    hide screen virtual_desktop
    $ jukebox_function_android_stop()
    $ pause(1.5)
    pause 1.5
    $ renpy.full_restart(transition=None, label="DDLC_splashscreen")



style virtual_desktop_text:
    font gui.virtual_desktop_text_font
    color gui.virtual_desktop_text_color
    size 24
    outlines []

style virtual_desktop_bold_text is virtual_desktop_text:
    font gui.virtual_desktop_bold_text_font

style virtual_desktop_button_text is virtual_desktop_text

style virtual_desktop_frame:
    background Frame("gui/virtual_desktop/files windows background.png")
    padding (0,0)

style virtual_desktop_vscrollbar:
    xsize 6
    thumb Frame(gui.virtual_desktop_text_color)
    base_bar Frame("#00000000")
    thumb_offset 0

style virtual_desktop_datetime is virtual_desktop_bold_text:
    color gui.virtual_desktop_start_color
    size 22

style virtual_desktop_popup_text is virtual_desktop_bold_text:
    size get_variable_size(19, 32)
    yalign 0.5

transform login_button_outer_grow:
    align (0.5, 0.5)
    anchor (0.5, 0.5)
    xysize (0.8, 0.8)
    subpixel True
    on idle:
        block:
            easeout_quad 0.5 xysize (1.0,1.0)
            easein_quad 0.8 xysize (0.8,0.8)
            pause 0.6
            repeat
    on hover:
        easeout_quad 0.2 xysize (0.4,0.4)
    on selected_hover:
        easeout_quad 0.2 xysize (0.4,0.4)
transform login_button_inner_grow:
    align (0.5, 0.5)
    anchor (0.5, 0.5)
    xysize (0.8, 0.8)
    subpixel True
    on idle:
        block:
            easeout_quad 0.5 xysize (0.88,0.88)
            easein_quad 0.8 xysize (0.8,0.8)
            pause 0.6
            repeat
    on hover:
        easeout_quad 0.2 xysize (0.4,0.4)
    on selected_hover:
        easeout_quad 0.2 xysize (0.4,0.4)
transform login_button_center_grow:
    align (0.5, 0.5)
    anchor (0.5, 0.5)
    xysize (0.8, 0.8)
    subpixel True
    on hover:
        easeout_quad 0.2 xysize (1.75,1.75)
    on selected_hover:
        easeout_quad 0.2 xysize (1.75,1.75)
transform login_button_fadeout:
    align (0.5, 0.5)
    anchor (0.5, 0.5)
    xysize (0.4, 0.4)
    alpha 1.0
    subpixel True
    parallel:
        easeout_quad 0.4 alpha 0.0
    parallel:
        easeout_quad 0.7 xysize (0.8, 0.8)
transform login_button_center_fadeout:
    align (0.5, 0.5)
    anchor (0.5, 0.5)
    xysize (1.75,1.75)
    alpha 1.0
    subpixel True
    parallel:
        easeout_quad 0.4 alpha 0.0
    parallel:
        easeout_quad 0.7 xysize (0.8, 0.8)



screen bootup_login_pre_click():
    style_prefix "bootup_login"


    add "gui/virtual_desktop/login gradient.png" fit "contain"

    key ['mouseup_3'] action NullAction()
    key ['mouseup_2'] action NullAction()



    add "gui/virtual_desktop/user icon.png":
        align (0.5, 0.4)
        zoom 0.7

    if renpy.mobile:
        button:
            xalign 0.5
            yalign 0.75
            xysize (180, 180)
            action [Hide("bootup_login_pre_click"), Show("bootup_login_post_click")]
            has fixed
            xysize (180, 180)
            add "gui/virtual_desktop/login_button_outer.png" at login_button_outer_grow
            add "gui/virtual_desktop/login_button_inner.png" at login_button_inner_grow
            add "gui/virtual_desktop/login_button_center.png" at login_button_center_grow
        $ login_button_text = "Login"
        text " " + "[login_button_text!t]":
            yalign 0.85
            xalign 0.5

    else:
        hbox xalign 0.5 yalign 0.7:
            add "gui/virtual_desktop/login_enter.png":
                zoom 0.4
            $ login_button_text = "Login"
            text " " + "[login_button_text!t]":
                yalign 0.5

        button:
            action [Hide("bootup_login_pre_click"), Show("bootup_login_post_click")]
            align (0.5, 0.5)
            xysize (1.0, 1.0)

screen bootup_login_post_click():
    style_prefix "bootup_login"


    add "gui/virtual_desktop/login gradient.png" fit "contain"

    key ['mouseup_3'] action NullAction()
    key ['mouseup_2'] action NullAction()



    add "gui/virtual_desktop/user icon.png":
        align (0.5, 0.4)
        zoom 0.7

    if renpy.mobile:
        button:
            xalign 0.5
            yalign 0.75
            xysize (180, 180)
            action NullAction()
            has fixed
            xysize (180, 180)
            add "gui/virtual_desktop/login_button_outer.png" at login_button_fadeout
            add "gui/virtual_desktop/login_button_inner.png" at login_button_fadeout
            add "gui/virtual_desktop/login_button_center.png" at login_button_center_fadeout
        add "gui/virtual_desktop/spinner.png" at loginSpinnerLocation
        text "root":
            align (0.5, 0.6)

        text "Logging in...":
            align (0.5, 0.85)

    else:
        text "root":
            align (0.5 , 0.6)
        text "Logging in...":
            align (0.5 , 0.7)
        add "gui/virtual_desktop/spinner.png" at loginSpinnerLocation
    timer 2 action [Hide("bootup_login_post_click"), Play("sound", "sfx/DLCP_sfx/a2.wav"), Return()]

transform loginSpinnerLocation:
    align (0.5, 0.8)
    zoom 0.15
    block:
        linear 2 rotate 1440

style bootup_login_text is virtual_desktop_text:
    color ("#ffffff87" if renpy.mobile else "#ffffff")
    size get_variable_size(20, 28, gui.text_scale)







screen virtual_desktop():

    $ plus_purchased = get_plus_content_purchase_state()

    use virtual_desktop_wallpaper
    use virtual_desktop_start_menu




    style_prefix "virtual_desktop_start_menu"




    key ['mouseup_3'] action NullAction()
    key ['mouseup_2'] action NullAction()


    add "gui/virtual_desktop/taskbar.png" yalign 1.0 fit "contain" at virtual_desktop_to_ddlc_fadeout


    timer 0.30 action change_hour repeat True
    text "[h_hours]:[m_minutes] [am_pm!t]" at virtual_desktop_to_ddlc_fadeout:
        style "virtual_desktop_datetime"
        yalign 1.0
        xalign 1.0
        yoffset -4
        xoffset -20


    hbox at virtual_desktop_to_ddlc_fadeout:
        xsize 1.0
        ysize 40
        yalign 1.0
        spacing 0


        frame:
            style "virtual_desktop_taskbar_icon_frame"
            background Frame("gui/virtual_desktop/heart highlight white.png")
            add "gui/virtual_desktop/MES Logo button color.png":
                align (0.5, 0.5)
                zoom 0.7



        frame:
            style "virtual_desktop_taskbar_icon_frame"
            background "#00000000"



            showif show_taskbar_icon is True:

                frame at virtual_desktop_taskbar_app_background:
                    xysize (1.0, 1.0)
                    background Frame("gui/virtual_desktop/heart highlight gradient.png")
            showif show_taskbar_icon is True:

                add open_taskbar_icon at virtual_desktop_taskbar_app_icon:
                    align (0.5, 0.5)

    if show_side_stories_this_desktop:
        timer 0.1 action [Show("virtual_desktop_sidestories_app"), SetVariable("show_side_stories_this_desktop", False)]

style virtual_desktop_taskbar_icon_frame:
    xsize 100
    ysize 1.0
    padding (0,0)

screen virtual_desktop_wallpaper:


    frame at virtual_desktop_to_ddlc_fadeout:
        padding 0,0,0,0
        background Frame("[plus_persistent.desktop_wallpaper]")


        if renpy.mobile == False:
            drag:
                drag_name "desktop_box"
                draggable True
                dragging desktop_box_set
                dragged desktop_box_end
                clicked desktop_box_skip

            if desktop_box_b != (-1, -1):
                $ boxsize = (abs(desktop_box_b[0] - desktop_box_a[0]), abs(desktop_box_b[1] - desktop_box_a[1]))
                $ topleft = (min(desktop_box_a[0], desktop_box_b[0]),min(desktop_box_a[1], desktop_box_b[1]))
                add Solid("#E2E2E280",pos=topleft, xysize = boxsize)

                add Solid("#FFFFFF",pos=topleft, xysize = (boxsize[0], 1))
                add Solid("#FFFFFF",pos=topleft, xysize = (1, boxsize[1]))

                add Solid("#FFFFFF",pos=(topleft[0], max(desktop_box_a[1], desktop_box_b[1]) - 1), xysize = (boxsize[0], 1))
                add Solid("#FFFFFF",pos=(max(desktop_box_a[0], desktop_box_b[0]) - 1, topleft[1]), xysize = (1, boxsize[1]))

transform virtual_desktop_to_ddlc_fadeout:
    alpha 1.0
    on hide:
        pause 0.5
        easeout_quad 0.20 alpha 0.0

screen virtual_desktop_start_menu:

    style_prefix "virtual_desktop_start_menu"



    $ start_menu_height = 0.57
    $ start_menu_width = 0.25


    if renpy.mobile:
        $ start_menu_height = 0.71
        $ start_menu_width = 0.34

    if len(renpy.translate_string("Side Stories")) >= 17:

        $ start_menu_width = (0.4 if renpy.mobile else 0.26)


    add "gui/virtual_desktop/uidropshadow.png" at desktopMenuEndLocation id "start_menu_shadow":
        xalign -0.23
        alpha 0.17
        yoffset 60


    frame at desktopMenuEndLocation id "start_menu":
        background Frame("gui/virtual_desktop/start menu background.png")
        xysize (start_menu_width, start_menu_height)
        xpadding 0
        ypadding 7

        $ plus_content_unlocked = get_plus_content_purchase_state()



        vbox at virtual_desktop_start_menu_vbox_slide:
            spacing 0

            button:
                action Jump("desktop_to_ddlc")
                add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                hbox at virtual_desktop_start_menu_hover:
                    add "desktop_DDLC_I":
                        yalign 0.5
                    text "DDLC"

            button:
                action (Show("virtual_desktop_sidestories_app") if plus_content_unlocked else Show("virtual_desktop_plus_iap_screen"))
                add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                hbox at virtual_desktop_start_menu_hover:
                    add "desktop_SideStories_I":
                        yalign 0.5
                    text _("Side Stories")
                if not plus_content_unlocked:
                    add "virtual_desktop_iap_lock"
                elif has_notification("sidestory"):
                    add "virtual_desktop_notification"

            button:
                action [Function(update_virtual_file_states), Show("virtual_desktop_files_app")]
                add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                hbox at virtual_desktop_start_menu_hover:
                    add "desktop_Files_I":
                        yalign 0.5
                    text _("Files")

            button:
                action (Show("virtual_desktop_mail_app") if plus_content_unlocked else Show("virtual_desktop_plus_iap_screen"))
                add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                hbox at virtual_desktop_start_menu_hover:
                    add "desktop_Mail_I":
                        yalign 0.5
                    text _("Mail")
                if not plus_content_unlocked:
                    add "virtual_desktop_iap_lock"
                elif has_notification("mail"):
                    add "virtual_desktop_notification"

            button:
                action ([Function(gallery_refresh_unlock_states), Show("virtual_desktop_gallery_app")] if plus_content_unlocked else Show("virtual_desktop_plus_iap_screen"))
                add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                hbox at virtual_desktop_start_menu_hover:
                    add "desktop_Pictures_I":
                        yalign 0.5
                    text _("Pictures")
                if not plus_content_unlocked:
                    add "virtual_desktop_iap_lock"
                elif has_notification("bg"):
                    add "virtual_desktop_notification"

            button:
                action (Show("virtual_desktop_music_app") if plus_content_unlocked else Show("virtual_desktop_plus_iap_screen"))
                add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                hbox at virtual_desktop_start_menu_hover:
                    add "desktop_Music_I":
                        yalign 0.5
                    text _("Music")
                if not plus_content_unlocked:
                    add "virtual_desktop_iap_lock"
                elif has_notification("bgm"):
                    add "virtual_desktop_notification"

            button:
                action Show("virtual_desktop_settings_app")
                add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                hbox at virtual_desktop_start_menu_hover:
                    add "desktop_Settings_I":
                        yalign 0.5
                    text _("Settings")

            if not renpy.mobile:
                button:
                    action Quit(False)
                    add "virtual_desktop_start_menu_highlight" at virtual_desktop_start_menu_hover_highlight
                    hbox at virtual_desktop_start_menu_hover:
                        add "desktop_Quit_I":
                            yalign 0.5
                        text _("Quit")

image virtual_desktop_start_menu_highlight:
    "gui/virtual_desktop/start menu highlight.png"

image virtual_desktop_iap_lock:
    "gui/virtual_desktop/plus_iap_lock_icon.png"
    zoom 0.2
    align (0.925, 0.35)

image virtual_desktop_notification:
    "gui/virtual_desktop/New.png"
    zoom 0.342
    align (0.0, 0.1)

    xpos 40
    on hover:
        xoffset 10
        linear 0.15 xoffset 0
    on idle:
        xoffset 0

style virtual_desktop_start_menu_button:
    xpadding 0
    ypadding 0
    ysize (70 if renpy.mobile else 49)
style virtual_desktop_start_menu_hbox:
    xanchor 0.0
    yalign 0.5
    spacing 25
    ysize 30
style virtual_desktop_start_menu_text:
    font gui.virtual_desktop_start_text_font
    color gui.virtual_desktop_start_color
    size (28 if renpy.mobile else 24)
    kerning 1
    outlines []
    yalign 0.5

transform desktopMenuEndLocation:
    yalign 1.0
    yoffset -30
    on show:
        alpha 0.0
        yoffset 150
        pause 0.2
        parallel:
            easein 0.5 yoffset -30
        parallel:
            pause 0.2
            easein 0.3 alpha 1.0
    on hide:
        alpha 1.0
        yoffset -30
        parallel:
            easeout 0.5 yoffset 150
        parallel:
            easeout 0.3 alpha 0.0


transform virtual_desktop_start_menu_hover:

    matrixcolor BrightnessMatrix(0.0)
    xpos 20
    on hover:
        matrixcolor BrightnessMatrix(5.0)
        xoffset 10
        linear 0.15 xoffset 0
    on idle:
        matrixcolor BrightnessMatrix(0.0)
        xoffset 0

transform virtual_desktop_start_menu_vbox_slide:
    on show:
        yoffset 250
        easein_quad 0.7 yoffset 0
        easein_quad 0.7 xoffset 0

transform virtual_desktop_start_menu_hover_highlight:
    xysize (1.0,1.0)
    yalign 0.0
    alpha 0.0
    fit "fill"
    on hover:
        linear 0.15 alpha 1.0
    on idle:
        linear 0.15 alpha 0.0







screen virtual_desktop_app_window(screen_name, window_width=880, taskbar_icon="", footer_height=30):

    on "show" action Play("sound", "sfx/DLCP_sfx/i4.wav")
    on "hide" action Play("sound", "sfx/DLCP_sfx/n1.wav")
    if taskbar_icon != "":
        on "show" action Function(set_taskbar_app, taskbar_icon)
        on "hide" action Function(clear_taskbar_app)


    style_prefix "virtual_desktop"


    dismiss action [Hide(), Play("sound", "sfx/DLCP_sfx/n1.wav"), SetVariable("confirm_title_message", "Confirm")]


    frame at virtual_desktop_app_window_start_close_alpha:
        area (0,0,1.0,1.0)
        background Solid("#24172F70")


    frame at virtual_desktop_app_window_start_close_alpha, virtual_desktop_app_window_start_close_zoom:
        modal True

        xysize (window_width, 680)
        xycenter (0.5, 0.5)
        yoffset -20
        background "#fff"

        has side "t b c"

        frame at virtual_desktop_app_window_reveal:
            xysize (1.0,get_variable_size(40, 65))
            left_padding get_variable_size(20, 30)
            background Solid("#fff")
            text screen_name style "virtual_desktop_bold_text":
                size get_variable_size(19, 32)
                yalign 0.5
            button:
                align (1.0, 0.5)
                xsize get_variable_size(50, 80)
                ysize 1.0
                hover_background "#f1f1f1"
                action Hide()
                add "gui/virtual_desktop/app_close_x.png":
                    xysize (20,20)
                    align (0.5, 0.5)


        frame at virtual_desktop_app_window_reveal:
            xysize (1.0, footer_height)
            background Solid(gui.virtual_desktop_soft_accent_color)


        frame at virtual_desktop_app_window_reveal:
            xfill True
            yfill True
            ymaximum (640 - footer_height)
            background Frame("gui/virtual_desktop/files windows background.png")

            transclude

    key ['mouseup_3'] action NullAction()
    key ['mouseup_2'] action NullAction()

screen virtual_desktop_confirm_dialog_popup(screen_name, footer_height=30):
    on "show" action Play("sound", "sfx/DLCP_sfx/n2.wav")
    on "hide" action Play("sound", "sfx/DLCP_sfx/n1.wav")

    style_prefix "virtual_desktop"


    frame at virtual_desktop_app_window_start_close_alpha:
        area (0,0,1.0,1.0)
        background Solid("#24172F70")


    frame at virtual_desktop_app_window_start_close_alpha, virtual_desktop_app_window_start_close_zoom:

        modal True
        xmaximum 700
        ymaximum 500
        xycenter (0.5, 0.5)
        background "#fff"

        has side "t b c"

        frame at virtual_desktop_app_window_reveal:
            xysize (1.0,get_variable_size(40, 65))
            left_padding get_variable_size(20, 30)
            background Solid("#fff")
            text screen_name style "virtual_desktop_bold_text":
                size get_variable_size(19, 32)
                yalign 0.5











        frame at virtual_desktop_app_window_reveal:
            xysize (1.0, footer_height)
            background Solid(gui.virtual_desktop_soft_accent_color)


        frame at virtual_desktop_app_window_reveal:
            xfill True
            yfill True

            padding (10, 10)
            background Frame("gui/virtual_desktop/files windows background.png")

            transclude

style virtual_desktop_framed_button:
    yminimum 50
    xminimum 200
    padding (20, 5)
    idle_background "virtual_desktop_button_outline"
    insensitive_background Transform("virtual_desktop_button_outline",matrixcolor=OpacityMatrix(value=0.3))
    hover_background "virtual_desktop_button_highlight"





transform virtual_desktop_app_window_start_close_alpha:
    on show:
        alpha 0.0
        parallel:
            linear (0.15 * desktop_window_animation_multi) alpha 1.0
    on hide:
        pause 0.075
        parallel:
            linear (0.2 * desktop_window_animation_multi) alpha 0.0

transform virtual_desktop_taskbar_app_background:
    alpha 0.0
    on show:
        linear (0.15 * desktop_window_animation_multi) alpha 1.0
    on hide:
        pause 0.15
        linear (0.2 * desktop_window_animation_multi) alpha 0.0

transform virtual_desktop_taskbar_app_icon:
    on show:
        alpha 0.0
        zoom 0.75
        pause 0.15
        parallel:
            linear (0.15 * desktop_window_animation_multi) zoom 1.0
        parallel:
            linear (0.15 * desktop_window_animation_multi) alpha 1.0
    on appear:
        alpha 0.0
        zoom 0.75
        pause 0.15
        parallel:
            linear (0.15 * desktop_window_animation_multi) zoom 1.0
        parallel:
            linear (0.15 * desktop_window_animation_multi) alpha 1.0
    on hide:
        alpha 1.0
        zoom 1.0
        parallel:
            linear (0.2 * desktop_window_animation_multi) zoom 0.5
        parallel:
            linear (0.2 * desktop_window_animation_multi) alpha 0.0
transform virtual_desktop_app_window_start_close_zoom:


    on show:
        zoom 0.95
        alpha 0.0
        parallel:
            easeout_cubic (0.15 * desktop_window_animation_multi) zoom 1.0
        parallel:
            linear (0.15 * desktop_window_animation_multi) alpha 1.0
    on hide:
        pause 0.075
        parallel:
            linear (0.2 * desktop_window_animation_multi) alpha 0.0
        parallel:
            easein_quad (0.15 * desktop_window_animation_multi) zoom 0.95

transform virtual_desktop_app_window_reveal:
    alpha 0.0
    pause 0.15
    easeout_cubic 0.15 alpha 1.0

    on hide:
        linear 0.075 alpha 0.0

screen virtual_desktop_plus_iap_screen:


    dismiss action [Hide(), Play("sound", "sfx/DLCP_sfx/n1.wav"), SetVariable("confirm_title_message", "Confirm")]

    style_prefix "virtual_desktop_iap"


    frame at virtual_desktop_app_window_start_close_alpha:
        area (0,0,1.0,1.0)
        background Solid("#24172F70")

    frame at virtual_desktop_app_window_start_close_alpha, virtual_desktop_app_window_start_close_zoom:
        modal True
        xysize (1160, 680)
        xycenter (0.5, 0.5)
        yoffset -20
        frame:
            xysize (1.0, 1.0)
            padding (0, 0)
            background "#fff"
            add "gui/virtual_desktop/iap_plus_monika.png" fit "contain" align (1.0, 1.0)
            add "gui/virtual_desktop/iap_top_shadow.png" xsize 1.0 ysize 20 align (0.5, 0.0)
        frame:
            padding (30, 20, 30, 10)
            background None
            has vbox
            spacing 0
            fixed:
                xsize 1.0
                yfit True
                text _("Doki Doki Literature Club Plus!") style "virtual_desktop_iap_plus_label_text":
                    align (0.0, 0.0)
                    size 38
            fixed:
                xsize 700
                yfit True
                text _("If you enjoy DDLC, please consider supporting us with a one-time purchase to access lots of bonus content:")

            null height 10

            fixed:
                ysize 450
                vbox:
                    box_justify "all"
                    xsize 0.5
                    yminimum 300
                    ymaximum 360
                    vbox:
                        hbox:
                            add "iap_plus_icon"
                            text _("Side Stories") style "virtual_desktop_iap_plus_label_text"
                        text _("6 new Side Stories about the Literature Club members") xoffset 64

                    vbox:
                        hbox:
                            add "iap_plus_icon"
                            text _("Image Gallery") style "virtual_desktop_iap_plus_label_text"
                        text _("100+ images and concept art") xoffset 64

                    vbox:
                        hbox:
                            add "iap_plus_icon"
                            text _("Music Player") style "virtual_desktop_iap_plus_label_text"
                        text _("Includes the complete OST and bonus tracks") xoffset 64

                    hbox:
                        add "iap_plus_icon"
                        text _("And more...") style "virtual_desktop_iap_plus_label_text"
            null height 10
            fixed:
                ysize 1.0
                vbox:
                    yalign 1.0
                    button:
                        xysize (0.5, 75)
                        xalign 0.0
                        background Frame("gui/virtual_desktop/start menu highlight.png")
                        action iap.Purchase("plus_content", success=[Jump("iap_purchase_fanfare")])
                        has hbox
                        align (0.5, 0.5)
                        add "virtual_desktop_iap_lock" at virtual_desktop_iap_button_lock_icon
                        $ unlock_string = "Unlock DDLC Plus!:"
                        text _("[unlock_string!t]") + " " + str(iap.get_price("plus_content")):
                            size 30
                            color "#fff"
                            font gui.virtual_desktop_bold_text_font
                    button:
                        xysize (0.5, 50)
                        xalign 0.5
                        background None
                        action [iap.Restore(), Hide(), Function(renpy.utter_restart)]
                        text _("Restore Purchase"):
                            align (0.5, 0.5)
                            size 26
                            color gui.virtual_desktop_accent_color
                            font gui.virtual_desktop_bold_text_font
        button:
            align (1.0, 0.0)
            xsize 80
            ysize 65
            hover_background "#f1f1f1"
            action Hide()
            add "gui/virtual_desktop/app_close_x.png":
                xysize (20,20)
                align (0.5, 0.5)

image iap_plus_icon:
    "gui/virtual_desktop/plus-icon.png"
    zoom 0.14
    yalign 0.5

style virtual_desktop_iap_frame is virtual_desktop_frame

style virtual_desktop_iap_text is virtual_desktop_text:
    size 20

style virtual_desktop_iap_hbox:
    spacing 20
    ymaximum 50

style virtual_desktop_iap_vbox:
    spacing 0

style virtual_desktop_iap_plus_label_text:
    size 32
    font gui.riffic_font
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    layout "nobreak"
    yalign 0.5

transform virtual_desktop_iap_button_lock_icon:
    matrixcolor BrightnessMatrix(5.0)

label iap_purchase_fanfare:



    $ quick_menu = False

    hide screen virtual_desktop_plus_iap_screen
    scene black with fade
    hide screen virtual_desktop_files_app
    hide screen virtual_desktop_start_menu
    hide screen virtual_desktop_wallpaper
    hide screen virtual_desktop
    show iap_fanfare_black_bg with fade



    show iap_fanfare_gradient at truecenter
    show iap_fanfare_logo_bg zorder 1 at truecenter
    show iap_fanfare_bg_scanlines zorder 4 at truecenter
    show iap_fanfare_logo_border zorder 2 at truecenter



    $ pause(0.3)
    show iap_fanfare_lock_masked zorder 3 at truecenter
    $ pause(2.0)
    hide iap_fanfare_lock_masked


    show iap_fanfare_logo_with_heart zorder 1 at truecenter
    $ pause(0.8)



    show iap_fanfare_logo_letter_outlines zorder 4 at truecenter
    show iap_fanfare_logo_letters zorder 5 at truecenter


    $ pause(0.2)
    show iap_fanfare_logo_blurred zorder 0 at truecenter
    show iap_fanfare_letter_shadow zorder 0 at truecenter
    hide iap_fanfare_logo_bg


    $ pause(0.6)
    show iap_fanfare_mouse_cursor zorder 7 at iap_fanfare_fadeout
    show iap_fanfare_logo_plus zorder 6 at iap_fanfare_fadeout

    $ pause(3.0)

    show iap_fanfare_black_bg as iap_fanfare_ending_cover zorder 10 at iap_fanfare_ending_cover_fadein

    $ pause(2.0)

    $ renpy.full_restart(transition=False, label="splashscreen")

transform iap_fanfare_fadeout:
    on hide:
        alpha 1.0

transform iap_fanfare_ending_cover_fadein:
    alpha 0.0
    easein 0.8 alpha 1.0

image iap_fanfare_black_bg:
    Frame("#000000")

image iap_fanfare_gradient:
    "images/iap_fanfare/Fanfare__0001_Background-Gradient.png"
    alpha 1.0
    on hide:
        easein 1.5 alpha 0.0

image iap_fanfare_logo_bg:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_Puck-Inside-No-Heart.png"
    zoom 0.3
    alpha 0.0
    easein 0.3 alpha 1.0
    iap_fanfare_fadeout

image iap_fanfare_bg_scanlines:
    AlphaMask(Fixed("iap_fanfare_scanlines", xysize=(270,270)), Transform("images/iap_fanfare/ddlc_plus_logo_fanfare_Center-Mask.png", zoom=0.3))

image iap_fanfare_scanlines:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_scan-lines.png"
    subpixel True
    zoom 0.3
    ytile 4
    block:
        yoffset 0
        linear 2.0 yoffset -16
        repeat

image iap_fanfare_logo_border:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_Outer-Ring.png"
    zoom 0.3
    alpha 0.0
    easein 0.3 alpha 1.0
    iap_fanfare_fadeout

image iap_fanfare_logo_blurred:
    "images/iap_fanfare/Fanfare__0000_PuckBlur.png"
    zoom 0.3
    alpha 0.0
    easein 5.0 alpha 1.0
    iap_fanfare_fadeout

image iap_fanfare_lock_frame:
    "images/iap_fanfare/LockFrame.png"
    zoom 0.3
    anchor (0.5, 0.5)

image iap_fanfare_lock_plus:
    "images/iap_fanfare/LockPlus.png"
    zoom 0.3
    anchor (0.5, 0.5)

image iap_fanfare_lock_arm:
    "images/iap_fanfare/LockArm.png"
    zoom 0.3
    anchor (0.5, 0.5)
    yoffset 0
    pause 0.8
    easein_quad 0.3 yoffset -45

image iap_fanfare_lock:
    subpixel True
    Composite(
        (400, 552),
        (0,0), "iap_fanfare_lock_frame", 
        (0,0), "iap_fanfare_lock_plus",
        (0,0), "iap_fanfare_lock_arm")
    ycenter 252
    align (0.5, 0.5)
    blur 1
    zoom 0.01

    parallel:
        zoom 0.01
        easein_elastic 0.34 zoom 0.2
        pause 0.16
    pause 0.2
    parallel:
        easein 0.05 blur 0.0
    pause 0.1
    easeout_cubic 0.15 yoffset 10
    easein_cubic 0.15 yoffset 0

    pause 0.1
    parallel:
        easeout_cubic 0.5 rotate -45
    parallel:
        pause 0.1
        easeout_cubic 0.5 yoffset 200

image iap_fanfare_lock_masked:
    AlphaMask(Fixed("iap_fanfare_lock", xysize=(270,270)), Transform("images/iap_fanfare/ddlc_plus_logo_fanfare_Center-Mask.png", zoom=0.3))

image iap_fanfare_logo_with_heart:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_Puck-Inside-with-Heart.png"
    zoom 0.3
    alpha 0.0
    easein 0.4 alpha 0.9
    alpha 0.6
    easein 0.1 alpha 0.8
    pause 0.1
    alpha 0.7
    easein 0.1 alpha 0.8
    alpha 0.7
    easein 0.1 alpha 1.0
    iap_fanfare_fadeout


transform iap_fanfare_letter_start:
    zoom 0.01
    align (0.5, 0.5)

transform iap_fanfare_letter_bounce_in:
    easein_elastic 1.0 zoom 1.0

transform iap_fanfare_D1:
    iap_fanfare_letter_start
    offset (-243, -73)
    pause (0.2)
    iap_fanfare_letter_bounce_in

transform iap_fanfare_D2:
    iap_fanfare_letter_start
    offset (-211, 128)
    pause (0.4)
    iap_fanfare_letter_bounce_in

transform iap_fanfare_OO:
    iap_fanfare_letter_start
    offset (-61, 37)
    pause (0.1)
    iap_fanfare_letter_bounce_in

transform iap_fanfare_K1:
    iap_fanfare_letter_start
    offset (73, -120)
    pause (0.3)
    iap_fanfare_letter_bounce_in

transform iap_fanfare_K2:
    iap_fanfare_letter_start
    offset (136, 77)
    pause (0.5)
    iap_fanfare_letter_bounce_in

transform iap_fanfare_I1:
    iap_fanfare_letter_start
    offset (222, -126)
    pause (0.6)
    iap_fanfare_letter_bounce_in

transform iap_fanfare_I2:
    iap_fanfare_letter_start
    offset (282, 92)
    pause (0.7)
    iap_fanfare_letter_bounce_in

transform iap_fanfare_bottom_text:
    iap_fanfare_letter_start
    offset (156, 265)
    pause (0.8)
    iap_fanfare_letter_bounce_in

image iap_fanfare_logo_D1:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_D-01.png"
    iap_fanfare_D1

image iap_fanfare_logo_D1_outline:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_D-01_s-Outer-Stroke.png"
    iap_fanfare_D1

image iap_fanfare_logo_D2:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_D-02.png"
    iap_fanfare_D2

image iap_fanfare_logo_D2_outline:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_D-02_s-Outer-Stroke.png"
    iap_fanfare_D2

image iap_fanfare_logo_OO:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_OO.png"
    iap_fanfare_OO

image iap_fanfare_logo_OO_outline:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_OO_s-Outer-Stroke.png"
    iap_fanfare_OO

image iap_fanfare_logo_K1:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_K-1.png"
    iap_fanfare_K1

image iap_fanfare_logo_K1_outline:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_K-1_s-Outer-Stroke.png"
    iap_fanfare_K1

image iap_fanfare_logo_K2:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_K2.png"
    iap_fanfare_K2

image iap_fanfare_logo_K2_outline:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_K2_s-Outer-Stroke.png"
    iap_fanfare_K2

image iap_fanfare_logo_I1:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_I-1.png"
    iap_fanfare_I1

image iap_fanfare_logo_I1_outline:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_I-1_s-Outer-Stroke.png"
    iap_fanfare_I1

image iap_fanfare_logo_I2:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_I-2.png"
    iap_fanfare_I2

image iap_fanfare_logo_I2_outline:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_I-2_s-Outer-Stroke.png"
    iap_fanfare_I2

image iap_fanfare_logo_bottom_text:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_Text-and-Text-Box.png"
    iap_fanfare_bottom_text

image iap_fanfare_logo_letters:
    Fixed(
        "iap_fanfare_logo_D1",
        "iap_fanfare_logo_D2",
        "iap_fanfare_logo_OO",
        "iap_fanfare_logo_K1",
        "iap_fanfare_logo_K2",
        "iap_fanfare_logo_I1",
        "iap_fanfare_logo_I2",
        "iap_fanfare_logo_bottom_text"
    )
    zoom 0.3
    xycenter (0.5, 0.5)
    offset (-42, -13)
    iap_fanfare_fadeout

image iap_fanfare_logo_letter_outlines:
    Fixed(
        "iap_fanfare_logo_D1_outline",
        "iap_fanfare_logo_D2_outline",
        "iap_fanfare_logo_OO_outline",
        "iap_fanfare_logo_K1_outline",
        "iap_fanfare_logo_K2_outline",
        "iap_fanfare_logo_I1_outline",
        "iap_fanfare_logo_I2_outline"
    )
    zoom 0.3
    xycenter (0.5, 0.5)
    offset (-42, -13)
    iap_fanfare_fadeout

image iap_fanfare_letter_shadow:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_Shadow.png"
    zoom 0.3
    xycenter (0.5, 0.5)
    blur 5

image iap_fanfare_mouse_cursor:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_cursor.png"
    subpixel True
    zoom 0.3
    anchor (0, 0)
    pos (0.5, 0.5)
    offset (-106, 44)
    alpha 0.0

    parallel:
        easeout 0.2 alpha 1.0
        pause 0.6
    parallel:
        easein_cubic 0.8 offset (86, -18) knot (20, 130)
    pause 0.2

    linear 0.1 zoom 0.28
    easein 0.1 zoom 0.3
    iap_fanfare_fadeout

image iap_fanfare_logo_plus:
    "images/iap_fanfare/ddlc_plus_logo_fanfare_plus.png"
    subpixel True
    zoom 0.01
    alpha 0.0
    align (0.5, 0.5)
    offset (90, -44)
    rotate 90
    pause 1.1
    parallel:
        easein_elastic 0.9 rotate 0
    parallel:
        easein_quad 0.1 alpha 1.0
        pause 0.8
    parallel:
        easein_elastic 0.9 zoom 0.3
    iap_fanfare_fadeout
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
