

























init:
    default enable_autofocus = False

init python:
    def autofocus(event, interact, **kwargs):
        if not store.enable_autofocus: return
        if not interact: return
        if renpy.is_skipping(): return
        if 'no_autofocus' in kwargs and kwargs['no_autofocus']: return
        name = renpy.get_say_image_tag()
        if not name:
            return
        
        
        
        
        key_exists = renpy.exports.scene_lists().at_list['master'].get(name, None)
        if key_exists is None:
            return
        
        at_list = renpy.exports.scene_lists().at_list['master'][name]
        interrupt = not at_list or any(
                [('autofocus_interrupt', 'True') in a.parameters.parameters
                for a in at_list])
        if not interrupt:
            
            displayables = renpy.exports.scene_lists().get_all_displayables()
            transforms = [t for t in displayables
                        if type(t) == renpy.display.transform.ATLTransform
                        and t.child
                        and t.child.name[0] == name]
            
            
            
            if any([t.st == 0 for t in transforms]):
                return
        if event == 'begin':
            renpy.show(name, at_list=[autofocus_in], zorder=3)
        if event == 'end':
            renpy.show(name, at_list=[autofocus_out], zorder=2)


    config.all_character_callbacks += [autofocus]

transform autofocus_in(z=0.80, autofocus_interrupt=True):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:
        zoom z*0.95 alpha 0.00
        yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 zoom z*1.05 alpha 1.00
        parallel:
            easein .15 yoffset 0

transform autofocus_out(z=0.80, autofocus_interrupt=True):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
