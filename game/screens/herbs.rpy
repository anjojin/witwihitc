screen crocus:
    imagebutton:
        xpos 1605
        ypos 655
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
        xpos 969
        ypos 450
        idle "gui/button/mushroom.png"
        hover "gui/button/mushroom_hover.png"
        action Jump("ld1_click_mushroom")

screen ad_juniper:
    tag herb_screen
    imagebutton:
        xpos 0
        ypos 832
        idle "gui/button/junipera.png"
        hover "gui/button/junipera_hover.png"
        action Jump("ad1_click_juniper")

screen n_tansy:
    tag herb_screen
    imagebutton:
        xpos 450
        ypos 660
        idle "gui/button/tansy.png"
        hover "gui/button/tansy_hover.png"
        action Jump("n1_click_tansy")

screen md_berries:
    tag herb_screen
    imagebutton:
        xpos 1384
        ypos 30
        idle "gui/button/berry.png"
        hover "gui/button/berry_hover.png"
        action Jump("md1_click_berries")

screen freshkill:
    tag herb_screen
    imagebutton:
        xpos 1605
        ypos 587
        idle "gui/button/freshkill.png"
        hover "gui/button/freshkill_hover.png"
        action Jump("click_freshkill")

screen freshkill_night:
    tag herb_screen
    imagebutton:
        xpos 1605
        ypos 587
        idle "gui/button/freshkill_night.png"
        hover "gui/button/freshkill_hover.png"
        action Jump("cl3_freshkill")

screen clanmates:
    tag herb_screen
    imagebutton:
        xpos 0
        ypos 405
        idle "gui/button/clanmates.png"
        hover "gui/button/clanmates_hover.png"
        action Jump("cl3_clanmates")

screen willowkit:
    tag herb_screen
    imagebutton:
        xpos 595
        ypos 695
        idle "gui/button/willowkit.png"
        hover "gui/button/willowkit_hover.png"
        action Jump("ed3_willowkit")

screen talon_nest:
    tag herb_screen
    imagebutton:
        xpos 1220
        ypos 515
        idle "gui/button/nest.png"
        hover "gui/button/nest_hover.png"
        action Jump ("wd3_ending")