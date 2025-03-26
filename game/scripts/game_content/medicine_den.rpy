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
        show locustleaf with moveinright
        show maplebreeze with moveinleft
        m "{i}*Wheeze*{/i} I-I'm not ... {i}*Wheeze*{/i} I'm not that sick, Locustleaf ... {i}*Wheeze*{/i} Honest ..."
        m "These herbs should go to ... {i}*Wheeze*{/i} somecat who really ... {i}*Wheeze*{/i} needs them ..."
        l "Shut up and eat your catmint."
        t "Locustleaf!"
        l "Talonclaw?"
        l "What do I always say? The medicine den is for emergencies, only!"
        t "But it {i}is{/i} an emergency!"
        t "Featherkit's gotten sick, and --"
        m "*Gasp* Oh, no! Will she be alright?"
        l "Stay out of this, Maplebreeze."
        l "Featherkit ... she's one of Sunshadow's new litter, right?"
        l "Has she stopped eating?"
        t "Yes."
        l "And developed a cough?"
        t "Yes! Now, come on, we need to hurry! Do you have anything I can --"
        stop music
        l "She'll be dead by sundown."
        m "*Gasp*"
        play music "music/ES_Days That Matter - Headlund.mp3" loop
        t "What?!"
        l "I'm sorry. There's nothing I can do."
        l "A cat her age, in these conditions, doesn't stand a chance against any sort of cough without the proper nutrition."
        l "Herbs, or no herbs."
        t "No, no, that can't be right."
        t "She just got sick this morning! There must still be some time to save her!"
        m "{i}Wheeze{/i} ... Yes, Locustleaf, surely there's still something we can --"
        l "Quiet, Maplebreeze!"
        m "..."
        l "... Okay. Maybe, if I had the herbs to spare, I would be more inclined to agree with you."
        l "But, in case you haven't noticed, this den is already filled with the sick and dying, inclduing our own deputy."
        t "But Featherkit's so small -- she'll only need a tiny scrap of catmint!"
        t "Maplebreeze was just saying she didn't need hers!"
        m "Yes ... {i}wheeze{/i}... I'd be happy to spare a little ..."
        l "Maplebreeze is a {i}medicine cat.{/i}"
        l "If these herbs could go towards saving one starving kit, versus saving Maplebreeze, who will go on to save dozens ..."
        l "Well, I'll let you do the math on that one."
        l "Need I remind you how much worse things got for ThunderClan after we lost our last apprentice?"
        t "..."
        t "... What if I could find more?"
        l "Excuse me?"
        t "More catmint. Then, could you spare some for Featherkit?"
        l "Ha! If you find any catmint out there, you could line your nest with it, for all I care."
        l "Better yet, you could find a whole branch and spend the afternoon hitting yourself over the head with it."
        if quest_favorite_prey.started:
            l "It'd probably be a better use of your time."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} Hunting for catmint means Talonclaw will no longer be able to complete the following questline: {b}Burial Rites.{/b}"
            play sound "sfx/game_tip.mp3"
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
            play sound "sfx/game_tip.mp3"
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
            play sound "sfx/game_tip.mp3"
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
    l "Yeah. That's what I thought."
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
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Medical Opinion"
    $ quest_medical_opinion.started = False
    $ quest_medical_opinion.completed = True
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Grim Tidings"
    $ quest_grim_tidings.started = True
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
    elif nursery_visited==False:
        jump md1
    elif nursery_visited==True and not quest_medical_opinion.started or quest_medical_opinion.completed:
        stop music fadeout 0.5
        play music "music/ES_Enough by Now - Headlund.mp3" loop
        scene med_den_ext with fade
        t "I really hope I'm right about Featherkit ..."
        t "If her cough turns out to be serious, Beetle can always fetch Locustleaf herself."
        t "The medicine den is only a few paces away from the nursery, after all."
        t "I'm a warrior. It's my job to hunt for the Clan. Not worry about kits with the sniffles."
        t "Yup. Definitely not worried."
        t "Definitely not ..."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
        else:
            call screen gameUI
    else:
        stop music fadeout 0.5
        play music "music/ES_Enough by Now - Headlund.mp3" loop
        scene med_den_ext with fade
        t "I doubt Locustleaf wants to see me back so soon ..."
        if quest_gather_herbs.started:
            t "I'll follow up with him when I get the herbs, like I promised."
        else:
            t "I hope he's doing okay."
            t "If we lost him ..."
            t "{i}*Shudder*{/i}"
            t "Probably best not to think about things like that."
            t "Locustleaf is the most talented medicine cat in the forest. I know he'll be fine."
            t "He has to."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
        else:
            call screen gameUI