image poem_special1 = Transform("poem_special/poem_special1.png", zoom=res_ratio)
image poem_special2 = Transform("poem_special/poem_special2.png", zoom=res_ratio)
image poem_special3 = Transform("poem_special/poem_special3.png", zoom=res_ratio)
image poem_special4 = Transform("poem_special/poem_special4.png", zoom=res_ratio)
image poem_special5:
    Transform("poem_special/poem_special5a.png", zoom=res_ratio)
    10.0
    Transform("poem_special/poem_special5b.png", zoom=res_ratio)
image poem_special6 = Transform("poem_special/poem_special6.png", zoom=res_ratio)
image poem_special7a = Transform("poem_special/poem_special7a.png", zoom=res_ratio)
image poem_special7b = Transform("poem_special/poem_special7b.png", zoom=res_ratio)
image poem_special8 = Transform("poem_special/poem_special8.png", zoom=res_ratio)
image poem_special9 = Transform("poem_special/poem_special9.png", zoom=res_ratio)
image poem_special10 = Transform("poem_special/poem_special10.png", zoom=res_ratio)
image poem_special11 = Transform("poem_special/poem_special11.png", zoom=res_ratio)
image poem_end = ConditionSwitch(
    "persistent.clearall == True", Transform("poem_special/poem_end_clearall.png", zoom=res_ratio),
    "True", Transform("poem_special/poem_end.png", zoom=res_ratio))

label poem_special_1:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special1")
    show poem_special1 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_2:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special2")
    show poem_special2 with Dissolve(1.0)
    $ pause()
    play sound "sfx/giggle.ogg"
    $ quick_menu = True
    return
label poem_special_3:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special3")
    show poem_special3 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_4:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special4")
    show poem_special4 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_5:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special5a")
    $ unlock("special5b")
    show poem_special5 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_6:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special6")
    show poem_special6 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_7:
    $ quick_menu = False
    play sound page_turn
    show poem_special7a as ps with Dissolve(1.0)
    $ pause()
    show poem_special7b as ps
    $ pause(0.01)
    $ quick_menu = True
    return
label poem_special_8:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special8")
    show poem_special8 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_9:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special9")
    show poem_special9 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_10:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special10")
    show poem_special10 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_11:
    $ quick_menu = False
    play sound page_turn
    $ unlock("special11")
    show poem_special11 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
