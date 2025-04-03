screen Camp():
    tag herb_screen
    if not already_patrolled:
        add "bg/camp_bg.png"
    else:
        add "bg/camp_bg_night.png"
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/button_click_1.mp3"
        auto "gui/button/back_%s.png"
        action Hide("Camp")

    imagebutton:
        xpos 898
        ypos 241
        auto "gui/button/lead_den_%s.png"
        insensitive "gui/button/lead_den_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not currently_in=="leaders":
            if already_patrolled==False:
                if leaders_visited==False:
                    action [Hide("Camp"), SetVariable("currently_in", "leaders"), Jump("ld1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "leaders"), Jump("ld2")]

    imagebutton:
        xpos 620
        ypos 213
        auto "gui/button/go_patrol_%s.png"
        insensitive "gui/button/go_patrol_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if already_patrolled==False:
                action Show("PatrolSelect")
        else:
            if quest_harbringer.started or quest_harbringer_final.started:
                action ShowMenu("SunSelect")

    imagebutton:
        xpos 587
        ypos 362
        auto "gui/button/med_den_%s.png"
        insensitive "gui/button/med_den_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not currently_in == "med_den":
            if already_patrolled == False:
                if med_den_visited == False:
                    action [Hide("Camp"), SetVariable("currently_in", "med_den"), Jump("md1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "med_den"), Jump("md2")]

    imagebutton:
        xpos 590
        ypos 632
        auto "gui/button/app_den_%s.png"
        insensitive "gui/button/app_den_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not currently_in=="apprentices":
            if already_patrolled==False:
                action [Hide("Camp"), SetVariable("currently_in", "apprentices"), Jump("ad1")]
            else:
                if not quest_check_nursery.started:
                    if not apprentice_visited_postp:
                        action [Hide("Camp"), SetVariable("currently_in", "apprentices"), Jump("ad3")]

                    else:
                        action [Hide("Camp"), SetVariable("currently_in", "apprentices"), Jump("ad4")]


    imagebutton:
        xpos 901 
        ypos 698
        auto "gui/button/elders_den_%s.png"
        insensitive "gui/button/elders_den_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not currently_in=="elders":
            if already_patrolled==False:
                if elders_visited==False:
                    action [Hide("Camp"), SetVariable("currently_in", "elders"), Jump("ed1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "elders"), Jump("ed2")]
            else:
                if not quest_check_nursery.started:
                    action [Hide("Camp"), SetVariable("currently_in", "elders"), Jump("ed3")]


    imagebutton:
        xpos 1181
        ypos 631
        auto "gui/button/warriors_den_%s.png"
        insensitive "gui/button/warriors_den_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not currently_in=="warriors":
            if already_patrolled == False:
                if warriors_visited == False:
                    action [Hide("Camp"), SetVariable("currently_in", "warriors"), Jump("wd1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "warriors"), Jump("wd2")]
            else:
                if not quest_check_nursery.started:
                    if not warriors_visited_postp:
                        action [Hide("Camp"), SetVariable("currently_in", "warriors"), Jump("wd3")]
                    else:
                        action [Hide("Camp"), SetVariable("currently_in", "warriors"), Jump("wd4")]

    imagebutton:
        xpos 1220
        ypos 361
        auto "gui/button/nursery_%s.png"
        insensitive "gui/button/nursery_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not currently_in=="nursery":
            if already_patrolled == False:
                if nursery_visited == False:
                    action [Hide("Camp"), SetVariable("currently_in", "nursery"), Jump("n1")]
                else:
                    action [Hide("Camp"), SetVariable("currently_in", "nursery"), Jump("n2")]
            else:
                if nursery_visited_postp==False:
                    action [Hide("Camp"), SetVariable("currently_in", "nursery"), Jump("n3")]

    imagebutton:
        xpos 916
        ypos 472
        idle "gui/button/clearing_idle.png"
        hover "gui/button/clearing_hover.png"
        insensitive "gui/button/clearing_unavailable.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not currently_in=="clearing":
            if already_patrolled==False:
                action [Hide("Camp"), SetVariable("currently_in", "clearing"), Jump("cl2")]
            else:
                if not quest_check_nursery.started:
                    action [Hide("Camp"), SetVariable("currently_in", "clearing"), Jump("cl4")]