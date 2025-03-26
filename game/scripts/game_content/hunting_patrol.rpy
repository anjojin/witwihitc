label hunting_start:
    $ proceed_counter = 3
    $ currently_in = "outside"
    $ already_patrolled = True
    call shuffle_patrols from _call_shuffle_patrols
    if quest_favorite_prey.started:
        $ talon_chance = 13 - (talon_sun_bonus/2)
    else:
        $ talon_chance = 13 - talon_clan_bonus
    scene patrol bg with fade
    $ quick_menu = True
    stop music fadeout 1.0
    play music "music/ES_Naranjas en Diciembre - Vendla.mp3" loop
    if quest_babysitting.started:
        play audio "sfx/slideup.mp3"
        show cloverpaw_roll_right with easeinright
        c "Finally, fresh air!"
        c "That's it, I'm never going back to camp. This is officially the start of my new life as a rogue."
        c "From now on, call me ... 'Clovetopher.'"
        play audio "sfx/slideup.mp3"
        show redpaw_left with easeinleft
        r "Could you stop kidding around?"
        r "If we don't take this seriously, the warriors are never going to trust us with another hunt."
        c "Hmph. You clan cats are always so uptight."
        t "Alright, everyone, focus up. We're about to get started."
        play audio "sfx/slideup.mp3"
        hide cloverpaw_roll_right with moveoutright
        play audio "sfx/slideup.mp3"
        hide redpaw_left with moveoutleft
    else:
        t "So cold ... It feels like my paws are about to snap off."
        if talon_sun_bonus > 2:
            t "I can't even imagine how much pain Sunshadow must be in, digging that grave out there all by himself."
            t "Just hang on a little while longer, buddy. I'll be there with you before you know it."
        elif talon_clan_bonus > 2 and quest_feed_deputy.started:
            t "Still, Briarstar is counting on me to bring something back for Pouncetail. The whole Clan is."
            t "I'd better get a move on. For everycat's sake."
        else:
            t "Let's hope I manage to catch something that's worth all this trouble."

label hunting_instructions:    
    play sound "sfx/game_tip.mp3"
    "Talonclaw is now {b}hunting:{/b} scouring the territory for the sights, sounds, or scents of possible prey."
    play sound "sfx/game_tip.mp3"
    "Food is scarce, so it may take a few seconds for him to find anything."
    play sound "sfx/game_tip.mp3"
    "Once he does, he can either {b}proceed{/b} or {b}not proceed{/b} to attempt the catch."
    play sound "sfx/game_tip.mp3"
    if quest_babysitting.started:
        "If he {b}proceeds,{/b} he will either succeed at making the catch, or fail."
        play sound "sfx/game_tip.mp3"
        "If he {b}does not proceed,{/b} one of the {b}apprentices{/b} will make the attempt."
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
        "Would you like to hear the instructions again?"
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
    $ prey_potential = 1
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
                call hunting_call from _call_hunting_call
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You poke your nose into the leaves, but there's nothing there. Your ears must have been playing tricks on you."
                call hunting_call from _call_hunting_call_1
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            "It must just be the wind. You decide to keep moving."
            call hunting_call from _call_hunting_call_2

label hunting_2:
    $ prey_potential = 1
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
                call hunting_call from _call_hunting_call_3
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You track the scent in circles before finally giving up. It's clear that the mouse is long gone."
                call hunting_call from _call_hunting_call_4
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            "No use trying to track something so tiny. You decide to look elsewhere."
            call hunting_call from _call_hunting_call_5

label hunting_3:
    $ prey_potential = 1
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
                call hunting_call from _call_hunting_call_6
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You kill the mouse but, in the process, discover it's barely worth a mouthful of prey. You decide to bury it and move on."
                call hunting_call from _call_hunting_call_7
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "This mouse isn't even big enough to feed a tiny kitten. Best not to waste your time."
                call hunting_call from _call_hunting_call_8

label hunting_4:
    $ prey_potential = 1
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
                call hunting_call from _call_hunting_call_9
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You investigate, but no matter how hard you look, the branches remain curiously empty. Your eyes must have been playing tricks on you."
                call hunting_call from _call_hunting_call_10
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "Your eyes must be playing tricks on you. You decide to keep looking."
                call hunting_call from _call_hunting_call_11

label hunting_5:
    $ prey_potential = 1
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
                call hunting_call from _call_hunting_call_12
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You dig until your paws are sore, but by the time you break ground, the mole is already gone."
                call hunting_call from _call_hunting_call_13
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "There's no use trying to hunt something you can't even see. You decide to keep looking."
                call hunting_call from _call_hunting_call_14

label hunting_6:
    $ prey_potential = 1
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
                call hunting_call from _call_hunting_call_15
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "Just as you're about to pounce, the sparrow is startled off by a gust of wind."
                call hunting_call from _call_hunting_call_16
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "The sparrow is startled off by a gust of wind."
                call hunting_call from _call_hunting_call_17

label hunting_7:
    $ prey_potential = 1
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} A bright red cardinal feather flutters in the breeze, trapped against some branches."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You track the source of the feather to a plump male cardinal. Gathering your haunches, you make quick work of it."
                call hunting_call from _call_hunting_call_18
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "Try as you might, you can't track down the source of the feather."
                call hunting_call from _call_hunting_call_19
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "A strong wind carries off the feather."
                call hunting_call from _call_hunting_call_20


label hunting_8:
    $ prey_potential = 1
    play sound "sfx/prey_minor_encounter.mp3"
    "{b}(!){/b} You hear the shrill alarm call of a chickadee."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You dive for the chickadee, purring as the prey-taste floods your tongue."
                call hunting_call from _call_hunting_call_21
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You dive for the chickadee, but your claws close around empty air as it flutters away."
                call hunting_call from _call_hunting_call_22
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "The chickadee flits away."
                call hunting_call from _call_hunting_call_23

label hunting_9:
    $ prey_potential = 1.5
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} You encounter a bushful of bright, red berries. If your memory serves you right, Locustleaf once told you these were edible ...?"
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance + 5:
                $ proceed_counter += 1
                $ prey_caught += 1
                play sound "sfx/prey_major_win.mp3"
                "You taste a few of the berries, and they fill you with a rush of energy. {b}(+1 Proceed){/b}"
                "You meticulously collect the rest, forming a sizable pile to take back to camp with you."
                call hunting_call from _call_hunting_call_24
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You meticulously collect the berries, forming a sizable pile to take back to camp with you."
                call hunting_call from _call_hunting_call_25
            elif h1_int < 5:
                $ proceed_counter -= 1
                play sound "sfx/prey_major_loss.mp3"
                "You taste a few of the berries, and they sap you of your strength, filling your throat with a horrible, sickly feeling. {b}(-1 Proceed){/b}"
                call hunting_call from _call_hunting_call_26
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "After spending ages meticulously collecting the berries, you realize that these are not, in fact, the kind of berries Locustleaf told you about."
                call hunting_call from _call_hunting_call_27
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "You decide to move on."
                call hunting_call from _call_hunting_call_28

label hunting_10:
    $ prey_potential = 1.5
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} A metal twoleg trap glints in the light, filled with the tantalizing scent of food."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance + 5:
                $ proceed_counter += 1
                $ prey_caught += 1
                play sound "sfx/prey_major_win.mp3"
                "You take a few bites of the twoleg food, purring as the delicious taste hits your tongue. {b}(+1 Proceed){/b}"
                "You grab the container and slip out, careful not to trigger the trap."
                call hunting_call from _call_hunting_call_29
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You carefully slip in and out of the trap, snagging the container of twoleg food behind you. Hopefully, your Clanmates won't turn up their noses at it!"
                call hunting_call from _call_hunting_call_30
            elif h1_int < 5:
                $ proceed_counter -= 1
                play sound "sfx/prey_major_loss.mp3"
                "As soon as you step inside the trap, the door swings shut behind you. It takes you hours to free yourself, and by the time you do, it's nearly dark. {b}(-1 Proceed){/b}"
                call hunting_call from _call_hunting_call_31
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You slip inside the trap, but when you try to pick up the twoleg food, it spills all over the ground."
                call hunting_call from _call_hunting_call_32
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "You nervously move past the trap, making a mental note to tell somecat about it later."
                call hunting_call from _call_hunting_call_33

label hunting_11:
    $ prey_potential = 1.5
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} A school of minnows rests in a half-frozen stream."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance + 5:
                $ proceed_counter += 1
                $ prey_caught += 1
                play sound "sfx/prey_major_win.mp3"
                "You scoop minnow after helpless minnow out of the stream, thrilled by your luck. {b}(+1 Proceed){/b}"
                "You manage to collect a sizeable pile before the cold becomes too much to bare."
                call hunting_call from _call_hunting_call_34
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You manage to scoop a few minnows out of the stream before the cold becomes too much to bare."
                call hunting_call from _call_hunting_call_35
            elif h1_int < 5:
                $ proceed_counter -= 1
                play sound "sfx/prey_major_loss.mp3"
                "The minnows are too fast, and now your paws are wet and freezing. It takes hours to warm them up again, and by the time you do, it's nearly dark. {b}(-1 Proceed){/b}"
                call hunting_call from _call_hunting_call_36
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You attempt to hook the minnows, but they're deceptively fast. You decide to move on."
                call hunting_call from _call_hunting_call_37
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "The minnows dart beneath a sheet of ice, out of reach."
                call hunting_call from _call_hunting_call_38

label hunting_12:
    $ prey_potential = 2
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!!){/b} You spot a flock of buzzards clustered around a fresh carcass."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 2
                play sound "sfx/prey_major_win.mp3"
                "The buzzards, docile and overfed, seem happy enough to share the kill. You tear off a huge chunk of meat, almost too large to carry back to camp."
                call hunting_call from _call_hunting_call_39
            else:
                play sound "sfx/prey_major_loss.mp3"
                "The buzzards beat you back in a swarm of beaks and wings."
                if prey_caught == 0:
                    $ proceed_counter -= 1
                    "You manage to escape unscathed, but it takes you a few moments to recover from the encounter. {b}(-1 Proceed){/b}"
                else:
                    $ prey_caught = 0
                    "When you return to the spot where your prey was buried, you discover all of your catches are gone."
                    t "Fox-dung!"
                call hunting_call from _call_hunting_call_40
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "Best not to get tangled up with buzzards. You wrinkle your nose and move ahead."
                call hunting_call from _call_hunting_call_41

label hunting_13:
    $ prey_potential = 1.5
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} High up in the branches of a tree, you notice a cluster of leaves and twigs: a gray squirrel's nest."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance + 5:
                $ prey_caught += 2
                play sound "sfx/prey_major_win.mp3"
                "You carefully pick your way up the tree and ambush the nest. Two plump squirrels become your new kills."
                call hunting_call from _call_hunting_call_42
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You carefully pick your way up the tree and ambush the nest. One skinny squirrel becomes your new kill."
                call hunting_call from _call_hunting_call_43
            elif h1_int < 5:
                $ proceed_counter -= 1
                play sound "sfx/prey_major_loss.mp3"
                "As you scramble up the tree, a dead branch gives beneath your paws. You slam to the ground, struggling to catch your breath. {b}(-1 Proceed){/b}"
                call hunting_call from _call_hunting_call_44
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You carefully pick your way up the tree, only for the nest to collapse beneath your paws. It's empty."
                call hunting_call from _call_hunting_call_45
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "You decide to move on."
                call hunting_call from _call_hunting_call_46


label hunting_14:
    $ prey_potential = 2
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!!){/b} You spot a mighty hawk feasting on the mostly-intact remains of a fresh kill."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance:
                $ prey_caught += 2
                play sound "sfx/prey_major_win.mp3"
                "You catch the hawk by surprise, startling it into the air."
                "As it flies off, you inspect its meal: a massive squirrel, large enough to feed two warriors!"
                call hunting_call from _call_hunting_call_47
            else:
                play sound "sfx/prey_major_loss.mp3"
                if prey_caught == 0:
                    $ proceed_counter -= 1
                    "The furious hawk chases you across the territory, talons outstretched. By the time it leaves you alone, it's already nearly dark. {b}(-1 Proceed){/b}"
                else:
                    $ prey_caught = 0
                    "The furious hawk chases you across the territory, lingering over where your prey was buried. To save your pelt, you're forced to abandon your catches."
                    t "Fox-dung!"
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "The hawk takes off into the air."
                call hunting_call from _call_hunting_call_48

label hunting_15:
    $ prey_potential = 1.5
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!){/b} A plump pigeon startles out of the bushes!"
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > 17:
                $ prey_caught += 2
                play sound "sfx/prey_major_win.mp3"
                "Out of pure instinct, you leap up and grab the pigeon out of the air!"
                "It's the fattest bird you've seen in moons. You purr, thinking of all the cats it will feed."
                call hunting_call from _call_hunting_call_49
            elif h1_int > talon_chance:
                $ prey_caught += 1
                play sound "sfx/prey_minor_win.mp3"
                "You barely to snag the pigeon with the edge of your claw. It's a messy kill, and a lot of the meat is spoiled, but enough should be intact to feed one cat."
                call hunting_call from _call_hunting_call_50
            elif h1_int < 7:
                play sound "sfx/prey_major_loss.mp3"
                $ proceed_counter -= 1
                "You attempt to pounce but falter, slamming into the ground hard enough to see stars. It takes you a few moments to catch your breath. {b}(-1 Proceed){/b}"
                call hunting_call from _call_hunting_call_51
            else:
                play sound "sfx/prey_minor_loss.mp3"
                "You attempt to pounce but falter, barely managing to stay upright as the pigeon whisks away into the air."
                call hunting_call from _call_hunting_call_52
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "The pigeon whisks away into the air."
                call hunting_call from _call_hunting_call_53

label hunting_16:
    $ prey_potential = 2
    play sound "sfx/prey_major_encounter.mp3"
    "{b}(!!!){/b} A lone crow, almost as large as you are, preens its jet-black feathers in the branches of a tree."
    menu:
        "Proceed (x[proceed_counter])" if proceed_counter > 0:
            $ h1_int = renpy.random.randint(1,20)
            $ proceed_counter -= 1
            if h1_int > talon_chance+5:
                $ prey_caught += 2
                play sound "sfx/prey_major_win.mp3"
                "You wait patiently until the crow flies to the ground, then tackle it in a whirl of black feathers. It's so much prey, you can barely haul it back to camp!"
                call hunting_call from _call_hunting_call_54
            else:
                play sound "sfx/prey_major_loss.mp3"
                if prey_caught == 0:
                    $ proceed_counter -= 1
                    "You scrabble up the tree, but just as you're about to pounce, the crow flutters to the ground."
                    "You give chase, crow eluding you at every turn, until, finally, winded and panting, the crow caws at you once and flies away. {b}(-1 Proceed){/b}"
                else:
                    $ prey_caught = 0
                    "You scrabble up the tree, but just as you're about to pounce, the crow flutters to the ground, where you see a mob of its friends surrounding your buried prey."
                    "By the time you make it down the tree, they've already taken off with your hard-earned kills, a flurry of caws in their wake."
                call hunting_call from _call_hunting_call_55
        "Do not proceed":
            if len(training_with) > 0:
                $ renpy.jump(training_with.pop(0))
            else:
                "The crow flies away."
                call hunting_call from _call_hunting_call_56

label hunting_call:
    if proceed_counter<=0:
        jump patrol_over
    else:
        $ diff_counter = patrol_max - patrol_counter
        if quest_babysitting.started:
            if diff_counter == 10:
                scene patrol bg 1 with fade
                "Darkness descends."
            elif diff_counter == 7:
                scene patrol bg 2 with fade
                "It's getting colder ..."
            elif diff_counter == 4:
                scene patrol bg 3 with fade
                "Night falls."
            elif diff_counter<=0:
                jump patrol_hard_over
        else:
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
    show redpaw_center with easeinright
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    r "I got it!"
    hide redpaw_center with moveoutleft
    if prey_potential == 1:
        if h1_int > red_hunting_chance:
            $ prey_caught += 1
            play sound "sfx/prey_minor_win.mp3"
            "Redpaw makes the catch!"
            jump red_hunting_success
        else:
            play sound "sfx/prey_minor_loss.mp3"
            "Redpaw trips over his own paws, landing unceremoniously in the dirt."
            jump red_hunting_fail
    elif prey_potential == 1.5:
        if h1_int > red_hunting_chance + 5:
            $ proceed_counter += 1
            $ prey_caught += 1
            play sound "sfx/prey_major_win.mp3"
            "With zero hesitation, Redpaw dives! His act of courage fills the whole patrol with a rush of energy. {b}(+1 Proceed){/b}"
            jump red_hunting_success
        elif h1_int > red_hunting_chance:
            $ prey_caught += 1
            play sound "sfx/prey_minor_win.mp3"
            "Redpaw makes the catch!"
            jump red_hunting_success
        elif h1_int < 7:
            $ proceed_counter -= 1
            play sound "sfx/prey_major_loss.mp3"
            "Redpaw dives with zero hesitation, only to slam into the ground, yowling in pain. It takes a few moments for him to recover. {b}(-1 Proceed){/b}"
            jump red_hunting_fail
        else:
            play sound "sfx/prey_minor_loss.mp3"
            "Redpaw trips over his own paws, landing unceremoniously in the dirt."
            jump red_hunting_fail
    else:
        if h1_int>red_hunting_chance:
            $ prey_caught += 2
            play sound "sfx/prey_major_win.mp3"
            "Redpaw dives, securing a huge catch!"
            jump red_hunting_success
        else:
            play sound "sfx/prey_major_loss.mp3"
            if prey_caught == 0:
                $ proceed_counter -= 1
                "Redpaw dives with zero hesitation, only to slam into the ground, yowling in pain. It takes a few moments for him to recover. {b}(-1 Proceed){/b}"
            else:
                $ prey_caught = 0
                "By the time you return to where your catches were buried, all of them are gone."
            jump red_hunting_fail
    
label hunting_lily: 
    $ h1_int = renpy.random.randint(1,20)
    show lilypaw_center with easeinleft
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    li "{i}*Whoosh*{/i}"
    hide lilypaw_center with moveoutright
    if prey_potential == 1:
        if h1_int > lily_hunting_chance:
            $ prey_caught += 1
            play sound "sfx/prey_minor_win.mp3"
            "Lilypaw makes the catch!"
            jump lily_hunting_success
        else:
            play sound "sfx/prey_minor_loss.mp3"
            "Lilypaw creeps forward, but hesitates at the last moment, allowing the catch to get away."
            jump lily_hunting_fail
    elif prey_potential == 1.5:
        if h1_int > lily_hunting_chance + 5:
            $ proceed_counter += 1
            $ prey_caught += 1
            play sound "sfx/prey_major_win.mp3"
            "Lilypaw makes the catch with such grace and precision, it fills the whole patrol with a rush of energy! {b}(+1 Proceed){/b}"
            jump lily_hunting_success
        elif h1_int > lily_hunting_chance:
            $ prey_caught += 1
            play sound "sfx/prey_minor_win.mp3"
            "Lilypaw makes the catch!"
            jump lily_hunting_success
        elif h1_int < 7:
            $ proceed_counter -= 1
            play sound "sfx/prey_major_loss.mp3"
            "As Lilypaw creeps forward, the snow gives way beneath her paws. It takes hours for the patrol to free her. {b}(-1 Proceed){/b}"
            jump lily_hunting_fail
        else:
            play sound "sfx/prey_minor_loss.mp3"
            "Lilypaw creeps forward, but hesitates at the last moment, allowing the catch to get away."
            jump lily_hunting_fail
    else:
        if h1_int>lily_hunting_chance:
            $ prey_caught += 2
            play sound "sfx/prey_major_win.mp3"
            "Lilypaw dispatches a huge catch, large enough to feed two cats, with grace and precision!"
            jump lily_hunting_success
        else:
            play sound "sfx/prey_major_loss.mp3"
            if prey_caught == 0:
                $ proceed_counter -= 1
                "As Lilypaw creeps forward, the snow gives way beneath her paws. It takes hours for the patrol to free her. {b}(-1 Proceed){/b}"
            else:
                $ prey_caught = 0
                "As Lilypaw creeps forward, the snow gives way beneath her paws. It takes hours for the patrol to free her."
                "When you finally finish, you return to where your catches are buried, only to discover all of them are gone."
            jump lily_hunting_fail

label hunting_fawn: 
    $ h1_int = renpy.random.randint(1,20)
    show fawnpaw_roll_center with easeinright
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    fa "Mrow!"
    hide fawnpaw_roll_center with moveoutleft
    if prey_potential == 1:
        if h1_int > fawn_hunting_chance:
            $ prey_caught += 1
            play sound "sfx/prey_minor_win.mp3"
            "Fawnpaw makes the catch!"
            jump fawn_hunting_success
        else:
            play sound "sfx/prey_minor_loss.mp3"
            "Fawnpaw pounces a bit prematurely, losing the catch."
            jump fawn_hunting_fail
    elif prey_potential == 1.5:
        if h1_int > fawn_hunting_chance + 5:
            $ proceed_counter += 1
            $ prey_caught += 1
            play sound "sfx/prey_major_win.mp3"
            "Fawnpaw makes the catch so quickly, it fills the whole patrol with a rush of energy! {b}(+1 Proceed){/b}"
            jump fawn_hunting_success
        elif h1_int > fawn_hunting_chance:
            $ prey_caught += 1
            play sound "sfx/prey_minor_win.mp3"
            "Fawnpaw makes the catch!"
            jump fawn_hunting_success
        elif h1_int < 7:
            $ proceed_counter -= 1
            play sound "sfx/prey_major_loss.mp3"
            "Fawnpaw is so focused on the catch, she creeps right into a thicket of brambles. It takes hours for the patrol to free her. {b}(-1 Proceed){/b}"
            jump fawn_hunting_fail
        else:
            play sound "sfx/prey_minor_loss.mp3"
            "Fawnpaw pounces a bit prematurely, losing the catch."
            jump fawn_hunting_fail
    else:
        if h1_int>fawn_hunting_chance:
            $ prey_caught += 2
            play sound "sfx/prey_major_win.mp3"
            "Fawnpaw trots back with a catch so large, she can barely carry it!"
            jump fawn_hunting_success
        else:
            play sound "sfx/prey_major_loss.mp3"
            if prey_caught == 0:
                $ proceed_counter -= 1
                "Fawnpaw is so focused on the catch, she creeps right into a thicket of brambles. It takes hours for the patrol to free her. {b}(-1 Proceed){/b}"
            else:
                $ prey_caught = 0
                "Fawnpaw is so focused on the catch, she creeps right into a thicket of brambles. It takes hours for the patrol to free her."
                "When you finally finish, you return to where your catches are buried, only to discover all of them are gone."
            jump fawn_hunting_fail
    
label hunting_clover: 
    show cloverpaw_center with easeinleft
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    c "This one's mine!"
    hide cloverpaw_center with moveoutright
    play sound "sfx/prey_major_win.mp3"
    "Cloverpaw charges in headfirst, yowling a battle cry as she pounces on the prey!"
    jump clover_hunting_success

label red_hunting_success:
    show redpaw_left with easeinleft
    show cloverpaw_sit_right with easeinright
    c "Wow, Red! I didn't know you had it in you!"
    r "Hehe ... Just doing it like we practiced."
    hide redpaw_left with moveoutleft
    hide cloverpaw_sit_right with moveoutright
    call hunting_call from _call_hunting_call_57

label red_hunting_fail:
    show redpaw_center with easeinleft
    r "Fox-dung!"
    t "Language."
    r "Sorry."
    t "It's okay. There's still plenty of daylight."
    t "Let's see what else we can find."
    hide redpaw_center with moveoutleft
    call hunting_call from _call_hunting_call_58

label lily_hunting_success:
    show lilypaw_sit_left with easeinleft
    t "StarClan, Lilypaw, where'd you learn to pounce like that?"
    li "Heh ... I dunno ... Just my training, I guess."
    t "That's more than just training. You're a natural talent!"
    show cloverpaw_roll_right with easeinright
    c "Yeah, don't be shy, Lilypaw!"
    c "She always does the best at our hunting practices."
    t "Is that so?"
    t "You must get it from your father, then. Squirrelpelt was always the best hunter in the Clan."
    li "Really?"
    t "Oh, yeah! I once saw that cat tear a swallow five fox-lengths out of the air!"
    t "You've got his blood in you, kitto. I just know he would be proud."
    li "{i}*Lilypaw beams with pride.*{/i}"
    hide lilypaw_sit_left with moveoutleft
    hide cloverpaw_roll_right with moveoutright
    call hunting_call from _call_hunting_call_59

label lily_hunting_fail:
    show lilypaw_sit_left with easeinleft
    li "..."
    show redpaw_right with easeinright
    show fawnpaw_right with easeinright
    fa "Aw, mouse-dung, Lilypaw, what happened? You were doing so well in hunting practice!"
    r "I'm telling you, she's too young. This is why we shouldn't have brought her along."
    r "We're practically warriors while she's barely out of the nursery."
    show cloverpaw_far_right with easeinright
    c "You two mouse-brains better shut up before I claw you!"
    c "It's okay, Lilypaw. You'll get it next time."
    li "..."
    hide cloverpaw_far_right with moveoutright
    hide fawnpaw_right with moveoutright
    hide redpaw_right with moveoutright
    hide lilypaw_sit_left with moveoutleft
    call hunting_call from _call_hunting_call_60

label fawn_hunting_success:
    show fawnpaw_left with easeinleft
    fa "Haha! Yes! I did it!"
    fa "I'm going to give this one to Flipcloud. It's his favorite."
    show redpaw_right with easeinright
    r "I always thought robins were Dad's favorite?"
    fa "Oh, yeah ... Maybe this is second favorite, then."
    r "Yeah. Well. It doesn't really matter."
    r "He's not exactly conscious to enjoy it, anyway."
    show cloverpaw_far_right with easeinleft
    c "Redpaw!"
    r "What? I'm just saying!"
    c "Grr! Why are you so --"
    fa "It's okay, Cloverpaw."
    fa "This will make Flipcloud feel better. I just know it."
    r "..."
    hide cloverpaw_far_right with moveoutleft
    hide redpaw_right with moveoutleft
    hide fawnpaw_left with moveoutright
    call hunting_call from _call_hunting_call_61

label fawn_hunting_fail:
    show fawnpaw_left with easeinleft
    fa "{i}No!!!{/i}"
    t "Whoa, Fawnpaw! Calm down! It's alright!"
    fa "It's not alright!"
    fa "I failed."
    t "Cats fail all the time. It's just part of being a warrior."
    fa "You don't understand."
    fa "My father's been sick in the medicine den for ages. That piece of prey was supposed to be for him."
    fa "Redpaw and I haven't been allowed to visit, and StarClan knows how often they've been feeding him in there."
    fa "I just thought ... If I caught something ... Maybe it could help him get better."
    t "I'm so sorry."
    show redpaw_right with easeinright
    r "Yeah, cheer up, Fawnpaw. Flipcloud's so far gone, that stupid little catch probably wouldn't have made much of a difference anyway."
    fa "*Gasp*"
    t "Redpaw!"
    fa "How could you say something like that?"
    fa "He's your father, too!"
    r "Yeah, well, the way things are going, he won't be for too much longer."
    r "Nothing we can do about it now, except keep moving forward."
    fa "..."
    fa "........."
    fa "... Let's just keep hunting."
    t "Are you sure?"
    fa "Would you rather stand around here bickering at each other?"
    fa "We're losing light. Let's go."
    hide fawnpaw_left with moveoutleft
    hide redpaw_right with moveoutright
    call hunting_call from _call_hunting_call_62

label clover_end_patrol:
    stop music fadeout 2.0
    show lilypaw_stand_left with easeinleft
    show redpaw_right with easeinright
    show fawnpaw_right with easeinright
    if prey_caught >0:
        fa "Wow, you're on fire, Talonclaw!"    
        r "Yeah, leave some prey for the rest of us."
        t "Hehe. Thanks, kittos."
    else:
        fa "I guess my mentor wasn't wrong. Prey really is scarce out here ..."
        t "Don't give up yet. We still have a little time left to turn things around."
    t "Say, where's Cloverpaw? She seemed the most excited to hunt out of any of you."
    fa "I think she's fallen behind a little."
    r "Probably too busy bossing the rest of us around to keep up ..."
    fa "Oh, here she comes, now!"
    show cloverpaw_stand_left with easeinleft
    fa "Hey, Cloverpaw!"
    c "{i}*Pant* ... *Pant* ...{/i}"
    fa "Where have you been? We've been waiting on you."
    r "Yeah. You seem a little out of shape."
    c "{i}*Pant* ... *Pant* ... *Pant* ...{/i}"
    t "... Cloverpaw?"
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    hide cloverpaw_stand_left
    show cloverpaw_sit_left
    c "{i}*Cough* *Cough*{/i}"
    play music "music/ES_Saint Valentine - Vendla.mp3" loop
    fa "*Gasp*"
    r "Great StarClan ..."
    c "{i}*Hack*{/i} I-I'm fine, guys -- {i}*Gasp*{/i} -- I just got some dust in my throat!"
    li "It all makes sense, now."
    li "The sneezing. The slowness. Now, the coughing, too."
    li "She's become infected."
    c "W-What? No, I'm not infected!"
    c "You guys have spent all day with me! I'm fine!"
    fa "Cloverpaw ..."
    c "W-Why's everyone looking at me like that?"
    c "C'mon, let's keep hunting! There's still plenty of li ..."
    c "Li ..."
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    c "... {i}*Cough* *Cough* *Hack* *Cough*{/i}"
    t "Okay. I think I've heard enough."
    t "I'm taking you all back to camp."
    c "{i}*Wheeze*{/i} -- W-What?! No!"
    t "Stay close, everyone."
    c "B-But --"
    t "Especially you, Cloverpaw."
    t "We're leaving."
    c "..."
    hide fawnpaw_right with moveoutright
    hide redpaw_right with moveoutright
    hide cloverpaw_sit_left with moveoutleft
    hide lilypaw_stand_left with moveoutleft
    jump patrol_over_quests

label clover_hunting_success:
    stop music fadeout 2.0
    show lilypaw_stand_left with easeinleft
    show cloverpaw_stand_left with easeinleft
    show redpaw_right with easeinright
    show fawnpaw_right with easeinright
    c "{i}*Pant* ... *Pant* ...{/i}"
    fa "Alright, Cloverpaw!"    
    r "Not bad for a rogue, 'Clovetopher.'"
    t "Yes, Cloverpaw, very well done!"
    c "{i}*Pant* ... *Pant* ... *Pant* ...{/i}"
    t "... Cloverpaw?"
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    hide cloverpaw_stand_left
    show cloverpaw_sit_left
    c "{i}*Cough* *Cough*{/i}"
    play music "music/ES_Saint Valentine - Vendla.mp3" loop
    fa "*Gasp*"
    r "Great StarClan ..."
    c "{i}*Hack*{/i} I-I'm fine, guys -- {i}*Gasp*{/i} -- I just got some dust in my throat!"
    li "It all makes sense, now."
    li "The sneezing. The slowness. Now, the coughing, too."
    li "She's become infected."
    c "W-What? No, I'm not infected!"
    c "You guys have spent all day with me! I'm fine!"
    fa "Cloverpaw ..."
    c "W-Why's everyone looking at me like that?"
    c "C'mon, let's keep hunting! There's still plenty of li ..."
    c "Li ..."
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    c "... {i}*Cough* *Cough* *Hack* *Cough*{/i}"
    t "Okay. I think I've heard enough."
    t "I'm taking you all back to camp."
    c "{i}*Wheeze*{/i} -- W-What?! No!"
    t "Gather your catches, everyone."
    t "Except you, Cloverpaw. You bury yours here."
    c "But that's perfectly good prey!"
    t "Leave it."
    c "..."
    hide fawnpaw_right with moveoutright
    hide redpaw_right with moveoutright
    hide cloverpaw_sit_left with moveoutleft
    hide lilypaw_stand_left with moveoutleft
    jump patrol_over_quests

label patrol_over:
    if quest_babysitting.started:
        jump clover_end_patrol
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
                call hunting_call from _call_hunting_call_63
            "No":
                jump patrol_hard_over
    else:
        jump patrol_hard_over

label patrol_hard_over:
    t "It's getting dark ... I should probably head back to camp."

label patrol_over_quests:
    play audio "sfx/quest_unlocked.mp3"
    "{b}Patrol Completed.{/b}"
    if quest_babysitting.started:
        $ quest_babysitting.started = False
        $ quest_babysitting.completed = True
        play audio "sfx/quest_unlocked.mp3"
        "{b}Quest Completed:{/b} Adult Supervision"
    elif prey_caught > 0:
        if quest_favorite_prey.started:
            $ quest_favorite_prey.started = False
            $ quest_favorite_prey.completed= True
            play audio "sfx/quest_unlocked.mp3"
            "{b}Quest Completed:{/b} Favorite Prey"

label patrol_over_prey:
    play audio "sfx/quest_unlocked.mp3"
    if prey_caught == 1:
        "You return to camp with {b}[prey_caught]{/b} piece of prey."
    else:
        "You return to camp with {b}[prey_caught]{/b} pieces of prey."
    jump cl3