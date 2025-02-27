screen crocus:
    imagebutton:
        xpos 1610
        ypos 656
        idle "gui/button/crocus.png"
        hover "gui/button/crocus_hover.png"
        action Jump("ed1_take_crocus")

screen dapple_nest:
    tag herb_screen
    imagebutton:
        xpos 782
        ypos 327
        idle "gui/button/dapple_nest.png"
        hover "gui/button/dapple_nest_hover.png"
        action Jump("wd1_take_nesting")

screen ld_mushroom:
    tag herb_screen
    imagebutton:
        xpos 965
        ypos 435
        idle "gui/button/mushroom.png"
        hover "gui/button/mushroom_hover.png"
        action Jump("ld1_click_mushroom")

screen ad_juniper:
    tag herb_screen
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/button/juniper.png"
        hover "gui/button/juniper_hover.png"
        action Jump("ad1_click_juniper")

screen n_tansy:
    tag herb_screen
    imagebutton:
        xpos 450
        ypos 660
        idle "gui/button/tansy.png"
        hover "gui/button/tansy_hover.png"
        action Jump("n1_click_tansy")