label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    if persistent.content_warnings_enabled == True:
        scene black
        $ show_content_warning("The remaining acts of this game will include themes of graphic suicide and self-harm, body horror, emotional manipulation, obsessive romantic fixation, and psychological abuse. Audio-visual distortions will include flickering and rapidly moving visual patterns, facial distortion, unsettling sound effects, Written and visual depictions of extreme mental health struggles, violent injury, self harm, and suicide are featured. Static and animated visuals of self-destructive behaviors, body damage, graphic blood, a damaged corpse, vomiting, and unsettling dialogue, including verbal harassment, discussions of neglect and abuse. There will also be moments in which, as the player, you will lose control over key choices and events. As tragic events unfold, the player may be led to believe they could have prevented them, though in reality, nothing can stop these events. Neither this overview, nor the specific content warnings to follow are fully exhaustive.")
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(12)
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is [s_name], my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let [s_name] catch up to me."

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat
    $ renpy.save_persistent()

    jump ch20_from_ch10
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
