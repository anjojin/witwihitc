label herb_start:
    stop music fadeout 1.0
    play music "music/ES_Saint Valentine - Vendla.mp3" loop
    $ currently_in = "outside"
    $ already_patrolled = True
    call define_herbs from _call_define_herbs
    scene patrol bg with fade
    show screen gameUI
    t "Hang in there, little ones."
    t "I'll be back with what you need before you know it ..."
    play sound "sfx/game_tip.mp3"
    menu:
        "Would you like to play through the tutorial?"
        "Yes":
            jump herb_tutorial
        "No":
            jump herb_real_start

label herb_tutorial:
    play sound "sfx/game_tip.mp3"
    "Talonclaw is now {b}gathering herbs.{/b} He will need to {b}track scents{/b} across the territory to find where the plants he needs are growing."
    show screen tutorial_frame_screen
    play sound "sfx/game_tip.mp3"
    "The {b}(!){/b} icon indicates that Talonclaw has caught the scent of a {b}blackberry plant.{/b} Click on the icon and see what happens!"
    call screen tutorial_frame_screen

label demonstrate_proceed:
    $ tutorial_frame.progress += 1
    scene herbbg_1 with fade
    show screen tutorial_frame_screen
    play sound "sfx/game_tip.mp3"
    "You successfully tracked the scent of {b}blackberry{/b} to the next part of the territory!"
    play sound "sfx/game_tip.mp3"
    "If you continue successfully pursuing this scent, eventually it will lead you to the blackberry plant."
    play sound "sfx/game_tip.mp3"
    "Once you find the plant, you can either choose to collect it to bring back to camp or use it on the territory."
    $ tutorial_proceeded = True
    $ tutorial_frame.progress = 1
    $ tutorial_frame.locked = False
    scene patrol bg with fade
    show screen gameUI
    play sound "sfx/game_tip.mp3"
    "Talonclaw will not always manage to track the scent successfully."
    play sound "sfx/game_tip.mp3"
    "Try pursuing the scent once more."
    call screen tutorial_frame_screen

label demonstrate_loss:
    $ tutorial_frame.empty = True
    scene herbbg_1 with fade
    show screen tutorial_frame_screen
    play sound "sfx/prey_minor_loss.mp3"
    "You lost the scent of blackberry."
    play sound "sfx/game_tip.mp3"
    "Weaker scents are more likely to be lost than stronger scents."
    play sound "sfx/game_tip.mp3"
    "However, different types of herb scents all have the same likelihood of being lost, regardless of their rarities."
    scene patrol bg with fade
    hide screen tutorial_frame_screen
    $ tutorial_frame.locked = False
    play sound "sfx/game_tip.mp3"
    "You have now completed the tutorial!"
    play sound "sfx/game_tip.mp3"
    menu:
        "Would you like to hear the instructions again?"
        "Yes":
            $ tutorial_frame.empty = False
            $ tutorial_proceeded = False
            jump herb_tutorial
        "No":
            jump herb_real_start

label herb_real_start:
    t "Alright. Let's get a move on."
    call screen herb_gathering_screen


label herbt_p1_clicked:
    show screen tutorial_frame_screen
    show screen locked_herbs
    menu:
        "The scent of blackberry is faint. Would you like to pursue it?"
        "Yes":
            jump demonstrate_lock
        "No":
            jump no_pursue_tutorial

label no_pursue_tutorial:
    "Choosing not to pursue the scent of blackberry means that, when you hit {b}Proceed,{/b} the scent of a different herb has the chance to generate in its place."
    "Click the icon again and, this time, try choosing to {b}pursue{/b} the scent!"
    call screen tutorial_frame_screen

label demonstrate_lock:
    $ tutorial_frame.locked = True
    show screen tutorial_frame_screen
    show screen locked_herbs
    play sound "sfx/game_tip.mp3"
    if not tutorial_proceeded:
        "The scent is now {b}locked in place.{/b} When you choose to proceed to the next part of the territory, {b}no other scent{/b} will generate in this location."
        play sound "sfx/game_tip.mp3"
        "Try hitting the {b}proceed{/b} button now!"
        call screen locked_herbs
    else:
        "Now, {b}proceed{/b} again."
        call screen locked_herbs

label herb1_p1_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame1.herb.name]{/b} is faint. Would you like to pursue it?"
        "Yes":
            jump pursuef1
        "No":
            jump no_pursue


label herb1_p2_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame1.herb.name]{/b} is getting stronger. Would you like to keep pursuing?"
        "Yes":
            jump pursuef1 
        "No":
            jump no_pursue

label herb1_p3_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame1.herb.name]{/b} so strong, you can almost taste it. Would you like to keep pursuing?"
        "Yes":
            jump pursuef1 
        "No":
            jump no_pursue

label pursuef1:
    $ frame1.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs

label herb2_p1_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame2.herb.name]{/b} is faint. Would you like to pursue it?"
        "Yes":
            jump pursuef2
        "No":
            jump no_pursue

label herb2_p2_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame2.herb.name]{/b} is getting stronger. Would you like to keep pursuing?"
        "Yes":
            jump pursuef2
        "No":
            jump no_pursue

label herb2_p3_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame2.herb.name]{/b} so strong, you can almost taste it. Would you like to keep pursuing?"
        "Yes":
            jump pursuef2
        "No":
            jump no_pursue

label pursuef2:
    $ frame2.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs

label herb3_p1_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame3.herb.name]{/b} is faint. Would you like to pursue it?"
        "Yes":
            jump pursuef3
        "No":
            jump no_pursue

label herb3_p2_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame3.herb.name]{/b} is getting stronger. Would you like to keep pursuing?"
        "Yes":
            jump pursuef3
        "No":
            jump no_pursue

label herb3_p3_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame3.herb.name]{/b} so strong, you can almost taste it. Would you like to keep pursuing?"
        "Yes":
            jump pursuef3
        "No":
            jump no_pursue

label pursuef3:
    $ frame3.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs

label herb4_p1_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame4.herb.name]{/b} is faint. Would you like to pursue it?"
        "Yes":
            jump pursuef4
        "No":
            jump no_pursue

label herb4_p2_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame4.herb.name]{/b} is getting stronger. Would you like to keep pursuing?"
        "Yes":
            jump pursuef4
        "No":
            jump no_pursue

label herb4_p3_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame4.herb.name]{/b} so strong, you can almost taste it. Would you like to keep pursuing?"
        "Yes":
            jump pursuef4
        "No":
            jump no_pursue

label pursuef4:
    $ frame4.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs

label herb5_p1_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame5.herb.name]{/b} is faint. Would you like to pursue it?"
        "Yes":
            jump pursuef5
        "No":
            jump no_pursue

label herb5_p2_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame5.herb.name]{/b} is getting stronger. Would you like to keep pursuing?"
        "Yes":
            jump pursuef5
        "No":
            jump no_pursue

label herb5_p3_clicked:
    show screen herb_gathering_screen
    show screen locked_herbs
    menu:
        "The scent of {b}[frame5.herb.name]{/b} so strong, you can almost taste it. Would you like to keep pursuing?"
        "Yes":
            jump pursuef5
        "No":
            jump no_pursue

label pursuef5:
    $ frame5.locked = True
    show screen herb_gathering_screen
    call screen locked_herbs

label no_pursue:
    show screen herb_gathering_screen
    call screen locked_herbs

label herb_proceed:
    hide screen herb_gathering_screen
    hide screen locked_herbs
    if q<herb_proceed_max:
        $ q += 1
    if q==herb_proceed_max:
        jump herb_end
    $ lost_leads = []
    call proceed_logic(frame1) from _call_proceed_logic
    call proceed_logic(frame2) from _call_proceed_logic_1
    call proceed_logic(frame3) from _call_proceed_logic_2
    call proceed_logic(frame4) from _call_proceed_logic_3
    call proceed_logic(frame5) from _call_proceed_logic_4
    scene herbbg with fade
    if len(lost_leads)>0:
        while len(lost_leads)>0:
            play sound "sfx/prey_minor_loss.mp3"
            "You lost the scent of [lost_leads.pop()]."
    call screen herb_gathering_screen

label herb1_found:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You found {b}[frame1.herb.name]{/b}!"
    if frame1.herb.turns == 2:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to refresh the scents in this part of the territory?"
            "Collect":
                jump herb1_collected
            "Use":
                $ frame1.progress = 1
                jump use_2turn
    elif frame1.herb.turns == 3:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to advance the progress of one other scent?"
            "Collect":
                jump herb1_collected
            "Use":
                $ frame1.progress = 1
                $ frame1.empty = True
                jump use_3turn
    elif frame1.herb.turns == 4:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to gain {b}four extra proceeds?{/b}"
            "Collect":
                jump herb1_collected
            "Use":
                $ frame1.progress = 1
                $ frame1.empty = True
                jump use_4turn

label herb1_collected:
    "You collected the {b}[frame1.herb.name].{/b}"
    $ herbs_gathered.append(frame1.herb.name)
    $ frame1.empty = True
    $ frame1.locked = False
    $ frame1.progress = 1
    show screen herb_gathering_screen
    call screen locked_herbs

label use_2turn:
    hide screen herb_gathering_screen
    call define_herbs from _call_define_herbs_1
    show screen herb_gathering_screen with fade
    call screen locked_herbs

label use_3turn:
    menu:
        "Which scent would you like to advance the progress of?"
        "[frame1.herb.name]" if not frame1.empty:
            $ frame1.progress += 1
        "[frame2.herb.name]" if not frame2.empty:
            $ frame2.progress += 1
        "[frame3.herb.name]" if not frame3.empty:
            $ frame3.progress += 1
        "[frame4.herb.name]" if not frame4.empty:
            $ frame4.progress += 1
        "[frame5.herb.name]" if not frame5.empty:
            $ frame5.progress += 1
    show screen herb_gathering_screen
    call screen locked_herbs

label use_4turn:
    $ herb_proceed_max += 4
    show screen herb_gathering_screen
    call screen locked_herbs

label herb2_found:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You found {b}[frame2.herb.name]{/b}!"
    if frame2.herb.turns == 2:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to refresh the scents in this part of the territory?"
            "Collect":
                $ frame2.progress = 1
                jump herb2_collected
            "Use":
                jump use_2turn
    elif frame2.herb.turns == 3:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to advance the progress of one other scent?"
            "Collect":
                jump herb2_collected
            "Use":
                $ frame2.progress = 1
                $ frame2.empty = True
                jump use_3turn
    elif frame2.herb.turns == 4:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to gain {b}four extra proceeds?{/b}"
            "Collect":
                jump herb2_collected
            "Use" if not already_used:
                $ frame2.progress = 1
                $ frame2.empty = True
                $ already_used = True
                jump use_4turn

label herb2_collected:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You collected the {b}[frame2.herb.name]{/b}."
    $ herbs_gathered.append(frame2.herb.name)
    $ frame2.empty = True
    $ frame2.locked = False
    $ frame2.progress = 1
    show screen herb_gathering_screen
    call screen locked_herbs

label herb3_found:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You found {b}[frame3.herb.name]{/b}!"
    if frame3.herb.turns == 2:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to refresh the scents in this part of the territory?"
            "Collect":
                jump herb3_collected
            "Use":
                $ frame3.progress = 1                
                jump use_2turn
    elif frame3.herb.turns == 3:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to advance the progress of one other scent?"
            "Collect":
                jump herb3_collected
            "Use":
                $ frame3.progress = 1
                $ frame3.empty = True
                jump use_3turn
    elif frame3.herb.turns == 4:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to gain {b}four extra proceeds?{/b}"
            "Collect":
                jump herb3_collected
            "Use":
                $ frame3.progress = 1
                $ frame3.empty = True
                jump use_4turn

label herb3_collected:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You collected the {b}[frame3.herb.name]{/b}."
    $ herbs_gathered.append(frame3.herb.name)
    $ frame3.empty = True
    $ frame3.locked = False
    $ frame3.progress = 1
    show screen herb_gathering_screen
    call screen locked_herbs

label herb4_found:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You found {b}[frame4.herb.name]{/b}!"
    if frame4.herb.turns == 2:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to refresh the scents in this part of the territory?"
            "Collect":
                jump herb4_collected
            "Use":
                $ frame4.progress = 1
                jump use_2turn
    elif frame4.herb.turns == 3:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to advance the progress of one other scent?"
            "Collect":
                jump herb4_collected
            "Use":
                $ frame4.progress = 1
                $ frame4.empty = True
                jump use_3turn
    elif frame4.herb.turns == 4:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to gain {b}four extra proceeds?{/b}"
            "Collect":
                jump herb4_collected
            "Use":
                $ frame4.progress = 1
                $ frame4.empty = True
                jump use_4turn

label herb4_collected:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You collected the {b}[frame4.herb.name]{/b}."
    $ herbs_gathered.append(frame4.herb.name)
    $ frame4.empty = True
    $ frame4.locked = False
    $ frame4.progress = 1
    show screen herb_gathering_screen
    call screen locked_herbs

label herb5_found:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You found {b}[frame5.herb.name]{/b}!"
    if frame5.herb.turns == 2:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to refresh the scents in this part of the territory?"
            "Collect":
                jump herb5_collected
            "Use":
                $ frame5.progress = 1
                jump use_2turn
    elif frame5.herb.turns == 3:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to advance the progress of one other scent?"
            "Collect":
                jump herb5_collected
            "Use":
                $ frame5.progress = 1
                $ frame5.empty = True
                jump use_3turn
    elif frame5.herb.turns == 4:
        menu:
            "Would you like to {b}collect it{/b} to bring back to camp, or {b}use it{/b} here to gain {b}four extra proceeds?{/b}"
            "Collect":
                jump herb5_collected
            "Use":
                $ frame5.progress = 1
                $ frame5.empty = True
                jump use_4turn

label herb5_collected:
    show screen herb_gathering_screen
    show screen locked_herbs
    "You collected the {b}[frame5.herb.name]{/b}."
    $ herbs_gathered.append(frame5.herb.name)
    $ frame5.empty = True
    $ frame5.locked = False
    $ frame5.progress = 1
    show screen herb_gathering_screen
    call screen locked_herbs

label herb_end:
    t "It's getting dark ... I should probably start getting back to camp."
    hide screen herb_gathering_screen
    play audio "sfx/quest_unlocked.mp3"
    "{b}Patrol Completed.{/b}"
    if "catmint" in herbs_gathered:
        play audio "sfx/quest_unlocked.mp3"
        $ quest_gather_herbs.started = False
        $ quest_gather_herbs.completed = True
        $ got_catmint = True
        "{b}Quest Completed:{/b} Collect Catmint"
    else:
        $ quest_gather_herbs.started = False
        $ quest_gather_herbs.failed = True
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Quest Failed:{/b} Collect Catmint"
    if len(herbs_gathered)==1:
        "You gathered {b}1{/b} herb in total."
    else:
        "You gathered {b}[len(herbs_gathered)]{/b} herbs in total."
    jump cl3