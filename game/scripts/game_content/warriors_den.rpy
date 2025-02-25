label warriors_den_first:
    $ warriors_visited = True
    scene warriors_den_dapple_nest with fade
    show screen gameUI

    t "Guess my conversation with Sunshadow took longer than I thought. All the healthy warriors have already gone out on patrol."
    t "Seems like I'll be hunting solo today."
    if quest_nesting_material.started:
        show screen dapple_nest
    call screen gameUI

label take_nesting:
    hide screen dapple_nest
    scene warriors_den_empty with fade
    "You picked up the {b}nesting materials.{/b}"
    $ quest_nesting_material.completed = True
    $ quest_nesting_material.started = False
    t "It feels so strange without Dapplefeather's nest there ..."
    t "The warriors' den just keeps getting smaller and smaller."
    call screen gameUI

label warriors_den_revisit:
    if quest_nesting_material.started:
        jump warriors_den_first
    if quest_nesting_material.completed:
        scene warriors_den_empty with fade
    else:
        scene warriors_den_dapple_nest with fade
    t "I hope the other warriors don't hate me for missing the morning patrol."
    t "Curse Sunshadow with his stupid, histrionic lectures."
    if quest_nesting_material.started:
        t "He really owes me after this. Why do I always let him talk me into doing the most mouse-brained stuff for him?"
    if quest_nesting_material.completed:
        t "... He'll be devastated when he sees Dapplefeather's nest is gone."
    else:
        t "... When they finally clear Dapplefeather's nest away, he'll be devastated."
    t "I hope burying her will at least help him find some healing."
    t "I could use a little healing, myself."
    t "This whole Clan could."
    call screen gameUI

