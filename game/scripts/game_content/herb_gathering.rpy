label herb_start:
    $ currently_in = "outside"
    $ already_patrolled = True
    $ print("I am now calling show_herbs")
    call show_herbs
    scene patrol bg with fade
    show screen gameUI

label herb1_clicked:
    $ frame1_clicked = True
    show screen locked_herbs
    menu:
        "You found [herbf1]. Would you like to pursue it?"
        "Yes":
            jump pursuef1 
        "No":
            jump no_pursue

label pursuef1:
    $ f1_locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb2_clicked:
    $ frame2_clicked = True
    show screen locked_herbs
    menu:
        "You found [herbf2]. Would you like to pursue it?"
        "Yes":
            jump pursuef2
        "No":
            jump no_pursue

label pursuef2:
    $ f2_locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb3_clicked:
    $ frame3_clicked = True
    show screen locked_herbs
    menu:
        "You found [herbf3]. Would you like to pursue it?"
        "Yes":
            jump pursuef3 
        "No":
            jump no_pursue

label pursuef3:
    $ f3_locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb4_clicked:
    $ frame4_clicked = True
    show screen locked_herbs
    menu:
        "You found [herbf4]. Would you like to pursue it?"
        "Yes":
            jump pursuef4
        "No":
            jump no_pursue

label pursuef4:
    $ f4_locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb5_clicked:
    $ frame5_clicked = True
    show screen locked_herbs
    menu:
        "You found [herbf5]. Would you like to pursue it?"
        "Yes":
            jump pursuef5
        "No":
            jump no_pursue

label pursuef5:
    $ f5_locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label no_pursue:
    "You decide not to pursue the herb."

label herb_proceed:
    $ lost_leads = []
    call proceed_logic
    scene herbbg with fade
    $ f1_locked = False
    $ f2_locked = False
    $ f3_locked = False
    $ f4_locked = False
    $ f5_locked = False
    if len(lost_leads)>0:
        $ j=0
        python:
            while j< len(lost_leads):
                renpy.say("You lost the scent of [lost_leads[j]].")
                j += 1
    call screen herb_gathering_screen
