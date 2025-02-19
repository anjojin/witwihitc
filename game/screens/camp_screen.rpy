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
        idle "gui/button/lead_den_idle.png"
        hover "gui/button/lead_den_hover.png"
        action Jump("leadersden")

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
        action Jump("medden")

    imagebutton:
        xpos 590
        ypos 632
        auto "gui/button/app_den_%s.png"
        if already_patrolled==False:
                action [Hide("Camp"), SetVariable("currently_in", "apprentices"), Jump("app_den_empty")]

    imagebutton:
        xpos 901 
        ypos 698
        auto "gui/button/elders_den_%s.png"
        if already_patrolled==False:
            if elders_visited==False:
                action [Hide("Camp"), SetVariable("currently_in", "elders"), Jump("elders_den_first")]
            else:
                action [Hide("Camp"), SetVariable("currently_in", "elders"), Jump("elders_den_revisit")]


    imagebutton:
        xpos 1181
        ypos 631
        auto "gui/button/warriors_den_%s.png"
        action Jump("warriorsden")

    imagebutton:
        xpos 1220
        ypos 361
        auto "gui/button/nursery_%s.png"
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
        if already_patrolled==False:
            if clearing_visited==False:
                action [Hide("Camp"), SetVariable("currently_in", "clearing"), Jump("clearing_first")]

    if currently_in == "apprentices":
        add "gui/button/app_den_unavailable.png" xpos 590 ypos 632

    if currently_in == "elders":
        add "gui/button/elders_den_unavailable.png" xpos 901 ypos 698

    if currently_in == "nursery":
        add "gui/button/nursery_unavailable.png" xpos 1220 ypos 361

    if currently_in == "leaders":
        add "gui/button/lead_den_unavailable.png" xpos 898 ypos 241

    if currently_in == "clearing":
        add "gui/button/clearing_unavailable.png" xpos 916 ypos 472

    if currently_in == "warriors":
        add "gui/button/warriors_den_unavailable.png" xpos 1191 ypos 631

    if currently_in == "med_den":
        add "gui/button/med_den_unavailable.png" xpos 587 ypos 362

    if already_patrolled:
        add "gui/button/go_patrol_unavailable.png" xpos 620 ypos 213