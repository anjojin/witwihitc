

label hunting_start:
    $ proceed_counter = 3
    call shuffle_patrols
    t "I am now hunting."
    call patrol_select

label hunting_1:
    "You encounter a mouse."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > 10:
                jump hunting_success
            else:
                jump hunting_fail
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            "You decide to look elsewhere."
            "."
            "."
            "."

label hunting_2:
    "You encounter a bird."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > 10:
                jump hunting_success
            else:
                jump hunting_fail
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            "You decide to look elsewhere."
            "."
            "."
            "."

label hunting_3:
    "You encounter a squirrel."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > 10:
                jump hunting_success
            else:
                jump hunting_fail
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            "You decide to look elsewhere."
            "."
            "."
            "."

label hunting_success:
    $ prey_caught += 1
    "You caught the prey!"
    call patrol_select

label hunting_fail:
    "You didn't catch the prey."
    call patrol_select


label hunting_major_fail:    
    "You lost all the prey."

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
    call patrol_select

label red_hunting_fail:
    "Redpaw tried to catch the prey, but failed."
    call patrol_select

label lily_hunting_success:
    "Lilypaw caught the prey!"
    call patrol_select

label lilypaw_hunting_fail:
    "Lilypaw tried to catch the prey, but failed."
    call patrol_select

label fawn_hunting_success:
    "Fawnpaw caught the prey!"
    call patrol_select

label fawn_hunting_fail:
    "Fawnpaw tried to catch the prey, but failed."
    call patrol_select

label clover_hunting_success:
    "Cloverpaw caught the prey!"
    call patrol_select

label clover_hunting_fail:
    "Cloverpaw tried to catch the prey, but failed."
    call patrol_select

label patrol_over:
    t "I should probably head back to camp."
