init offset = -2







python early:
    import math






    def get_variable_size(min:int, max:int, mod=None):
        if mod == None:
            mod = gui.text_scale
        return round(min * (1 - mod) + max * mod)



    def get_variable_size_f(min:float, max:float, mod=None):
        if mod == None:
            mod = gui.text_scale
        return (min * (1.0 - mod) + max * mod)




    def get_relative_size(size:int, ref_min:int, ref_max:int, mod=None):
        if mod == None:
            mod = gui.text_scale
        return round(size * (get_variable_size(ref_min, ref_max, mod) / ref_min))

    def get_relative_size_f(size:float, ref_min:float, ref_max:float, mod=None):
        if mod == None:
            mod = gui.text_scale
        return size * (get_variable_size_f(ref_min, ref_max, mod) / ref_min)






    def get_scaled_outlines(outlines, ref_min, ref_max, mod=None):
        if mod == None:
            mod = gui.text_scale
        
        if isinstance(outlines[0], int):
            return (math.ceil(get_relative_size_f(outlines[0], ref_min, ref_max, mod)), outlines[1], outlines[2], outlines[3])
        else:
            return_outlines = []
            for o in outlines:
                return_outlines.append((math.ceil(get_relative_size_f(o[0], ref_min, ref_max, mod)), o[1], o[2], o[3]))
            return return_outlines

    def vp_vert_scroll_mask(d):
        return AlphaMask(d, Frame("gui/viewport-vertical-fade.png", 0, 13))




init python:
    gui.init(1280, 720)







default preferences.text_scale = (1.0 if renpy.variant("small") else 0.0)
define gui.text_scale = gui.preference("text_scale", (1.0 if renpy.variant("small") else 0.0))

define gui.hover_sound = (None if renpy.mobile else "gui/sfx/hover.ogg")
define gui.activate_sound = "gui/sfx/select.ogg"
define gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg"






define gui.accent_color = '#ffffff'


define gui.idle_color = '#aaaaaa'



define gui.idle_small_color = '#333'


define gui.hover_color = '#cc6699'



define gui.selected_color = '#bb5588'


define gui.insensitive_color = '#aaaaaa7f'



define gui.muted_color = '#6666a3'
define gui.hover_muted_color = '#9999c1'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

define gui.hc_label_outline_color = "#8b2268"
define gui.hc_label_outline_selected_color = "#bb5599"




define gui.text_font = "gui/font/Aller_Rg.ttf"


define gui.name_text_font = "gui/font/RifficFree-Bold.ttf"


define gui.interface_text_font = "gui/font/Aller_Rg.ttf"


define gui.text_size = 24
define gui.max_text_size = 36


define gui.name_text_size = 24
define gui.max_name_text_size = 36


define gui.interface_text_size = 24
define gui.max_interface_text_size = 36


define gui.label_text_size = 28
define gui.max_label_text_size = 36


define gui.notify_text_size = 16
define gui.max_notify_text_size = 25


define gui.title_text_size = 38





define gui.main_menu_background = "menu_bg"
define gui.game_menu_background = "game_menu_bg"


define gui.show_name = False








define gui.textbox_height = 147
define gui.max_textbox_height = 211



define gui.textbox_yalign = 0.99




define gui.name_xpos = 0.13
define gui.name_ypos = 0.0



define gui.name_xalign = 0.5



define gui.namebox_width = 168
define gui.namebox_height = 39
define gui.max_namebox_width = 224
define gui.max_namebox_height = 52



define gui.namebox_borders = Borders(5, 5, 5, 2)



define gui.namebox_tile = False





define gui.dialogue_xpos = 40
define gui.dialogue_ypos = 23


define gui.dialogue_width = 764
define gui.max_dialogue_width = 1146



define gui.dialogue_text_xalign = 0.0

define gui.ctc_xalign = get_variable_size_f(0.81, 0.96, gui.text_scale)
define gui.ctc_zoom = ((1.25 if renpy.mobile else 1.0) + get_variable_size_f(0, 0.5, gui.text_scale))







define gui.button_width = None
define gui.button_height = 36


define gui.button_borders = Borders(4, 4, 4, 4)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size
define gui.max_button_text_size = gui.max_interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders((34 + get_variable_size(0, 16, gui.text_scale)), 4, 4, 4)

define gui.radio_button_text_yalign = 0.5
define gui.radio_button_text_xoffset = 5
define gui.check_button_borders = Borders((34 + get_variable_size(0, 16, gui.text_scale)), 4, 4, 4)
define gui.check_button_text_yoffset = get_variable_size(-8, -12, gui.text_scale)
define gui.check_button_text_xoffset = 5
define gui.quick_menu_spacing = 0
define gui.max_quick_menu_spacing = 30

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)


define gui.quick_button_text_size = 14
define gui.max_quick_button_text_size = 20
define gui.quick_button_text_idle_color = "#522"
define gui.quick_button_text_hover_color = "#fcc"
define gui.quick_button_text_selected_color = gui.accent_color
define gui.quick_button_text_insensitive_color = "#a66"












define gui.choice_button_width = 420
define gui.max_choice_button_width = 600
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.max_choice_button_text_size = gui.max_text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#000"
define gui.choice_button_text_hover_color = "#fa9"









define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_hover_color = gui.hover_color


define config.thumbnail_width = 256
define config.thumbnail_height = 144


define gui.file_slot_cols = 3
define gui.file_slot_rows = 2









define gui.navigation_xpos = 50
define gui.max_navigation_xpos = 80


define gui.skip_ypos = 10


define gui.notify_ypos = 45


define gui.choice_spacing = 22


define gui.navigation_spacing = 6
define gui.max_navigation_spacing = 36


define gui.pref_spacing = 10



define gui.pref_button_spacing = 10
define gui.max_pref_button_spacing = 20


define gui.page_spacing = 0


define gui.slot_spacing = 10








define gui.frame_borders = Borders(4, 4, 4, 4)


define gui.confirm_frame_borders = Borders(40, 40, 40, 40)


define gui.skip_frame_borders = Borders(16, 5, 50, 5)


define gui.notify_frame_borders = Borders(16, 5, 40, 5)


define gui.frame_tile = False











define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)


define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)



define gui.unscrollable = "hide"







define config.history_length = 50



define gui.history_height = None



define gui.history_name_xpos = 10
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 0.0


define gui.history_text_xpos = 20
define gui.history_text_ypos = get_variable_size(40, 57)
define gui.history_text_width = 800
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 10, 0, 20)



define gui.nvl_height = 115



define gui.nvl_spacing = 10



define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0






define gui.riffic_font = "gui/font/RifficFree-Bold.ttf"
define gui.halogen_font = "gui/font/Halogen.ttf"






define gui.virtual_desktop_text_font = "HKGrotesk-Medium.otf"
define gui.virtual_desktop_bold_text_font = "HKGrotesk-Bold.otf"
define gui.virtual_desktop_black_text_font = "HKGrotesk-Black.otf"
define gui.virtual_desktop_start_text_font = "VeraSans-Semi-Bolder.ttf"

init python:
    config.font_replacement_map["HKGrotesk-Medium.otf", True, False] = ["HKGrotesk-Bold.otf", False, False]


define gui.virtual_desktop_text_color = "#831f8a"
define gui.virtual_desktop_accent_color = "#e61484"
define gui.virtual_desktop_soft_accent_color = "#f38cc3"
define gui.virtual_desktop_start_color = "#800066"


define gui.virtual_desktop_app_width = 880
define gui.virtual_desktop_app_title_text_size = 19
define gui.virtual_desktop_app_close_button_text_size = 16
define gui.virtual_desktop_app_scrollbar_width = 6


define gui.virtual_desktop_side_stories_text_size = 24
define gui.virtual_desktop_side_story_button_height = 165
define gui.virtual_desktop_side_story_button_width = 265
define gui.virtual_desktop_side_story_button_wide_width = 535


define gui.virtual_desktop_files_text_size = 16
define gui.virtual_desktop_file_viewer_text_size = 15


define gui.virtual_desktop_mail_text_size = 16
define gui.virtual_desktop_mail_contents_text_size = 14
define gui.virtual_desktop_mail_signature_text_size = 12


define gui.virtual_desktop_pictures_header_text_size = 16

define gui.virtual_desktop_pictures_reel_thumb_width = 130
define gui.virtual_desktop_pictures_reel_thumb_height = 70

define gui.gallery_wallpaper_height = 535
define gui.gallery_wallpaper_width = (int(gui.gallery_wallpaper_height * 16 / 9))
define gui.gallery_wallpaper_offset = (int((1280 - (gui.gallery_wallpaper_width)) * 0.5), 14)
define gui.gallery_thumb_width = 160
define gui.gallery_thumb_height = 90
define gui.gallery_thumb_button_width = 180
define gui.gallery_thumb_button_height = 110


define gui.virtual_desktop_settings_vbox_spacing = 24
define gui.virtual_desktop_settings_vbox_spacing_max = 32
define gui.virtual_desktop_settings_tab_width = 120
define gui.virtual_desktop_settings_toggle_spacing = get_variable_size(20, 30)





init python:







    @gui.variant
    def small():
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        
        gui.quick_button_borders = Borders(60, 14, 60, 0)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
