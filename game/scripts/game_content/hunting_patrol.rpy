

label hunting_start:
    $ proceed_counter = 3
    $ currently_in = "outside"
    call shuffle_patrols from _call_shuffle_patrols
    if quest_favorite_prey.started:
        $ talon_chance = 12 - talon_sun_bonus
    else:
        $ talon_chance = 12 - talon_clan_bonus
    scene patrol bg with fade
    show screen gameUI
    t "I am now hunting."
    call patrol_select from _call_patrol_select

label hunting_1:
    "You encounter a mouse."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                jump hunting_success
            elif h1_int < 2:
                jump hunting_major_fail
            else:
                jump hunting_fail
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            "You decide to look elsewhere."

label hunting_2:
    "You encounter a bird."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                jump hunting_success
            else:
                jump hunting_fail
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            "You decide to look elsewhere."

label hunting_3:
    "You encounter a squirrel."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                jump hunting_success
            else:
                jump hunting_fail
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                jump hunting_dnp

label hunting_success:
    $ prey_caught += 1
    "You caught the prey!"
    call patrol_select from _call_patrol_select_1

label hunting_fail:
    "You didn't catch the prey."
    call patrol_select from _call_patrol_select_2

label hunting_dnp:
    "You decide to look elsewhere."
    call patrol_select from _call_patrol_select_11

label hunting_major_fail:    
    $ prey_caught = 0
    "You lost all the prey."
    call patrol_select from _call_patrol_select_12


label hunting_red: 
    $ h1_int = renpy.random.randint(1,20)
    if h1_int > 13:
        jump red_hunting_success
    else:
        jump red_hunting_fail
    
label hunting_lily:
    $ h1_int = renpy.random.randint(1,20)
    if h1_int > 11:
        jump lily_hunting_success
    else:
        jump lily_hunting_fail

label hunting_fawn: 
    $ h1_int = renpy.random.randint(1,20)
    if h1_int > 12:
        jump fawn_hunting_success
    else:
        jump fawn_hunting_fail
    
label hunting_clover:
    $ h1_int = renpy.random.randint(1,20)
    if h1_int > 13:
        jump clover_hunting_success
    else:
        jump clover_hunting_fail

label red_hunting_success:
    "Redpaw caught the prey!"
    call patrol_select from _call_patrol_select_3

label red_hunting_fail:
    "Redpaw tried to catch the prey, but failed."
    call patrol_select from _call_patrol_select_4

label lily_hunting_success:
    "Lilypaw caught the prey!"
    call patrol_select from _call_patrol_select_5

label lilypaw_hunting_fail:
    "Lilypaw tried to catch the prey, but failed."
    call patrol_select from _call_patrol_select_6

label fawn_hunting_success:
    "Fawnpaw caught the prey!"
    call patrol_select from _call_patrol_select_7

label fawn_hunting_fail:
    "Fawnpaw tried to catch the prey, but failed."
    call patrol_select from _call_patrol_select_8

label clover_hunting_success:
    "Cloverpaw caught the prey!"
    call patrol_select from _call_patrol_select_9

label clover_hunting_fail:
    "Cloverpaw tried to catch the prey, but failed."
    call patrol_select from _call_patrol_select_10

label patrol_over:
    t "I should probably head back to camp."
