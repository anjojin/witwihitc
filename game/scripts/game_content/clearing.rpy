label cl1:
    $ currently_in = "clearing"
    scene clearing bg with fade
    play sound "sfx/camp_click.mp3"
    show screen gameUI
    stop music fadeout 0.5
    play music "music/ES_Dreams of a Life - Damon Greene.mp3"
    if burial_rites:
        t "Okay. Nesting materials, prey, and crocuses ..."
        t "Nesting materials, I can probably find in the warrior's den."
        t "For crocuses, I'll have to search around camp."
        t "And for prey, I'll have to go on a hunting patrol." 
        t "Let's hope I manage to bring back more than one thing today ... I'd hate for my only catch to go to waste."
        play sound "sfx/game_tip.mp3"
        "The {b}Camp{/b} button can also be used to travel to different parts of camp, or go on patrol."
        play sound "sfx/game_tip.mp3"
        "Talonclaw does not have the strength to patrol more than once per day, so use it wisely."
        show screen freshkill
        call screen gameUI

    else:
        if talon_sun_bonus < 0:
            t "Mouse-brain ..."
            t "Whatever. He'll cool off eventually."
            t "He has to ..."
            t "In the meantime, I should probably see if anyone needs anything around camp."
        else:
            t "I should probably check out what's happening around camp."
        play sound "sfx/game_tip.mp3"
        "The {b}Camp{/b} button can also be used to travel to different parts of camp, or go on patrol."
        play sound "sfx/game_tip.mp3"
        "Talonclaw does not have the strength to patrol more than once per day, so use it wisely."
        show screen freshkill
        call screen gameUI

label click_freshkill:
    hide screen freshkill
    scene empty freshkill day
    show screen gameUI
    t "I hope the freshkill pile fills up soon."
    t "Though, even if it does, the prey never seems to last long ..."
    scene clearing bg with fade
    call screen gameUI

label cl2:
    scene clearing bg with fade
    show screen gameUI
    stop music fadeout 0.5
    play music "music/ES_Dreams of a Life - Damon Greene.mp3"
    t "The clearing is empty. Everycat's already gone out for the day."
    t "I'd better get a move on, myself, while there's still some light to lose."
    show screen freshkill
    call screen gameUI