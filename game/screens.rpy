init offset = -1





init python:

    class MobileSkipButton(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(MobileSkipButton, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.hover = False
            self.width = 0
            self.height = 0
        
        def render(self, width, height, st, at):
            t = Transform(child=self.child, alpha=(1.0 if config.allow_skipping and (renpy.game.preferences.skip_unseen or renpy.game.context().seen_current(True)) else 0.5))
            child_render = renpy.render(t, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (0,0))
            render.add_focus(self, None,
            0, 0, self.width, self.height,
            0, 0, render)
            return render
        
        def event(self, ev, x, y, st):
            import pygame
            handled = False
            if not self.is_focused():
                return None
            self.hover = ((x > 0 and x < self.width) and (y > 0 and y < self.height))
            if ev.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                if renpy.map_event(ev, "mousedown_1") and self.hover == True and config.allow_skipping == True and (renpy.game.preferences.skip_unseen or renpy.game.context().seen_current(True)):
                    config.skipping = True
                    handled = True
                elif config.skipping == True and (self.hover == False or renpy.map_event(ev, "mouseup_1")):
                    config.skipping = False
                    handled = True
            elif config.skipping == True and self.hover == False:
                config.skipping = False
                handled = True
            
            
            if handled == True:
                raise renpy.display.core.IgnoreEvent() 
            
            return self.child.event(ev, x, y, st)
        
        def focus(self, default=False):
            super().focus(default)
        
        def unfocus(self, default=False):
            super().unfocus(default)
            self.hover = False
            config.skipping = False
        
        def visit(self):
            return [self.child]


    renpy.register_shader('radial_alpha', variables="""
    uniform sampler2D tex0;
    uniform vec2 u_model_size;
    varying vec2 v_uv;
    uniform sampler2D u_gradient;
    uniform float u_prog;
""", vertex_300="""
    v_uv = a_position.xy / u_model_size;
""", fragment_300="""
    vec4 col = texture2D(tex0, v_uv);
    float grad = step(texture2D(u_gradient, v_uv).r, u_prog);
    gl_FragColor = col * grad;
""")

    def get_automode_time():
        if renpy.display.interface is None:
            return 0.0
        if renpy.display.interface.timeout_time is None:
            return 0.0
        return renpy.display.interface.timeout_time - renpy.display.core.get_time()

image radial_alpha_texture = "gui/radial_gradient.png"

transform radial_alpha(wait_timer, gradient_texture="radial_alpha_texture"):
    shader 'radial_alpha'
    u_gradient gradient_texture
    u_prog 0.0
    linear wait_timer u_prog 1.0





style default:
    font gui.text_font
    size get_variable_size(gui.text_size, gui.max_text_size, gui.text_scale)
    color gui.text_color
    outlines get_scaled_outlines([(2, "#000000aa", 0, 0)], gui.text_size, gui.max_text_size, gui.text_scale)
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines get_scaled_outlines([(10, "#000", 0, 0)], gui.text_size, gui.max_text_size, gui.text_scale)
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale)
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

style normal is default:
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale)
    ypos gui.dialogue_ypos

    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size get_variable_size(24, 36, gui.text_scale)
    color "#000"
    font gui.text_font
    text_align 0.5
    outlines []

style poemgame_button is button:
    xsize 226
    ysize 63

style poemgame_text:
    yalign 0.5
    font gui.halogen_font
    size get_variable_size(30, 36, gui.text_scale)
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines get_scaled_outlines([(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)], 30, 36, gui.text_scale)

style gui_text:
    font gui.interface_text_font
    color gui.interface_text_color
    size get_variable_size(gui.interface_text_size, gui.max_interface_text_size, gui.text_scale)

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    size get_variable_size(gui.button_text_size, gui.max_button_text_size, gui.text_scale)
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size get_variable_size(gui.label_text_size, gui.max_label_text_size, gui.text_scale)

style prompt_text is gui_text:
    color gui.text_color
    size get_variable_size(gui.interface_text_size, gui.max_interface_text_size, gui.text_scale)







style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/slider/horizontal_hover_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True
    thumb_offset (8, 8)

style vscrollbar_hc is vscrollbar:
    base_bar Frame("gui/scrollbar/vertical_poem_bar_hc.png", tile=False)
    thumb Frame("gui/slider/horizontal_hover_thumb_hc.png", left=6, top=6, tile=True)







style slider:
    ysize (34 if renpy.mobile else 18)
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Transform("gui/slider/horizontal_hover_thumb.png", zoom=(1.0 if renpy.mobile else 0.7), anchor=(0.5, 0.5))
    thumb_offset 8

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
    thumb_offset (8, 8)

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style virtual_desktop_confirm_text is virtual_desktop_text:
    size get_variable_size(24, 32)
    text_align 0.5
    xalign 0.5

style virtual_desktop_confirm_button_text is virtual_desktop_text:
    size get_variable_size(24, 32)
    xalign 0.5
    yalign 0.5
    hover_color "#D33582"




image textbox_border:
    Frame(Image("gui/textbox_border.png", oversample=3), 42, 42)
image textbox_highlight:
    Image("gui/textbox_highlight.png", oversample=3, xalign=0.5, yalign=1.0)
image textbox_alphamask:
    Frame(Image("gui/textbox_alphamask.png", oversample=3), 42, 42)
image textbox_alphamask_opaque:
    Frame(Image("gui/textbox_alphamask_opaque.png", oversample=3), 42, 42)
image textbox_buttonglare:
    Fixed(Frame(Image("gui/textbox_tile.png", oversample=3), tile=True), Crop((0,0,1.0,1.0), Frame("gui/quick_button_highlight.png")), fit_first=True)

init python:

    def textbox_frame(high_contrast=False, opaque=False, dots=True, glare=True, button_glare=False):
        
        alphamask = ("textbox_alphamask_opaque" if opaque else "textbox_alphamask")
        bg_glare = Crop((0,0,1.0,1.0), "textbox_highlight") if glare else Solid("#00000000")
        if button_glare and glare:
            bg_glare = Crop((0,0,1.0,1.0), Frame("gui/quick_button_highlight.png"))
        bg = Solid("#ffbde1")
        if high_contrast:
            bg = Solid("#39051d")
        elif dots:
            bg = Image("gui/textbox_tile.png", oversample=3)
        
        r = Fixed(
        Transform(AlphaMask(Fixed(Frame(bg, tile=True), bg_glare, fit_first=True), alphamask), xalign=0.5, yalign=0.5, zoom=1.002), 
        Frame(Image("gui/textbox_border.png", oversample=3), 42, 42)) 
        
        
        return r



image textbox_background = textbox_frame()
image textbox_background_opaque = textbox_frame(opaque=True)
image textbox_background_hc = textbox_frame(high_contrast=True, glare=False)
image textbox_background_hc_opaque = textbox_frame(high_contrast=True, opaque=True, glare=False)
image rounded_frame_background = textbox_frame(dots=False)
image rounded_frame_background_opaque = textbox_frame(opaque=True, dots=False)
image rounded_frame_background_hc = textbox_frame(high_contrast=True, glare=False)
image rounded_frame_background_hc_opaque = textbox_frame(high_contrast=True, opaque=True, glare=False)

image mobile_quick_button_background:
    textbox_frame(high_contrast=persistent.high_contrast, opaque=persistent.reduce_transparency, dots=True, glare=not persistent.high_contrast, button_glare=True)

transform mobile_quick_menu_icon:
    align (0.94, 0.1)
    xanchor 0.5
    yanchor 0.5


    on show:
        alpha 0.0
        zoom 0.7
        pause 0.05
        parallel:
            ease_quad 0.1 alpha 1.0
        parallel:
            easein_quad 0.1 zoom 1.0
    on hide:
        parallel:
            ease_quad 0.1 alpha 0.0
        parallel:
            easeout_quad 0.1 zoom 0.7
transform mobile_quick_menu_close_icon_spin:
    align (0.94, 0.1)
    xanchor 0.5
    yanchor 0.5
    xysize (100, 100)
    on show:
        alpha 0.0
        transform_anchor True
        rotate_pad True
        rotate 90
        parallel:
            easein_elastic 1.0 rotate 0
        parallel:
            easeout_quad 0.1 alpha 1.0
    on hide:
        transform_anchor True
        rotate_pad True
        rotate 0
        parallel:
            easeout_elastic 1.0 rotate 90
        parallel:
            easeout_quad 0.1 alpha 0.0


















default mobile_quick_menu_open = False

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background "saybox_background"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who" at loc_text_fit
        if not renpy.mobile:
            use quick_menu

    if renpy.mobile and quick_menu:
        use mobile_quick_menu
    elif renpy.mobile and not quick_menu:
        if config.skipping:

            $ config.skipping = False



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale) + (gui.dialogue_xpos * 2)
    yalign gui.textbox_yalign
    ysize get_variable_size(gui.textbox_height, gui.max_textbox_height, gui.text_scale)
    background "textbox_background"

style window_monika is window:
    background Frame(Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0))

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize get_variable_size(gui.namebox_width, gui.max_namebox_width, gui.text_scale)
    ypos gui.name_ypos
    ysize get_variable_size(gui.namebox_height, gui.max_namebox_height, gui.text_scale)
    yanchor 1.0

    background Frame("gui/namebox.png")
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_text_font
    size get_variable_size(gui.name_text_size, gui.max_name_text_size, gui.text_scale)
    xalign gui.name_xalign
    yalign 0.5
    outlines get_scaled_outlines([(3, "#b59", 0, 0), (1, "#b59", 1, 1)], gui.name_text_size, gui.max_name_text_size, gui.text_scale)

style say_dialogue:
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xfill True
    ypos gui.dialogue_ypos
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale)
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

image saybox_background:
    textbox_frame(high_contrast=persistent.high_contrast, opaque=persistent.reduce_transparency, dots=True, glare=not persistent.high_contrast)

image ctc_image:
    subpixel True
    alpha 0.0
    xoffset -5
    Transform("gui/ctc.png", zoom=res_ratio)
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

image auto_ctc_base = Transform("gui/auto_ctc_base.png", zoom=res_ratio)
image auto_ctc_fill = Transform("gui/auto_ctc_fill.png", zoom=res_ratio)

transform auto_ctc_pos:
    zoom 0.7
    yalign 0.98
    xoffset -5
    alpha 0.0
    easeout 0.1 alpha 0.8
    on hide:
        easeout 0.1 alpha 0.0

screen ctc:
    fixed at auto_ctc_pos:
        style "ctc_fixed"

        if _preferences.afm_enable == True:
            add "auto_ctc_base" at auto_ctc_pos:
                fit "cover"
                align (0.5, 0.5)
            add "auto_ctc_fill" at radial_alpha(wait_timer=get_automode_time()), auto_ctc_pos:
                fit "cover"
                align (0.5, 0.5)
        else:
            add "ctc_image" at auto_ctc_pos:
                fit "scale-up"
                align (0.5, 0.5)

style ctc_fixed:
    xalign gui.ctc_xalign
    xysize (round(50 * gui.ctc_zoom), round(50 * gui.ctc_zoom))












image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xpos gui.dialogue_xpos
        xanchor 0.5
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.dialogue_width
    xalign gui.dialogue_text_xalign
    text_align gui.dialogue_text_xalign

style input:
    caret "input_caret"
    xmaximum gui.dialogue_width
    xalign 0.5
    text_align 0.5










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    xsize get_variable_size(gui.choice_button_width, gui.max_choice_button_width, gui.text_scale)
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    size get_variable_size(gui.choice_button_text_size, gui.max_choice_button_text_size, gui.text_scale)
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)






screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            if persistent.high_contrast == True:
                style_prefix "quick_highcontrast"
            else:
                style_prefix "quick"

            xalign 0.5
            yalign 0.995


            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip()
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action [ShowMenu('save'), SensitiveIf(renpy.get_screen('save') == None and in_side_story is not True)]
            textbutton _("Load") action [ShowMenu('load'), SensitiveIf(renpy.get_screen('load') == None and in_side_story is not True)]


            textbutton _("Settings") action ShowMenu('preferences')





init python:
    config.overlay_screens.append("auto_indicator")

default quick_menu = True




style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size get_variable_size(gui.quick_button_text_size, gui.max_quick_button_text_size, gui.text_scale)
    outlines []

style quick_hbox:
    spacing get_variable_size(gui.quick_menu_spacing, gui.max_quick_menu_spacing, gui.text_scale)

style quick_highcontrast_button_text is quick_button_text:
    color "#ffd1f0"
    hover_color "#6f3636"
    selected_color "#522"

image mobile_quick_menu_divider:
    Transform(Solid(gui.interface_text_color), xsize=120, ysize=2)

transform mobile_quick_menu_frame_atl:
    on show:
        alpha 0.0
        yoffset -50
        parallel:
            easein_quad 0.2 alpha 1.0
        parallel:
            easein_quad 0.2 yoffset 0
    on hide:
        alpha 1.0
        yoffset 0
        parallel:
            pause 0.1
            easeout_quad 0.1 alpha 0.0
        parallel:
            easeout_quad 0.2 yoffset -50

transform mobile_quick_menu_side_frame_atl:
    on show:
        alpha 0.0
        xoffset 50
        parallel:
            easein_quad 0.2 alpha 1.0
        parallel:
            easein_quad 0.2 xoffset 0
    on hide:
        alpha 1.0
        xoffset 0
        parallel:
            pause 0.1
            easeout_quad 0.1 alpha 0.0
        parallel:
            easeout_quad 0.2 xoffset 50


screen mobile_quick_menu():

    zorder 200

    showif mobile_quick_menu_open == True:
        button at mobile_quick_menu_close_icon_spin:
            action SetVariable("mobile_quick_menu_open", False)
            add "gui/quick_menu_close_icon.png" fit "scale-down"
            activate_sound "gui/sfx/hover.ogg"

        frame at mobile_quick_menu_frame_atl:
            xalign 0.5
            yalign 0.0

            if persistent.high_contrast == True:
                style_prefix "mobile_quick_highcontrast"
            else:
                style_prefix "mobile_quick"


            hbox:
                spacing 12
                xsize 1.0
                yalign 0.0
                button:
                    action ShowMenu('history')
                    has fixed
                    text _("History") at loc_text_fit
                button:
                    action [ShowMenu('save'), SensitiveIf(in_side_story is not True)]
                    has fixed
                    text _("Save") at loc_text_fit
                button:
                    action [ShowMenu('load'), SensitiveIf(in_side_story is not True)]
                    has fixed
                    text _("Load") at loc_text_fit
                button:
                    action ShowMenu('preferences')
                    has fixed
                    text _("Settings") at loc_text_fit


        if not hide_quick_skip_and_auto:
            frame at mobile_quick_menu_side_frame_atl:
                yalign 0.5
                xalign 0.98
                if persistent.high_contrast == True:
                    style_prefix "mobile_quick_highcontrast"
                else:
                    style_prefix "mobile_quick"

                vbox:
                    spacing 55

                    add MobileSkipButton("mobile_quick_skip_button"):
                        xysize (100, 100)

                    button:
                        xysize (100, 100)
                        padding (0, 0)
                        yanchor 0.0
                        action [Preference("auto-forward", "toggle"), SetVariable("mobile_quick_menu_open", False)]
                        add "mobile_quick_auto_icon" xysize (100, 100) align (0.5, 0.5) yanchor 0.5
    elif not _preferences.afm_enable:
        button at mobile_quick_menu_icon:
            ysize 100
            action [Preference("auto-forward", "disable"), SetVariable("mobile_quick_menu_open", True)]
            activate_sound "gui/sfx/hover.ogg"
            add "gui/quick_menu_icon.png" fit "contain" zoom 0.8 yalign 0.5

image mobile_quick_skip_button:
    Fixed(Frame("mobile_quick_button_background"), Transform("mobile_quick_skip_icon", xysize=(70, 70), align=(0.6,0.5), yanchor=0.5))

style mobile_quick_frame:
    background None
    padding (0, 0)

style mobile_quick_button:
    background Frame("mobile_quick_button_background")
    ysize 120
    xmaximum 170
    yalign 0.0
    yoffset -40

style mobile_quick_fixed:
    xminimum 120
    xalign 0.5

style mobile_quick_vbox:
    spacing 12

style mobile_quick_text:
    font gui.interface_text_font
    layout "nobreak"
    outlines []
    color gui.quick_button_text_idle_color
    selected_color gui.quick_button_text_selected_color
    insensitive_color gui.quick_button_text_insensitive_color
    size get_variable_size(26, 34, gui.text_scale)
    xalign 0.5
    yalign 0.75

style mobile_quick_highcontrast_frame is mobile_quick_frame
style mobile_quick_highcontrast_button is mobile_quick_button
style mobile_quick_highcontrast_fixed is mobile_quick_fixed

style mobile_quick_highcontrast_text is mobile_quick_text:
    color gui.text_color
    outlines get_scaled_outlines([(2, "#000000aa", 0, 0)], gui.text_size, gui.max_text_size, gui.text_scale)
    selected_color "#522"
    hover_color "#6f3636"

image mobile_quick_skip_icon:
    ("gui/mobile_quick_menu_skip_icon_hc.png" if persistent.high_contrast else "gui/mobile_quick_menu_skip_icon.png")

image mobile_quick_auto_icon:
    ("gui/mobile_quick_menu_auto_icon_hc.png" if persistent.high_contrast else "gui/mobile_quick_menu_auto_icon.png")

transform loc_text_fit:
    fit "scale-down"












init python:
    def FinishEnterName():
        if not player: 
            if renpy.mobile:
                renpy.hide_screen("name_input")
            return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

screen navigation():

    if main_menu:
        add "menu_nav"
    else:
        add "game_nav"

    vbox:
        style_prefix "navigation"

        if renpy.mobile:
            xpos gui.navigation_xpos
            spacing gui.max_navigation_spacing
        else:
            xpos get_variable_size(gui.max_navigation_xpos, gui.navigation_xpos, gui.text_scale)
            spacing get_variable_size(gui.navigation_spacing, gui.max_navigation_spacing, gui.text_scale)

        yanchor 1.0
        yalign 0.85
        xmaximum 200

        if not persistent.autoload or not main_menu:

            if main_menu:

                if persistent.playthrough == 1:

                    button:
                        text (_("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") if gui.text_scale <= 0.4 else _("ŔŗñĮ¼»ŧþ")) at loc_text_fit style "navigation_button_text"
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:

                    button:
                        text _("New Game") at loc_text_fit style "navigation_button_text"
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

            else:


                button:
                    text _("History") at loc_text_fit style "navigation_button_text"
                    action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]


                button:
                    text _("Save Game") at loc_text_fit style "navigation_button_text"
                    action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None and in_side_story is not True)]


            button:
                text _("Load Game") at loc_text_fit style "navigation_button_text"
                action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None and in_side_story is not True)]


            button:
                text _("Settings") at loc_text_fit style "navigation_button_text"
                action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]



            if renpy.variant("pc"):


                textbutton _("Help") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))] at loc_text_fit

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True) at loc_text_fit

            elif not main_menu:
                if persistent.playthrough != 3:

                    button:
                        text _("Main Menu") at loc_text_fit style "navigation_button_text"
                        action [MainMenu(), SensitiveIf(in_side_story is not True)]
                else:

                    button:
                        text _("Main Menu") at loc_text_fit style "navigation_button_text"
                        action [NullAction(), SensitiveIf(in_side_story is not True)]





            button:
                text _("Exit DDLC") at loc_text_fit style "navigation_button_text"
                if not persistent.seen_bios:
                    action Confirm("Exit DDLC and return to the desktop?", Start("desktop_start"), [Hide(), unlock("dont_quit")])
                else:
                    action Confirm("Exit DDLC and return to the desktop?", Jump("desktop_from_main"), [Hide(), unlock("dont_quit")])
        else:
            timer 1.75 action Start("autoload_yurikill")


style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    size (gui.max_button_text_size if renpy.mobile else get_variable_size(gui.button_text_size, gui.max_button_text_size, gui.text_scale))

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    ysize 54
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    layout "nobreak"
    font gui.riffic_font
    color "#fff"
    outlines get_scaled_outlines([(4, "#b59", 0, 0), (2, "#b59", 2, 2)], (gui.max_button_text_size if renpy.mobile else gui.button_text_size), gui.max_button_text_size, gui.text_scale)
    hover_outlines get_scaled_outlines([(4, "#fac", 0, 0), (2, "#fac", 2, 2)], (gui.max_button_text_size if renpy.mobile else gui.button_text_size), gui.max_button_text_size, gui.text_scale)
    insensitive_outlines get_scaled_outlines([(4, "#fce", 0, 0), (2, "#fce", 2, 2)], (gui.max_button_text_size if renpy.mobile else gui.button_text_size), gui.max_button_text_size, gui.text_scale)








screen main_menu():
    tag menu



    style_prefix "main_menu"

    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
        frame




        use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version!t]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"

        if renpy.mobile:
            timer 4.0 action Show("fullscreen_return_button")
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m"
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

screen fullscreen_return_button:
    button:
        xysize (1.0,1.0)
        action Jump("quit")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background None

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size












screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None, yinitial=0.0):


    if main_menu and not in_side_story:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    use navigation

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if renpy.get_screen("history"):
                background Frame("history_background")
                padding (10, 10)
                xsize 1.0

            if scroll == "viewport":

                viewport:
                    at vp_vert_scroll_mask
                    scrollbars "vertical"
                    vscrollbar_xoffset -30
                    mousewheel True
                    draggable True
                    yinitial yinitial

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude



    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0 and persistent.content_warnings_enabled == False:
        on "show" action Show("game_menu_m")

    textbutton _("Return"):
        style "return_button"
        if renpy.mobile:
            xpos gui.navigation_xpos
        else:
            xpos get_variable_size(gui.max_navigation_xpos, gui.navigation_xpos, gui.text_scale)
        action Return()

    label title xoffset -16

    if main_menu and not in_side_story:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 30

    background None

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font gui.riffic_font
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos get_variable_size(gui.max_navigation_xpos, gui.navigation_xpos, gui.text_scale)
    yalign 1.0
    yoffset -30

image history_background:
    textbox_frame(high_contrast=persistent.high_contrast, opaque=persistent.reduce_transparency, dots=False, glare=False)








screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            unlock("sayori_load_fail")                                                                                                                                       
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
            ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.autoload == "yuri_kill_2" and renpy.current_screen().screen_name[0] == "load":
            
            return [Function(increment_yuri_kill), Jump("yuri_kill_from_load")]
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"


                xalign 0.5


                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        if renpy.mobile:
                            text FileTime(slot, format=_("{#file_time}%x %I:%M %p"), empty=_("empty slot")):
                                style "mobile_slot_time_text"
                        else:
                            text FileTime(slot, format=_("{#file_time}%x %I:%M %p"), empty=_("empty slot")):
                                style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset (-50 if renpy.mobile else 0)

                spacing gui.page_spacing








                for page in range(1, 10):
                    textbutton "[page!t]" action FilePage(page)


            if renpy.mobile:
                imagebutton:
                    xalign 0.0
                    yalign 0.5
                    action FilePagePrevious(max=9, wrap=True, auto=False, quick=False)
                    idle Transform("gui/settings_arrow.png", zoom=0.75, rotate=180)
                    hover Transform("gui/settings_arrow_selected.png", zoom=0.75, rotate=180)
                imagebutton:
                    xalign 1.0
                    yalign 0.5
                    action FilePageNext(max=9, wrap=True, auto=False, quick=False)
                    idle Transform("gui/settings_arrow.png", zoom=0.75)
                    hover Transform("gui/settings_arrow_selected.png", zoom=0.75)



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []

style mobile_slot_time_text is slot_button_text:
    size 24









image pref_background:
    textbox_frame(high_contrast=persistent.high_contrast, opaque=persistent.reduce_transparency, dots=False, glare=False)

screen preferences():
    tag menu
    default current_tab = "display"
    default music_volume_value = preferences.get_mixer("music")
    default sfx_volume_value = preferences.get_mixer("sfx")
    on "show" action [Function(settings_sanity_check), SetScreenVariable("music_volume_value", preferences.get_mixer("music")), SetScreenVariable("sfx_volume_value", preferences.get_mixer("sfx"))]
    on "replace" action Function(settings_sanity_check)


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings")):

        side "t c":
            hbox:
                xalign 0.5
                button:
                    style ("pref_active_tab_button" if current_tab == "display" else "pref_tab_button")
                    action SetScreenVariable("current_tab", "display")
                    left_padding 10
                    has side 'l c'
                    if renpy.mobile:
                        add ("gui/pref_display_icon_mobile_selected.png" if current_tab == "display" else "gui/pref_display_icon_mobile.png"):
                            yalign 0.75
                            zoom 0.5
                    else:
                        add ("gui/pref_display_icon_selected.png" if current_tab == "display" else "gui/pref_display_icon.png"):
                            yalign 0.75
                            zoom 0.5
                    label ("Audio" if renpy.mobile else "Graphics & Sound") yalign 0.0 style "pref_tab_label" text_size 24 at loc_text_fit
                button:
                    style ("pref_active_tab_button" if current_tab == "language" else "pref_tab_button")
                    action [SetScreenVariable("current_tab", "language"), Function(settings_sanity_check)]
                    has side 'l c'
                    add ("gui/pref_language_icon_selected.png" if current_tab == "language" else "gui/pref_language_icon.png"):
                        yalign 0.75
                        zoom 0.5
                    label "Language & Text" yalign 0.0 style "pref_tab_label" text_size 24 at loc_text_fit
                button:
                    style ("pref_active_tab_button" if current_tab == "accessibility" else "pref_tab_button")
                    action SetScreenVariable("current_tab", "accessibility")
                    has side 'l c'
                    add ("gui/pref_accessibility_icon_selected.png" if current_tab == "accessibility" else "gui/pref_accessibility_icon.png"):
                        yalign 0.75
                        zoom 0.25
                    label "Accessibility" yalign 0.0 style "pref_tab_label" text_size 24 at loc_text_fit
            frame:
                padding (30,30)
                background "pref_background"

                showif current_tab == "display":
                    vbox:







                        fixed:
                            ysize 200

                            if not renpy.mobile:
                                vbox:
                                    style_prefix "radio"
                                    xalign 0.0
                                    label _("Display")
                                    textbutton _("Window") action Preference("display", "window")
                                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                            vbox:
                                style_prefix "slider"
                                xalign (1.0 if not renpy.mobile else 0.0)
                                ysize 1.0
                                if config.has_music:
                                    label _("Music Volume")

                                    side "c l r":
                                        bar:
                                            value ScreenVariableValue("music_volume_value", range=1.0, offset=0, step=0.1, force_step=True, style="slider")
                                            changed preferences.set_mixer("music", music_volume_value)
                                        add "slider_volume_icon_min" yalign 0.5 zoom 0.5
                                        add "slider_volume_icon_max" yalign 0.5 zoom 0.5

                                if config.has_sound:

                                    label _("Sound Volume")

                                    side "c l r":
                                        bar:
                                            value ScreenVariableValue("sfx_volume_value", range=1.0, offset=0, step=0.1, force_step=True, style="slider")
                                            changed preferences.set_mixer("sfx", sfx_volume_value)
                                        add "slider_volume_icon_min" yalign 0.5 zoom 0.5
                                        add "slider_volume_icon_max" yalign 0.5 zoom 0.5

                                    if config.sample_sound:
                                        textbutton _("Test") action Play("sound", config.sample_sound)

                                if config.has_voice:
                                    label _("Voice Volume")

                                    side "c l r":
                                        bar value Preference("voice volume")
                                        add "slider_volume_icon_min" yalign 0.5 zoom 0.5
                                        add "slider_volume_icon_max" yalign 0.5 zoom 0.5
                                    if config.sample_voice:
                                        textbutton _("Test") action Play("voice", config.sample_voice)

                                if config.has_music or config.has_sound or config.has_voice:
                                    null height gui.pref_spacing






















                elif current_tab == "language":
                    vbox:

                        hbox:
                            style_prefix "slider"
                            box_wrap False

                            vbox:
                                label _("Text Speed")


                                side "c l r":
                                    bar value FieldValue(_preferences, "text_cps", range=180, step=30, force_step=True, max_is_zero=False, style="slider", offset=20):
                                        alt "Text Speed"
                                    add "slider_autopace_icon_min" yalign 0.5 zoom 0.5
                                    add "slider_autopace_icon_max" yalign 0.5 zoom 0.5

                                label _("Auto Mode Pace")

                                side "c l r":
                                    bar value FieldValue(_preferences, "afm_time", range=18, offset=1, step=3, style="slider", force_step=True):
                                        bar_invert True
                                    add "slider_autopace_icon_min" yalign 0.5 zoom 0.5
                                    add "slider_autopace_icon_max" yalign 0.5 zoom 0.5

                                label _("Text Size")

                                side "c l r":

                                    bar value FieldValue(_preferences, "text_scale", style="slider", range=0.5, offset=0.5, step=0.25, force_step=True):
                                        released gui.SetPreference("text_scale", preferences.text_scale)
                                        alt "Text Size"
                                    add "slider_textsize_icon_min" yalign 0.5 zoom 0.5
                                    add "slider_textsize_icon_max" yalign 0.5 zoom 0.5
                            vbox:
                                xsize 1.0
                                if renpy.mobile:
                                    style_prefix "radio"
                                    label _("Allow Skipping:")
                                    textbutton _("Previously-read text only") action Preference("skip", "seen")
                                    textbutton _("All text") action Preference("skip", "all")
                                else:
                                    style_prefix "check"
                                    label _("Skip")
                                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                                    textbutton _("After Choices") action Preference("after choices", "toggle")


                        null height 40

                        if persistent.high_contrast == True:
                            add "gui/long_divider_dark_hc.png":
                                xzoom 0.65
                                yzoom 0.80
                                xoffset 30
                        else:
                            add "gui/long_divider_dark.png":
                                xzoom 0.65
                                yzoom 0.80
                                xoffset 30

                        null height 14


                        label _("Language") style "slider_label"

                        hbox:
                            xsize 1.0
                            fixed:
                                xysize (get_variable_size_f(0.6, 0.7, gui.text_scale), get_variable_size(40, 70, gui.text_scale))
                                imagebutton:
                                    xalign 0.0
                                    yalign 0.5
                                    action Function(settings_scroll_language, increment=-1)
                                    idle Transform("settings_arrow", zoom=0.4, rotate=180)
                                    hover Transform("settings_arrow_selected", zoom=0.4, rotate=180)
                                text str(settings_localized_languages[settings_available_languages.index(settings_language)]):
                                    font "NotoSansCJKjp-Regular.otf"
                                    xalign 0.5
                                    textalign 0.5
                                    xmaximum 0.9
                                    yalign 0.5
                                imagebutton:
                                    xalign 1.0
                                    yalign 0.5
                                    action Function(settings_scroll_language, increment=1)
                                    idle Transform("settings_arrow", zoom=0.4)
                                    hover Transform("settings_arrow_selected", zoom=0.4)
                            fixed:
                                xysize (1.0, get_variable_size(40, 70, gui.text_scale))
                                textbutton _("Apply") style "apply_button":
                                    action Function(settings_apply_language)
                                    sensitive (settings_language != preferences.language)
                                    align (0.5, 0.5)

                elif current_tab == "accessibility":
                    viewport id "settings_accessibility_vp":
                        at vp_vert_scroll_mask
                        draggable True
                        ysize 1.0
                        has vbox
                        null height 20

                        vbox:
                            style_prefix "check"
                            xsize 1.0

                            textbutton _("Content Warnings") action ToggleField(persistent, "content_warnings_enabled", True, False) alt "Enable Content Warnings"
                            text _("Enables content warnings that will appear before scenes with disturbing subject matter.") style "pref_hint_text"
                            textbutton _("High Contrast Text Boxes") action [ToggleField(persistent, "high_contrast", True, False), Function(gui.rebuild)] alt "High Contrast Text Boxes"
                            text _("Replaces the dialogue box with a darker variant, making dialogue easier to read.") style "pref_hint_text"
                            textbutton _("Reduce Textbox Transparency") action [ToggleField(persistent, "reduce_transparency", True, False), Function(gui.rebuild)] alt "Reduce Textbox Transparency"
                            text _("Makes the dialogue box opaque, making dialogue easier to read.") style "pref_hint_text"
                            textbutton _("Alternate Poem Font") action ToggleField(persistent, "use_alt_poem_font", True, False) alt "Use Alternate Poem Font" style "check_button"
                            text _("Switches handwritten fonts in characters' poems with an easier-to-read font.") style "pref_hint_text"

                        null height 20
                        button:
                            action OpenURL("https://teamsalvato.com/ddlc-warnings")
                            has fixed
                            fit_first True
                            add "gui/large_button_rounded.png" fit "scale-down" xsize 700 ycenter 0.5
                            text _("Open Full-Disclosure Content Warnings Page"):
                                font gui.halogen_font
                                outlines []
                                color "#b59"
                                xcenter 0.5
                                ycenter 0.5
                                size 30
                        null height 80
                    vbar value YScrollValue("settings_accessibility_vp") xpos 1.0 xoffset -10 style ("vscrollbar" if not persistent.high_contrast else "vscrollbar_hc")







































































































    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style apply_button_text is confirm_button_text:
    size get_variable_size(28, 40, gui.text_scale)
    outlines (get_scaled_outlines([(3, "#b59", 0, 0), (1, "#b59", 1, 1)], 24, 34, gui.text_scale) if not persistent.high_contrast else get_scaled_outlines([(2, gui.hc_label_outline_color, 0, 0), (1, gui.hc_label_outline_color, 1, 1)], 24, 34, gui.text_scale))
    insensitive_outlines (get_scaled_outlines([(3, "#fce", 0, 0), (1, "#fce", 1, 1)], 24, 34, gui.text_scale) if not persistent.high_contrast else get_scaled_outlines([(2, "#b59", 0, 0), (1, "#b59", 1, 1)], 24, 34, gui.text_scale))
    insensitive_color ("#fff" if not persistent.high_contrast else "#ebbfddff")

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font gui.riffic_font
    size get_variable_size(24, 28, gui.text_scale)
    color "#fff"
    outlines (get_scaled_outlines([(3, "#b59", 0, 0), (1, "#b59", 1, 1)], 24, 28, gui.text_scale) if not persistent.high_contrast else get_scaled_outlines([(2, gui.hc_label_outline_color, 0, 0), (1, gui.hc_label_outline_color, 1, 1)], 24, 28, gui.text_scale))
    yalign 1.0

style pref_tab_button:
    xysize (300, 60)
    yalign 1.0
    background Frame("gui/namebox-deselected.png", 3, 3)
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound
    yoffset 9
style pref_active_tab_button is pref_tab_button:
    background Frame("gui/namebox-selected.png", 3, 3)
    yoffset 0
style pref_tab_label is pref_label
style pref_tab_label_text is pref_label_text:
    outlines [(4, "#b59", 0, 0), (1, "#b59", 1, 1)]
    layout "nobreak"

style pref_header_label is pref_label
style pref_header_label_text is pref_label_text:
    size get_variable_size(28, 38, gui.text_scale)
    outlines get_scaled_outlines([(4, "#b59", 0, 0), (1, "#b59", 1, 1)], 28, 38, gui.text_scale)

style pref_hint_text:
    font gui.halogen_font
    size get_variable_size(24, 30, gui.text_scale)
    outlines []
    color ("#b59" if not persistent.high_contrast else "#ffdfee")
    xoffset get_variable_size(40, 60, gui.text_scale)
    xmaximum 800

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing get_variable_size(gui.pref_button_spacing, gui.max_pref_button_spacing, gui.text_scale)

image check_foreground:
    Transform(("gui/button/check_foreground.png" if not persistent.high_contrast else "gui/button/check_foreground_hc.png"), yalign=0.5, zoom=0.5)
image check_selected_foreground:
    Transform(("gui/button/check_selected_foreground.png" if not persistent.high_contrast else "gui/button/check_selected_foreground_hc.png"), yalign=0.5, zoom=0.5)

image settings_arrow:
    ("gui/settings_arrow.png" if not persistent.high_contrast else "gui/settings_arrow_hc.png")

image settings_arrow_selected:
    ("gui/settings_arrow_selected.png" if not persistent.high_contrast else "gui/settings_arrow.png")

image slider_volume_icon_min:
    ("gui/slider_volume_icon_min.png" if not persistent.high_contrast else "gui/slider_volume_icon_hc_min.png")
image slider_volume_icon_max:
    ("gui/slider_volume_icon_max.png" if not persistent.high_contrast else "gui/slider_volume_icon_hc_max.png")

image slider_autopace_icon_min:
    ("gui/slider_autopace_icon_min.png" if not persistent.high_contrast else "gui/slider_autopace_icon_hc_min.png")
image slider_autopace_icon_max:
    ("gui/slider_autopace_icon_max.png" if not persistent.high_contrast else "gui/slider_autopace_icon_hc_max.png")

image slider_textsize_icon_min:
    ("gui/slider_textsize_icon_min.png" if not persistent.high_contrast else "gui/slider_textsize_icon_hc_min.png")
image slider_textsize_icon_max:
    ("gui/slider_textsize_icon_max.png" if not persistent.high_contrast else "gui/slider_textsize_icon_hc_max.png")


style radio_button:
    properties gui.button_properties("radio_button")
    foreground "check_[prefix_]foreground"
    yminimum get_variable_size(24, 32, gui.text_scale)
    ymaximum get_variable_size(48, 64, gui.text_scale)

style radio_button_text is default:
    properties gui.button_text_properties("radio_button")



style check_vbox:
    spacing get_variable_size(gui.pref_button_spacing, gui.max_pref_button_spacing, gui.text_scale)

style check_button:
    properties gui.button_properties("check_button")
    foreground "check_[prefix_]foreground"
    ysize get_variable_size(24, 32, gui.text_scale)

style check_button_text is default:
    properties gui.button_text_properties("check_button")



style slider_slider:
    xsize 350
    base_bar ("gui/scrollbar/horizontal_poem_bar_short.png" if not persistent.high_contrast else "gui/scrollbar/horizontal_poem_bar_short_hc.png")
    thumb ("gui/slider/horizontal_hover_thumb.png" if not persistent.high_contrast else "gui/slider/horizontal_hover_thumb_hc.png")
    yalign 0.5

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what:
                    ypos (gui.history_text_ypos if h.who else gui.history_name_ypos)
            null height get_variable_size(12, 15)

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text is namebox_label:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    xalign 0.0
    layout "nobreak"

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5












































































































































































screen name_input(message, ok_action):



    default inv = VariableInputValue("player")


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    if renpy.mobile:
        key "K_RETURN" action [inv.Disable(), Play("sound", gui.activate_sound), ok_action]
    else:
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    if renpy.mobile:

        button:
            xysize (1.0,1.0)
            action [inv.Disable(), Function(FinishEnterName)]
    frame:
        if renpy.mobile:
            yalign 0.0
            yoffset 10

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5





            fixed:
                fit_first True
                yminimum 10

                xalign 0.5
                input default "" value inv length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                if renpy.mobile:

                    button:
                        action inv.Enable()
                        xysize (get_variable_size(280, 400, gui.text_scale), 90)
                        align (0.5, 0.5)






            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action


screen dialog(message, ok_action, arg_name=None, arg_value=None):


    modal True

    zorder 200

    if not renpy.get_screen("virtual_desktop"):
        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            has vbox
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

    else:
        use virtual_desktop_confirm_dialog_popup(confirm_title_message):
            vbox:
                xalign .5
                yalign .5
                spacing 30


                if arg_name is not None:
                    if arg_name == "filename":
                        $ filename = arg_value

                text _(message):
                    style "virtual_desktop_confirm_text"
                    text_align 0.5
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 100
                    button:
                        style "virtual_desktop_framed_button"
                        ysize 54

                        action ok_action
                        text _("OK") style "virtual_desktop_confirm_button_text"

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    if not renpy.get_screen("virtual_desktop"):
        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            has vbox
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action



    else:

        $ transStr = "Are you sure you want to delete this file?"

        if message == "Are you sure you want to delete this file?\n\nmonika.chr":
            $ message = "[transStr!t]" + "\n\nmonika.chr"

        use virtual_desktop_confirm_dialog_popup(confirm_title_message):
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 75

                text _(message):
                    style "virtual_desktop_confirm_text"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    xsize 0.8
                    spacing 50

                    button:
                        style "virtual_desktop_framed_button"
                        ysize 54
                        action yes_action
                        text "Yes" style "virtual_desktop_confirm_button_text"

                    button:
                        style "virtual_desktop_framed_button"
                        ysize 54
                        action no_action
                        text "No" style "virtual_desktop_confirm_button_text"


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")

image skip_cw_cover:
    "#000000"







screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100

    style_prefix "skip"


    if not renpy.mobile:
        frame:
            has hbox
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size get_variable_size(gui.notify_text_size, gui.max_notify_text_size, gui.text_scale)

style skip_triangle:


    font "DejaVuSans.ttf"

screen auto_indicator():

    zorder 100
    showif renpy.mobile and _preferences.afm_enable:
        button:
            xysize (1.0, 1.0)
            style "gui_button"
            action Preference("auto-forward", "toggle")
        fixed at auto_indicator_atl:
            add "gui/autoplay_ddlc_white-center.png" at auto_indicator_idle_atl zoom 1.5
            add "gui/autoplayring_ddlc_white.png" at auto_indicator_idle_atl zoom 1.5

transform auto_indicator_atl:
    align (0.94, 0.1)
    xanchor 0.5
    yanchor 0.5
    on show:
        alpha 0.0
        easeout 0.1 alpha 1.0
    on replaced:
        easeout 0.05 alpha 1.0
    on hide:
        easein 0.15 alpha 0.0

transform auto_indicator_idle_atl:
    align (0.5, 0.5)
    ease 2.2 alpha 0.3
    ease 2.2 alpha 1.0
    repeat









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
