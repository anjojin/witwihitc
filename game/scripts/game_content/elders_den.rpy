label ed1:
    $ elders_visited = True
    scene elders_bg_crocus with fade
    stop music fadeout 1.0
    play music "ambience/ES_Forest High Wind Trees Creaking - Epidemic Sound.mp3" loop volume 1.5
    show screen gameUI
    t ""
    t "This used to be the elders' den, and now ..."
    t "..."
    t "......."
    t ".........."
    t "I shouldn't stay here long."
    t "Out of respect for the dead."
    if quest_crocus.started:
        show screen crocus
    call screen gameUI

label ed1_take_crocus:
    hide screen crocus
    scene elders_den_bg with fade
    play audio "sfx/plant_correct.mp3"
    play sound "sfx/game_tip.mp3"
    "You picked up the {b}crocus.{/b}"
    t "Crocuses. Probably best not to tell Sunshadow where they came from."
    t "How cruel, that something so beautiful can grow in a place like this."
    $ quest_crocus.completed = True
    $ quest_crocus.started = False
    call screen gameUI

label ed2:
    if quest_crocus.started:
        jump elders_den_first
    if quest_crocus.completed:
        show screen elders_den_bg with fade
    else:
        show screen elders_bg_crocus with fade
    show screen gameUI
    t ".........."
    t "I shouldn't stay here long."
    t "Out of respect for the dead."
    call screen gameUI