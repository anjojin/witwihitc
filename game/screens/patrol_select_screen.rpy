screen HuntingSelected():
    tag menu
    style_prefix "hunting_select"
    add "bg/patrol_select_bg.png"

    imagebutton:
        xpos 433
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        idle "gui/button/proceed_idle.png"
        hover "gui/button/proceed_hover.png"
        action Jump("hunting_start")

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
            text "Talonclaw is currently committed to a {b}hunting patrol.{/b}"

    add "gui/button/hunting_idle.png" xalign 0.5 ypos 255

screen AppHuntingSelected():
    tag menu
    style_prefix "apphunting_select"
    add "bg/patrol_select_bg.png"
   
    imagebutton:
        xpos 433
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        idle "gui/button/proceed_idle.png"
        hover "gui/button/proceed_hover.png"
        action Jump("hunting_start")

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
            text "Talonclaw is committed to a {b}hunting patrol with the apprentices.{/b}"

    add "gui/button/hunting_idle.png" xalign 0.5 ypos 255

screen HerbSelected():
    tag menu
    style_prefix "herb_select"
    add "bg/patrol_select_bg.png"

    imagebutton:
        xpos 433
        ypos 895
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        idle "gui/button/proceed_idle.png"
        hover "gui/button/proceed_hover.png"
        action NullAction

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
            text "Talonclaw is currently committed to an {b}herb gathering patrol.{/b}"
    
    add "gui/button/herb_idle.png" xalign 0.5 ypos 255

screen PostPatrolSelect:
    tag menu
    style_prefix patrol_select

    imagebutton:
            xalign 0.5
            ypos 255
            idle "gui/button/training_idle.png"
            hover "gui/button/training_hover.png"
            action [SetVariable("config.intra_transition", None), ShowMenu("TrainingSelected")] 

screen TrainingSelected():
    tag menu
    style_prefix "training_select"
    add "bg/patrol_select_bg.png"

    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "gui/button/back_%s.png"
        action Return()

    imagebutton:
        xpos 433
        ypos 895
        idle "gui/button/proceed_idle.png"
        hover "gui/button/proceed_hover.png"
        if training_with == "Shimmerpaw":
            action Jump("shimmer_training")

        if training_with == "None":
            action Jump("lonely_training")

    imagebutton:
        xpos 1096
        ypos 895
        idle "gui/button/do_not_proceed_idle.png"
        hover "gui/button/do_not_proceed_hover.png"
        action ShowMenu("PatrolSelect")

    hbox:
        xpos 285
        ypos 562
        xmaximum 1430
        ymaximum 871
        frame:
            background Solid("#af9c6b")

            xmargin 45
            ymargin 45
            text "Training selected. You are currently set to train with: [training_with]."

    add "gui/button/hunting_unavailable.png" xpos 852 ypos 255
    add "gui/button/training_hover.png" xpos 524 ypos 255
    add "gui/button/herb_unavailable.png" xpos 1197 ypos 255

style training_select_text:
    color "#1c1503"

style hunting_select_text:
    color "#1c1503"

style herb_select_text:
    color "#1c1503"

style apphunting_select_text:
    color "#1c1503"