
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 33

style choice_button:
    is default # This means it doesn't use the usual button styling
    xysize (926, None)
    background Frame("gui/button/choice_[prefix_]background.png",
        150, 25, 150, 25, tile=False)
    padding (12, 12)
    hover_sound "audio/sfx/button_hover_3.mp3"
    activate_sound "audio/sfx/button_click_3.mp3"

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    idle_color "#302919"
    hover_color "#000000"
    insensitive_color "#5a5a5a"
