init python:
    class DesktopMailEntry:
        def __init__(self, data: dict, id: str) -> None:
            self.unlock_id = id
            self.sender = data['sender']
            self.address = data['address']
            self.job_title = data['job_title']
            self.subject = data['subject']
            self.message = data['message']





    def unlock_new_mail():
        unlock_percent = get_unlock_percent()
        
        if unlock_percent >= 55:
            unlock("email_1")
            set_mail_unlock_time("email_1")
        if unlock_percent >= 60:
            unlock("email_2")
            set_mail_unlock_time("email_2")
        if unlock_percent >= 65:
            unlock("email_3")
            set_mail_unlock_time("email_3")
        if unlock_percent >= 70:
            unlock("email_4")
            set_mail_unlock_time("email_4")
        if unlock_percent >= 75:
            unlock("email_5")
            set_mail_unlock_time("email_5")
        if unlock_percent >= 80:
            unlock("email_6")
            set_mail_unlock_time("email_6")
        if unlock_percent >= 85:
            unlock("email_7")
            set_mail_unlock_time("email_7")
        if unlock_percent >= 90:
            unlock("email_8")
            set_mail_unlock_time("email_8")
        if unlock_percent >= 100:
            unlock("email_9")
            set_mail_unlock_time("email_9")

    def parse_desktop_mails():
        import tomllib
        mails = {}
        with renpy.file("desktopmails.toml", False) as f:
            mail_toml_dict = tomllib.load(f)
            for mail_id, data in mail_toml_dict.items():
                mails[mail_id] = DesktopMailEntry(data, mail_id)
        return mails
    def mark_mail_as_read(mail_id: str):
        if mail_id not in plus_persistent.read_mails:
            plus_persistent.read_mails.append(mail_id)
            if mail_id == "email_3":
                unlock("email3_read")

    def set_mail_unlock_time(email_name):
        if email_name != None:
            email_number = int(email_name.split('_')[1]) - 1
            if plus_persistent.mail_unlock_times[email_number] == "":
                plus_persistent.mail_unlock_times[email_number] = datetime.datetime.today().strftime('%Y-%m-%d')
                unlock_notification("mail")

    def get_mail_unlock_data(email_name):
        if email_name != None:
            email_number = int(email_name.split('_')[1]) - 1
            return plus_persistent.mail_unlock_times[email_number]
        else:
            return "ERROR"






define desktop_mails = parse_desktop_mails()
default plus_persistent.read_mails = []

screen virtual_desktop_mail_app:

    $ unlock_new_mail()

    on "show" action Function(clear_notification, "mail")

    default mail_to_view = None

    style_prefix "virtual_desktop"
    modal True

    use virtual_desktop_app_window("Mail", window_width=get_variable_size(880, 1100, gui.text_scale), taskbar_icon="desktop_Mail_H"):
        key ['K_ESCAPE'] action NullAction()

        if not is_unlocked_all("email_1"):
            frame:
                has fixed
                vbox:
                    spacing 5
                    align (0.5, 0.5)
                    add "gui/virtual_desktop/no mail icon.png":
                        xalign 0.5
                        zoom 0.3
                    text __("No new mail."):
                        xalign 0.5
                        size get_variable_size(18, 24, gui.text_scale)
        else:
            text __("Inbox"):
                pos (20,10)
                size get_variable_size(18, 22, gui.text_scale)
            vbox:

                ypos 70
                box_reverse True
                spacing 1

                style_prefix "virtual_desktop_mail"


                for id in desktop_mails:
                    $ mail = desktop_mails[id]
                    if is_unlocked_all(mail.unlock_id):
                        $ mail_unlock_time = get_mail_unlock_data(mail.unlock_id)
                        button:
                            sensitive mail_to_view == None
                            action [SetScreenVariable("mail_to_view", id), Function(mark_mail_as_read, id)]
                            add "virtual_desktop_mail_entry_highlight" at virtual_desktop_mail_entry_hover
                            frame:
                                left_padding 50
                                right_padding 20
                                background "#00000000"
                                $ read_unread_color = "#800066" if id not in plus_persistent.read_mails else "#000"
                                xfill True

                                text __(mail.sender):
                                    xpos 0.0
                                    idle_color read_unread_color
                                text __(mail.subject) at loc_text_fit:
                                    text_align 0.0
                                    xmaximum 500
                                    xpos 0.2
                                    idle_color read_unread_color
                                text mail_unlock_time:
                                    text_align 1.0
                                    xalign 1.0
                                    idle_color read_unread_color


        fixed at mail_viewer_crop:
            showif mail_to_view != None:
                fixed at mail_viewer_fadeinout:
                    xysize (1.0,1.0)
                    xanchor 0.5
                    use virtual_desktop_mail_viewer(mail_to_view)
        showif mail_to_view != None:
            button:
                action SetScreenVariable("mail_to_view", None)
                idle_background "#fff"
                hover_background "#f1f1f1"

                xsize get_variable_size(50, 80)
                ysize get_variable_size(40, 65)
                anchor (1.0,1.0)
                pos (1.0,0.0)

                text "←":
                    align (0.5, 0.5)
                    size get_variable_size(18, 32, gui.text_scale)

image virtual_desktop_mail_entry_highlight:
    "gui/virtual_desktop/file highlight.png"

image mes_logo_mail_signature:
    "gui/virtual_desktop/mail/MES Logo Horizontal_smaller.png"
    zoom 0.7
    align (0.05, 0.1)

transform virtual_desktop_mail_entry_hover:
    xysize (1.0,1.0)
    on hover:
        linear 0.15 alpha 1.0
    on idle:
        linear 0.15 alpha 0.0

transform mail_viewer_crop:
    crop (0,0,1.0,1.0)

transform mail_viewer_fadeinout:
    on show:
        alpha 0.0
        xpos 0.6
        parallel:
            linear 0.15 alpha 1.0
        parallel:
            easein_cubic 0.3 xpos 0.5

    on hide:
        alpha 1.0
        xpos 0.5
        parallel:
            linear 0.2 alpha 0.0
        parallel:
            easein_cubic 0.3 xpos 0.6

style virtual_desktop_mail_text is virtual_desktop_text:
    shaper "freetype"
    size get_variable_size(18, 26, gui.text_scale)
    kerning -1
    yalign 0.5
    hover_color "#fff"

style virtual_desktop_mail_frame is virtual_desktop_frame

style virtual_desktop_mail_button:
    padding (0,0)
    ysize 50
    background "#fff"

style virtual_desktop_mail_vscrollbar is virtual_desktop_vscrollbar

screen virtual_desktop_mail_viewer(mail_id):

    default mail_entry = None

    if mail_id != None:
        $ mail_entry = desktop_mails[mail_id]

    style_prefix "virtual_desktop_mail"

    if mail_entry != None:
        vbox:
            xysize (1.0, 1.0)


            $ mail_unlock_time = get_mail_unlock_data(mail_entry.unlock_id)
            frame:
                xfill True
                ysize get_variable_size(120,160,gui.text_scale)
                xpadding 20
                top_padding 5
                has vbox
                style_prefix "virtual_desktop_mail_viewer"
                spacing 5
                text __("{b}From: {/b}") + __(mail_entry.sender) + "<" + __(mail_entry.address) + ">"
                text "{b}" + __("To:") + "{/b} " + __("Untitled Mail Group (DO NOT USE)")
                text __("{b}Date: {/b}") + mail_unlock_time
                text __("{b}Subject: {/b}") + __(mail_entry.subject)


            frame:
                background "#fff"
                left_padding 20
                right_padding 30
                viewport id "desktop_mail_viewport":
                    draggable True
                    has vbox
                    null height 20
                    text __(mail_entry.message):
                        color "#2c2c2c"
                        size get_variable_size(14,26,gui.text_scale)

                    null height 70


                    add "mes_logo_mail_signature":
                        zoom get_variable_size_f(0.4, 0.7, gui.text_scale)
                        xalign 0.0
                    null height 5
                    text __(mail_entry.sender):
                        color "#2c2c2c"
                        font "fonts/HKGrotesk-SemiBold-rounded.otf"
                        size get_variable_size(12, 20, gui.text_scale)
                        kerning 1
                    text __(mail_entry.job_title):
                        color "#444444"
                        size get_variable_size(12, 20, gui.text_scale)
                    null height 50
                vbar value YScrollValue("desktop_mail_viewport") xpos 1.0 xoffset 20


style virtual_desktop_mail_viewer_text is virtual_desktop_mail_text
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
