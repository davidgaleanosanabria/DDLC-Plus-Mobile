
init python:
    jukebox_selection = -1
    jukebox_playing = False
    jukebox_loop = False
    jukebox_playlist_mode = False

    def jukebox_parse_entries():
        import tomllib
        ret = []
        with renpy.file("desktopmusic.toml", False) as f:
            toml_dict = tomllib.load(f)
            for id, data in toml_dict.items():
                ret.append(data)
        return ret

    jukebox_definitions = jukebox_parse_entries()

    def on_jukebox_close():
        unlock_candy_heartz()
        record_time_in_jukebox()

    def unlock_candy_heartz():
        if is_unlocked(plus_persistent.all_unlocked, "candy_heartz_UNLOCKED"):
            unlock("candy_heartz")
        if is_unlocked(plus_persistent.all_unlocked, "candy_heartz_first_UNLOCKED"):
            unlock("candy_heartz_first")

    def record_time_in_jukebox():
        plus_persistent.jukebox_timer += (time.time() - plus_persistent.jukebox_enter_time)
        if plus_persistent.jukebox_timer >= 1200:
            unlock("mixtape")
        plus_persistent.save()

    def set_jukebox_enter_time():
        plus_persistent.jukebox_enter_time = time.time()
        plus_persistent.save()

    def jukebox_function_check_is_unlocked(music_id):
        
        unlocked = True
        
        unlock_string = jukebox_definitions[music_id]["unlock_show"] 
        if unlock_string != "" and unlock_string != '':
            if not jukebox_function_check_string_all_unlocked(unlock_string):
                unlocked = False
        
        if unlocked:
            unlock_string = jukebox_definitions[music_id]["unlock_hide"] 
            if unlock_string != "" and unlock_string != '':
                unlocked = False
                if not jukebox_function_check_string_all_unlocked(unlock_string):
                    unlocked = True
        
        if not unlocked:
            unlock_string = jukebox_definitions[music_id]["unlock_reshow"] 
            if unlock_string != "" and unlock_string != '':
                unlocked = True
                if not jukebox_function_check_string_all_unlocked(unlock_string):
                    unlocked = False
        
        return unlocked

    def jukebox_function_check_string_all_unlocked(unlock_string):
        split = unlock_string.split(';')
        for s in split:
            if s not in plus_persistent.bgm_unlocked and s not in plus_persistent.all_unlocked:
                return False
        return True

    def jukebox_function_toggle_playlist(music_id):
        if music_id in plus_persistent.jukebox_playlist:
            plus_persistent.jukebox_playlist.remove(music_id)
        else:
            plus_persistent.jukebox_playlist.append(music_id)
        plus_persistent.save()
        if jukebox_get_playing() != None:
            jukebox_function_play_song()

    def jukebox_function_select(music_id):
        global jukebox_selection
        jukebox_selection = music_id
        jukebox_function_play_button()

    def jukebox_function_play_button():
        global jukebox_selection
        global jukebox_playing
        
        if (jukebox_get_playing() != None) and (jukebox_get_playing() in jukebox_definitions[jukebox_selection]["track_definition"]):
            renpy.music.stop()
            jukebox_playing = False
            jukebox_function_android_stop()
        else:
            jukebox_function_play_song()

    def jukebox_function_stop_all():
        global jukebox_playing
        
        renpy.music.stop()
        jukebox_playing = False
        jukebox_function_android_stop()

    def jukebox_function_forward():
        global jukebox_selection
        global jukebox_playlist_mode
        global jukebox_playing
        if (jukebox_selection < 0):
            jukebox_selection = 0
            return
        if jukebox_playlist_mode and len(plus_persistent.jukebox_playlist) > 0:
            if jukebox_selection in plus_persistent.jukebox_playlist:
                jukebox_selection = plus_persistent.jukebox_playlist[(plus_persistent.jukebox_playlist.index(jukebox_selection) + 1) % len(plus_persistent.jukebox_playlist)]
            else:
                jukebox_selection = plus_persistent.jukebox_playlist[0]
        else:
            while True:
                jukebox_selection = (jukebox_selection + 1) % len(jukebox_definitions)
                if jukebox_function_check_is_unlocked(jukebox_selection):
                    break
        
        if jukebox_playing:
            jukebox_function_play_song()

    def jukebox_function_back():
        global jukebox_selection
        global jukebox_playlist_mode
        global jukebox_playing
        if (jukebox_selection < 0):
            jukebox_selection = 0
            return
        if jukebox_playlist_mode and len(plus_persistent.jukebox_playlist) > 0:
            if jukebox_selection in plus_persistent.jukebox_playlist:
                jukebox_selection = plus_persistent.jukebox_playlist[(plus_persistent.jukebox_playlist.index(jukebox_selection) + len(plus_persistent.jukebox_playlist) - 1) % len(plus_persistent.jukebox_playlist)]
            else:
                jukebox_selection = plus_persistent.jukebox_playlist[0]
        else:
            while True:
                jukebox_selection = (jukebox_selection + len(jukebox_definitions) - 1) % len(jukebox_definitions)
                if jukebox_function_check_is_unlocked(jukebox_selection):
                    break
        if jukebox_playing:
            jukebox_function_play_song()

    def jukebox_function_loop():
        global jukebox_loop
        jukebox_loop = not jukebox_loop
        if jukebox_get_playing() != None:
            jukebox_function_play_song()

    def jukebox_function_playlist_mode(on):
        global jukebox_playlist_mode
        jukebox_playlist_mode = on

    def jukebox_function_play_song():
        global jukebox_selection
        global jukebox_playing
        global jukebox_loop
        if jukebox_selection < 0:
            return
        current = jukebox_get_playing()
        
        if jukebox_loop:
            next = jukebox_definitions[jukebox_selection]["track_definition"]
        else:
            next = jukebox_function_get_mid(jukebox_definitions[jukebox_selection])
        
        if "Candy_Hearts" in next:
            unlock("candy_heartz_first_UNLOCKED")
        if "Candy_Heartz_First_Time" in next:
            unlock("candy_heartz_UNLOCKED")
        
        jukebox_playing = True
        
        if current == None or current != next:
            
            if renpy.android:
                renpy.music.play(next, loop=jukebox_loop, relative_volume=0.0)
                jukebox_function_android_play()
            else:
                renpy.music.play(next, loop=jukebox_loop)

    def jukebox_function_android_play():
        if not renpy.android:
            return
        
        global jukebox_selection
        global jukebox_playing
        global jukebox_loop
        global jukebox_playlist_mode
        
        import jnius
        handle = jnius.autoclass("org.renpy.android.PlaybackService")
        
        if not jukebox_playing or jukebox_selection < 0:
            handle.Stop()
            return
        
        if not jukebox_loop:
            if jukebox_playlist_mode and jukebox_selection in plus_persistent.jukebox_playlist:
                handle.ClearPlaylist()
                for p in plus_persistent.jukebox_playlist:
                    dat = jukebox_definitions[p]
                    handle.AddPlaylist(jukebox_function_get_mid(dat), dat["track_name"], dat["artist"], dat["asset_name"])
                handle.SetLoop(2)
                handle.SetVolume(preferences.get_mixer("music"))
                handle.Play(plus_persistent.jukebox_playlist.index(jukebox_selection))
            else:
                handle.ClearPlaylist()
                ind = 0
                ic = -1
                for i, dat in enumerate(jukebox_definitions):
                    if jukebox_function_check_is_unlocked(i):
                        handle.AddPlaylist(jukebox_function_get_mid(dat), dat["track_name"], dat["artist"], dat["asset_name"])
                        ic += 1
                        if i == jukebox_selection:
                            ind = ic
                handle.SetLoop(2)
                handle.SetVolume(preferences.get_mixer("music"))
                handle.Play(ind)
        else:
            handle.ClearPlaylist()
            ind = 0
            ic = -1
            for i, dat in enumerate(jukebox_definitions):
                if jukebox_function_check_is_unlocked(i):
                    handle.AddPlaylist(jukebox_function_get_mid(dat), dat["track_name"], dat["artist"], dat["asset_name"])
                    ic += 1
                    if i == jukebox_selection:
                        ind = ic
            handle.SetLoop(1)
            handle.SetVolume(preferences.get_mixer("music"))
            handle.Play(ind)


    def jukebox_function_android_init():
        import jnius
        jnius.autoclass("org.renpy.android.PlaybackService").Init()

    def jukebox_function_android_stop():
        if not renpy.android:
            return
        import jnius
        jnius.autoclass("org.renpy.android.PlaybackService").Stop()

    def jukebox_get_playing():
        return renpy.music.get_playing()


    def jukebox_function_format_time(length):
        if length == None:
            return "0:00"
        length = math.ceil(float(length))
        mins = math.floor(length / 60)
        secs = math.floor(length % 60)
        if secs > 9:
            return str(mins) + ":" + str(secs)
        else:
            return str(mins) + ":0" + str(secs)

    def jukebox_function_get_duration(music_id):
        if music_id < 0:
            return "0:00"
        return jukebox_function_format_time(jukebox_definitions[music_id]["length"])

    def jukebox_function_get_mid(data):
        mid = data["track_definition"].split(">")
        mid = mid[len(mid)-1]
        return mid

    def jukebox_function_get_pos():
        if not renpy.android:
            return renpy.music.get_pos()
        else:
            import jnius
            return jnius.autoclass("org.renpy.android.PlaybackService").SeekPosition()

    def jukebox_update_volume():
        if renpy.android:
            import jnius
            jnius.autoclass("org.renpy.android.PlaybackService").SetVolume(preferences.get_mixer("music"))

    def jukebox_function_refresh_next_song():
        global jukebox_selection
        global jukebox_playing
        if renpy.android:
            import jnius
            handle = jnius.autoclass("org.renpy.android.PlaybackService")
            if not handle.IsPlaying():
                jukebox_playing = False
            else:
                jukebox_playing = True
                uri = handle.CurrentlyPlaying()
                if jukebox_selection < 0 or (jukebox_function_get_mid(jukebox_definitions[jukebox_selection]) != uri and jukebox_definitions[jukebox_selection]["track_definition"] != uri):
                    for i, k in enumerate(jukebox_definitions):
                        if jukebox_function_get_mid(k) == uri or k["track_definition"] == uri:
                            jukebox_selection = i
        
        else:
            current = jukebox_get_playing()
            
            if current == None and jukebox_playing:
                if jukebox_loop:
                    jukebox_function_play_song()
                else:
                    jukebox_function_forward()
        
        trigger_unlock = jukebox_definitions[jukebox_selection]["unlock_trigger"]
        
        if trigger_unlock != "" and trigger_unlock != '' and jukebox_function_get_pos() != None and jukebox_function_get_pos() / float(jukebox_definitions[jukebox_selection]["length"]) > 0.3:
            unlock(trigger_unlock)




screen jukebox_toggle_playlist(music_id):
    frame:
        xysize (22,22)
        align (0.5,0.5)
        if music_id in plus_persistent.jukebox_playlist:
            background Frame("gui/virtual_desktop/music/remove button icon.png")
            hover_background Frame("gui/virtual_desktop/music/remove_icon_highlighted.png")
        else:
            background Frame("gui/virtual_desktop/music/add icon.png")
            hover_background Frame("gui/virtual_desktop/music/add_icon_highlighted.png")

screen jukebox_small_button(image_name, active):
    frame:
        xsize get_variable_size(53, 78, gui.text_scale)
        ysize get_variable_size(36, 53, gui.text_scale)

        if active:
            background Frame("gui/virtual_desktop/music/media controls button active.png")
        else:
            background Frame("gui/virtual_desktop/music/media controls button.png")
        hover_background Frame("gui/virtual_desktop/music/media controlls button selected.png")

        add image_name at jukebox_thirdsize:
            align (0.5, 0.5)

transform jukebox_thirdsize:
    zoom 0.3
    matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)
    on hover:
        matrixcolor ColorizeMatrix("000000", "FFFFFF")
    on idle:
        matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)

screen jukebox_large_button(text_content, active):
    frame:
        xysize (133, 34)
        if active:
            background Frame("gui/virtual_desktop/music/music - active tab.png")
        else:
            background Frame("gui/virtual_desktop/music/music -inactive tab.png")
        hover_background Frame("gui/virtual_desktop/music/music - active selected tab.png")

        if active:
            text text_content:
                size 15
                align (0.5, 0.5)
                bold True
                color "FFFFFF"
        else:
            text text_content:
                size 15
                align (0.5, 0.5)
                bold True
                color gui.virtual_desktop_text_color
                hover_color "FFFFFF"

image jukebox_media_button_active_background = Frame("gui/virtual_desktop/music/media controls button active.png")
image jukebox_media_button_inactive_background = Frame("gui/virtual_desktop/music/media controls button.png")
image jukebox_media_button_hover_background = Frame("gui/virtual_desktop/music/media controlls button selected.png")

style jukebox_large_button:
    background Frame("gui/virtual_desktop/music/music -inactive tab.png")
    insensitive_background Frame("gui/virtual_desktop/music/music - active selected tab.png")
    hover_background Frame("gui/virtual_desktop/music/music - active tab.png")
    xsize 0.5
    ysize get_variable_size(34, 52, gui.text_scale)

style jukebox_large_button_text is jukebox_bold_text:
    color gui.virtual_desktop_text_color
    hover_color "#FFFFFF"
    insensitive_color "#FFFFFF"

    size get_variable_size(15, 24, gui.text_scale)
    text_align 0.5






screen virtual_desktop_music_app:

    on "show" action ([Function(clear_notification, "bgm"), Function(set_jukebox_enter_time)])
    on "hide" action ([Function(jukebox_function_stop_all), Function(on_jukebox_close)])

    style_prefix "virtual_desktop"
    use virtual_desktop_app_window("Music", window_width=get_variable_size(880, 1100, gui.text_scale), taskbar_icon="desktop_Music_H"):
        key ['K_ESCAPE'] action NullAction()
        if renpy.android:
            $ jukebox_function_android_init()
        frame:
            xpadding 10
            viewport id "desktop_popup_canvas":
                draggable True mousewheel True
                xalign 1.0
                xsize 0.65

                $ music_count = len(jukebox_definitions)

                vbox:
                    spacing 0
                    style_prefix "jukebox"
                    align (0.5, 1.0)
                    if jukebox_playlist_mode:
                        $ list = plus_persistent.jukebox_playlist
                    else:
                        $ list = range(music_count)
                    $ count = 0
                    for music_id in list:
                        if jukebox_function_check_is_unlocked(music_id):
                            $ count += 1
                            button:
                                padding 0,0,0,0
                                xysize 1.0, get_variable_size(40, 60, gui.text_scale)
                                action Function(jukebox_function_select, music_id = music_id)
                                hover_background Frame("gui/virtual_desktop/file highlight.png", color="FFFFFF2D")
                                frame:
                                    padding 20,0,20,0
                                    xysize 1.0, 1.0
                                    background None
                                    if music_id != jukebox_selection:
                                        text "[count]":
                                            align 0.05, 0.5
                                            text_align 0.0
                                    else:
                                        add "gui/virtual_desktop/music/music note white.png" at jukebox_titlerow_hover:
                                            align 0.05, 0.5
                                            xysize 16, 16
                                    fixed:
                                        xsize get_variable_size(350, 420)
                                        yalign 0.5
                                        xalign 0.1
                                        ysize 1.0
                                        text _(jukebox_definitions[music_id]["track_name"]) at loc_text_fit:
                                            style "jukebox_bold_text"
                                            idle_color ("#CF3482" if music_id == jukebox_selection else gui.virtual_desktop_text_color)
                                            xanchor 0.0
                                            align 0.1, 0.5
                                            text_align 0.0
                                            shaper "freetype"
                                            layout "nobreak"

                                    text "[jukebox_function_get_duration(music_id)]":
                                        align 0.85, 0.5
                                        xsize 0
                                    button:
                                        align 1.0, 0.5
                                        action Function(jukebox_function_toggle_playlist, music_id = music_id)
                                        use jukebox_toggle_playlist(music_id)
                                add Solid(gui.virtual_desktop_soft_accent_color, ysize=1):
                                    yalign 1.0
            frame:
                xsize 0.32
                xalign 0.0

                has vbox
                style_prefix "jukebox"
                null height 10
                grid 2 1:
                    spacing 5

                    xsize 1.0
                    xalign 0.5
                    button:
                        action Function(jukebox_function_playlist_mode, on = False)
                        style "jukebox_large_button"
                        sensitive jukebox_playlist_mode == True
                        text _("All Songs") style "jukebox_large_button_text" at loc_text_fit

                    button:
                        action Function(jukebox_function_playlist_mode, on = True)
                        style "jukebox_large_button"
                        sensitive jukebox_playlist_mode == False
                        text _("Playlist") style "jukebox_large_button_text" at loc_text_fit

                null height get_variable_size(30, 10, gui.text_scale)
                add Solid(gui.virtual_desktop_soft_accent_color, ysize=1)
                null height 10

                $ jukebox_function_refresh_next_song()

                if jukebox_selection != -1:
                    add jukebox_definitions[jukebox_selection]["asset_name"]:
                        xalign 0.5
                        xysize 266,266
                    null height 10
                    frame:
                        background None
                        padding 0,0,0,0
                        xysize 1.0, 25
                        text jukebox_definitions[jukebox_selection]["track_name"] style "jukebox_playing_song_title_text" at loc_text_fit:
                            size get_variable_size(18, 22, gui.text_scale)
                            layout "nobreak"
                    text jukebox_definitions[jukebox_selection]["artist"] style "jukebox_playing_song_artist_text"
                else:
                    add Solid("00000000"):
                        xalign 0.5
                        xysize 266,266
                    null height 10
                    frame:
                        background None
                        padding 0,0,0,0
                        xysize 1.0, 25
                        text _("Not Playing") style "jukebox_playing_song_title_text":
                            size (get_variable_size(18, 22, gui.text_scale))
                    text " " style "jukebox_playing_song_artist_text"
                null height 10
                if jukebox_function_get_pos() == None:
                    bar:
                        style "jukebox_bar"
                        value 0.0
                else:
                    bar:
                        style "jukebox_bar"
                        range 1.0
                        value float(jukebox_function_get_pos()) / float(jukebox_definitions[jukebox_selection]["length"])
                null height 5
                frame:
                    xysize 0.9, 20
                    align 0.5,0.5
                    background None
                    padding 0,0,0,0
                    text "[jukebox_function_format_time(jukebox_function_get_pos())]":
                        xalign 0.0
                        text_align 0.0
                        xanchor 0.0
                        size 13
                    text "[jukebox_function_get_duration(jukebox_selection)]":
                        xalign 1.0
                        text_align 1.0
                        xanchor 1.0
                        size 13
                null height 10
                hbox:
                    xalign 0.5
                    button:
                        action Function(jukebox_function_back)
                        use jukebox_small_button("gui/virtual_desktop/music/previous button white.png", False)
                    button:
                        action Function(jukebox_function_forward)
                        use jukebox_small_button("gui/virtual_desktop/music/next icon white.png", False)
                    if str(jukebox_get_playing()) in jukebox_definitions[jukebox_selection]["track_definition"]:
                        button:
                            action Function(jukebox_function_play_button)
                            use jukebox_small_button("gui/virtual_desktop/music/stop icon white.png", False)
                    else:
                        button:
                            action Function(jukebox_function_play_button)
                            use jukebox_small_button("gui/virtual_desktop/music/play icon white.png", False)
                    button:
                        action Function(jukebox_function_loop)
                        use jukebox_small_button("gui/virtual_desktop/music/loop white.png", jukebox_loop)
            add Solid(gui.virtual_desktop_soft_accent_color, xsize=1):
                xalign 0.34
            vbar value YScrollValue("desktop_popup_canvas") xpos 1.0


style jukebox_text is virtual_desktop_text:
    align (0.5, 0.5)
    xycenter (0.5, 0.5)
    xanchor 0.5
    size get_variable_size(18, 22, gui.text_scale)

    idle_color gui.virtual_desktop_text_color
    hover_color "FFFFFF"

style jukebox_bold_text is jukebox_text:
    font "fonts/HKGrotesk-SemiBold-rounded.otf"
    shaper "freetype"
    kerning 1.25

style jukebox_button_text is jukebox_text

style jukebox_playing_song_title_text is jukebox_bold_text:
    xalign 0.5
    text_align 0.5

    color gui.virtual_desktop_text_color
    layout "nobreak"

style jukebox_playing_song_artist_text is jukebox_playing_song_title_text:

    font gui.virtual_desktop_text_font

style jukebox_bar:
    xysize (0.9,12)
    align (0.5,0.5)
    left_bar Frame("gui/virtual_desktop/music/music progress bar.png")
    right_bar Frame("gui/virtual_desktop/music/music track bar.png")
    thumb None

transform jukebox_titlerow_hover:
    matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)
    on hover:
        matrixcolor ColorizeMatrix("000000", "FFFFFF")
    on idle:
        matrixcolor ColorizeMatrix("000000", gui.virtual_desktop_accent_color)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
