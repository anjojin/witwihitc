label md1:
    $ med_den_visited = True
    stop music fadeout 0.5
    play music "music/ES_Enough by Now - Headlund.mp3" loop
    if not quest_medical_opinion.started or quest_medical_opinion.completed:
        scene med_den_ext with fade
        t "The medicine den."
        t "Locustleaf would have a fit if I went in there without a good reason."
        t "Especially since I'm one of the only healthy warriors left ..."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
        else:
            call screen gameUI
    
    else:
        scene med_den_bg with fade
        show screen gameUI
        stop music fadeout 0.5
        play music "music/ES_Enough by Now - Headlund.mp3" loop
        show locustleaf with moveinright
        show maplebreeze with moveinleft
        m "{i}*Wheeze*{/i} I-I'm not ... {i}*Wheeze*{/i} I'm not that sick, Locustleaf ... {i}*Wheeze*{/i} Honest ..."
        m "These herbs should go to ... {i}*Wheeze*{/i} somecat who really ... {i}*Wheeze*{/i} needs them ..."
        l "Shut up and eat your catmint."
        t "Locustleaf!"
        l "Talonclaw?"
        l "What have I told you? The medicine den is for emergencies only!"
        t "But it {i}is{/i} an emergency!"
        t "Featherkit, she's gotten sick, and --"
        m "*Gasp* Oh, no! Will she be alright?"
        l "Stay out of this, Maplebreeze."
        l "Featherkit ... Has she stopped eating?"
        t "Yes."
        l "And developed a cough?"
        t "Yes! Now, come on, we need to hurry! Do you have anything I can --"
        l "She'll be dead by sundown."
        t "What?!"
        m "*Gasp*"
        l "I'm sorry. There's nothing more I can do."
        l "A cat her age, in these conditions, doesn't stand a chance against any sort of cough."
        l "Herbs, or no herbs."
        t "No, no, that can't be right."
        t "She just got sick this morning! There must still be some time to save her!"
        m "{i}Wheeze{/i} ... Yes, Locustleaf, surely there's still something --"
        l "Quiet, Maplebreeze!"
        m "..."
        l "... Okay. Maybe, if I had herbs to spare, I would be more inclined to agree with you."
        l "But, in case you haven't noticed, this den is full of the sick and dying, inclduing our own deputy."
        t "But Featherkit's so small -- she'll only need a tiny scrap of catmint!"
        t "Maplebreeze was just saying she didn't need hers!"
        m "Yes ... {i}wheeze{/i}... I'd be happy to spare a little ..."
        l "Maplebreeze is a {i}medicine cat.{/i}"
        l "If these herbs could go towards saving one life, versus saving Maplebreeze, who will go on to save dozens ..."
        l "Well, I'll let you do the math on that one."
        l "Need I remind you how much worse things got for ThunderClan after we lost our last apprentice?"
        t "..."
        t "... What if I could find more?"
        l "Excuse me?"
        t "More catmint. Then, could you spare some for Featherkit?"
        l "Ha! If you find any catmint on that territory, you could line your nest with it, for all I care."
        l "Better yet, you could find a whole branch and spend the afternoon hitting yourself over the head with it."
        if quest_favorite_prey.started:
            l "It'd probably be a better use of your time."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} hunting for catmint means Talonclaw will no longer be able to complete the following questline: {b}Burial Rites.{/b}"
            menu:
                "How would you like to proceed?"
                "Stick with burying Dapplefeather":
                    jump md1_give_up
                "Switch to finding catmint":
                    jump md1_accept_challenge

        elif quest_feed_deputy.started:
            l "It'd probably be a better use of your time."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} hunting for catmint means Talonclaw will no longer be able to complete the following quest: {b}Feed the Deputy.{/b}"
            menu:
                "How would you like to proceed?"
                "Stick with hunting for Pouncetail":
                    jump md1_give_up
                "Switch to finding catmint":
                    jump md1_accept_challenge

        elif quest_babysitting.started:
            l "It'd probably be a better use of your time."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} hunting for catmint means Talonclaw will no longer be able to complete the following quest: {b}Babysitting.{/b}"
            menu:
                "How would you like to proceed?"
                "Stick with patrolling with the apprentices":
                    jump md1_accept_challenge
                "Switch to finding catmint":
                    jump md1_give_up
        else:
            menu:
                l "It'd probably be a better use of your time."
                "Challenge Accepted":
                    jump md1_accept_challenge
                "Give Up":
                    jump md1_give_up

label md1_accept_challenge:
    $ quest_gather_herbs.started = True
    if quest_favorite_prey.started:
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Questline Cancelled:{/b} Burial Rites"
        if quest_crocus.started:
            $ quest_crocus.started = False
            $ quest_crocus.cancelled = True
        $ quest_favorite_prey.started = False
        $ quest_favorite_prey.cancelled = True
        if quest_nesting_material.started:
            $ quest_nesting_material.started = False
            $ quest_nesting_material.cancelled = True
    if quest_feed_deputy.started:
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Quest Cancelled:{/b} Feed the Deputy"
        $ quest_feed_deputy.started = False
        $ quest_feed_deputy.cancelled = True
    if quest_babysitting.started:
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Quest Cancelled:{/b} Babysitting"
        $ quest_babysitting.started = False
        $ quest_babysitting.cancelled = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Gather Herbs"
    t "Fine! I will, then!"
    t "... N-Not the branch thing. The catmint thing."
    t "I'm going to find catmint, and I'm going to save Featherkit's life, and I'm going to make everything better!"
    l "..."
    l "... Heh. Heh."
    l "Hahaha! Ahahaha!"
    jump md1_end

label md1_give_up:
    t "..."
    t "... I don't believe this."
    t "How can this be happening?"
    t "What did any of us do to deserve this?"
    l "Believe me, when I find out, you'll be the first to know."
    l "I'd just put it out of your mind. Focus on the things you can still change."
    l "That way, you ... you ... *koff* *koff*"
    t "!!!"
    jump md1_end

label md1_end:
    play audio "sfx/ES_Male 03 - Epidemic Sound.mp3" 
    l "{i}*Koff* *Koff* *Koff*{/i}"
    t "Are you alright?!"
    l "{i}*Gasp*{/i} I-I'm fine."
    l "Get out."
    l "{i}*Choke* *Wheeze*{/i}"
    t "Locustleaf --"
    l "I said, get OUT!!!"
    l "{i}*Koff* *Koff* *Koff*{/i}"
    play sound "quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Medical Opinion"
    $ quest_medical_opinion.started = False
    $ quest_medical_opinion.completed = True
    call screen gameUI

label md1_click_berries:
    play audio "sfx/plant_error.mp3"
    t "I wonder if these berries are edible. Locustleaf would probably know."
    t "... And would probably have my head on a pike in the middle of camp if I wasted his time with such a mouse-brained question."
    hide screen md_berries
    call screen gameUI

label md2:
    if quest_medical_opinion.started:
        jump md1
    else:
        stop music fadeout 0.5
        play music "music/ES_Enough by Now - Headlund.mp3" loop
        scene med_den_ext with fade
        t "Locustleaf would have a fit if I went back in there without a good reason."
        if quest_gather_herbs.started:
            t "I'll come back when I have the herbs I need."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
        else:
            call screen gameUI