init python:
    import renpy.store as store
    import renpy.exports as renpy

    ## This is the Quest Class that is used to store the quest's information
    class HerbFrame(store.object):
        ## When the variable is created, the information such as 
        ## name, description, available and completed will be set
        def __init__(self, number, herb="", xpos=0, ypos=0, progress=1, clicked=False, empty=False, locked=False, prev=""):
            self.number = number
            self.herb = herb
            self.xpos = xpos
            self.ypos = ypos
            self.progress = progress
            self.clicked = clicked
            self.empty = empty
            self.locked = locked
            self.prev = prev

## This is the Quest Class that is used to store the quest's information
    class Herb(store.object):
        ## When the variable is created, the information such as 
        ## name, description, available and completed will be set
        def __init__(self, name, turns):
            self.name = name
            self.turns = turns

default herbs_gathered = []
default q = 0

default frame1 = HerbFrame(number=1, xpos=290, ypos=611)
default frame2 = HerbFrame(number=2, xpos=480, ypos=331)
default frame3 = HerbFrame(number=3, xpos = 919, ypos = 642)
default frame4 = HerbFrame(number=4, xpos=1386, ypos = 391)
default frame5 = HerbFrame(number=5, xpos=1628, ypos=658)

image herb1f1 = "gui/button/[frame1.herb.name]1.png"
image herb1f1_h = "gui/button/[frame1.herb.name]1_hover.png"
image herb2f1 = "gui/button/[frame1.herb.name]2.png"
image herb2f1_h = "gui/button/[frame1.herb.name]2_hover.png"
image herb3f1 = "gui/button/[frame1.herb.name]3.png"
image herb3f1_h = "gui/button/[frame1.herb.name]3_hover.png"
image herbf1_l = "gui/button/[frame1.herb.name]_locked.png"
image herbf1_d = "gui/button/[frame1.herb.name].png"
image herbf1_h = "gui/button/[frame1.herb.name]_hover.png"

image herb1f2 = "gui/button/[frame2.herb.name]1.png"
image herb1f2_h = "gui/button/[frame2.herb.name]1_hover.png"
image herb2f2 = "gui/button/[frame2.herb.name]2.png"
image herb2f2_h = "gui/button/[frame2.herb.name]2_hover.png"
image herb3f2 = "gui/button/[frame2.herb.name]3.png"
image herb3f2_h = "gui/button/[frame2.herb.name]3_hover.png"
image herbf2_l = "gui/button/[frame2.herb.name]_locked.png"
image herbf2_d = "gui/button/[frame2.herb.name].png"
image herbf2_h = "gui/button/[frame2.herb.name]_hover.png"

image herb1f3 = "gui/button/[frame3.herb.name]1.png"
image herb1f3_h = "gui/button/[frame3.herb.name]1_hover.png"
image herb2f3 = "gui/button/[frame3.herb.name]2.png"
image herb2f3_h = "gui/button/[frame3.herb.name]2_hover.png"
image herb3f3 = "gui/button/[frame3.herb.name]3.png"
image herb3f3_h = "gui/button/[frame3.herb.name]3_hover.png"
image herbf3_l = "gui/button/[frame3.herb.name]_locked.png"
image herbf3_d = "gui/button/[frame3.herb.name].png"
image herbf3_h = "gui/button/[frame3.herb.name]_hover.png"

image herb1f4 = "gui/button/[frame4.herb.name]1.png"
image herb1f4_h = "gui/button/[frame4.herb.name]1_hover.png"
image herb2f4 = "gui/button/[frame4.herb.name]2.png"
image herb2f4_h = "gui/button/[frame4.herb.name]2_hover.png"
image herb3f4 = "gui/button/[frame4.herb.name]3.png"
image herb3f4_h = "gui/button/[frame4.herb.name]3_hover.png"
image herbf4_l = "gui/button/[frame4.herb.name]_locked.png"
image herbf4_d = "gui/button/[frame4.herb.name].png"
image herbf4_h = "gui/button/[frame4.herb.name]_hover.png"

image herb1f5 = "gui/button/[frame5.herb.name]1.png"
image herb1f5_h = "gui/button/[frame5.herb.name]1_hover.png"
image herb2f5 = "gui/button/[frame5.herb.name]2.png"
image herb2f5_h = "gui/button/[frame5.herb.name]2_hover.png"
image herb3f5 = "gui/button/[frame5.herb.name]3.png"
image herb3f5_h = "gui/button/[frame5.herb.name]3_hover.png"
image herbf5_l = "gui/button/[frame5.herb.name]_locked.png"
image herbf5_d = "gui/button/[frame5.herb.name].png"
image herbf5_h = "gui/button/[frame5.herb.name]_hover.png"

image herb1ft = "gui/button/[tutorial_frame.herb.name]1.png"
image herb1ft_h = "gui/button/[tutorial_frame.herb.name]1_hover.png"
image herb2ft = "gui/button/[tutorial_frame.herb.name]2.png"
image herb2ft_h = "gui/button/[tutorial_frame.herb.name]2_hover.png"
image herb3ft = "gui/button/[tutorial_frame.herb.name]3.png"
image herb3ft_h = "gui/button/[tutorial_frame.herb.name]3_hover.png"
image herbft_l = "gui/button/[tutorial_frame.herb.name]_locked.png"
image herbft_d = "gui/button/[tutorial_frame.herb.name].png"
image herbft_h = "gui/button/[tutorial_frame.herb.name]_hover.png"

image herbbg = "images/bg/herbbg_[q].png"

default blackberry = Herb(name="blackberry", turns=3)
default catmint = Herb(name="catmint", turns=4)
default juniper = Herb(name="juniper", turns=2)
default burdock = Herb(name="burdock", turns=2)
default daisy = Herb(name="daisy", turns=3)
default dandelion = Herb(name="dandelion", turns=4)

default lost_leads = []
default tutorial_frame = HerbFrame(number=6, herb=blackberry, xpos=919, ypos=642)

label define_herb(frame_herb):
    $ rand_herb = renpy.random.randint(0,30)
    if rand_herb >= (29 - talon_clan_bonus):
        $ frame_herb.herb = catmint
    elif 29 > rand_herb >=27:
        $ frame_herb.herb = dandelion 
    elif 27> rand_herb >= 25:
        $ frame_herb.herb = daisy
    elif 25> rand_herb >=22:
        $ frame_herb.herb = blackberry
    elif 22>rand_herb>=19:
        $ frame_herb.herb = burdock
    elif 19>rand_herb>=16:
        $ frame_herb.herb = juniper
    else:
        $ frame_herb.empty = True
    return

label define_progress(frame_herb):
    $ rand_progress = renpy.random.randint(1,10)
    if rand_progress >= 9:
        $ frame_herb.progress = 2
    else:
        $ frame_herb.progress = 1
    return


label define_herbs:
    call define_herb(frame1)
    call define_herb(frame2)
    call define_herb(frame3)
    call define_herb(frame4)
    call define_herb(frame5)
    call define_progress(frame1)
    call define_progress(frame2)
    call define_progress(frame3)
    call define_progress(frame4)
    call define_progress(frame5)
    return

label proceed_logic(herbframe):
    $ herbframe.prev = herbframe.herb
    $ herbframe.empty = False
    call define_herb(herbframe)
    if herbframe.locked:
        $ herbframe.herb = herbframe.prev
        $ lead_chance = renpy.random.randint(1,10)
        if herbframe.progress == 1:
            if lead_chance >= 6:
                $ herbframe.progress += 1
                $ herbframe.locked = False
            else:
                $ herbframe.empty = True
                $ herbframe.progress = 1
                $ lost_leads.append(herbframe.herb.name)
                $ herbframe.locked = False
            return
        elif herbframe.progress == 2:
            if lead_chance >= 4:
                $ herbframe.progress += 1
                $ herbframe.locked = False
            else:
                $ herbframe.empty = True
                $ herbframe.progress = 1
                $ lost_leads.append(herbframe.herb.name)
                $ herbframe.locked = False
        elif herbframe.progress > 2:
            if lead_chance >= 3:
                $ herbframe.progress += 1
                $ herbframe.locked = False
            else:
                $ herbframe.empty = True
                $ herbframe.progress = 1
                $ lost_leads.append(herbframe.herb.name)
                $ herbframe.locked = False
            return
    else:
        if not herbframe.empty:
            call define_progress(herbframe)
        return


