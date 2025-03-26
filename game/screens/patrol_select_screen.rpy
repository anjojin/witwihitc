screen PatrolSelect():
    style_prefix "patrol_select"
    add "bg/patrol_select_bg.png"

    imagebutton:
        xpos 433
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        idle "gui/button/proceed_idle.png"
        hover "gui/button/proceed_hover.png"
        insensitive "gui/button/proceed_unavailable.png"
        if not quest_medical_opinion.started:
            if not quest_crocus.started:
                if not quest_nesting_material.started:
                    if not quest_grim_tidings.started:
                        if quest_gather_herbs.started:
                            action NullAction
                        else:
                            action [Hide ("PatrolSelect"), Hide("Camp"), Jump("hunting_start")]

    imagebutton:
        xpos 1096
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/button_click_2.mp3"
        idle "gui/button/do_not_proceed_idle.png"
        hover "gui/button/do_not_proceed_hover.png"
        action [Hide ("PatrolSelect"), Hide("Camp")]

    hbox:
        xpos 285
        ypos 562
        xmaximum 1430
        ymaximum 871
        frame:
            background Solid("#af9c6b")
            xmargin 45
            ymargin 45
            if quest_medical_opinion.started:
                text "Talonclaw cannot go on patrol until he completes the following quest: {b}Medical Opinion.{/b}"
            elif quest_crocus.started:
                text "Talonclaw cannot go on patrol until he completes the following quest: {b}Crocuses.{b}"
            elif quest_nesting_material.started:
                text "Talonclaw cannot go on patrol until he completes the following quest: {b}Nesting Material.{/b}"
            elif quest_babysitting.started:
                text "Talonclaw is committed to a {b}hunting patrol with the apprentices.{/b}"
            elif quest_gather_herbs.started:
                text "Talonclaw is currently committed to an {b}herb gathering patrol.{/b}"
            elif quest_grim_tidings.started:
                text "Talonclaw cannot go on patrol until he completes the following quest: {b}Grim Tidings.{/b}"
            else:
                text "Talonclaw is currently committed to a {b}hunting patrol.{/b}"


    if quest_gather_herbs.started:
        add "gui/button/herb_idle.png" xalign 0.5 ypos 255
    else:
        add "gui/button/hunting_idle.png" xalign 0.5 ypos 255

screen SunSelect:
    style_prefix "sun_select"
    add "bg/sun_select_bg.png"

    imagebutton:
        xpos 433
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        idle "gui/button/proceed_idle.png"
        hover "gui/button/proceed_hover.png"
        insensitive "gui/button/proceed_unavailable.png"
        action [Hide ("SunSelect"), Hide("Camp"), Jump("bs2"), SetVariable("currently_in", "bury")]

    imagebutton:
        xpos 1096
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/button_click_2.mp3"
        idle "gui/button/do_not_proceed_idle.png"
        hover "gui/button/do_not_proceed_hover.png"
        action [Hide ("SunSelect"), Hide("Camp")]

    hbox:
        xpos 285
        ypos 562
        xmaximum 1430
        ymaximum 871
        frame:
            background Solid("#af9c6b")
            xmargin 45
            ymargin 45
            text "Talonclaw is currently committed to travel to the {b}burial site.{/b}"

style patrol_select_text:
    color "#1c1503"

style sun_select_text:
    color "#1c1503"
