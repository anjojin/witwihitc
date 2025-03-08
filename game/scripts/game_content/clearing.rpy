label cl1:
    $ currently_in = "clearing"
    scene clearing bg with fade
    show screen gameUI
    stop music fadeout 0.5
    if burial_rites:
        t "Okay. Nesting materials, prey, and crocuses ..."
        t "Nesting materials, I can probably find in the warrior's den."
        t "For crocuses, I'll have to search around camp."
        t "And for prey, I'll have to go on a hunting patrol." 
        t "Let's hope I manage to bring back more than one ... I'd hate for the only thing I catch today to go to waste."
        "The {b}Camp{/b} button can also be used to travel to different parts of camp, or go on patrol."
        "Talonclaw does not have the strength to patrol more than once per day, so use it wisely."
        call screen gameUI

    else:
        if talon_sun_bonus < 0:
            t "Mouse-brain ..."
            t "Whatever. He'll cool off eventually."
            t "He has to ..."
            t "In the meantime, I should probably see if anyone needs anything around camp."
        else:
            t "I should probably check out what's happening around camp."
        "The {b}Camp{/b} button can also be used to travel to different parts of camp, or go on patrol."
        "Talonclaw does not have the strength to patrol more than once per day, so use it wisely."
        call screen gameUI

label cl2:
    scene clearing bg with fade
    show screen gameUI
    stop music fadeout 0.5
    "x"
    call screen gameUI