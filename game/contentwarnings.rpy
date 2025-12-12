default persistent.content_warnings_enabled = False
default cw_prev_volume = preferences.get_mixer("music")

init python:
    def show_content_warning(warning: str):
        global cw_prev_volume
        if not persistent.content_warnings_enabled:
            return
        hide_quick_skip_and_auto = True
        renpy.show_screen("content_warning_popup", warning_message=warning)
        mc.add_history(None, "", (_("Content Warning:") + warning))
        
        cw_prev_volume = preferences.get_mixer("music")
        if cw_prev_volume > 0:
            renpy.music.set_volume(cw_prev_volume / 2) 
        
        
        
        
        pause(3.0)

    def cw_restore_volume():
        global cw_prev_volume
        renpy.music.set_volume(cw_prev_volume, 2)
    def cw_special_poem_query(special_poem_index):
        if special_poem_index == 1:
            show_content_warning("Crude sketch of a stick figure in the likeness of a character hanging from a noose.")
        elif special_poem_index == 4:
            show_content_warning("First-person written account glorifying self harm via cutting, and considering potential suicide. Visual depiction of blood smeared on paper.")
        elif special_poem_index == 9:
            show_content_warning("First-person written references to implied neglect and potential abuse by a parent, including withholding food.")
        elif special_poem_index == 10:
            show_content_warning("Brief, first person written account of implied mental health struggles and potential future self harm.")
        elif special_poem_index == 11:
            show_content_warning("First-person written account of implied drowning and accompanying panic, physical struggle, and claustrophobia.")

transform cw_fade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

image cw_darken:
    Solid("000000")
    alpha 0.7


image cw_frame_background:
    Frame(Transform("gui/cw_frame.png", zoom=1.0), 30, 30)

screen content_warning_popup(warning_message):
    default cw_confirm_ready = False
    modal True
    zorder 200
    on "show" action SetVariable("hide_quick_skip_and_auto", True)
    on "hide" action SetVariable("hide_quick_skip_and_auto", False)

    frame at cw_fade:
        background "cw_darken"


    if renpy.mobile:
        use mobile_quick_menu()

    frame at cw_popup_fade:
        background "cw_frame_background"
        padding 25,30
        align (0.5, 0.5)
        xminimum 500

        xmaximum 0.82
        ymaximum 1.0
        has vbox
        xalign 0.5
        yalign 0.5
        spacing 20
        add "gui/cwicon.png" xalign 0.5 zoom 0.3

        text "[warning_message!t]" style "cw_popup_text"
        textbutton _("OK") style "confirm_button":
            sensitive cw_confirm_ready
            action [Function(cw_restore_volume), Hide()]
            xalign 0.5

    timer 3.0 action SetLocalVariable("cw_confirm_ready", True)

style cw_popup_text is default:
    xalign 0.5
    outlines []
    color "#000"
    size get_variable_size(24, 30, gui.text_scale)
    textalign 0.5

transform cw_popup_fade:
    subpixel True
    on show:
        alpha 0.0
        yoffset 40
        parallel:
            easein_quad 0.4 alpha 1.0
        parallel:
            easein_quad 1.2 yoffset 0
    on hide:
        parallel:
            easeout_quad 0.4 alpha 0.0
        parallel:
            easeout_quad 1.2 yoffset 40
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
