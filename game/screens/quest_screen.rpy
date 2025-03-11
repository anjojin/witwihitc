screen quests_ui:
    style_prefix "quests_screen"
    add "bg/quest_bg.png"

    ## Show a Return button
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "gui/button/back_%s.png"
        hover_sound "audio/sfx/button_hover_1.mp3"
        activate_sound "audio/sfx/button_click_1.mp3"
        action Return()

    frame:
        background None
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 70
            vbox:
                text "{b}In-Progress{/b}"
                for quest in my_quests:
                    if quest.started:
                        text "\n[quest.name]: \n[quest.description]" 
            vbox:
                text "{b}Completed{/b}"
                for quest in my_quests:
                    if quest.completed:
                        text "[quest.name]"
            vbox:
                text "{b}Cancelled{/b}"
                for quest in my_quests:
                    if quest.cancelled:
                        text "[quest.name]"

style quests_screen_text:
    color "#1c1503"
    size 30
