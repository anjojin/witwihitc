label wd1:
    $ warriors_visited = True
    scene warriors_den_dapple_nest with fade
    stop music fadeout 1.0
    play music "music/ES_Autumn Skies - Roots and Recognition.mp3"
    show screen gameUI
    t "Guess my conversation with Sunshadow took longer than I thought. All the healthy warriors have already gone out on patrol."
    t "Seems like I'll be hunting solo today."
    if quest_nesting_material.started:
        show screen dapple_nest
    call screen gameUI

label wd1_take_nesting:
    play audio "sfx/plant_correct.mp3"
    hide screen dapple_nest
    scene warriors_den_empty with fade
    play sound "sfx/game_tip.mp3"
    $ talon_sun_bonus += 1
    "You picked up the {b}nesting materials.{/b}"
    $ quest_nesting_material.completed = True
    $ quest_nesting_material.started = False
    t "It feels so strange without Spottedlight's nest there ..."
    t "The warriors' den just keeps getting smaller and smaller."
    call screen gameUI

label wd2:
    if quest_nesting_material.started:
        jump wd1
    if quest_nesting_material.completed:
        scene warriors_den_empty with fade
    else:
        scene warriors_den_dapple_nest with fade
    stop music fadeout 1.0
    t "I hope the other warriors don't hate me for missing the morning patrol."
    t "Curse Sunshadow with his stupid, histrionic lectures."
    if quest_nesting_material.started:
        t "He really owes me after this. Why do I always let him talk me into doing the most mouse-brained stuff for him?"
    if quest_nesting_material.completed:
        t "... He'll be devastated when he sees Spottedlight's nest is gone."
    else:
        t "... When they finally clear Spottedlight's nest away, he'll be devastated."
    t "I hope burying her will at least help him find some healing."
    t "I think I could use a little of that, myself."
    t "This whole Clan could."
    call screen gameUI

label wd3:
    $ warriors_visited_postp = True
    stop music fadeout 1.0
    play music "music/ES_Autumn Skies - Roots and Recognition.mp3"
    if quest_nesting_material.completed:
        scene warriors night with fade
    else:
        scene warriors night dapple with fade
    show screen gameUI
    t "Great StarClan, I'm exhausted ..."
    t "It feels like I could curl up in my nest and sleep until newleaf."
    play sound "sfx/game_tip.mp3"
    "When you're ready, you can {b}click on Talonclaw's nest{/b} to end the game."
    play sound "sfx/game_tip.mp3"
    "However, this is not the only way to end the story ..."
    play sound "sfx/game_tip.mp3"
    "See if you can discover all the endings!"
    show screen talon_nest
    call screen gameUI

label wd3_ending:
    hide screen talon_nest
    scene black with fade
    t "Zzz..."
    $ MainMenu(confirm=False)()


label wd4:
    stop music fadeout 1.0
    play music "music/ES_Autumn Skies - Roots and Recognition.mp3"
    if quest_nesting_material.completed:
        scene warriors night with fade
    else:
        scene warriors night dapple with fade
    show screen gameUI
    t "..."
    show screen talon_nest
    call screen gameUI






    

