default herbs_gathered = []

default herbf1 = ""
default herbf2 = ""
default herbf3 = ""
default herbf4 = ""
default herbf5 = ""

default i = 0

image herb1f1 = "gui/button/[herbf1]1.png"
image herb1f1_h = "gui/button/[herbf1]1_hover.png"
image herb1f1_u = "gui/button/[herbf1]1_unavailable.png"
image herb2f1 = "gui/button/[herbf1]2.png"
image herb2f1_h = "gui/button/[herbf1]2_hover.png"
image herb2f1_u = "gui/button/[herbf1]2_unavailable.png"
image herb3f1 = "gui/button/[herbf1]3.png"
image herb3f1_h = "gui/button/[herbf1]3_hover.png"
image herb3f1_u = "gui/button/[herbf1]3_unavailable.png"
image herbf1_l = "gui/button/[herbf1]_locked.png"
image herbf1_d = "gui/button/[herbf1].png"
image herbf1_h = "gui/button/[herbf1]_hover.png"

image herb1f2 = "gui/button/[herbf2]1.png"
image herb1f2_h = "gui/button/[herbf2]1_hover.png"
image herb1f2_u = "gui/button/[herbf2]1_unavailable.png"
image herb2f2 = "gui/button/[herbf2]2.png"
image herb2f2_h = "gui/button/[herbf2]2_hover.png"
image herb2f2_u = "gui/button/[herbf2]2_unavailable.png"
image herb3f2 = "gui/button/[herbf2]3.png"
image herb3f2_h = "gui/button/[herbf2]3_hover.png"
image herb3f2_u = "gui/button/[herbf2]3_unavailable.png"
image herbf2_l = "gui/button/[herbf2]_locked.png"
image herbf2_d = "gui/button/[herbf2].png"
image herbf2_h = "gui/button/[herbf2]_hover.png"

image herb1f3 = "gui/button/[herbf3]1.png"
image herb1f3_h = "gui/button/[herbf3]1_hover.png"
image herb1f3_u = "gui/button/[herbf3]1_unavailable.png"
image herb2f3 = "gui/button/[herbf3]2.png"
image herb2f3_h = "gui/button/[herbf3]2_hover.png"
image herb2f3_u = "gui/button/[herbf3]2_unavailable.png"
image herb3f3 = "gui/button/[herbf3]3.png"
image herb3f3_h = "gui/button/[herbf3]3_hover.png"
image herb3f3_u = "gui/button/[herbf3]3_unavailable.png"
image herbf3_l = "gui/button/[herbf3]_locked.png"
image herbf3_d = "gui/button/[herbf3].png"
image herbf3_h = "gui/button/[herbf3]_hover.png"

image herb1f4 = "gui/button/[herbf4]1.png"
image herb1f4_h = "gui/button/[herbf4]1_hover.png"
image herb1f4_u = "gui/button/[herbf4]1_unavailable.png"
image herb2f4 = "gui/button/[herbf4]2.png"
image herb2f4_h = "gui/button/[herbf4]2_hover.png"
image herb2f4_u = "gui/button/[herbf4]2_unavailable.png"
image herb3f4 = "gui/button/[herbf4]3.png"
image herb3f4_h = "gui/button/[herbf4]3_hover.png"
image herb3f4_u = "gui/button/[herbf4]3_unavailable.png"
image herbf4_l = "gui/button/[herbf4]_locked.png"
image herbf4_d = "gui/button/[herbf4].png"
image herbf4_h = "gui/button/[herbf4]_hover.png"

image herb1f5 = "gui/button/[herbf5]1.png"
image herb1f5_h = "gui/button/[herbf5]1_hover.png"
image herb1f5_u = "gui/button/[herbf5]1_unavailable.png"
image herb2f5 = "gui/button/[herbf5]2.png"
image herb2f5_h = "gui/button/[herbf5]2_hover.png"
image herb2f5_u = "gui/button/[herbf5]2_unavailable.png"
image herb3f5 = "gui/button/[herbf5]3.png"
image herb3f5_h = "gui/button/[herbf5]3_hover.png"
image herb3f5_u = "gui/button/[herbf5]3_unavailable.png"
image herbf5_l = "gui/button/[herbf5]_locked.png"
image herbf5_d = "gui/button/[herbf5].png"
image herbf5_h = "gui/button/[herbf5]_hover.png"

image herbbg = "images/bg/herbbg_[i].png"

default xpos1 = 290
default ypos1 = 611
default xpos2 = 480
default ypos2 = 331
default xpos3 = 919
default ypos3 = 642
default xpos4 = 1386
default ypos4 = 391
default xpos5 = 1628
default ypos5 = 658

default frame1_progress = 1
default frame2_progress = 1
default frame3_progress = 1
default frame4_progress = 1
default frame5_progress = 1

default frame1_clicked = False
default frame2_clicked = False
default frame3_clicked = False
default frame4_clicked = False
default frame5_clicked = False

default frame1_empty = False
default frame2_empty = False
default frame3_empty = False
default frame4_empty = False
default frame5_empty = False

default f1_locked = False
default f2_locked = False
default f3_locked = False
default f4_locked = False
default f5_locked = False

default herb_turns = {"blackberry":2, "catmint":3}

default turn_max1 = frame1_progress - 1
default herb_max1 = herb_turns.get(herbf1)
default turn_max2 = frame2_progress - 1
default herb_max2 = herb_turns.get(herbf2)
default turn_max3 = frame3_progress - 1
default herb_max3 = herb_turns.get(herbf3)
default turn_max4 = frame4_progress - 1
default herb_max4 = herb_turns.get(herbf4)   
default turn_max5 = frame5_progress - 1
default herb_max5 = herb_turns.get(herbf5)      

default lost_leads = []

label define_herb(frame_herb):
    $ rand_herb = renpy.random.randint(1,10)
    if rand_herb > 8:
        if frame_herb == "f1":
            $ herbf1 = "catmint"
        elif frame_herb == "f2":
            $ herbf2 = "catmint"
        elif frame_herb == "f3":
            $ herbf3 = "catmint"
        elif frame_herb == "f4":
            $ herbf4 = "catmint"
        else:
            $ herbf5 = "catmint"
    elif rand_herb < 5:
        if frame_herb == "f1":
            $ herbf1 = "blackberry"
        elif frame_herb == "f2":
            $ herbf2 = "blackberry"
        elif frame_herb == "f3":
            $ herbf3 = "blackberry"
        elif frame_herb == "f4":
            $ herbf4 = "blackberry"
        else:
            $ herbf5 = "blackberry"    
    else:
        if frame_herb == "f1":
            $ frame1_empty = True
            $ print("frame1 should be empty")
        elif frame_herb == "f2":
            $ frame2_empty = True
        elif frame_herb == "f3":
            $ frame3_empty = True
        elif frame_herb == "f4":
            $ frame4_empty = True
        else:
            $ frame5_empty = True  
    return

label show_herbs:
    call define_herb("f1")
    call define_herb("f2")
    call define_herb("f3")
    call define_herb("f4")
    call define_herb("f5")
    return

label proceed_logic:
    $ i += 1
    $ f1_prev = herbf1
    $ f2_prev = herbf2
    $ f3_prev = herbf3
    $ f4_prev = herbf4
    $ f5_prev = herbf5
    $ frame1_empty = False
    $ frame2_empty = False
    $ frame3_empty = False
    $ frame4_empty = False
    $ frame5_empty = False
    jump show_herbs
    if f1_locked:
        $ print("I know f1 is locked")
        $ herbf1 = f1_prev
        $ lead_chance = renpy.random.randint(1,10)
        if lead_chance > 0:
            $ print("I know the lead chance is greater than zero")
            $ frame1_progress += 1
            $ turn_max1 += 1
        else:
            $ frame1_empty = True
            $ frame1_progress = 1
            $ lost_leads.append(herbf1)
            $ herbf1 = ""
            $ print("frame1 should be empty")
    elif f2_locked:
        $ herbf2 = f2_prev
        $ lead_chance = renpy.random.randint(1,10)
        if lead_chance >=6:
            $ frame2_progress += 1
            $ turn_max2 += 2
        else:
            $ frame2_empty = True
            $ frame2_progress = 1
            $ herbf2 = ""
            $ lost_leads.append(herbf2)
    elif f3_locked:
        $ herbf3 = f3_prev
        $ lead_chance = renpy.random.randint(1,10)
        if lead_chance >=6:
            $ frame3_progress += 1
            $ turn_max3 += 1
        else:
            $ frame3_empty = True
            $ frame3_progress = 1
            $ herbf3 = ""
            $ lost_leads.append(herbf3)
    elif f4_locked:
        $ herbf4 = f4_prev
        $ lead_chance = renpy.random.randint(1,10)
        if lead_chance >=6:
            $ frame4_progress += 1
            $ turn_max4 += 1
        else:
            $ frame4_empty = True 
            $ frame4_progress = 1
            $ herbf4 = ""
            $ lost_leads.append(herbf4)
    elif f5_locked:
        $ herbf5 = f5_prev
        $ lead_chance = renpy.random.randint(1,10)
        if lead_chance >=6:
            $ frame5_progress += 1
            $ turn_max5 += 1
        else:
            $ frame5_empty = True
            $ frame5_progress = 1
            $ herbf5 = ""
            $ lost_leads.append(herbf5)
    else:
        return


