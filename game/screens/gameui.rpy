screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "gui/button/camp_idle.png"
        hover "gui/button/camp_hover.png"
        hover_sound "audio/sfx/button_hover_5.mp3"
        activate_sound "audio/sfx/button_click_2.mp3"
        if currently_in == "bury":
            action Jump("cl1")
        elif currently_in == "outside":
            action Jump("cl2")
        elif currently_in == "bury2":
            action Jump("cl4")
        else:
            action [Show("Camp")]

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -160
        yoffset 20
        idle "gui/button/quest_idle.png"
        hover "gui/button/quest_hover.png"
        hover_sound "audio/sfx/button_hover_5.mp3"
        activate_sound "audio/sfx/button_click_2.mp3"
        action ShowMenu("quests_ui")

    if final_game_screen:
        $ print(final_game_screen)
        add "gui/textbox.png"