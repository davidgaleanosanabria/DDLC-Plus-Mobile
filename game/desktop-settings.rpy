

init python:

    config.font_replacement_map["fonts/HKGrotesk-Medium.otf", True, False] = ("fonts/HKGrotesk-SemiBold-rounded.otf", False, False)
    config.font_replacement_map["fonts/Vera.ttf", True, False] = ("fonts/HKGrotesk-Bold.otf", False, False)

    settings_fullscreen = preferences.fullscreen
    settings_tearing = preferences.gl_tearing
    settings_resolution = None
    settings_language = None


    settings_available_resolutions = [(640,360),(854,480),(960,540),(1024,576),(1280,720),(1366,768),(1600,900),(1920,1080)]

    settings_available_languages = [None,"spanish","spanish_latin_america","french","german","italian","portuguese","russian","korean","japanese","chinese_simplified","chinese_traditional"]
    settings_localized_languages = ["English","Español (España)","Español (Latinoamérica)","Français","Deutsch","Italiano","Português","Русский","한국어","日本語","简体中文","繁體中文"]

    def settings_sanity_check():
        global settings_resolution
        global settings_available_resolutions
        global settings_language
        global settings_available_languages
        if settings_resolution == None:
            if renpy.get_physical_size() in settings_available_resolutions:
                settings_resolution = renpy.get_physical_size()
            else:
                settings_resolution = settings_available_resolutions[7]
        
        
        if preferences.language in settings_available_languages:
            settings_language = preferences.language
        else:
            settings_language = settings_available_languages[0]
        
        lang_dialogue_pre_postfix()

    def settings_scroll_within_list(value, list, increment):
        if value in list:
            value = list[(list.index(value) + increment + len(list)) % len(list)]
        return value

    def settings_scroll_resolution(increment):
        global settings_resolution
        global settings_available_resolutions
        settings_resolution = settings_scroll_within_list(settings_resolution, settings_available_resolutions, increment)
        settings_apply_display()

    def settings_scroll_language(increment):
        global settings_language
        global settings_available_languages
        settings_language = settings_scroll_within_list(settings_language, settings_available_languages, increment)
        settings_apply_display()



    def startup_settings_apply():   
        
        lang_dialogue_pre_postfix()
        
        
        if renpy.mobile:
            return
        
        preferences.fullscreen = True 
        if plus_persistent.settings_fullscreen is False:
            preferences.fullscreen = False
        
        preferences.gl_tearing = True
        if plus_persistent.settings_vsync is False:
            preferences.gl_tearing = False
        
        if preferences.fullscreen is False:
            renpy.set_physical_size(plus_persistent.settings_resolution)

    def settings_apply_display():
        global settings_fullscreen
        global settings_tearing
        global settings_resolution
        global settings_available_resolutions
        if settings_resolution is not None and renpy.get_physical_size() != settings_resolution:
            renpy.set_physical_size(settings_resolution)
        if preferences.fullscreen is not settings_fullscreen:
            preferences.fullscreen = settings_fullscreen
        if preferences.gl_tearing is not settings_tearing:
            preferences.gl_tearing = settings_tearing
        
        plus_persistent.settings_fullscreen = settings_fullscreen
        plus_persistent.settings_vsync = settings_tearing
        plus_persistent.settings_resolution = settings_resolution
        
        renpy.save_persistent()

    def settings_apply_language():
        global settings_language
        global settings_available_languages
        if settings_language is not "" and settings_language is not preferences.language and settings_language in settings_available_languages:
            renpy.change_language(settings_language)
        
        lang_dialogue_pre_postfix()

    def lang_dialogue_pre_postfix():
        global settings_language
        lang_name = settings_language
        if lang_name == None:
            lang_name = preferences.language
        
        if lang_name == "japanese":
            store.dialogue_prefix = ''
            store.dialogue_suffix = ''
        else:
            store.dialogue_prefix = '"'
            store.dialogue_suffix = '"'

image settings_toggle_container:
    Transform("gui/virtual_desktop/settings/commentary toggle.png", xysize=(get_variable_size(40, 52), get_variable_size(26, 30)))

image settings_toggle_knob_on:
    Transform("gui/virtual_desktop/settings/settings slider scrub icon.png", xysize=(get_variable_size(16,22,gui.text_scale),get_variable_size(16,22,gui.text_scale)))

image settings_toggle_knob_off:
    Transform("gui/virtual_desktop/settings/settings slider scrub icon off.png", xysize=(get_variable_size(16,22,gui.text_scale),get_variable_size(16,22,gui.text_scale)))

screen settings_toggle_button(check):

    default toggle_text_width = get_variable_size(30, 52)
    default char_width = get_variable_size(10, 17)

    python:
        if preferences.language != None:
            toggle_text_width = get_variable_size(30, 52)
            off_len = len(renpy.translate_string("Off"))
            on_len = len(renpy.translate_string("On"))
            loc_toggle_text_width = (int(off_len * char_width) if (off_len > on_len) else int(on_len * char_width))
            if loc_toggle_text_width > 52:
                toggle_text_width = loc_toggle_text_width

    fixed:

        ymaximum 32
        xfit True
        hbox:
            spacing gui.virtual_desktop_settings_toggle_spacing
            fixed:
                fit_first True
                ysize 28

                yalign 0.5
                add "settings_toggle_container" yalign 0.5
                if not check:
                    add "settings_toggle_knob_off":

                        align (0.078, 0.5)
                        xanchor 0.0
                else:
                    add "settings_toggle_knob_on":

                        align (0.94, 0.5)
                        xanchor 1.0
            fixed:
                xsize toggle_text_width

                text (_("On") if check==True else _("Off")):
                    style "settings_text"
                    yalign 0.5
                    xalign 0.5
                    if check==True:
                        color gui.virtual_desktop_accent_color

screen settings_scroller_button(left):
    frame:
        xysize (20, 20)
        align (0.5, 0.5)
        if left:
            background Frame("/gui/virtual_desktop/music/play icon white.png") at settings_scroller_left
        else:
            background Frame("/gui/virtual_desktop/music/play icon white.png", color=gui.virtual_desktop_text_color) at settings_scroller_right

transform settings_shrink:
    zoom 0.2

transform settings_scroller_right:
    matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_text_color)
    on hover:
        matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)
    on idle:
        matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_text_color)

transform settings_scroller_left:
    xzoom -1.0
    matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_text_color)
    on hover:
        matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)
    on idle:
        matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_text_color)

image settings_tab_divider = Solid(gui.virtual_desktop_soft_accent_color, xsize=2, ysize=1.0)

transform virtual_desktop_settings_tab_text_fade:
    on show:
        xoffset 10
        alpha 0.0
        parallel:
            easein_quad 0.15 xoffset 0
        parallel:
            linear 0.2 alpha 1.0

transform virtual_desktop_settings_vbox_fade:
    on show:
        alpha 0.0
        xoffset 20
        parallel:
            easein_quad 0.15 xoffset 0
        parallel:
            linear 0.2 alpha 1.0

style virtual_desktop_settings_container_frame is virtual_desktop_frame:
    xsize 0.8
    xalign 0.5
    padding (0, 50, 0, 0)
    background None







screen virtual_desktop_settings_app:

    default current_tab = "display"

    default music_volume_value = preferences.get_mixer("music")
    default sfx_volume_value = preferences.get_mixer("sfx")

    on "show" action [Function(settings_sanity_check), SetScreenVariable("music_volume_value", preferences.get_mixer("music")), SetScreenVariable("sfx_volume_value", preferences.get_mixer("sfx"))]

    on "hide" action [Function(renpy.save_persistent)]

    $ number = get_unlock_percent()
    $ settings_spacing = get_variable_size(gui.virtual_desktop_settings_vbox_spacing, gui.virtual_desktop_settings_vbox_spacing_max, gui.text_scale)
    style_prefix "virtual_desktop"

    use virtual_desktop_app_window("Settings", window_width=get_variable_size(920,1100, gui.text_scale), taskbar_icon="desktop_Settings_H"):

        key ['mouseup_3'] action NullAction()
        key ['mouseup_2'] action NullAction()
        key ['K_ESCAPE'] action NullAction()

        style_prefix "settings"

        side "t c":
            xysize (1.0, 1.0)
            fixed:
                xysize (0.95, 60)
                xalign 0.5
                hbox:

                    add "settings_tab_divider"
                    button:
                        style "settings_tab_button"
                        action SetScreenVariable("current_tab", "display")
                        add ("gui/virtual_desktop/settings/slider_volume_icon_max.png" if renpy.mobile else "gui/virtual_desktop/plus_pref_display_icon.png") xalign 0.5 fit "scale-down"
                    add "settings_tab_divider"
                    button:
                        style "settings_tab_button"
                        action [SetScreenVariable("current_tab", "language"), Function(settings_sanity_check)]
                        add "gui/virtual_desktop/plus_pref_language_icon.png" xalign 0.5 fit "scale-down"
                    add "settings_tab_divider"
                    button:
                        style "settings_tab_button"
                        action SetScreenVariable("current_tab", "accessibility")
                        add "gui/virtual_desktop/plus_pref_accessibility_icon.png" xalign 0.5 fit "scale-down"
                    add "settings_tab_divider"

                    null width 16



















                if plus_purchased:
                    fixed:
                        xmaximum 0.3
                        ysize 1.0
                        xalign 1.0
                        text _("Data Collected: [number]%") at loc_text_fit:
                            xalign 1.0
                            yalign 0.5
                            layout "nobreak"

                hbox:
                    yalign 1.0
                    showif current_tab == "display":
                        add Solid("#00000000", ysize=2, xsize=gui.virtual_desktop_settings_tab_width+2, yalign=1.0)
                    else:
                        add Solid(gui.virtual_desktop_soft_accent_color, ysize=2, xsize=gui.virtual_desktop_settings_tab_width+2, yalign=1.0)
                    showif current_tab == "language":
                        add Solid("#00000000", ysize=2, xsize=gui.virtual_desktop_settings_tab_width+2, yalign=1.0)
                    else:
                        add Solid(gui.virtual_desktop_soft_accent_color, ysize=2, xsize=gui.virtual_desktop_settings_tab_width+2, yalign=1.0)
                    showif current_tab == "accessibility":
                        add Solid("#00000000", ysize=2, xsize=gui.virtual_desktop_settings_tab_width+2, yalign=1.0)
                    else:
                        add Solid(gui.virtual_desktop_soft_accent_color, ysize=2, xsize=gui.virtual_desktop_settings_tab_width+2, yalign=1.0)
                    add Solid(gui.virtual_desktop_soft_accent_color, ysize=2, xsize=1.0, yalign=1.0)

            frame:
                xysize (1.0, 1.0)
                background None
                padding (0, 0, 0, 0)

                showif current_tab == "display":
                    frame at virtual_desktop_settings_vbox_fade:
                        style "virtual_desktop_settings_container_frame"
                        has vbox

                        if not renpy.mobile:
                            text _("Display") style "settings_bold_text"
                            hbox:
                                style "virtual_desktop_settings_toggle_hbox"
                                text _("Resolution")
                                button:
                                    action Function(settings_scroll_resolution, increment=-1)
                                    use settings_scroller_button(True)
                                text str(settings_resolution)
                                button:
                                    action Function(settings_scroll_resolution, increment=1)
                                    use settings_scroller_button(False)
                            hbox:


                                style "virtual_desktop_settings_toggle_hbox"
                                button:
                                    action [SetVariable("settings_fullscreen", not settings_fullscreen), Function(settings_apply_display)]
                                    use settings_toggle_button(settings_fullscreen)
                                text _("Fullscreen") yalign 0.5
                            hbox:
                                style "virtual_desktop_settings_toggle_hbox"

                                button:
                                    action [SetVariable("settings_tearing", not settings_tearing), Function(settings_apply_display)]
                                    use settings_toggle_button(settings_tearing)
                                text _("Vsync") yalign 0.5

                            null height settings_spacing


                        text _("Sound") style "settings_bold_text"
                        text _("Music Volume")
                        side "c l r":
                            bar:
                                style "settings_slider"
                                value ScreenVariableValue("music_volume_value", range=1.0, offset=0, step=0.1, force_step=True)
                                changed preferences.set_mixer("music", music_volume_value)
                            add "gui/virtual_desktop/settings/slider_volume_icon_min.png" yalign 0.5 zoom 0.5
                            add "gui/virtual_desktop/settings/slider_volume_icon_max.png" yalign 0.5 zoom 0.5

                        $ jukebox_update_volume()
                        text "Sound Volume"
                        side "c l r":
                            bar:
                                style "settings_slider"
                                value ScreenVariableValue("sfx_volume_value", range=1.0, offset=0, step=0.1, force_step=True)
                                changed preferences.set_mixer("sfx", sfx_volume_value)
                            add "gui/virtual_desktop/settings/slider_volume_icon_min.png" yalign 0.5 zoom 0.5
                            add "gui/virtual_desktop/settings/slider_volume_icon_max.png" yalign 0.5 zoom 0.5
                        null height settings_spacing


                        if renpy.mobile and config.developer:
                            hbox:
                                button:
                                    action Function(debug_unlock_all)
                                    has frame
                                    xsize 420
                                    idle_background "virtual_desktop_button_outline"
                                    insensitive_background Transform("virtual_desktop_button_outline",matrixcolor=OpacityMatrix(value=0.3))
                                    hover_background "virtual_desktop_button_highlight"
                                    text _("DEBUG: Unlock All"):
                                        size 24
                                        align (0.5, 0.5)
                                        insensitive_color "#831f8a44"
                            null height 40
                            hbox:
                                button:
                                    action Function(debug_clear_plus_persistent)
                                    has frame
                                    xsize 420
                                    idle_background "virtual_desktop_button_outline"
                                    insensitive_background Transform("virtual_desktop_button_outline",matrixcolor=OpacityMatrix(value=0.3))
                                    hover_background "virtual_desktop_button_highlight"
                                    text _("DEBUG: Clear Plus Persistent"):
                                        size 24
                                        align (0.5, 0.5)
                                        insensitive_color "#831f8a44"


                        if False:
                            hbox:
                                style "virtual_desktop_settings_toggle_hbox"
                                button:
                                    action ToggleField(_preferences, "self_voicing")
                                    use settings_toggle_button(preferences.self_voicing)
                                text _("Self-Voicing") yalign 0.5
                            text _("Uses text-to-speech to voice the game's various text.") style "settings_description_text"

                elif current_tab == "language":
                    frame at virtual_desktop_settings_vbox_fade:
                        xsize 0.8
                        xalign 0.5
                        has vbox
                        spacing settings_spacing
                        first_spacing 0
                        null height get_variable_size(20, 12)
                        hbox:
                            spacing settings_spacing
                            vbox:
                                text _("Text Speed")
                                side "c l r":
                                    bar:
                                        style "settings_slider"
                                        value FieldValue(_preferences, "text_cps", range=180, step=30, force_step=True, max_is_zero=False, offset=20)
                                    add "gui/virtual_desktop/settings/slider_autopace_icon_min.png" yalign 0.5 zoom 0.5
                                    add "gui/virtual_desktop/settings/slider_autopace_icon_max.png" yalign 0.5 zoom 0.5
                                null height 20
                                text _("Auto Mode Pace")
                                side "c l r":
                                    bar:
                                        style "settings_slider"
                                        bar_invert True
                                        value FieldValue(_preferences, "afm_time", range=18, offset=1, step=3, force_step=True)
                                    add "gui/virtual_desktop/settings/slider_autopace_icon_min.png" yalign 0.5 zoom 0.5
                                    add "gui/virtual_desktop/settings/slider_autopace_icon_max.png" yalign 0.5 zoom 0.5
                                null height 20
                                text _("Text Size")
                                side "c l r":
                                    bar:
                                        style "settings_slider"

                                        value FieldValue(_preferences, "text_scale", range=0.5, offset=0.5, step=0.25, force_step=True)
                                        released gui.SetPreference("text_scale", preferences.text_scale)
                                        alt "Text Size"
                                    add "gui/virtual_desktop/settings/slider_textsize_icon_min.png" yalign 0.5 zoom 0.5
                                    add "gui/virtual_desktop/settings/slider_textsize_icon_max.png" yalign 0.5 zoom 0.5
                            vbox:
                                xsize 1.0
                                spacing 4
                                if renpy.mobile:
                                    style_prefix "plus_radio"
                                    label _("Allow Skipping:")
                                    textbutton _("Previously-read text only") action Preference("skip", "seen")
                                    textbutton _("All text") action Preference("skip", "all")
                                else:
                                    text _("Skip") style "settings_bold_text"
                                    null height 20
                                    hbox:
                                        style "virtual_desktop_settings_toggle_hbox"
                                        button:
                                            action Preference("skip", "toggle")
                                            use settings_toggle_button(preferences.skip_unseen)
                                        text _("Unseen Text") yalign 0.5
                                    null height 20
                                    hbox:
                                        style "virtual_desktop_settings_toggle_hbox"
                                        button:
                                            action Preference("after choices", "toggle")
                                            use settings_toggle_button(preferences.skip_after_choices)
                                        text _("After Choices") yalign 0.5

                        add Solid(gui.virtual_desktop_soft_accent_color, xysize=(1.0, 2))


                        fixed:
                            ysize 50

                            button:
                                action [Function(settings_apply_language)]
                                align (1.0, 0.5)
                                yanchor 0.5
                                ysize 50
                                sensitive (settings_language != preferences.language)
                                has frame
                                padding (20, 5)
                                xminimum 120
                                xmaximum 150
                                ysize 1.0

                                idle_background "virtual_desktop_button_outline"
                                insensitive_background Transform("virtual_desktop_button_outline",matrixcolor=OpacityMatrix(value=0.3))
                                hover_background "virtual_desktop_button_highlight"

                                text _("Apply") at loc_text_fit:
                                    align (0.5, 0.5)
                                    insensitive_color "#831f8a44"

                            text _("Language") xalign 0.0 yalign 0.5

                            fixed:
                                xysize (0.65, 1.0)
                                align (0.55, 0.5)
                                button:
                                    align (0.0, 0.5)
                                    style "settings_language_button"
                                    action Function(settings_scroll_language, increment=-1)
                                    use settings_scroller_button(True)
                                text str(settings_localized_languages[settings_available_languages.index(settings_language)]):
                                    font "NotoSansCJKjp-Regular.otf"
                                    xalign 0.5
                                button:
                                    align (1.0, 0.5)
                                    style "settings_language_button"
                                    action Function(settings_scroll_language, increment=1)
                                    use settings_scroller_button(False)

                elif current_tab == "accessibility":
                    frame at virtual_desktop_settings_vbox_fade:
                        xsize 0.8
                        xalign 0.5
                        has viewport id "virtual_desktop_settings_vp" at vp_vert_scroll_mask
                        draggable True
                        vbox:
                            first_spacing 0
                            null height get_variable_size(50, 30)

                            hbox:
                                style "settings_toggle_option_fixed"
                                button:
                                    yalign 0.5
                                    action ToggleField(persistent, "content_warnings_enabled", True, False)
                                    use settings_toggle_button(persistent.content_warnings_enabled)
                                text _("Content Warnings") style "settings_toggle_option_text"
                            text _("Enables content warnings that will appear before scenes with disturbing subject matter.") style "settings_description_text"
                            null height settings_spacing
                            hbox:
                                style "settings_toggle_option_fixed"
                                button:
                                    yalign 0.5
                                    action ToggleField(persistent, "high_contrast", True, False)
                                    use settings_toggle_button(persistent.high_contrast)
                                text _("High Contrast Text Boxes") style "settings_toggle_option_text"
                            text _("Replaces the dialogue box with a darker variant, making dialogue easier to read.") style "settings_description_text"
                            null height settings_spacing
                            hbox:
                                style "settings_toggle_option_fixed"
                                button:
                                    yalign 0.5
                                    action ToggleField(persistent, "reduce_transparency", True, False)
                                    use settings_toggle_button(persistent.reduce_transparency)
                                text _("Reduce Textbox Transparency") style "settings_toggle_option_text"
                            text _("Makes the dialogue box opaque, making dialogue easier to read.") style "settings_description_text"
                            null height settings_spacing
                            hbox:
                                style "settings_toggle_option_fixed"
                                button:
                                    yalign 0.5
                                    action ToggleField(persistent, "use_alt_poem_font", True, False)
                                    use settings_toggle_button(persistent.use_alt_poem_font)
                                text _("Alternate Poem Font") style "settings_toggle_option_text"
                            text _("Switches handwritten fonts in characters' poems with an easier-to-read font.") style "settings_description_text"
                            null height settings_spacing
                            button:
                                action OpenURL("https://teamsalvato.com/ddlc-warnings")
                                has frame
                                padding (50, 10)
                                idle_background "virtual_desktop_button_outline"
                                insensitive_background Transform("virtual_desktop_button_outline",matrixcolor=OpacityMatrix(value=0.3))
                                hover_background "virtual_desktop_button_highlight"
                                text _("Open Full-Disclosure Content Warnings Page"):
                                    size 24
                                    align (0.5, 0.5)
                                    insensitive_color "#831f8a44"
                            null height 50
                    vbar value YScrollValue("virtual_desktop_settings_vp") xpos 1.0 xoffset -20 style "virtual_desktop_vscrollbar"













































































































































style settings_frame:
    background None

style settings_arrow_button:
    color gui.virtual_desktop_text_color

style settings_text:
    font gui.virtual_desktop_text_font
    align (0.0, 0.5)
    xanchor 0.0
    size get_variable_size(24, 34, gui.text_scale)
    color gui.virtual_desktop_text_color
    outlines []

style settings_bold_text is settings_text:
    font "fonts/HKGrotesk-SemiBold-rounded.otf"
    kerning 1.25
    shaper "freetype"

style settings_button_text is settings_text

style settings_toggle_option_text is settings_text:
    yalign 0.5
    xalign 0.0

    yoffset -2

style settings_toggle_option_fixed:
    fit_first "height"
    spacing gui.virtual_desktop_settings_toggle_spacing

style virtual_desktop_settings_toggle_hbox:
    first_spacing get_variable_size(20, 40, gui.text_scale)
    spacing 10

style settings_button:
    padding (0, 0)

style settings_tab_button:
    xysize (gui.virtual_desktop_settings_tab_width, 1.0)

style settings_description_text is settings_text:
    size get_variable_size(16, 28, gui.text_scale)

style settings_slider:
    xysize (get_variable_size(280,340,gui.text_scale), (40 if renpy.mobile else 17))
    align (0.0, 0.5)
    anchor (0.0, 0.5)
    base_bar Frame("gui/virtual_desktop/settings/settings slider 51.png", tile=False, ysize=(40 if renpy.mobile else 17))
    thumb Frame("gui/virtual_desktop/settings/settings slider scrub icon.png", xsize=(40 if renpy.mobile else 17), ysize=(40 if renpy.mobile else 17))
    thumb_offset 8

style settings_language_button:
    xysize (100, 100)

image plus_check_foreground:
    Transform("gui/button/plus_check_foreground.png", yalign=0.5, zoom=get_variable_size_f(0.4, 0.6, gui.text_scale))
image plus_check_selected_foreground:
    Transform("gui/button/plus_check_selected_foreground.png", yalign=0.5, zoom=get_variable_size_f(0.4, 0.6, gui.text_scale))

style plus_radio_label_text is settings_bold_text
style plus_radio_button_text is settings_text
style plus_radio_button:
    properties gui.button_properties("radio_button")
    foreground "plus_check_[prefix_]foreground"
    yminimum get_variable_size(24, 32, gui.text_scale)
    ymaximum 156
style plus_radio_vbox is radio_vbox

transform settings_titlerow_hover:
    matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)
    on hover:
        matrixcolor ColorizeMatrix("000000", "FFFFFF")
    on idle:
        matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)






translate japanese python:
    gui.text_font = "NotoSansCJKjp-Regular.otf"
    gui.name_text_font = "NotoSansCJKjp-Regular.otf"
    gui.riffic_font = "NotoSansCJKjp-Regular.otf"
    gui.halogen_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_text_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_bold_text_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_black_text_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_start_text_font = "NotoSansCJKjp-Regular.otf"
    gui.choice_button_text_font = "NotoSansCJKjp-Regular.otf"
    gui.interface_text_font = "NotoSansCJKjp-Regular.otf"

translate japanese style monika_credits_text font "NotoSansCJKjp-Regular.otf"
translate japanese style virtual_desktop_file_viewer_text font "NotoSansCJKjp-Regular.otf"
translate japanese style gallery_wallpaper_acquisition_text font "NotoSansCJKjp-Regular.otf"
translate japanese style gallery_wallpaper_description_text font "NotoSansCJKjp-Regular.otf"
translate japanese style settings_bold_text font "NotoSansCJKjp-Regular.otf"
translate japanese style jukebox_bold_text font "NotoSansCJKjp-Regular.otf"
translate japanese style quick_button_text font "NotoSansCJKjp-Regular.otf"
translate japanese style navigation_button_text font "NotoSansCJKjp-Regular.otf"
translate japanese style mobile_captcha_text font "NotoSansCJKjp-Regular.otf"
translate japanese style confirm_prompt_text font "NotoSansCJKjp-Regular.otf"
translate japanese style edited font "NotoSansCJKjp-Regular.otf"
translate japanese style credits_text_xs line_spacing -8
translate japanese style pluscredits_name_xsmall line_spacing -8
translate japanese style console_text font "NotoSansCJKjp-Regular.otf"


translate russian python:
    gui.text_font = "NotoSansCJKjp-Regular.otf"
    gui.name_text_font = "NotoSansCJKjp-Regular.otf"
    gui.riffic_font = "NotoSansCJKjp-Regular.otf"
    gui.halogen_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_text_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_bold_text_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_black_text_font = "NotoSansCJKjp-Regular.otf"
    gui.virtual_desktop_start_text_font = "NotoSansCJKjp-Regular.otf"
    gui.choice_button_text_font = "NotoSansCJKjp-Regular.otf"
    gui.interface_text_font = "NotoSansCJKjp-Regular.otf"

translate russian style monika_credits_text font "NotoSansCJKjp-Regular.otf"
translate russian style virtual_desktop_file_viewer_text font "NotoSansCJKjp-Regular.otf"
translate russian style gallery_wallpaper_acquisition_text font "NotoSansCJKjp-Regular.otf"
translate russian style gallery_wallpaper_description_text font "NotoSansCJKjp-Regular.otf"
translate russian style settings_bold_text font "NotoSansCJKjp-Regular.otf"
translate russian style jukebox_bold_text font "NotoSansCJKjp-Regular.otf"
translate russian style quick_button_text font "NotoSansCJKjp-Regular.otf"
translate russian style navigation_button_text font "NotoSansCJKjp-Regular.otf"
translate russian style mobile_captcha_text font "NotoSansCJKjp-Regular.otf"
translate russian style confirm_prompt_text font "NotoSansCJKjp-Regular.otf"
translate russian style edited font "NotoSansCJKjp-Regular.otf"
translate russian style credits_text_xs line_spacing -8
translate russian style pluscredits_name_xsmall line_spacing -8
translate russian style console_text font "NotoSansCJKjp-Regular.otf"


translate korean python:
    gui.text_font = "NotoSansCJKkr-Regular.otf"
    gui.name_text_font = "NotoSansCJKkr-Regular.otf"
    gui.riffic_font = "NotoSansCJKkr-Regular.otf"
    gui.halogen_font = "NotoSansCJKkr-Regular.otf"
    gui.virtual_desktop_text_font = "NotoSansCJKkr-Regular.otf"
    gui.virtual_desktop_bold_text_font = "NotoSansCJKkr-Regular.otf"
    gui.virtual_desktop_black_text_font = "NotoSansCJKkr-Regular.otf"
    gui.virtual_desktop_start_text_font = "NotoSansCJKkr-Regular.otf"
    gui.choice_button_text_font = "NotoSansCJKkr-Regular.otf"
    gui.interface_text_font = "NotoSansCJKkr-Regular.otf"

translate korean style monika_credits_text font "NotoSansCJKkr-Regular.otf"
translate korean style virtual_desktop_file_viewer_text font "NotoSansCJKkr-Regular.otf"
translate korean style gallery_wallpaper_acquisition_text font "NotoSansCJKkr-Regular.otf"
translate korean style gallery_wallpaper_description_text font "NotoSansCJKkr-Regular.otf"
translate korean style settings_bold_text font "NotoSansCJKkr-Regular.otf"
translate korean style jukebox_bold_text font "NotoSansCJKkr-Regular.otf"
translate korean style quick_button_text font "NotoSansCJKkr-Regular.otf"
translate korean style navigation_button_text font "NotoSansCJKkr-Regular.otf"
translate korean style mobile_captcha_text font "NotoSansCJKkr-Regular.otf"
translate korean style confirm_prompt_text font "NotoSansCJKkr-Regular.otf"
translate korean style edited font "NotoSansCJKkr-Regular.otf"
translate korean style credits_text_xs line_spacing -8
translate korean style pluscredits_name_xsmall line_spacing -8
translate korean style console_text font "NotoSansCJKkr-Regular.otf"


translate chinese_simplified python:
    gui.text_font = "NotoSansCJKsc-Regular.otf"
    gui.name_text_font = "NotoSansCJKsc-Regular.otf"
    gui.riffic_font = "NotoSansCJKsc-Regular.otf"
    gui.halogen_font = "NotoSansCJKsc-Regular.otf"
    gui.virtual_desktop_text_font = "NotoSansCJKsc-Regular.otf"
    gui.virtual_desktop_bold_text_font = "NotoSansCJKsc-Regular.otf"
    gui.virtual_desktop_black_text_font = "NotoSansCJKsc-Regular.otf"
    gui.virtual_desktop_start_text_font = "NotoSansCJKsc-Regular.otf"
    gui.choice_button_text_font = "NotoSansCJKsc-Regular.otf"
    gui.interface_text_font = "NotoSansCJKsc-Regular.otf"

translate chinese_simplified style monika_credits_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style virtual_desktop_file_viewer_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style gallery_wallpaper_acquisition_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style gallery_wallpaper_description_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style settings_bold_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style jukebox_bold_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style quick_button_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style navigation_button_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style mobile_captcha_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style confirm_prompt_text font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style edited font "NotoSansCJKsc-Regular.otf"
translate chinese_simplified style credits_text_xs line_spacing -8
translate chinese_simplified style pluscredits_name_xsmall line_spacing -8
translate chinese_simplified style console_text font "NotoSansCJKsc-Regular.otf"


translate chinese_traditional python:
    gui.text_font = "NotoSansCJKtc-Regular.otf"
    gui.name_text_font = "NotoSansCJKtc-Regular.otf"
    gui.riffic_font = "NotoSansCJKtc-Regular.otf"
    gui.halogen_font = "NotoSansCJKtc-Regular.otf"
    gui.virtual_desktop_text_font = "NotoSansCJKtc-Regular.otf"
    gui.virtual_desktop_bold_text_font = "NotoSansCJKtc-Regular.otf"
    gui.virtual_desktop_black_text_font = "NotoSansCJKtc-Regular.otf"
    gui.virtual_desktop_start_text_font = "NotoSansCJKtc-Regular.otf"
    gui.choice_button_text_font = "NotoSansCJKtc-Regular.otf"
    gui.interface_text_font = "NotoSansCJKtc-Regular.otf"

translate chinese_traditional style monika_credits_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style virtual_desktop_file_viewer_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style gallery_wallpaper_acquisition_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style gallery_wallpaper_description_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style settings_bold_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style jukebox_bold_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style quick_button_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style navigation_button_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style mobile_captcha_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style confirm_prompt_text font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style edited font "NotoSansCJKtc-Regular.otf"
translate chinese_traditional style credits_text_xs line_spacing -8
translate chinese_traditional style pluscredits_name_xsmall line_spacing -8
translate chinese_traditional style console_text font "NotoSansCJKtc-Regular.otf"
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
