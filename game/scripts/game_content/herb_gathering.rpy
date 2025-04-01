label herb_start:
    $ currently_in = "outside"
    $ already_patrolled = True
    $ print(i)
    call define_herbs
    scene patrol bg with fade
    show screen gameUI
    call screen herb_gathering_screen

label herb1_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "You found [frame1.herb.name]. Would you like to pursue it?"
        "Yes":
            jump pursuef1 
        "No":
            jump no_pursue

label pursuef1:
    $ frame1.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb2_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "You found [frame2.herb.name]. Would you like to pursue it?"
        "Yes":
            jump pursuef2
        "No":
            jump no_pursue

label pursuef2:
    $ frame2.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb3_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "You found [frame3.herb.name]. Would you like to pursue it?"
        "Yes":
            jump pursuef3 
        "No":
            jump no_pursue

label pursuef3:
    $ frame3.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb4_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "You found [frame4.herb.name]. Would you like to pursue it?"
        "Yes":
            jump pursuef4
        "No":
            jump no_pursue

label pursuef4:
    $ frame4.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label herb5_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "You found [frame5.herb.name]. Would you like to pursue it?"
        "Yes":
            jump pursuef5
        "No":
            jump no_pursue

label pursuef5:
    $ frame5.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs
    "x"

label no_pursue:
    "You decide not to pursue the herb."

label herb_proceed:
    $ q += 1
    $ lost_leads = []
    call proceed_logic(frame1)
    call proceed_logic(frame2)
    call proceed_logic(frame3)
    call proceed_logic(frame4)
    call proceed_logic(frame5)
    scene herbbg with fade
    if len(lost_leads)>0:
        "You lost the scent of [lost_leads]."
    call screen herb_gathering_screen
