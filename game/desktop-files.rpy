
init python:
    import time
    from enum import Enum


    config.repeat_transform_events.append("navigate")
    config.repeat_transform_events.append("back")
    if persistent.vm_timestamp == None:
        persistent.vm_timestamp = datetime.datetime.now()
    if persistent.ddlc_reset_timestamp == None:
        persistent.ddlc_reset_timestamp = persistent.vm_timestamp
    if plus_persistent.real_file_path_names == None:
        plus_persistent.real_file_path_names = [""]





    class DesktopVirtualFile:
        def __init__(self, data:dict, id:str):
            self.name = id                                                              
            self.virtual_path = data["virtual_path"]                                    
            self.utc_type = data["utc_type"]                                            
            self.file_size = get_human_readable_file_size(data["size"])                 
            self.icon = "virtual_desktop_generic_file_icon"
            self.file_type = "File"
            if "real_path" in data:
                self.real_path = data["real_path"]                                      
            else:
                self.real_path = None
            if "txt_file" in data:
                self.txt_file = data["txt_file"]                                        
                if self.txt_file == "plus-desktop-files/towerkeys.txt":
                    self.icon = "virtual_desktop_generic_file_icon"
                    self.file_type = "File"
                else:
                    self.icon = "virtual_desktop_text_file_icon"
                    self.file_type = "Text document"
            else:
                self.txt_file = None
            if "img_file" in data:
                self.img_file = data["img_file"]                                        
                self.icon = "virtual_desktop_image_file_icon"
                self.file_type = "Image"
            else:
                self.img_file = None
            if "timegate_hour" in data:
                self.timegate = [data["timegate_hour"], data["timegate_minute"]]        
            else:
                self.timegate = None
            self.visible = True                                                         
            self.utc = datetime.datetime.now()
            self.save_time = 0

    class DesktopVirtualFolder:
        def __init__(self, name: str) -> None:
            self.name = name
            self.subfolders = []
            self.files = []

    def parse_virtual_files():
        import tomllib
        files = {}
        with renpy.file("desktopfiles.toml", False) as f:
            file_toml_dict = tomllib.load(f)
            for file_id, data in file_toml_dict.items():
                files[file_id] = DesktopVirtualFile(data, file_id)
        return files

    def build_folder_structure(file_dict):
        folder_structure = {} 
        
        
        folder_structure[""] = DesktopVirtualFolder("root") 
        
        for file_name, file in file_dict.items():
            
            if file.virtual_path == "":
                folder_structure[""].files.append(file.name)
                continue
            
            
            split_path = file.virtual_path.split("/")
            current_path = "" 
            
            
            for folder_name in split_path:
                
                folder_path = folder_name if current_path == "" else current_path + "/" + folder_name
                
                
                if folder_path not in folder_structure:
                    folder_structure[folder_path] = DesktopVirtualFolder(folder_name)
                    folder_structure[current_path].subfolders.append(folder_path)
                
                
                current_path = folder_path 
                
                
                if current_path == file.virtual_path:
                    folder_structure[current_path].files.append(file.name)
        
        
        folder_structure["game/saves"] = DesktopVirtualFolder("saves")
        folder_structure["game"].subfolders.append("game/saves")
        
        
        
        excluded_folders = ["internal/5/4/5", "internal/4/2/0", "internal/1/5/1"]
        
        
        def create_dummy_folders(base_path="internal", depth=0):
            count = 0
            while count < 6:
                folder_name = str(count)
                new_path = base_path + "/" + folder_name
                if new_path not in folder_structure and new_path not in excluded_folders:
                    folder_structure[new_path] = DesktopVirtualFolder(folder_name)
                    folder_structure[base_path].subfolders.append(new_path)
                if depth < 2:
                    create_dummy_folders(new_path, depth + 1)
                count += 1
        
        create_dummy_folders()
        
        
        for folder in folder_structure:
            folder_structure[folder].subfolders.sort()
        
        return folder_structure    


    def update_virtual_file_states():
        global virtual_files
        update_virtual_save_entries()
        for file_name, file in virtual_files.items():
            
            
            
            if file.real_path != None:
                file.visible = True 
                if renpy.mobile:
                    if file.real_path not in plus_persistent.real_file_path_names:
                        file.visible = False
                else:
                    try: renpy.file("../" + file.real_path)
                    except: file.visible = False
            
            if file.visible == True:
                file.utc = get_modified_utc(file)





    def update_virtual_save_entries():
        global virtual_folders
        global virtual_files
        
        
        for file in virtual_folders["game/saves"].files:
            virtual_files.pop(file, None)
        virtual_folders["game/saves"].files.clear()
        
        
        real_saves = renpy.list_saved_games()
        for save in real_saves:
            data_dict = {}
            data_dict["virtual_path"] = "game/saves"
            data_dict["utc_type"] = "save"
            data_dict["size"] = -1
            save_name = str(save[0]) + "-LT1.save" 
            virtual_files[save_name] = DesktopVirtualFile(data_dict, save_name)
            virtual_files[save_name].save_time = datetime.datetime.fromtimestamp(save[3])
            virtual_folders["game/saves"].files.append(save_name)






    def try_open_file(file_id):
        
        renpy.run(SetScreenVariable("selected_entry", None)) 
        
        
        if file_id == None:
            return
        if file_id not in virtual_files:
            return
        
        file = virtual_files[file_id]
        txt_file_contents = ""
        img_file_displayable = None
        
        
        if file.timegate is not None:
            current_time = [datetime.datetime.now().hour, datetime.datetime.now().minute]
            if current_time[0] >= 12: 
                current_time[0] -= 12
            if current_time != file.timegate:
                renpy.run(SetVariable("confirm_title_message", "Error"))
                renpy.show_screen("dialog", "Unable to open [filename!t]: Unknown error. Please try again later.", Hide(), "filename", file_id)
                return
        
        
        if file.name == "reset.sh":
            if plus_persistent.game_cleared_once == True:
                renpy.run(SetVariable("confirm_title_message", "Reset VM"))
                renpy.run(Confirm("Reset this virtual machine?\n\nDOKI DOKI LITERATURE CLUB\n\nAll modified entities, environments, and data will be reverted to their original state.", Call("virtual_desktop_reset_ddlc"), Hide()))
            else:
                renpy.run(SetVariable("confirm_title_message", "Error"))
                renpy.show_screen("dialog", "Unable to run [filename!t]: Unknown error. Please try again later.", Hide(), "filename", file_id)
            return
        
        
        if file.txt_file is not None:
            with renpy.file(file.txt_file, encoding="unicode-escape") as f:
                txt_file_contents = f.read()
        elif file.name == "traceback.txt":
            txt_file_contents = traceback_text  
        
        
        if file.img_file is not None:
            img_file_displayable = renpy.get_registered_image(file.img_file)
        
        
        if txt_file_contents == "" and img_file_displayable == None:
            renpy.run(SetVariable("confirm_title_message", "Error"))
            renpy.show_screen("dialog", "Unable to open [filename!t]: Unknown file type.", Hide(), "filename", file_id)
            return
        
        
        renpy.show_screen("virtual_desktop_file_viewer", file_name=file.name, img_file=img_file_displayable, txt_string=txt_file_contents)
        
        if file.name == "project plan.txt":
            unlock("project_plan_open")


    def try_delete_file(file_id):
        renpy.run(SetScreenVariable("selected_entry", None))
        
        if file_id == "monika.chr" and (persistent.playthrough == 3 or (plus_persistent.game_cleared_once == True and persistent.playername == "")):
            renpy.run(SetVariable("confirm_title_message", "Delete File"))
            renpy.run(Confirm("Are you sure you want to delete this file?\n\nmonika.chr", [Function(delete_character, "monika"), Function(update_virtual_file_states)]))
        else:
            renpy.run(SetVariable("confirm_title_message", "Error"))
            renpy.show_screen("dialog", "Unable to delete [filename!t]: Elevated access permissions are required to perform this action.", Hide(), "filename", file_id)






    def get_modified_utc(file_data):
        if file_data.utc_type == "vm":
            return persistent.vm_timestamp
        elif file_data.utc_type == "ddlc":
            return persistent.ddlc_reset_timestamp
        elif file_data.utc_type == "save":
            return file_data.save_time
        elif file_data.utc_type == "real" and file_data.real_path != None:
            try:
                return datetime.datetime.fromtimestamp(os.path.getmtime(config.basedir + "/" + file_data.real_path))
            except:
                return datetime.datetime.now()
        return datetime.datetime.now()

    def get_human_readable_file_size(bytes):
        if bytes < 0:
            return ""
        
        
        suffixes = ["B", "KB", "MB"]
        size_barrier = 10 * 1024
        fraction_size = bytes
        suffix_index = 0
        while (suffix_index + 1) < len(suffixes):
            if fraction_size < size_barrier:
                break
            fraction_size /= 1024
            suffix_index += 1
        return str(int(fraction_size)) + " " + suffixes[suffix_index]  







    class NavigateToVirtualFolder(Action):
        def __init__(self, new_path, nav_atl_event="navigate"):
            self.new_path = new_path
            self.nav_atl_event = nav_atl_event
        def __call__(self):
            renpy.run(SetScreenVariable("current_path", self.new_path))
            renpy.run(SetScreenVariable("selected_entry", None))
            trigger_displayable_event("virtual_desktop_files_app", "list", self.nav_atl_event)
        def periodic(self, st):
            
            
            trigger_displayable_event("virtual_desktop_files_app", "list", None)



    def trigger_displayable_event(screen_name, displayable_id, event_name):
        screen_displayable = renpy.display.screen.get_displayable(screen_name, displayable_id)
        if screen_displayable is not None:
            screen_displayable.transform_event_responder = True 
            screen_displayable.set_transform_event(event_name)



image virtual_desktop_file_entry_highlight = Frame("gui/virtual_desktop/file highlight.png")
image virtual_desktop_file_entry_selected:
    Frame("gui/virtual_desktop/start menu highlight.png")
    xzoom -1.0

image virtual_desktop_path_nested_folder_icon = im.Scale("gui/virtual_desktop/filebrowser/breadcrumb folder nested.png", 26, 25)
image virtual_desktop_path_active_folder_icon = im.Scale("gui/virtual_desktop/filebrowser/breadcrumb folder active.png", 26, 25)

image virtual_desktop_generic_file_icon = im.Scale("gui/virtual_desktop/filebrowser/file icon generic.png", 22, 24)
image virtual_desktop_image_file_icon = im.Scale("gui/virtual_desktop/filebrowser/file icon image.png", 22, 24)
image virtual_desktop_text_file_icon = im.Scale("gui/virtual_desktop/filebrowser/file icon text.png", 22, 24)
image virtual_desktop_folder_icon = im.Scale("gui/virtual_desktop/filebrowser/folder.png", 25, 25)

image virtual_desktop_file_section_divider = im.Scale("gui/virtual_desktop/filebrowser/filetype section divider.png",2, 22)
image virtual_desktop_file_header_divider = im.Scale("gui/virtual_desktop/filebrowser/filetype header divider.png", 20, 2)

image virtual_file_hxppy_thxughts:
    "hxppy thxughts.png"
    zoom 1.3

transform file_list_icon_position:
    xpos 0.0
    yalign 0.5
transform file_list_name_position:
    xpos 0.06
    yalign 0.5
transform file_list_date_position:
    xpos 0.425
    yalign 0.5
transform file_list_type_position:
    xpos 0.68
    yalign 0.5
transform file_list_size_position:
    xpos 1.0
    yalign 0.5
    xanchor 1.0

transform file_list_crop:
    crop (0,0,1.0,1.0)

transform file_list_on_navigate:
    alpha 1.0
    xpos 0.0
    on navigate:
        alpha 0.0
        xpos 0.1
        parallel:
            easeout_quad 0.25 alpha 1.0
        parallel:
            ease_cubic 0.2 xpos 0.0
    on back:
        alpha 0.0
        xpos -0.1
        parallel:
            easeout_quad 0.25 alpha 1.0
        parallel:
            ease_cubic 0.2 xpos 0.0

transform virtual_desktop_file_entry_hover:
    xysize (1.0,1.0)
    on hover:
        linear 0.15 alpha 1.0
    on idle:
        linear 0.15 alpha 0.0



transform bios_reset_ddlc_initial:
    pos (0.18, 0.1)
    yanchor 0.0
transform bios_reset_ddlc_scroll:
    pos (0.18, 0.9)
    yanchor 1.0

transform bios_reset_scroll_cover:
    xysize (1.0, 0.1)
    yanchor (0.0)
    pos (0.5,0.0)


define virtual_files = parse_virtual_files()
define virtual_folders = build_folder_structure(virtual_files)







screen virtual_desktop_files_app():

    default current_path = ""
    default selected_entry = None
    default on_navigate = False

    $ folder_utc = persistent.vm_timestamp.strftime(_("%m-%d-%Y %H:%M"))

    style_prefix "virtual_desktop"

    use virtual_desktop_app_window("Files", window_width=get_variable_size(986, 1200, gui.text_scale), taskbar_icon="desktop_Files_H", footer_height=get_variable_size(30, 50)):
        key ['K_ESCAPE'] action NullAction()

        add "#efece8"

        vbox:

            hbox:
                xanchor 0.0
                xpos 10
                ysize 46
                first_spacing 20
                spacing 78
                if current_path != "":
                    $ prev_folder = current_path.rsplit('/', 1)[0]
                    $ back_folder = prev_folder if prev_folder != current_path else ""
                    button:
                        action NavigateToVirtualFolder(back_folder, "back")
                        idle_background "#00000000"
                        hover_background "#f1f1f1"
                        xysize (46, 34)
                        yalign 0.5
                        text "←":
                            align (0.5, 0.5)
                            size 16
                    $ folders = current_path.split('/')
                    for folder in folders:
                        frame:
                            if folder is folders[-1]:
                                background "#f7f5f3"
                            else:
                                background "#00000000"
                            xminimum 95
                            ysize 0.7
                            yalign 0.5
                            ypadding 6
                            xpadding 10
                            fixed:
                                xfit True
                                add "virtual_desktop_path_active_folder_icon" yalign 0.5 alpha 0.6
                                text _(folder):
                                    yalign 0.5
                                    xpos 35
                                    size get_variable_size(16, 22, gui.text_scale)


            frame:
                style_prefix "virtual_desktop_files"
                ysize get_variable_size(22, 28, gui.text_scale)
                xsize 1.0
                padding (0, 0)
                add "virtual_desktop_file_header_divider":
                    xsize 1.0
                    ypos 0.0
                frame:
                    text _("Name") at file_list_icon_position:
                        xoffset -14
                    add "virtual_desktop_file_section_divider" at file_list_date_position:
                        xoffset -8
                    text _("Date") at file_list_date_position
                    add "virtual_desktop_file_section_divider" at file_list_type_position:
                        xoffset -8
                    text _("Type") at file_list_type_position
                    add "virtual_desktop_file_section_divider":
                        xpos 0.9
                        xoffset -8
                        yalign 0.5
                    text _("Size"):
                        xpos 0.9
                        yalign 0.5



            fixed:
                fixed at file_list_crop:
                    fixed id "list" at file_list_on_navigate:
                        viewport id "desktop_file_viewport":

                            draggable True
                            style_prefix "virtual_desktop_files"


                            button:
                                xysize (1.0, 1.0)
                                action SetScreenVariable("selected_entry", None)

                            vbox:

                                for folder_path in virtual_folders[current_path].subfolders:
                                    $ folder_name = folder_path.rsplit('/', 1)[-1]
                                    if folder_name == "internal" and (renpy.mobile and not plus_purchased):
                                        pass
                                    else:
                                        button:

                                            if renpy.mobile:
                                                action NavigateToVirtualFolder(folder_path)
                                                hover_background "virtual_desktop_file_entry_selected"
                                            elif selected_entry == folder_name:
                                                style_prefix "virtual_desktop_files_selected"
                                                action NavigateToVirtualFolder(folder_path)
                                                background "virtual_desktop_file_entry_selected"
                                            else:
                                                action SetScreenVariable("selected_entry", folder_name)
                                                hover_background "virtual_desktop_file_entry_highlight"
                                            frame:
                                                add "virtual_desktop_folder_icon" at file_list_icon_position
                                                text _(folder_name) at file_list_name_position

                                                text "[folder_utc]" at file_list_date_position
                                                text _("File Folder") at file_list_type_position
                                                text "--" at file_list_size_position


                                for file in virtual_folders[current_path].files:
                                    $ file_data = virtual_files[file]
                                    if file_data.visible:
                                        button:

                                            if selected_entry == file:
                                                style_prefix "virtual_desktop_files_selected"
                                                action Function(try_open_file, file)
                                                background "virtual_desktop_file_entry_selected"
                                            else:
                                                action SetScreenVariable("selected_entry", file)
                                                hover_background "virtual_desktop_file_entry_highlight"
                                            frame:
                                                add file_data.icon at file_list_icon_position
                                                $ translated_file_name = renpy.translate_string(file_data.name)
                                                $ translated_file_name = translated_file_name if len(translated_file_name) < 30 else (translated_file_name[:28] + "...")
                                                text translated_file_name at file_list_name_position
                                                $ entry_utc = file_data.utc.strftime(_("%m-%d-%Y %H:%M"))
                                                text "[entry_utc]" at file_list_date_position
                                                text _(file_data.file_type) at file_list_type_position
                                                text _(file_data.file_size) at file_list_size_position
                vbar value YScrollValue("desktop_file_viewport") xpos 1.0 xoffset -10


        if selected_entry != None and selected_entry in virtual_files:
            hbox:
                style_prefix "virtual_desktop_files_footer"
                yanchor 0.0
                ypos 1.0
                xalign 1.0
                ysize get_variable_size(30,50,gui.text_scale)
                button:
                    action Function(try_delete_file, selected_entry)
                    text _("Delete")
                null width get_variable_size(1,40, gui.text_scale)
                button:
                    hover_background "#ffffffaa"
                    action Function(try_open_file, selected_entry)
                    text _("Open")
                null width 10

style virtual_desktop_files_footer_button:
    hover_background "#ffffffaa"
    ysize 1.0
    xpadding get_variable_size(10, 30, gui.text_scale)
style virtual_desktop_files_footer_text is virtual_desktop_text:
    size get_variable_size(17, 30, gui.text_scale)
    color "#fff"
    yalign 0.5

style virtual_desktop_files_text is virtual_desktop_text:
    shaper "freetype"
    size get_variable_size(16, 22, gui.text_scale)
    yalign 0.5
    hover_color "#fff"
style virtual_desktop_files_button:
    padding (0,0)
    ysize 56
    xsize 1.0
style virtual_desktop_files_frame:
    left_padding 21
    right_padding 27
    xfill True
    yfill True
    background "#00000000"
style virtual_desktop_files_selected_text is virtual_desktop_files_text:
    color "fff"
style virtual_desktop_files_selected_button is virtual_desktop_files_button
style virtual_desktop_files_selected_frame is virtual_desktop_files_frame



screen virtual_desktop_file_viewer(file_name, img_file=None, txt_string=None):
    modal True
    use virtual_desktop_app_window(file_name, get_variable_size(986, 1200), "", footer_height=1):
        key ['K_ESCAPE'] action NullAction()
        style_prefix "virtual_desktop"
        frame:
            background "#f6f6f6"
            xfill True
            yfill True
            showif img_file is not None:
                frame:
                    background "#00000000"
                    padding (50,50)
                    xysize (1.0,1.0)
                    add img_file xalign 0.5
            showif txt_string != "":
                if file_name == "poemwords.txt":
                    $ unlock("poemword_file_open")
                viewport id "txt":
                    if renpy.mobile:
                        draggable True
                    frame:
                        background "#00000000"
                        padding (50, 50)
                        text _(txt_string) style "virtual_desktop_file_viewer_text"
                vbar value YScrollValue("txt") xpos 1.0 xoffset -10

style virtual_desktop_file_viewer_text:
    font "fonts/NotoMono-Regular.ttf"
    size get_variable_size(15, 22, gui.text_scale)
    color "#171717"
    outlines []





label virtual_desktop_reset_ddlc:

    $ hex_characters = "1234567890ABCDEF"

    hide screen virtual_desktop_files_app
    hide screen virtual_desktop_start_menu
    hide screen virtual_desktop_wallpaper
    hide screen virtual_desktop

    show bios_layer at bios_glow_shader
    scene black onlayer bios
    show black onlayer bios zorder 300 at bios_reset_scroll_cover
    show bios_output_text "" onlayer bios at bios_reset_ddlc_initial



    $ b1 = "Initializing..."
    $ bios_output = "[b1!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(0.5)
    $ b2 = "Connecting"
    $ bios_output += "\n" + "[b2!t]"
    $ connecting_count = 0
    while connecting_count < 5:
        $ bios_output += "."
        show bios_output_text (bios_output + "█")
        $ connecting_count += 1
        pause(0.5)
    $ b3 = "Connected"
    $ bios_output += " " + "[b3!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(2.0)
    $ b4 = "Stopping virtual machine..."
    $ bios_output += "\n" + "[b4!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(1.0)
    $ b5 = "Stopped"
    $ bios_output += "\n" + "[b5!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(2.5)
    $ b6 = "Beginning virtual machine restore"
    $ bios_output += "\n" + "[b6!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(0.1)



    $ delete_all_saves()

    $ b7 = "Restoring environment database..."
    $ bios_output += "\n" + "[b7!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(0.1)


    $ env_count = 0
    while env_count < 33:

        python:
            pause_time = random.uniform(0.025, 0.1)
            if random.randint(0, 19) == 0: 
                pause_time += 0.2
            elif random.randint(0, 9) == 0: 
                pause_time += 0.1
            entry_1 = ''.join(random.choices(hex_characters, k=16))
            entry_2 = ''.join(random.choices(hex_characters, k=16))
            entry_3 = ''.join(random.choices(hex_characters[:10], k=3)) 
            env_count += 1
        pause(pause_time)
        $ b8 = "ENVIRONMENT_ENTRIES"
        $ bios_output += "\n" + "[b8!t]" + "[[" + entry_1 + "/" + entry_2 + "/00000" + entry_3 + "]"
        call virtual_desktop_reset_update_output (bios_output)

    $ b9 = "Restoring entities..."
    $ bios_output += "\n" + "[b9!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(0.1)





    python:
        delete_character("sayori")
        delete_character("natsuki")
        delete_character("yuri")
        delete_character("monika")


        plus_persistent.reapplyPreferences = True
        save_preferences_to_external()


    $ ent_count = 0
    $ char_names = ["sayori", "natsuki", "yuri", "monika"]
    while ent_count < 4:
        python:
            pause_time = random.uniform(1.5, 3)
            e1 = "'MONITOR_KERNAL_ACCESS'"
            e2 = "'NONE'"
            entity_access = "[e1!t]" if ent_count == 3 else "[e2!t]"
            entity_entry = ''.join(random.choices(hex_characters, k=16))

            if renpy.mobile:
                if ("characters/" + char_names[ent_count] + ".chr") not in plus_persistent.real_file_path_names:
                    plus_persistent.real_file_path_names.append("characters/" + char_names[ent_count] + ".chr")
            else:
                try: renpy.file("../characters/" + char_names[ent_count] + ".chr")
                except: open(config.basedir + "/characters/" + char_names[ent_count] + ".chr", "wb").write(renpy.file(char_names[ent_count] + ".chr").read())
            ent_count += 1
        $ b10 = "ENTITY"
        $ bios_output += "\n" + "[b10!t]" + "[[" + entity_entry + ", " + entity_access + "]"
        call virtual_desktop_reset_update_output (bios_output)
        pause(pause_time)



    $ b11 = "Rebuilding filesystem..."
    $ bios_output += "\n" + "[b11!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(3.8)



    $ b12 = "Filesystem rebuild complete"
    $ bios_output += "\n" + "[b12!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(0.1)

    $ b13 = "Virtual machine restored successfully."
    $ b14 = "Starting virtual machine..."
    $ bios_output += "\n" + "[b13!t]" + "\n" + "[b14!t]"
    call virtual_desktop_reset_update_output (bios_output)
    pause(4.8)

    $ b15 = "Started"
    $ bios_output += "\n" + "[b15!t]"
    call virtual_desktop_reset_update_output (bios_output)

    python:

        plus_persistent.seen = persistent._seen_ever 
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        renpy.utter_restart() 



label virtual_desktop_reset_update_output(bios_output=""):
    $ bios_line_count = bios_output.count('\n')
    if bios_output.count('\n') > 23:
        show bios_output_text bios_output at bios_reset_ddlc_scroll
    else:
        show bios_output_text bios_output at bios_reset_ddlc_initial
    pause(0.01)
    show bios_output_text (bios_output + "\n█")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
