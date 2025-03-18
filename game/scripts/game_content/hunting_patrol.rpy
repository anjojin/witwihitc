

label hunting_start:
    $ proceed_counter = 3
    $ currently_in = "outside"
    call shuffle_patrols from _call_shuffle_patrols
    if quest_favorite_prey.started:
        $ talon_chance = 13 - talon_sun_bonus
    else:
        $ talon_chance = 13 - talon_clan_bonus
    scene patrol bg with fade
    stop music fadeout 1.0
    play audio "ambience/ES_Bieszczady Forest, Winter, Silence - Epidemic Sound.mp3" loop
    play music "music/ES_Naranjas en Diciembre - Vendla.mp3" loop
    if quest_babysitting.started:
        t "Hello, apprentices!"
    else:
        t "So cold ... It feels like my paws are about to snap off."
        if talon_sun_bonus > 2:
            t "I can't even imagine how much pain Sunshadow must be in, digging that grave out there all by himself."
            t "Just hang on a little while longer, buddy. I'll be there with you before you know it."
        elif talon_clan_bonus > 2 and quest_feed_deputy.started:
            t "Still, Briarstar is counting on me to bring something back for Pouncetail. The whole Clan is."
            t "I'd better get a move on. For everycat's sake."
        else:
            t "Let's hope I manage to catch something that makes all this worth it."

label hunting_instructions:    
    play sound "sfx/game_tip.mp3"
    "Talonclaw is now {b}hunting:{/b} scouring the territory for the sights, sounds, or scents of possible prey."
    play sound "sfx/game_tip.mp3"
    "Food is scarce, so it may take a few seconds for him to find anything."
    play sound "sfx/game_tip.mp3"
    "Once he does, he can either {b}proceed{/b} or {b}not proceed{/b} to make the catch."
    play sound "sfx/game_tip.mp3"
    if quest_babysitting.started:
        "If he {b}proceeds,{/b} he will either succeed at making the catch, or fail. If he {b}does not proceed,{/b} one of the {b}apprentices{/b} will attempt to make the catch."
    else:
        "If he {b}proceeds,{/b} he will either succeed at making the catch, or fail. If he {b}does not proceed,{/b} the catch will be skipped over."
    play sound "sfx/game_tip.mp3"
    "Not all opportunities are created equal. Catches marked with {b}(!){/b} are low risk, low reward. However, catches marked with {b}(!!!){/b} promise much higher rewards, with harsher consequences."
    play sound "sfx/game_tip.mp3"
    "Talonclaw has the strength to proceed {b}3 times;{/b} however, opportunities to catch prey will eventually run out."
    play sound "sfx/game_tip.mp3"
    "The patrol will end when Talonclaw can no longer proceed, or when Talonclaw has exhausted all available catches on the territory."
    play sound "sfx/game_tip.mp3"
    menu:
        "Would you like to repeat the instructions?"
        "Yes":
            jump hunting_instructions
        "No":
            jump hunting_no
label hunting_no:
    t "Alright. Let's get a move on."
    play sound "sfx/game_tip.mp3"
    "You are now {b}searching the territory ...{/b}"
    call patrol_select from _call_patrol_select

label hunting_1:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} You hear a faint rustle in the undergrowth."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You pounce, snapping a small mouse up your jaws!"
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You poke your nose into the undergrowth, only to find the scent of old prey. Your ears must have been playing tricks on you."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            "It must just be the wind. You decide to keep moving."
            call hunting_call

label hunting_2:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} You catch the faint, day-old scent of a mouse."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You manage to track the scent to a small burrow, where you ambush the rodent, killing it in one swift bite."
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You track the scent in circles before finally giving up. The mouse must have left already."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            "No use trying to track something so small. You decide to look elsewhere."
            call hunting_call

label hunting_3:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} A tiny mouse, frail with hunger, shudders at the entrance of its burrow."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You make quick work of the mouse, careful not to damage its tiny body as you bury it nearby."
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You kill the mouse but, in the process, discover it's barely even a mouthful of prey. You decide to bury it and move on."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "This mouse isn't even big enough to feed a tiny kitten. You decide to move on."
                call hunting_call

label hunting_4:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} Out of the corner of your eye, you swear, you detect a flash of movement in the bushes ..."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You dive into the branches, emerging with a tiny sparrow. It's not much, but it's better than nothing."
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You investigate, but no matter how hard you look, the branches remain curiously empty. Your eyes must have been playing tricks on you."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "Your eyes must be playing tricks on you. You decide to keep looking."
                call hunting_call

label hunting_5:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} You sense the vibration of a ground mole's heartbeat buried deep underneath the snow."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You flush the mole out of its burrow, dispatching it in one swift pounce. It's smaller than you expected, but still good."
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You dig until your paws are sore, but by the time you break ground, you can't detect the mole anymore. It seems it's already moved on."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "There's no use trying to hunt something you can't even see. You decide to keep looking."
                call hunting_call

label hunting_6:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} A tiny sparrow pecks at some seeds underneath the snow."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You launch yourself at the sparrow, killing it in a single strike. It should be good for a few mouthfulls of prey."
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "Just as you're about to pounce, the sparrow is startled off by a gust of wind."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "The sparrow is startled off by a gust of wind."
                call hunting_call

label hunting_7:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} A bright red cardinal feather gently drifts down onto the snow."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You track the source of the feather to an oblivious male cardinal. Gathering your haunches, you make quick work of it."
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "Try as you might, you cannot find the source of the feather. The cardinal must have shed it long ago."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "The feather is carried off by the breeze, vanishing from sight."
                call hunting_call


label hunting_8:
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} You hear the shrill alarm call of a chickadee."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You dive for the chickadee, silencing its call. It takes you a few moments to clear the feathers from your tongue."
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You dive for the chickadee, but your claws close around empty air as it flutters away."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "The chickadee quickly flits away."
                call hunting_call

label hunting_9:
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} You encounter a bushful of bright, red berries. If your memory serves you right, Locustleaf once told you these were edible ...?"
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > 19:
                $ proceed_counter += 1
                $ prey_caught += 1
                play sound "sfx/prey_major_win.mp3"
                "You taste a few of the berries, and they fill you with a rush of energy. {b}(+1 Proceed){/b}"
                "You meticulously collect the rest of the berries, forming a sizable pile to take back to camp with you."
                call hunting_call
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You meticulously collect the berries, forming a sizable pile to take back to camp with you."
                call hunting_call
            elif h1_int < 5:
                $ proceed_counter -= 1
                play sound "sfx/prey_major_loss.mp3"
                "You taste a few of the berries, and they sap you of your strength, filling your throat with a horrible, sickly feeling. {b}(-1 Proceed){/b}"
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "After spending ages meticulously collecting the berries, you realize that these are not, in fact, the kind of berries Locustleaf told you about."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "You decide to move on, not wanting to risk being wrong."
                call hunting_call

label hunting_10:
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} A metal twoleg trap glints in the light, filled with the tantalizing scent of food."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > 19:
                $ proceed_counter += 1
                $ prey_caught += 1
                play sound "sfx/prey_major_win.mp3"
                "You take a few bites of the twoleg food, purring as the delicious taste hits your tongue. {b}(+1 Proceed){/b}"
                "You grab the container holding the rest of the food and slip out of the trap, careful not to trigger it."
                call hunting_call
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You carefully slip in and out of the trap, snagging the container of twoleg food behind you. Hopefully, your Clanmates won't turn their up their noses!"
                call hunting_call
            elif h1_int < 5:
                $ proceed_counter -= 1
                play sound "sfx/prey_major_loss.mp3"
                "As soon as you step inside the trap, the door swings shut behind you. It takes you hours to free yourself, and by the time you do, it's nearly dark. {b}(-1 Proceed){/b}"
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You slip inside the trap, but when you try to pick up the twoleg food, it spills all over the ground. It's useless to you, now."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "You nervously move past the trap, making a mental note to tell somecat about it later."
                call hunting_call

label hunting_11:
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} A school of minnows rests in a half-frozen stream."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > 19:
                $ proceed_counter += 1
                $ prey_caught += 1
                play sound "sfx/prey_major_win.mp3"
                "You scoop minnow after helpless minnow out of the stream, thrilled by your luck. {b}(+1 Proceed){/b}"
                "You manage to collect a sizeable pile before the cold becomes too much to bare, worth at least a few mouthfulls."
                call hunting_call
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You manage to scoop a few minnows out of the stream before the cold becomes too much to bare."
                call hunting_call
            elif h1_int < 5:
                $ proceed_counter -= 1
                play sound "sfx/prey_major_loss.mp3"
                "The minnows are too fast, and now your paws are wet and freezing. It takes hours to warm them up again, and by the time you do, it's nearly dark. {b}(-1 Proceed){/b}"
                call hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You attempt to hook the minnows, but they're deceptively fast. You decide to move on."
                call hunting_call
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop())
            else:
                "The minnows dart beneath a sheet of ice, safely out of reach."
                call hunting_call

label hunting_call:
    if proceed_counter==0:
        jump patrol_over
    else:
        $ diff_counter = patrol_max - patrol_counter
        if diff_counter == 6:
            scene patrol bg 1 with fade
            "Darkness descends."
        elif diff_counter == 4:
            scene patrol bg 2 with fade
            "It's getting colder ..."
        elif diff_counter == 2:
            scene patrol bg 3 with fade
            "Night falls."
        elif diff_counter<=0:
            jump patrol_hard_over
        play sound "sfx/game_tip.mp3"
        "You are now {b}searching the territory ...{/b}"
        call patrol_select from _call_patrol_select_1


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
    if prey_caught>0 and not eaten_prey:
        t "{i}*Huff* ... *Huff* ... {/i}"
        "Talonclaw is hungry and exhausted. The prey he caught is looking mighty tempting ..."
        menu:
            "Would you like to exchange one of your [prey_caught] catches for {b}2 extra Proceeds?{/b}"
            "Yes":
                $ proceed_counter += 2
                $ patrol_max += 2
                $ prey_caught -= 1
                $ eaten_prey = True
                "Talonclaw guiltily scarfs down a piece of prey."
                "Some energy restored, he heads back onto the territory."
                call hunting_call
            "No":
                jump patrol_hard_over
    else:
        jump patrol_hard_over
    call screen gameUI

label patrol_hard_over:
    t "It's getting dark ... I should probably head back to camp."
    call screen gameUI
