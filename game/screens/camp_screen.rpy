screen Camp():
    $ Hide("quick_menu")
    if not already_patrolled:
        add "bg/camp_bg.png"
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "gui/button/back_%s.png"
        action Hide("Camp")

    imagebutton:
        xpos 898
        ypos 241
        auto "gui/button/lead_den_%s.png"
        if not currently_in=="leaders":
            if already_patrolled==False:
                if leaders_visited==False:
                    action [Hide("Camp"), SetVariable("currently_in", "leaders"), Jump("ld1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "leaders"), Jump("ed2")]

    imagebutton:
        xpos 620
        ypos 213
        auto "gui/button/go_patrol_%s.png"
        if already_patrolled==False:
            action ShowMenu("PatrolSelect")
        else:
            action ShowMenu("PostPatrolSelect")

    imagebutton:
        xpos 587
        ypos 362
        auto "gui/button/med_den_%s.png"
        if not currently_in=="med_den":
            action Jump("medicine")

    imagebutton:
        xpos 590
        ypos 632
        auto "gui/button/app_den_%s.png"
        if not currently_in=="apprentices":
            if already_patrolled==False:
                action [Hide("Camp"), SetVariable("currently_in", "apprentices"), Jump("app_den_empty")]

    imagebutton:
        xpos 901 
        ypos 698
        auto "gui/button/elders_den_%s.png"
        if not currently_in=="elders":
            if already_patrolled==False:
                if elders_visited==False:
                    action [Hide("Camp"), SetVariable("currently_in", "elders"), Jump("ed1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "elders"), Jump("ed2")]

    imagebutton:
        xpos 1181
        ypos 631
        auto "gui/button/warriors_den_%s.png"
        if not currently_in=="warriors":
            if already_patrolled == False:
                if warriors_visited == False:
                    action [Hide("Camp"), SetVariable("currently_in", "warriors"), Jump("wd1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "warriors"), Jump("wd2")]

    imagebutton:
        xpos 1220
        ypos 361
        auto "gui/button/nursery_%s.png"
        if not currently_in=="nursery":
            if already_patrolled == False:
                if nursery_visited == False:
                    action [Hide("Camp"), SetVariable("currently_in", "nursery"), Jump("nursery_first")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "nursery"), Jump("nursery_revisit")]

    imagebutton:
        xpos 916
        ypos 472
        idle "gui/button/clearing_idle.png"
        hover "gui/button/clearing_hover.png"
        if not currently_in=="clearing":
            if already_patrolled==False:
                if clearing_visited==False:
                    action [Hide("Camp"), SetVariable("currently_in", "clearing"), Jump("clearing_first")]