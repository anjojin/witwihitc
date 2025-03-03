label md1:
    $ med_den_visited = True
    if not quest_medical_opinion.started or quest_medical_opinion.completed:
        scene med_den_ext with fade
        t "The medicine den."
        t "Locustleaf would have a fit if I went in there without a good reason."
        t "Especially since I'm one of the only healthy warriors left ..."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
    
    else:
        scene nursery bg with fade
        show screen gameUI
        show locustleaf with moveinright
        show maplebreeze with moveinleft
        m "{i}Wheeze{/i} I-I'm not ... {i}wheeze{/i} I'm not that sick, Locustleaf ... {i}wheeze{/i} Honest ..."
        m "These herbs should go to ... {i}wheeze{/i} somecat who really ... {i}wheeze{/i} needs them ..."
        l "Shut up and eat your catmint."
        t "Locustleaf!"
        l "Talonclaw?"
        l "What did I tell you last time? The medicine den is no place for healthy warriors!"
        t "But it's an emergency!"
        t "Featherkit, she's gotten sick, and --"
        l "Has she stopped eating?"
        t "Yes."
        l "And developed a cough?"
        t "Yes! Now, come on, we need to hurry! Do you have anything I can --"
        l "She'll be dead by sundown."
        t "What?!"
        l "I'm sorry. There's nothing I can do."
        l "A cat her age, in these conditions, doesn't stand a chance against any sort of cough. Herbs, or no herbs."
        t "No, no, that can't be right."
        t "She just got sick this morning! There must still be some time to save her!"
        l "Maybe if I had herbs to spare, I would be more inclined to agree with you."
        l "But, in case you haven't noticed, this den is full of the sick and dying, inclduing our Clan's deputy."
        t "She's so small -- she'll only need a tiny scrap of catmint!"
        t "Maplebreeze was just saying she didn't need hers!"
        m "{i}Wheeze{/i} ... Yes, Locustleaf ... Surely, I can spare a little ..."
        l "Maplebreeze is a {i}medicine cat.{/i}"
        l "If these herbs could go towards saving one kit, versus saving Maplebreeze, who will go on to save the lives of dozens of kits ..."
        l "Well, I'll let you do the math."
        l "Need I remind you how much worse things got for ThunderClan after Fleetpaw's death?"
        t "... What if I could find more?"
        l "Excuse me?"
        t "More catmint. Then, could you spare some for Featherkit?"
        l "Ha! If you find any catmint on that territory, you could line your nest with it, for all I care."
        l "Whatever."

label md1_click_berries:
    t "I wonder if these berries are edible. Locustleaf would probably know."
    t "... And would probably have my head on a pike in the middle of camp if I wasted his time with such a mouse-brained question."
    hide screen md_berries
    call screen gameUI
