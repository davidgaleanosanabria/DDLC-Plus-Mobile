

init python:

    class DesktopGalleryImage:
        def __init__(self, data:dict, id:str):
            self.id = id
            self.image_name = data["name"]
            self.section_name = data["section"]
            self.asset_name = data["asset_name"].lower()
            self.asset_bundle = data["asset_bundle"].lower()
            self.thumb_name = data["thumb_name"].lower()
            self.unlock_string = data["unlock_string"]
            self.description_text = data["description"]
            self.unlock_condition_text = data["unlock_condition"]
            self.currently_unlocked = False
            if "poem_id" in data:
                self.poem_id = data["poem_id"]
                self.use_poem_screen = True
            else:
                self.use_poem_screen = False
            if "vertical_asset_name" in data:
                self.vertical_asset_name = data["vertical_asset_name"]
                self.has_vertical = True
            else:
                self.has_vertical = False


    def parse_gallery_images():
        import tomllib
        ret_images = {}
        with renpy.file("desktopwallpapers.toml", False) as f:
            image_dict = tomllib.load(f)
            for image_id, data in image_dict.items():
                ret_images[image_id] = DesktopGalleryImage(data, image_id)
        return ret_images


    def build_gallery_sections(image_dict):
        sections = {}
        for id, img in image_dict.items():
            if img.section_name not in sections:
                sections[img.section_name] = []
            sections[img.section_name].append(id)
        return sections

    def gallery_refresh_unlock_states():
        global virtual_gallery_images
        for id in virtual_gallery_images:
            if virtual_gallery_images[id].unlock_string == "" or virtual_gallery_images[id].unlock_string == '':
                virtual_gallery_images[id].currently_unlocked = True
            elif virtual_gallery_images[id].unlock_string in plus_persistent.img_unlocked:
                virtual_gallery_images[id].currently_unlocked = True
            elif virtual_gallery_images[id].unlock_string in plus_persistent.all_unlocked:
                virtual_gallery_images[id].currently_unlocked = True
            else:
                virtual_gallery_images[id].currently_unlocked = False


    def gallery_save_to_photos(image_id, vertical):
        if not renpy.android:
            return
        import jnius
        jnius.autoclass("org.renpy.android.PlaybackService").DownloadPhoto(virtual_gallery_images[image_id].asset_bundle + "/" + (virtual_gallery_images[image_id].asset_name if not vertical else virtual_gallery_images[image_id].vertical_asset_name), virtual_gallery_images[image_id].image_name, virtual_gallery_images[image_id].description_text)


    def gallery_photo_save_success():
        return


    def gallery_photo_save_failed():
        return



    def gallery_get_adjacent_images(image_id, range=3):
        
        section_list = list(virtual_gallery_sections.keys())
        starting_section_index = section_list.index(virtual_gallery_images[image_id].section_name)
        starting_index = virtual_gallery_sections[virtual_gallery_images[image_id].section_name].index(image_id)
        
        
        left_images = []
        index = starting_index
        section_index = starting_section_index
        while len(left_images) < range:
            
            index -= 1
            if index < 0:
                section_index -= 1
                if section_index < 0:
                    left_images.append(None) 
                    continue
                else:
                    index = len(virtual_gallery_sections[section_list[section_index]]) - 1
            if virtual_gallery_images[virtual_gallery_sections[section_list[section_index]][index]].currently_unlocked == True:
                left_images.append(virtual_gallery_sections[section_list[section_index]][index])
        
        
        right_images = []
        index = starting_index
        section_index = starting_section_index
        while len(right_images) < range:
            
            index += 1
            if section_index > len(section_list) - 1 or index > len(virtual_gallery_sections[section_list[section_index]]) - 1:
                section_index += 1
                if section_index > len(section_list) - 1:
                    right_images.append(None) 
                    continue
                else:
                    index = 0
            if virtual_gallery_images[virtual_gallery_sections[section_list[section_index]][index]].currently_unlocked == True:
                right_images.append(virtual_gallery_sections[section_list[section_index]][index])
        
        left_images.reverse()
        return left_images + [image_id] + right_images

    def function_set_wallpaper(image_id):
        plus_persistent.desktop_wallpaper = virtual_gallery_images[image_id].asset_name
        unlock("change_wallpaper")
        plus_persistent.save()



    def gallery_compute_grid(img_id):
        global virtual_gallery_zoom_alignment
        global virtual_gallery_zoom_selection
        global virtual_gallery_zoom_cache
        
        virtual_gallery_zoom_selection = img_id
        virtual_gallery_zoom_scroll_offset = 0
        
        
        
        r = renpy.focus_coordinates()
        if r[3] != gui.gallery_thumb_button_height and r[1] < gui.gallery_thumb_button_height:
            virtual_gallery_zoom_alignment = (r[0], r[1] + r[3] - gui.gallery_thumb_button_height, r[2], gui.gallery_thumb_button_height)
        else:
            virtual_gallery_zoom_alignment = r
        
        if virtual_gallery_zoom_cache is None:
            virtual_gallery_zoom_cache = {}
            
            spacing = (200.0, 130.0) 
            section = 34 
            
            iterator = (0.0, 0.0)
            for s in virtual_gallery_sections:
                for i in virtual_gallery_sections[s]:
                    virtual_gallery_zoom_cache[i] = iterator
                    if (iterator[0] < 2.5 * spacing[0]): 
                        iterator = (iterator[0] + spacing[0], iterator[1])
                    else:
                        iterator = (0.0, iterator[1] + spacing[1])
                iterator = (0.0, iterator[1] + spacing[1])


    def gallery_get_grid_bounds(img_id):
        global virtual_gallery_zoom_alignment
        global virtual_gallery_zoom_selection
        global virtual_gallery_zoom_cache
        
        
        x = virtual_gallery_zoom_alignment[0] + virtual_gallery_zoom_cache[img_id][0] - virtual_gallery_zoom_cache[virtual_gallery_zoom_selection][0]
        y = virtual_gallery_zoom_alignment[1] + virtual_gallery_zoom_cache[img_id][1] - virtual_gallery_zoom_cache[virtual_gallery_zoom_selection][1]
        
        
        
        return (10.0 + x, 0.0 + y) 



    def gallery_calculate_shrink_atl(img_id):
        global virtual_gallery_zoom_scroll_offset
        
        
        y = gallery_get_grid_bounds(img_id)[1] - gui.gallery_thumb_button_height 
        
        
        if y < 0:
            virtual_gallery_zoom_scroll_offset = y + (gui.gallery_thumb_button_height / 2)
        elif y > 400:
            virtual_gallery_zoom_scroll_offset = y - (gui.gallery_thumb_button_height / 2) - (gui.gallery_thumb_button_height * 3)
        else:
            virtual_gallery_zoom_scroll_offset = 0


    def gallery_set_scroll(img_id):
        global virtual_gallery_scroll_adjustment
        global virtual_gallery_zoom_scroll_offset
        virtual_gallery_scroll_adjustment.change(virtual_gallery_scroll_adjustment.value + virtual_gallery_zoom_scroll_offset)

    class SetGallerySection(Action):
        def __init__(self, new_section, nav_atl_event="navigate"):
            self.new_section = new_section
            self.nav_atl_event = nav_atl_event
        def __call__(self):
            renpy.run(SetScreenVariable("current_gallery_section", self.new_section))
            trigger_displayable_event("virtual_desktop_gallery_app", "list", self.nav_atl_event)
        def periodic(self, st):
            
            
            trigger_displayable_event("virtual_desktop_gallery_app", "list", None)



define virtual_gallery_images = parse_gallery_images()
define virtual_gallery_sections = build_gallery_sections(virtual_gallery_images)

define virtual_gallery_zoom_cache = None
define virtual_gallery_zoom_alignment = (0,0)
define virtual_gallery_zoom_selection = None
define virtual_gallery_zoom_scroll_offset = 0
define virtual_gallery_scroll_adjustment = ui.adjustment()

image desktop_gallery_locked = "gui/virtual_desktop/photos/locked.png"






screen virtual_desktop_gallery_app():

    default gallery_section_names = list(virtual_gallery_sections.keys())
    default current_gallery_section = gallery_section_names[0]

    on "show" action Function(clear_notification, "bg")

    style_prefix "virtual_desktop"

    key ['mouseup_3'] action NullAction()
    key ['mouseup_2'] action NullAction()

    use virtual_desktop_app_window("Pictures", window_width=1180, taskbar_icon="desktop_Pictures_H"):
        key ['K_ESCAPE'] action NullAction()
        side 'l c':

            frame:
                background None
                xmaximum 350
                ysize 1.0
                vbox:
                    for section in gallery_section_names:
                        button:
                            xsize 1.0
                            ysize 64
                            padding (13, 10)
                            if section == current_gallery_section:
                                background Frame("virtual_desktop_start_menu_highlight") at gallery_selected_section_fade
                                add "/gui/virtual_desktop/music/play icon white.png" zoom 0.3 align (1.0, 0.5)
                            hbox:
                                yalign 0.5
                                spacing 10
                                if section == current_gallery_section:
                                    add "gui/virtual_desktop/photos/section_folder_icon_white.png" xysize (60, 40) yalign 0.5
                                else:
                                    add "gui/virtual_desktop/photos/section_folder_icon.png" xysize (60, 40) yalign 0.5
                                text "[section!t]" style "gallery_section_text":
                                    yalign 0.5
                                    if section == current_gallery_section:
                                        color "#fff"

                            action (SetGallerySection(section) if section != current_gallery_section else NullAction())

                add Solid(gui.virtual_desktop_soft_accent_color, xsize=1) xalign 1.0


            frame at file_list_crop:
                fixed id "list" at gallery_grid_on_navigate:
                    vpgrid id "desktop_popup_canvas":
                        style_prefix "gallery"
                        draggable True mousewheel True
                        yadjustment virtual_gallery_scroll_adjustment
                        align (0.5, 0.0)
                        cols 4
                        spacing 20
                        for img_id in virtual_gallery_sections[current_gallery_section]:
                            if virtual_gallery_images[img_id].currently_unlocked:
                                button id img_id:
                                    action [Function(gallery_compute_grid, img_id), Function(gallery_calculate_shrink_atl, img_id), Show("virtual_desktop_wallpapers_app", image_id=img_id)]
                                    add "gallery_thumbnail_background"
                                    add virtual_gallery_images[img_id].thumb_name at gallery_button_thumbnail
                            else:
                                button id img_id:
                                    action NullAction()
                                    add "gallery_thumbnail_background"
                                    add "desktop_gallery_locked" at gallery_button_thumbnail
                vbar value YScrollValue("desktop_popup_canvas") xpos 1.0 xoffset -20






























style gallery_button:
    hover_background Frame("gui/virtual_desktop/photos/highlight.png")
    xysize (gui.gallery_thumb_button_width, gui.gallery_thumb_button_height)

style gallery_section_text is virtual_desktop_text:
    size get_variable_size(16, 30, gui.text_scale)
    text_align 0.5

image gallery_thumbnail_background:
    Frame("#FFFFFFFF")
    xysize (gui.gallery_thumb_width + 2, gui.gallery_thumb_height + 2)
    align (0.0, 0.0)
    offset (5, 5)

transform gallery_button_thumbnail:
    xysize (gui.gallery_thumb_width, gui.gallery_thumb_height)
    align (0.0, 0.0)
    offset (6, 6)

transform gallery_selected_section_fade:


    alpha 0.0


    linear 0.15 alpha 1.0



transform gallery_grid_on_navigate:
    alpha 1.0
    xpos 0.0
    on navigate:
        alpha 0.0
        xpos -0.025
        parallel:
            easeout_quad 0.2 alpha 1.0
        parallel:
            easein_quad 0.2 xpos 0.0















screen virtual_desktop_wallpapers_app(image_id, selected_reel_offset=0):
    predict False

    dismiss action NullAction()
    key ['mouseup_3'] action NullAction()
    key ['mouseup_2'] action NullAction()

    $ current_image = virtual_gallery_images[image_id]
    $ reel_images = gallery_get_adjacent_images(image_id, 3)
    $ current_poem = (None if not current_image.use_poem_screen else eval(current_image.poem_id))


    frame:
        background Frame("gui/virtual_desktop/photos/wallpapers_background.png")
        style_prefix "gallery"
        xysize (1.0, 1.0)
        align (0.5, 0.5)
        padding (0, 0)
        has vbox
        xsize 0.75
        align (0.5, 1.0)
        yoffset -30

        frame:
            background None
            xysize (1.0, 94)
            frame:
                background None
                xsize 0.76
                xalign 0.5
                fixed id "reel" at gallery_wallpaper_reel_crop:
                    grid 7 1 at gallery_wallpaper_reel_navigate(startoffset=selected_reel_offset):
                        align (0.5, 0.5)
                        spacing 16
                        for img in reel_images:
                            if img != None:



                                $ unique_reel_offset = (reel_images.index(img) - 3) * (1 - renpy.random.random() * 0.01)
                                button:
                                    action Show("virtual_desktop_wallpapers_app", image_id=img, selected_reel_offset=unique_reel_offset)
                                    xysize (gui.virtual_desktop_pictures_reel_thumb_width, gui.gallery_thumb_height)
                                    hover_background None
                                    add virtual_gallery_images[img].thumb_name:
                                        xysize (gui.virtual_desktop_pictures_reel_thumb_width, 70)
                                        align (0.5, 0.5)
                            else:
                                frame:
                                    xysize (gui.virtual_desktop_pictures_reel_thumb_width, 70)
                                    background None

                add Solid(gui.virtual_desktop_accent_color, ysize=2, xsize=gui.virtual_desktop_pictures_reel_thumb_width-6):
                    align (0.5, 1.0)
                    yoffset 4
                    xoffset 3




            $ arrow_reel_offset = (1 - renpy.random.random() * 0.001)

            showif reel_images[2] != None:
                button at gallery_wallpaper_reel_button_hover:
                    action [Function(gallery_calculate_shrink_atl, reel_images[2]), Show("virtual_desktop_wallpapers_app", image_id=reel_images[2], selected_reel_offset=-1 * arrow_reel_offset)]
                    style "gallery_wallpaper_reel_button"
                    xysize (100, gui.gallery_thumb_height)
                    yalign 0.5
                    add "gui/virtual_desktop/photos/thumbnail arrow left.png" align (0.5, 0.5) zoom 0.3
                    xalign 0.0

            showif reel_images[4] != None:
                button at gallery_wallpaper_reel_button_hover:
                    action [Function(gallery_calculate_shrink_atl, reel_images[4]), Show("virtual_desktop_wallpapers_app", image_id=reel_images[4], selected_reel_offset=1 * arrow_reel_offset)]
                    style "gallery_wallpaper_reel_button"
                    xysize (100, gui.gallery_thumb_height)
                    yalign 0.5
                    add "gui/virtual_desktop/photos/thumbnail arrow right.png" align (0.5, 0.5) zoom 0.3
                    xalign 1.0


        hbox:
            box_reverse True
            xalign 1.0
            textbutton _("Back") style "gallery_wallpaper_button":
                hover_background "#f1f1f144"
                xpadding 15
                action [Function(gallery_set_scroll, image_id), Hide()]
            if renpy.mobile:
                textbutton _("Save Image") style "gallery_wallpaper_button":
                    sensitive (not current_image.use_poem_screen)
                    hover_background "#f1f1f144"
                    xpadding 15
                    action Show("gallery_wallpaper_download_confirm", current_image=current_image)
            textbutton _("Set Wallpaper") style "gallery_wallpaper_button":
                hover_background "#f1f1f144"
                sensitive (not current_image.use_poem_screen)
                xpadding 15
                action [SetVariable("confirm_title_message", _("Set Wallpaper")), Confirm(_("Set as wallpaper?"), Function(function_set_wallpaper, image_id=current_image.id), Hide())]



    if current_image.use_poem_screen:
        frame:
            xysize (gui.gallery_wallpaper_width, gui.gallery_wallpaper_height)
            offset gui.gallery_wallpaper_offset
            background Frame("bg club_day")
            padding (0, 0)


            use poem(current_poem, gallery=True, gallery_width=gui.gallery_wallpaper_width)
            button:
                xysize (1.0, 1.0)
                action Show("gallery_wallpaper_fullscreen", image_id=image_id)
    else:
        imagebutton at gallery_wallpaper_reel_zoom(gallery_get_grid_bounds(image_id)):
            idle current_image.asset_name
            action Show("gallery_wallpaper_fullscreen", image_id=image_id)



    frame at gallery_wallpaper_reel_reveal:
        background None
        style_prefix "gallery"
        padding (0, 0)
        xysize (gui.gallery_wallpaper_width, gui.gallery_wallpaper_height)
        align (0.0, 0.0)
        offset gui.gallery_wallpaper_offset

        showif current_image.description_text != "" or current_image.unlock_condition_text != "":
            frame:
                xsize 1.0
                yalign 1.0
                padding (0, 5)
                background Frame("#000000DD")
                has vbox
                xsize 1.0
                xalign 0.5
                showif current_image.description_text != "":
                    text "[current_image.description_text!t]":
                        style "gallery_wallpaper_description_text"
                showif current_image.description_text != "" and current_image.unlock_condition_text != "":
                    null height 5
                showif current_image.unlock_condition_text != "":
                    $ acqText = _("ACQUISITION PROCEDURE")
                    text "[[" + "[acqText!t]" + "]: " + _("[current_image.unlock_condition_text!t]"):
                        style "gallery_wallpaper_acquisition_text"


style gallery_wallpaper_acquisition_text:
    xanchor 0.5
    text_align 0.5
    color "#9C9C9C"
    font "fonts/NotoMono-Regular.ttf"
    size get_variable_size(14, 20, gui.text_scale)
    outlines []
    xalign 0.5

style gallery_wallpaper_description_text:
    xanchor 0.5
    text_align 0.5
    color "#ccc"
    size get_variable_size(14, 20, gui.text_scale)
    outlines []
    xalign 0.5

style gallery_wallpaper_button_text:
    font gui.virtual_desktop_text_font
    size get_variable_size(17, 30, gui.text_scale)
    color "#fff"
    insensitive_color "#ffffff6a"
    text_align 1.0
    align (0.5, 0.5)
    outlines []

style gallery_wallpaper_reel_button:
    xysize (40,45)
    yalign 0.5

transform gallery_wallpaper_reel_crop:
    crop (0,0,1.0,1.0)

transform gallery_wallpaper_reel_button_hover:
    alpha 1.0
    on hover:
        linear 0.1 alpha 0.6
    on idle:
        linear 0.1 alpha 1.0

transform gallery_wallpaper_reel_zoom(alignment):
    xysize (gui.gallery_wallpaper_width, gui.gallery_wallpaper_height)
    align (0.0, 0.0)
    offset gui.gallery_wallpaper_offset
    on show:
        xysize (gui.gallery_thumb_width, gui.gallery_thumb_height + 10)
        offset alignment
        parallel:
            easein_cubic 0.25 xysize (int((gui.gallery_wallpaper_width)), gui.gallery_wallpaper_height)
        parallel:
            easein_cubic 0.25 offset gui.gallery_wallpaper_offset
    on hide:
        xysize (int((gui.gallery_wallpaper_width)), gui.gallery_wallpaper_height)
        offset gui.gallery_wallpaper_offset
        parallel:
            easein_cubic 0.25 xysize ((gui.gallery_thumb_width, gui.gallery_thumb_height))
        parallel:
            easein_cubic 0.25 offset (alignment[0], alignment[1] - virtual_gallery_zoom_scroll_offset + 10)

transform gallery_wallpaper_reel_reveal():
    alpha 1.0
    on show:
        alpha 0.0
        pause 0.2
        ease 0.15 alpha 1.0
    on hide:
        alpha 0.0

transform gallery_wallpaper_reel_navigate(startoffset=0):
    subpixel True


    xpos 0.5
    xoffset 0.5 + gui.virtual_desktop_pictures_reel_thumb_width * startoffset
    linear 0.15 xoffset 0.5






screen gallery_wallpaper_fullscreen(image_id):

    key ['mouseup_3'] action NullAction()
    key ['mouseup_2'] action NullAction()

    frame at gallery_wallpaper_fullscreen_backdrop:
        background Frame("#000000DD")
        xysize (1.0,1.0)

    if virtual_gallery_images[image_id].use_poem_screen:
        $ current_poem = (None if not virtual_gallery_images[image_id].use_poem_screen else eval(virtual_gallery_images[image_id].poem_id))
        frame at gallery_wallpaper_fullscreen_img:
            xysize (1.0, 1.0)
            align (0.5, 0.5)
            background None
            padding (0, 0)
            dismiss action Hide()
            use poem(current_poem)
    else:
        $ focused_image = virtual_gallery_images[image_id].asset_name
        frame at gallery_wallpaper_fullscreen_img:
            xysize (1.0, 1.0)
            align (0.5, 0.5)
            background Frame(focused_image)
            dismiss action Hide()

transform gallery_wallpaper_fullscreen_img:
    on show:
        xysize (0.75, gui.gallery_wallpaper_height)
        align (0.5,0.1)
        parallel:
            easein_cubic 0.2 xysize (1.0, 1.0)
        parallel:
            easeout_cubic 0.2 align (0.5, 0.5)
    on hide:
        xysize (1.0, 1.0)
        align (0.5, 0.5)
        parallel:
            easeout 0.2 xysize (0.75, gui.gallery_wallpaper_height)
        parallel:
            easein 0.2 align (0.5, 0.1)
        parallel:
            pause 0.15
            ease_quad 0.05 alpha 0.0

transform gallery_wallpaper_fullscreen_backdrop:
    alpha 0.0
    on show:
        easeout_cubic 0.1 alpha 1.0
    on hide:
        easein_cubic 0.2 alpha 0.0

screen gallery_wallpaper_download_confirm(current_image):

    default download_vertical = True

    use virtual_desktop_confirm_dialog_popup(_("Save Image")):
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25

            text _("Save this image to your device?"):
                style "virtual_desktop_confirm_text"
                xalign 0.5

            if current_image.has_vertical == True:
                vbox:
                    xalign 0.5
                    spacing 10
                    style_prefix "plus_confirm_radio"

                    textbutton _("Portrait") action SetScreenVariable("download_vertical", True)
                    textbutton _("Landscape") action SetScreenVariable("download_vertical", False)

            null height 2

            vbox:
                xalign 0.5
                xsize 0.8
                spacing 10

                button:
                    style "virtual_desktop_framed_button"
                    xalign 0.5
                    ysize 54
                    action [Function(gallery_save_to_photos, image_id=current_image.id, vertical=(download_vertical if current_image.has_vertical else False)), Hide()]
                    text _("Save") style "virtual_desktop_confirm_button_text"

                button:
                    style "virtual_desktop_framed_button"
                    xalign 0.5
                    ysize 54
                    action Hide()
                    text _("Cancel") style "virtual_desktop_confirm_button_text"

style plus_confirm_radio_button_text is virtual_desktop_confirm_text
style plus_confirm_radio_button is plus_radio_button:
    yminimum get_variable_size(24, 32, gui.text_scale)
    ymaximum get_variable_size(42, 56, gui.text_scale)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
