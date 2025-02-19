screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "gui/button/camp_idle.png"
        hover "gui/button/camp_hover.png"
        if currently_in == "burial":
            action Jump("cl1")
        else:
            action Show("Camp")


    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -160
        yoffset 20
        idle "gui/button/quest_idle.png"
        hover "gui/button/quest_hover.png"
        action ShowMenu("quests_ui")

    if final_game_screen:
        $ print(final_game_screen)
        add "gui/textbox.png"