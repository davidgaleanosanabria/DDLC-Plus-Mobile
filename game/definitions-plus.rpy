define config.steam_appid = 1388880


define config.limit_transform_crop = "only_float"
define config.limit_transform_crop = True
define config.window_next = False
define config.window_functions_set_auto = True
define bubble.clear_retain_statements = [ ]
define config.box_reverse_align = True

init python:

    class UnlockEntry:
        def __init__(self, data: dict, id: str) -> None:
            self.id = id
            self.id_num = data['id']
            self.name = data['name']
            self.display_name = data['display_name']
            self.show_notification = False if data['show_notification'] == "false" else True
            self.trigger_progressed = False if data['trigger_progressed'] == "false" else True
            self.ignore_in_completion = False if data['ignore_in_completion'] == "false" else True
            self.persistance = data['persistance'] 
            self.type = data['type'] 

    def parse_unlock_entries():
        import tomllib
        unlocks = {}
        with renpy.file("unlock_data.toml", False) as f:
            unlocks_toml_dict = tomllib.load(f)
            for entry_id, data in unlocks_toml_dict.items():
                unlocks[entry_id] = UnlockEntry(data, entry_id)
        return unlocks




    plus_persistent = MultiPersistent("teamsalvato.ddlcplus")


    if plus_persistent.desktop_wallpaper is None:
        plus_persistent.desktop_wallpaper = "images/gallery_images/gallery_default_wallpaper.png"

    if plus_persistent.side_stories_unlocked is None:
        plus_persistent.side_stories_unlocked = [False, False, False, False, False, False, False, False, False, False, False, False]
    if plus_persistent.side_stories_read is None:
        plus_persistent.side_stories_read = [False, False, False, False, False, False]
    if plus_persistent.bgm_unlocked is None:
        plus_persistent.bgm_unlocked = []
    if plus_persistent.img_unlocked is None:
        plus_persistent.img_unlocked = []
    if plus_persistent.all_unlocked is None:
        plus_persistent.all_unlocked = []
    if plus_persistent.read_mails is None:
        plus_persistent.read_mails = []
    if plus_persistent.mail_unlock_times is None:
        plus_persistent.mail_unlock_times = ["", "", "", "", "", "", "", "", ""]
    if plus_persistent.ddlc_reset_timestamp is None:
        plus_persistent.ddlc_reset_timestamp = datetime.datetime.now()
    if plus_persistent.vm_timestamp is None:
        plus_persistent.vm_timestamp = datetime.datetime.now()
    if plus_persistent.game_cleared_once is None:
        plus_persistent.game_cleared_once = False
    if plus_persistent.desktop_boxes_drawn is None:
        plus_persistent.desktop_boxes_drawn = 0
    if plus_persistent.monika_delete_once is None:
        plus_persistent.monika_delete_once = False
    if plus_persistent.settings_fullscreen is None:
        plus_persistent.settings_fullscreen = False
    if plus_persistent.settings_vsync is None:
        plus_persistent.settings_vsync = True
    if plus_persistent.settings_resolution is None:
        plus_persistent.settings_resolution = (1920,1080)
    if plus_persistent.notifications is None:
        plus_persistent.notifications = []
    if plus_persistent.jukebox_playlist is None:
        plus_persistent.jukebox_playlist = []
    if plus_persistent.jukebox_timer is None:
        plus_persistent.jukebox_timer = 0
    if plus_persistent.jukebox_time_entered is None:
        plus_persistent.jukebox_time_entered = 0

    def is_unlocked(check_list, unlock_string):
        if unlock_string in check_list:
            return True

    def is_unlocked_all(unlock_string):
        return is_unlocked(plus_persistent.all_unlocked, unlock_string)

    def add_unlocked(check_list, unlock_string):
        if is_unlocked(check_list, unlock_string):
            return
        
        check_list.append(unlock_string)
        
        if check_list == plus_persistent.bgm_unlocked:
            unlock_notification("bgm")
        elif check_list == plus_persistent.img_unlocked:
            unlock_notification("bg")

    def check_domino_unlocks():
        
        
        if "special_all" not in plus_persistent.all_unlocked:
            if ("special2" in plus_persistent.all_unlocked and
            "special3" in plus_persistent.all_unlocked and
            "special4" in plus_persistent.all_unlocked and
            "special5b" in plus_persistent.all_unlocked and
            "special6" in plus_persistent.all_unlocked and
            "special8" in plus_persistent.all_unlocked and
            "special9" in plus_persistent.all_unlocked and
            "special10" in plus_persistent.all_unlocked and
            "special11" in plus_persistent.all_unlocked):
                unlock("special_all")
        
        
        if "ax_sayori" not in plus_persistent.all_unlocked:
            if ("dear_sunshine" in plus_persistent.all_unlocked and
            "bottles" in plus_persistent.all_unlocked and
            "take_my_hand" in plus_persistent.all_unlocked and
            "become_the_flower" in plus_persistent.all_unlocked):              
                unlock("ax_sayori")
        
        if "ax_natsuki" not in plus_persistent.all_unlocked:
            if ("eagles_can_fly" in plus_persistent.all_unlocked and
            "amy_likes_spiders" in plus_persistent.all_unlocked and
            "ill_be_your_beach" in plus_persistent.all_unlocked and
            "because_you" in plus_persistent.all_unlocked and
            "the_best_place_in_the_world" in plus_persistent.all_unlocked):             
                unlock("ax_natsuki") 
        
        if "ax_yuri" not in plus_persistent.all_unlocked:
            if ("ghost_under_the_light" in plus_persistent.all_unlocked and
            "the_raccoon" in plus_persistent.all_unlocked and
            "beach" in plus_persistent.all_unlocked and
            "ghost_under_the_light_2" in plus_persistent.all_unlocked and
            "wheel" in plus_persistent.all_unlocked):             
                unlock("ax_yuri")
        
        if "ax_monika" not in plus_persistent.all_unlocked:
            if ("hole_in_wall" in plus_persistent.all_unlocked and
            "save_me" in plus_persistent.all_unlocked and
            "the_lady_who_knows_everything" in plus_persistent.all_unlocked and
            "hole_in_wall_2" in plus_persistent.all_unlocked and
            "happy_end" in plus_persistent.all_unlocked):             
                unlock("ax_monika")
        
        
        if "epilogue" not in plus_persistent.all_unlocked:
            if False not in plus_persistent.side_stories_read:
                unlock("epilogue")

    def unlock(unlock_string):
        
        value_pair = unlock_string.split("_", 1)
        
        
        if value_pair[0] == "bgm":
            add_unlocked(plus_persistent.bgm_unlocked, unlock_string)
        
        
        elif value_pair[0] == "bg":
            add_unlocked(plus_persistent.img_unlocked, unlock_string)
        
        
        elif value_pair[0] == "sayori":
            if value_pair[1] == "exclusive1":
                unlock_sidestory(0)                
                unlock("sidestory_1")
            elif value_pair[1] == "exclusive2":
                unlock_sidestory(6)
        elif value_pair[0] == "yuri":
            if value_pair[1] == "exclusive1":
                unlock_sidestory(2)
            elif value_pair[1] == "exclusive2":
                unlock_sidestory(8)
        elif value_pair[0] == "natsuki":
            if value_pair[1] == "exclusive1":
                unlock_sidestory(4)
            elif value_pair[1] == "exclusive2":
                unlock_sidestory(10)
        
        elif value_pair[0] == "sm":
            if value_pair[1] == "part2":
                unlock_sidestory(1)
            elif value_pair[1] == "exclusive":
                add_unlocked(plus_persistent.img_unlocked, unlock_string)
        elif value_pair[0] == "sy":
            if value_pair[1] == "part2":
                unlock_sidestory(3)
            elif value_pair[1] == "exclusive":
                add_unlocked(plus_persistent.img_unlocked, unlock_string)
        elif value_pair[0] == "nm":
            if value_pair[1] == "part2":
                unlock_sidestory(5)
            elif value_pair[1] == "exclusive":
                add_unlocked(plus_persistent.img_unlocked, unlock_string)
        elif value_pair[0] == "sn":
            if value_pair[1] == "part2":
                unlock_sidestory(7)
            elif value_pair[1] == "exclusive":
                add_unlocked(plus_persistent.img_unlocked, unlock_string)
        elif value_pair[0] == "ym":
            if value_pair[1] == "part2":
                unlock_sidestory(9)
            elif value_pair[1] == "exclusive":
                add_unlocked(plus_persistent.img_unlocked, unlock_string)
        elif value_pair[0] == "ny":
            if value_pair[1] == "part2":
                unlock_sidestory(11)
            elif value_pair[1] == "exclusive":
                add_unlocked(plus_persistent.img_unlocked, unlock_string)
        
        
        elif value_pair[0] == "epilogue":
            if len(value_pair) > 1 and value_pair[1] == "cg":
                add_unlocked(plus_persistent.img_unlocked, unlock_string)
        
        add_unlocked(plus_persistent.all_unlocked, unlock_string)
        
        
        check_domino_unlocks()
        
        
        if not achievement.has(unlock_string):
            achievement.grant(unlock_string)
            achievement.sync()
        
        plus_persistent.save()

    def unlock_sidestory(index):
        if plus_persistent.side_stories_unlocked[index] == False:
            plus_persistent.side_stories_unlocked[index] = True
            unlock_notification("sidestory")

    def remove_first():
        plus_persistent.all_unlocked.pop(0)

    def get_unlock_percent():    
        unlocked_count = 0
        total_count = 0
        for key, value in unlocks.items():
            if value.ignore_in_completion is False:
                total_count += 1
        for value in plus_persistent.all_unlocked:
            if value in unlocks and unlocks[value].ignore_in_completion is False:
                unlocked_count += 1
        return round((unlocked_count / total_count) * 100, 2)

    def unlock_notification(app):
        if app not in plus_persistent.notifications:
            plus_persistent.notifications.append(app)

    def clear_notification(app):
        if app in plus_persistent.notifications:
            plus_persistent.notifications.remove(app)
            plus_persistent.save()

    def has_notification(app):
        if app in plus_persistent.notifications:
            return True
        else:
            return False

    def debug_unlock_all():
        if not config.developer:
            return False
        
        debug_clear_plus_persistent()
        for key, value in unlocks.items():
            unlock(key)            

    def debug_clear_plus_persistent():
        if not config.developer:
            return False
        
        plus_persistent.side_stories_unlocked = [False, False, False, False, False, False, False, False, False, False, False, False]
        plus_persistent.side_stories_read = [False, False, False, False, False, False]
        plus_persistent.bgm_unlocked = []
        plus_persistent.img_unlocked = []
        plus_persistent.all_unlocked = []
        plus_persistent.read_mails = []
        plus_persistent.mail_unlock_times = ["", "", "", "", "", "", "", "", ""]
        plus_persistent.ddlc_reset_timestamp = datetime.datetime.now()
        plus_persistent.vm_timestamp = datetime.datetime.now()
        plus_persistent.game_cleared_once = False
        plus_persistent.monika_delete_once = False
        plus_persistent.notifications = []


    def copy_old_seen():
        if plus_persistent.seen is not None and len(persistent._seen_ever) < len(plus_persistent.seen):
            persistent._seen_ever = plus_persistent.seen
        else:
            plus_persistent.seen = persistent._seen_ever


    def save_preferences_to_external():
        plus_persistent.music_volume_value = preferences.get_mixer("music")
        plus_persistent.sfx_volume_value = preferences.get_mixer("sfx")
        plus_persistent.text_cps = preferences.text_cps
        plus_persistent.afm_time = preferences.afm_time
        plus_persistent.text_scale = preferences.text_scale
        plus_persistent.skip_after_choices = preferences.skip_after_choices
        plus_persistent.skip_unseen = preferences.skip_unseen
        plus_persistent.language = preferences.language
        plus_persistent.content_warnings_enabled = persistent.content_warnings_enabled
        plus_persistent.high_contrast = persistent.high_contrast
        plus_persistent.use_alt_poem_font = persistent.use_alt_poem_font
        plus_persistent.reduce_transparency = persistent.reduce_transparency
        renpy.save_persistent()
        plus_persistent.save()
        print("SAVED PREFERENCES")

    def write_preferences():
        preferences.set_mixer("music", plus_persistent.music_volume_value)
        preferences.set_mixer("sfx", plus_persistent.sfx_volume_value)
        preferences.text_cps = plus_persistent.text_cps
        preferences.afm_time = plus_persistent.afm_time
        preferences.text_scale = plus_persistent.text_scale
        gui.text_scale = gui.preference("text_scale", preferences.text_scale)
        preferences.skip_after_choices = plus_persistent.skip_after_choices
        preferences.skip_unseen = plus_persistent.skip_unseen
        preferences.language = plus_persistent.language
        persistent.content_warnings_enabled = plus_persistent.content_warnings_enabled
        persistent.high_contrast = plus_persistent.high_contrast
        persistent.use_alt_poem_font = plus_persistent.use_alt_poem_font
        persistent.reduce_transparency = plus_persistent.reduce_transparency
        plus_purchased = plus_persistent.plus_purchased
        renpy.save_persistent()
        plus_persistent.save()
        print("WROTE PREFERENCES")

    def check_reapply_preferences():
        if plus_persistent.reapplyPreferences:
            write_preferences()
        plus_persistent.reapplyPreferences = False
        renpy.save_persistent()
        
        if preferences.language != None:
            renpy.change_language(preferences.language)
        else:
            renpy.change_language("english")
            plus_persistent.language = "english"
            plus_persistent.save()



    iap.register("plus_content") 

    iap.init()

    def get_plus_content_purchase_state():
        if renpy.mobile: 
            if plus_persistent.plus_purchased:
                plus_purchased = True
                renpy.save_persistent()
                return True
            return iap.has_purchased("plus_content")
        else:
            
            return True

    def apply_plus_content_purchase():
        if get_plus_content_purchase_state():
            plus_purchased = True
            plus_persistent.plus_purchased = True
            renpy.save_persistent()
            plus_persistent.save()

define unlocks = parse_unlock_entries()

define res_ratio = 0.666667

define plus_purchased = get_plus_content_purchase_state()

image bg pclub_morning:
    "images/side_stories/bg/club_morning.png"
    truecenter
    size (config.screen_width, config.screen_height)
image bg pstairwell:
    "images/side_stories/bg/stairwell.png"
    truecenter
    size (config.screen_width, config.screen_height)
image bg pmusicroom:
    "images/side_stories/bg/musicroom.png"
    truecenter
    size (config.screen_width, config.screen_height)
image bg pclub_sm_intro:
    "images/side_stories/bg/club-sm-intro.png"
    truecenter
    size (config.screen_width, config.screen_height)
image wiperight:
    "images/side_stories/menu/wiperight.png"
    size (config.screen_width, config.screen_height)

image nf1 1:
    "images/side_stories/nf1/1.png"
    size (960, 960)
image nf1 2:
    "images/side_stories/nf1/2.png"
    size (960, 960)
image nf2 1:
    "images/side_stories/nf2/1.png"
    size (960, 960)
image nf2 2:
    "images/side_stories/nf2/2.png"
    size (960, 960)


image desktop_DDLC_I = im.Scale("gui/virtual_desktop/ddlc icon.png", 28, 28)
image desktop_DDLC_H = im.Scale("gui/virtual_desktop/ddlc icon highlight.png", 28, 28)
image desktop_SideStories_I = im.Scale("gui/virtual_desktop/side stories icon.png", 26, 26)
image desktop_SideStories_H = im.Scale("gui/virtual_desktop/side stories icon highlight.png", 26, 26)
image desktop_Files_I = im.Scale("gui/virtual_desktop/files icon.png", 26, 24)
image desktop_Files_H = im.Scale("gui/virtual_desktop/files icon highlight.png", 26, 24)
image desktop_Mail_I = im.Scale("gui/virtual_desktop/mail icon.png", 26, 21)
image desktop_Mail_H = im.Scale("gui/virtual_desktop/mail icon highlight.png", 26, 21)
image desktop_Pictures_I = im.Scale("gui/virtual_desktop/photos icon.png", 26, 26)
image desktop_Pictures_H = im.Scale("gui/virtual_desktop/photos icon highlight.png", 26, 26)
image desktop_Music_I = im.Scale("gui/virtual_desktop/music icon.png", 28, 28)
image desktop_Music_H = im.Scale("gui/virtual_desktop/music icon highlight.png", 28, 28)
image desktop_Settings_I = im.Scale("gui/virtual_desktop/settings icon.png", 28, 28)
image desktop_Settings_H = im.Scale("gui/virtual_desktop/settings icon highlight.png", 28, 28)
image desktop_Quit_I = im.Scale("gui/virtual_desktop/app icon.png", 28, 28)
image desktop_Quit_H = im.Scale("gui/virtual_desktop/app icon highlight.png", 28, 28)


image sideStory_trust_UL = im.Scale("gui/virtual_desktop/sidestory/trust.png", 360, 210)
image sideStory_trust_L = im.Scale("gui/virtual_desktop/sidestory/trust_g.png", 360, 210)
image sideStory_understanding_UL = im.Scale("gui/virtual_desktop/sidestory/understanding.png", 360, 210)
image sideStory_understanding_L = im.Scale("gui/virtual_desktop/sidestory/understanding_g.png", 360, 210)
image sideStory_respect_UL = im.Scale("gui/virtual_desktop/sidestory/respect.png", 360, 210)
image sideStory_respect_L = im.Scale("gui/virtual_desktop/sidestory/respect_g.png", 360, 210)
image sideStory_balance_UL = im.Scale("gui/virtual_desktop/sidestory/balance.png", 360, 210)
image sideStory_balance_L = im.Scale("gui/virtual_desktop/sidestory/balance_g.png", 360, 210)
image sideStory_reflection_UL = im.Scale("gui/virtual_desktop/sidestory/reflection.png", 360, 210)
image sideStory_reflection_L = im.Scale("gui/virtual_desktop/sidestory/reflection_g.png", 360, 210)
image sideStory_selfLove_UL = im.Scale("gui/virtual_desktop/sidestory/self love.png", 360, 210)
image sideStory_selfLove_L = im.Scale("gui/virtual_desktop/sidestory/self love_g.png", 360, 210)
image sideStory_equals_UL = im.Scale("gui/virtual_desktop/sidestory/equals.png", 520, 150)
image sideStory_equals_L = im.Scale("gui/virtual_desktop/sidestory/equals_g.png", 520, 150)
image sideStory_testVM = im.Scale("gui/virtual_desktop/sidestory/testvm.png", 520, 150)

define nf1 = Character('Friend 1', image='nf1', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed", callback=autofocus, cb_args={"who": "nf1"})
define nf2 = Character('Friend 2', image='nf2', what_prefix="[dialogue_prefix]", what_suffix="[dialogue_suffix]", ctc="ctc", ctc_position="fixed", callback=autofocus, cb_args={"who": "nf2"})

define audio.p1 = "<from 27 to 123.75 loop 75.75>bgm/DLCP_bgm/p1.ogg"
define audio.p2 = "<from 0 to 66.285714 loop 11.4285714>bgm/DLCP_bgm/p2.ogg"
define audio.p3 = "<from 0 to 100.909091 loop 13.6363636>bgm/DLCP_bgm/p3.ogg"
define audio.p4 = "<from 0 to 97.8 loop 30.6>bgm/DLCP_bgm/p4.ogg"
define audio.p5 = "<from 8 to 82 loop 18>bgm/DLCP_bgm/p5.ogg"
define audio.p6 = "<from 0 to 67.6363636 loop 24>bgm/DLCP_bgm/p6.ogg"
define audio.p7a = "<from 0 to 13.7142857 loop 6.85714286>bgm/DLCP_bgm/p7a.ogg"
define audio.p7b = "<from 0 to 65.1428571 loop 10.2857143>bgm/DLCP_bgm/p7b.ogg"
define audio.p7c = "<from 0 to 52.2857143 loop 10.2857143>bgm/DLCP_bgm/p7c.ogg"
define audio.p8 = "<from 0 to 74 loop 10>bgm/DLCP_bgm/p8.ogg"
define audio.p9 = "<from 0 to 112.5 loop 22.5>bgm/DLCP_bgm/p9.ogg"
define audio.p10 = "bgm/DLCP_bgm/p10.ogg"

define audio.p1_piano = "bgm/DLCP_bgm/p1-piano.ogg"
define audio.intro = "<from 0 to 123.75 loop 75.75>bgm/DLCP_bgm/p1.ogg"

define audio.camera = "sfx/camera.ogg"

transform cg_in:
    alpha 0
    linear 0.5 alpha 1
    on hide:
        alpha 1
        linear 0.5 alpha 0
transform cg_in_instant:
    alpha 1
    on hide:
        alpha 1
        linear 0.5 alpha 0


image sm_base:
    "images/side_stories/plus_cg/sm/sm_base.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_m1:
    "images/side_stories/plus_cg/sm/sm_m1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_m2:
    "images/side_stories/plus_cg/sm/sm_m2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_m3:
    "images/side_stories/plus_cg/sm/sm_m3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_s1:
    "images/side_stories/plus_cg/sm/sm_s1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_s2:
    "images/side_stories/plus_cg/sm/sm_s2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_s3:
    "images/side_stories/plus_cg/sm/sm_s3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_s4:
    "images/side_stories/plus_cg/sm/sm_s4.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sm_s5:
    "images/side_stories/plus_cg/sm/sm_s5.png"
    truecenter
    size (config.screen_width, config.screen_height)

image sy_base:
    "images/side_stories/plus_cg/sy/sy_base.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_s1:
    "images/side_stories/plus_cg/sy/sy_s1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_s2:
    "images/side_stories/plus_cg/sy/sy_s2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_y1:
    "images/side_stories/plus_cg/sy/sy_y1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_y2:
    "images/side_stories/plus_cg/sy/sy_y2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_y3:
    "images/side_stories/plus_cg/sy/sy_y3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_y4:
    "images/side_stories/plus_cg/sy/sy_y4.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_y5:
    "images/side_stories/plus_cg/sy/sy_y5.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_y6:
    "images/side_stories/plus_cg/sy/sy_y6.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sy_y7:
    "images/side_stories/plus_cg/sy/sy_y7.png"
    truecenter
    size (config.screen_width, config.screen_height)

image nm_base:
    "images/side_stories/plus_cg/nm/nm_base.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_ma:
    "images/side_stories/plus_cg/nm/nm_ma.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_mb:
    "images/side_stories/plus_cg/nm/nm_mb.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m1:
    "images/side_stories/plus_cg/nm/nm_m1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m2:
    "images/side_stories/plus_cg/nm/nm_m2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m3:
    "images/side_stories/plus_cg/nm/nm_m3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m4:
    "images/side_stories/plus_cg/nm/nm_m4.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m5:
    "images/side_stories/plus_cg/nm/nm_m5.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m6:
    "images/side_stories/plus_cg/nm/nm_m6.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m7:
    "images/side_stories/plus_cg/nm/nm_m7.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m8:
    "images/side_stories/plus_cg/nm/nm_m8.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_m9:
    "images/side_stories/plus_cg/nm/nm_m9.png"
    truecenter
    size (config.screen_width, config.screen_height)
image nm_n1:
    "images/side_stories/plus_cg/nm/nm_n1.png"
    truecenter
    size (config.screen_width, config.screen_height)

image sn_base:
    "images/side_stories/plus_cg/sn/sn_base.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sn_n1:
    "images/side_stories/plus_cg/sn/sn_n1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sn_n2:
    "images/side_stories/plus_cg/sn/sn_n2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sn_n3:
    "images/side_stories/plus_cg/sn/sn_n3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sn_s1:
    "images/side_stories/plus_cg/sn/sn_s1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sn_s2:
    "images/side_stories/plus_cg/sn/sn_s2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sn_s3:
    "images/side_stories/plus_cg/sn/sn_s3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image sn_s4:
    "images/side_stories/plus_cg/sn/sn_s4.png"
    truecenter
    size (config.screen_width, config.screen_height)

image ny_base:
    "images/side_stories/plus_cg/ny/ny_base.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_n1:
    "images/side_stories/plus_cg/ny/ny_n1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_n2:
    "images/side_stories/plus_cg/ny/ny_n2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_n3:
    "images/side_stories/plus_cg/ny/ny_n3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_n4:
    "images/side_stories/plus_cg/ny/ny_n4.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_n5:
    "images/side_stories/plus_cg/ny/ny_n5.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_n6:
    "images/side_stories/plus_cg/ny/ny_n6.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_n7:
    "images/side_stories/plus_cg/ny/ny_n7.png"
    truecenter
    size (config.screen_width, config.screen_height)

image ny_y1:
    "images/side_stories/plus_cg/ny/ny_y1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_y2:
    "images/side_stories/plus_cg/ny/ny_y2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_y3:
    "images/side_stories/plus_cg/ny/ny_y3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_y4:
    "images/side_stories/plus_cg/ny/ny_y4.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_y5:
    "images/side_stories/plus_cg/ny/ny_y5.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ny_y6:
    "images/side_stories/plus_cg/ny/ny_y6.png"
    truecenter
    size (config.screen_width, config.screen_height)

image ym_base:
    "images/side_stories/plus_cg/ym/ym_base.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_paper:
    "images/side_stories/plus_cg/ym/ym_paper.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_y1:
    "images/side_stories/plus_cg/ym/ym_y1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_y2:
    "images/side_stories/plus_cg/ym/ym_y2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_y3:
    "images/side_stories/plus_cg/ym/ym_y3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_y4:
    "images/side_stories/plus_cg/ym/ym_y4.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_y5:
    "images/side_stories/plus_cg/ym/ym_y5.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_y6:
    "images/side_stories/plus_cg/ym/ym_y6.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_m1:
    "images/side_stories/plus_cg/ym/ym_m1.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_m2:
    "images/side_stories/plus_cg/ym/ym_m2.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_m3:
    "images/side_stories/plus_cg/ym/ym_m3.png"
    truecenter
    size (config.screen_width, config.screen_height)
image ym_m4:
    "images/side_stories/plus_cg/ym/ym_m4.png"
    truecenter
    size (config.screen_width, config.screen_height)

define audio.bios_buzz = "sfx/DLCP_sfx/bios.ogg"
define audio.bios_boot = "sfx/DLCP_sfx/boot.ogg"
define audio.bios_login = "sfx/DLCP_sfx/a2.wav"
define audio.bios_tick = "sfx/DLCP_sfx/tick.ogg"


default desktop_window_animation_multi = 1.0

default confirm_title_message = "TEMP_TITLE"
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
