label herb_start:
    $ currently_in = "outside"
    $ already_patrolled = True
    call show_herbs
    scene patrol bg with fade
    show screen gameUI
    call screen herb_gathering_screen

label herb1_clicked:
    $ frame1_clicked = True
    menu:
        "You found [herbf1]. Would you like to pursue it?"
        "Yes":
            jump pursuef1 
        "No":
            jump no_pursue

label pursuef1:
    $ f1_locked = True
    call screen herb_gathering_screen
    show screen frame1_locked
    "x"

label herb2_clicked:
    $ frame2_clicked = True
    menu:
        "You found [herbf2]. Would you like to pursue it?"
        "Yes":
            jump pursuef2
        "No":
            jump no_pursue

label pursuef2:
    $ f2_locked = True
    call screen herb_gathering_screen
    show screen frame2_locked
    "x"

label herb3_clicked:
    $ frame3_clicked = True
    menu:
        "You found [herbf3]. Would you like to pursue it?"
        "Yes":
            jump pursuef3 
        "No":
            jump no_pursue

label pursuef3:
    $ f3_locked = True
    call screen herb_gathering_screen
    show screen frame3_locked
    "x"

label herb4_clicked:
    $ frame4_clicked = True
    menu:
        "You found [herbf4]. Would you like to pursue it?"
        "Yes":
            jump pursuef4
        "No":
            jump no_pursue

label pursuef4:
    $ f4_locked = True
    call screen herb_gathering_screen
    show screen frame4_locked
    "x"

label herb5_clicked:
    $ frame5_clicked = True
    menu:
        "You found [herbf5]. Would you like to pursue it?"
        "Yes":
            jump pursuef5
        "No":
            jump no_pursue

label pursuef5:
    $ f5_locked = True
    call screen herb_gathering_screen
    show screen frame5_locked
    "x"

label no_pursue:
    "You decide not to pursue the herb."

label herb_proceed:
    scene herbbg with fade
    call proceed_logic
    call screen herb_gathering_screen