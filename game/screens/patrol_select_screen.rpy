screen PatrolSelect():
    tag menu
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
                    if quest_gather_herbs.started:
                        action NullAction
                    else:
                        action [Jump("hunting_start"), SetVariable("already_patrolled", True)]

    imagebutton:
        xpos 1096
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/button_click_2.mp3"
        idle "gui/button/do_not_proceed_idle.png"
        hover "gui/button/do_not_proceed_hover.png"
        action Return()

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

            else:
                text "Talonclaw is currently committed to a {b}hunting patrol.{/b}"


    if quest_gather_herbs.started:
        add "gui/button/herb_idle.png" xalign 0.5 ypos 255
    else:
        add "gui/button/hunting_idle.png" xalign 0.5 ypos 255

screen PostPatrolSelect:
    tag menu
    style_prefix patrol_select

    imagebutton:
            xalign 0.5
            ypos 255
            idle "gui/button/training_idle.png"
            hover "gui/button/training_hover.png"
            action [SetVariable("config.intra_transition", None), ShowMenu("TrainingSelected")] 

style patrol_select_text:
    color "#1c1503"