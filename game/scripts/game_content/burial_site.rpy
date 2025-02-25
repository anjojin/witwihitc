label bs_1:
    $ currently_in = "burial"
    t "Some eulogy."
    show burial site bg with fade
    show side sun sitting
    s "I only said what's been on every ThunderClan cat's mind."
    t "I had a few thoughts about the part where you condemned our warrior ancestors to an eternity of suffering and torment ..."
    hide side sun sitting
    show side sun rising
    s "This is funny to you?"
    s "I'm not in the mood to laugh, Talonclaw."
    t "I'm sorry. But, as you yourself pointed out, the bodies are quite literally beginning to pile up around camp."
    t "Please forgive me if I'm not overwhelmed with sympathy."
    hide side sun rising
    show side sun sitting
    s "Well, I can tell you one thing right now. My Dapplefeather is not going to go on the pile."
    s "She's going to get a proper ThunderClan burial. All the rites. All the rituals."
    s "Nothing withheld."
    t "Sunshadow."
    s "What?"
    t "You can't be serious."
    s "Do I seem unserious to you?"
    t "We're one bad day away from all of ThunderClan joining the pile."
    t "We barely have enough energy to keep everyone fed, let alone perform an elaborate grave-digging ritual in the middle of leaf-bare."
    s "See, that, Talonclaw, is an appeal to logic. To reason."
    s "But those things don't matter anymore. Nothing makes sense and it hasn't for a long time."
    s "My mate is dead. I can join the pile, for all I care. Let the worms eat us both."
    t "Don't say things like that."
    s "Why not? Suddenly overwhelmed with sympathy?"
    menu:
        t "What about ..."
        "The Warrior Code?":
            jump bs1_warrior_code
        "Your kits?":
            jump bs1_kits
        "Me?":
            jump bs1_me

label bs1_warrior_code:
    t "The Warrior Code clearly states that keeping the Clan fed must always be our top priority, even at the expense of --"
    s "StarClan, that's the problem with you, Talonclaw."
    s "Our friends and family are dropping like flies, and yet still, you cling to the rules."
    s "Why do you think this famine happened, in the first place?"
    menu: 
        t "..."
        "The Moonpool running dry.":
            jump bs1_wc_moonpool
        "The greencough outbreak.":
            jump bs1_wc_greencough
        "Overpopulation.":
            jump bs1_wc_overpopulation
        "The harsh weather.":
            jump bs1_wc_leafbare

label bs1_wc_moonpool:
    t "You can't deny that the moment we lost our connection to StarClan, things started going wrong."
    s "Am I really expected to believe that the power of our warrior ancestors is contained within a little pool of water?"
    s "If that's the case, why do we even worship them at all?"
    s "What happens when the Moonpool freezes? Or when twolegs decide to fill it in?"
    s "No, what happens in the land of the living -- that's what really matters."
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Wrenstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Dapplefeather, I believe that puts us at twenty-eight."
    jump bs1_sun_lament

label bs1_wc_greencough:
    t "The medicine cats say that this greencough strain is one of the deadliest that the forest has seen in moons."
    s "And how do outbreaks spread, Talonclaw?"
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Wrenstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the sickness spread so fast."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Dapplefeather, I believe that puts us at twenty-eight."
    jump bs1_sun_lament

label bs1_wc_overpopulation:
    t "I think every cat in ThunderClan is already well aware of your opinions on this matter, Sunshadow."
    s "It's not an opinion. It's simple fact."
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Wrenstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "Hn. Well, if your theory is true, the hard times shouldn't last much longer."
    t "By my last head count, I believe our ranks are down to twenty-eight."
    jump bs1_sun_lament

label bs1_wc_leafbare:
    t "Say what you will, but you can't deny that we've never lived through a leafbare this harsh before."
    t "That, coupled with the drought earlier this greenleaf, must have wiped out just about all of the prey that was left in the forest."
    s "ShadowClan, WindClan, and RiverClan have all endured the exact same conditions that we have. And yet, they have not suffered nearly as much."
    s "Why? Because they've kept their ranks at manageable sizes."
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Wrenstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Dapplefeather, I believe that puts us at twenty-eight."

label bs1_sun_lament:
    t "That's counting your new kits."
    s "Twenty-eight cats ..."
    s "And I suspect at least a few of those won't make it to the end of leaf-bare."
    t "Stop it."
    t "Don't do that."
    t "ThunderClan is strong. We can survive this if we just --"
    s "Follow the Warrior Code?"
    s "The same Warrior Code that ordered us to shelter all those kits and outsiders? "
    s "The same Warrior Code that got us into this mess, in the first place?"
    t "... I was going to say 'if we just stick together.'"
    s "Yes. Well."
    s "Dapplefeather thought so, too."
    t "..."
    hide side sun sitting
    show side sun rising
    jump sun_ultimatum

label bs1_kits:
    t "You have five kits waiting for you back at camp."
    t "It's bad enough that they lost their mother. Now, they're going to grow up without a father, too?"
    menu:
        t "I'm an orphan, Sunshadow. I know how that feels. You can't do that to them. It's ..."
        "Selfish":
            jump bs1_kits_selfish
        "Irrational":
            jump bs1_kits_irrational
        "Unfair":
            jump bs1_kits_unfair

label bs1_kits_selfish:
    t "It's the most selfish, irresponsible thing I can think of. I'm sorry, but that's just the truth."
    t "You really think that your peace of mind over Dapplefeather's body is worth more than the lives of those kits?"
    t "What do you think is going to happen to them? You think they'll be happy growing up knowing that their father chose a corpse over them?"
    jump bs1_kit_quiz

label bs1_kits_irrational:
    t "It's just not rational to throw your life away over a cat who's already gone."
    t "I'm sorry, Sunshadow. I know how much you loved her. But doing this won't bring her back."
    t "What happens to Dapplefeather's body won't make a difference in the lives of your kits."
    t "But what happens to you, will."
    t "Just ... Come on, Sunshadow. Come back to camp with me. Get some food in your belly. Warm your paws. I can cover your hunting patrols for the day."
    jump bs1_kit_quiz

label bs1_kits_unfair:
    t "It isn't fair to them."
    t "And I know how much that must hurt. Because it isn't fair to you, either."
    t "And it especially isn't fair to Dapplefeather."
    s "..."
    t "StarClan, I still remember when the two of you were just a couple of feather-brained apprentices ..."
    t "Remember when you got that massive sting on your muzzle, trying to pick those flowers to impress her?"
    s "... I ate all my food pre-chewed for a week, after that."
    t "And you deserved it, too! Don't you know a wasp's nest when you see one?"
    s "Ha!"
    t "Heh."
    s "... But she never left me."
    s "All that time in the medicine den, she stayed right by my side."
    t "... Yeah. She was a special cat."
    t "She deserves a proper burial."
    t "Every cat we've lost does."
    t "But we can't give that to them, Sunshadow."
    t "Not while our Clanmates are counting on us to keep them alive."
    t "And I think Dapplefeather would agree."
    jump bs1_sun_relent

label bs1_kit_quiz:
    s "..."
    s "What are my kits' names?"
    t "What?"
    menu:
        s "My kits. Since you care so much about them, tell me their names."
        "Willowkit, Wolfkit, Stormkit, Briarkit, and Featherkit":
            jump bs1_kits_correct
        "Willowkit, Wolfkit, Shadekit, Bluekit, and Dapplekit":
            jump bs1_kits_incorrect1
        "Willowkit, Spottedkit, Shadekit, Briarkit, and Featherkit":
            jump bs1_kits_incorrect2

label bs1_kits_correct:
    $ sunshadow_rel += 10
    t "Willowkit, Wolfkit, Stormkit, Briarkit, and Featherkit."
    t "And now, you look like a fool."
    s "..."
    jump sun_ultimatum

label bs1_kits_incorrect1:
    t "Willowkit, Wolfkit, Shadekit, Bluekit, and ... Dapplekit?"
    jump bs1_sun_furious

label bs1_kits_incorrect2:
    t  "Willowkit, Spottedkit ... Shadekit ... Briarkit, and Featherkit?"
    jump bs1_sun_furious

label bs1_sun_furious:
    $ sunshadow_rel -= 40
    s "..."
    s "Get out."
    t "Sunshadow --"
    s "You have some nerve, lecturing me about my family."
    s "To think I once considered you their kin."
    s "{i}She{/i} considered you their kin."
    t "Please, just --"
    s "{i}Out.{/i} Now. You don't deserve to be here."
    s "You're polluting the air with your scent."
    t "..."
    show screen gameUI with fade
    "Click the {b}'?!'{/b} button to access your Quest list."
    "Click the {b}Camp{/b} button to travel back to camp."
    call screen gameUI

label bs1_me:
    t "What about me?"
    t "You're my best friend, Sunshadow. The closest thing to kin I have."
    t "If I lost you ..."
    s "It's not that simple. You know that."
    s "If you ever lost your mate, I would be devastated for you."
    s "I would be there for you, the same way I'm asking you to be here for me now."
    t "I've never had a mate, Sunshadow. You know that."
    t "I've never had a mother, or a father. I don't know any of my brothers or sisters."
    t "All I have is you."
    t "Please. I can't do this alone."
    jump bs1_sun_relent


label sun_ultimatum:
    s "I'm giving my mate a proper burial, Talonclaw."
    s "Whether you like it, or not."
    menu:
        s "I'll die before I let the vultures carry her off."
        "Offer to help":
            jump bs1_offer_help
        "Leave him to it":
            jump bs1_leave_to_it

label bs1_offer_help:
    $ sunshadow_rel += 20
    t "... Then let me help you."
    s "What?"
    t "If there's nothing I can do to stop you, then at least let me help you."
    t "If we hurry, maybe we can be done by dark."
    t "We might even have a little energy left over to hunt for the Clan."
    s "..."
    s "You're a good cat, Talonclaw."
    t "Yeah, yeah."
    t "Just tell me what you need."
    jump bs1_quest

label bs1_leave_to_it:
    $ sunshadow_rel -= 20
    t "Fine. See what I care."
    t "While you're doing that, I'll be out feeding the sick and the starving."
    t "You know, the cats whose fates can still actually be changed."
    s "..."
    show screen gameUI with fade
    "Click the {b}'?!'{/b} button to access your Quest list."
    "Click the {b}Camp{/b} button to travel back to camp."
    call screen gameUI


label bs1_sun_relent:
    $ sunshadow_rel += 40
    s "..."
    s "StarClan, Talonclaw. I really hate you."
    s "How is it that you always know exactly what to say?"
    t "Because I've spent too much time around you, mouse-brain."
    t "That, and I have psychic powers. But don't tell anyone."
    s "*Snrk*"
    t "Ha! See? I made you laugh!" 
    t "Don't ever say I haven't achieved the impossible."
    s "I would never say that."
    t "..."
    s "..."
    t "Come back to camp with me, Sunshadow."
    t "Get some food in your belly. Warm your paws. I can cover your hunting patrols for the day."
    s "I ..."
    s "I can't."
    t "Why?"
    s "Look at the sky. The vultures are already circling."
    s "How can I walk away knowing that, as soon as I do, they'll carry her off and I'll never see her again?"
    s "I know that it's pointless and I know that it's foolish. But I just ..."
    s "Oh, StarClan, Talonclaw. She wanted to take our kits to the creek. In greenleaf, she said."
    s "When everything got better, we were supposed to go swimming."
    s "Do you think they'll even remember what she smells like?"
    s "Will I?"
    s "It's all coming apart ..."
    t "..."
    t "Let me help you."
    s "What?"
    t "Let me help you bury Dapplefeather."
    s "But I thought you said --"
    t "Forget what I said."
    t "Just tell me what you need."
    s "Talonclaw, I --"
    t "I know. Get on with it."
    s "..."

label bs1_quest:
    $ burial_rites = True
    s "There are three things."
    s "One: a scrap of moss from her nest."
    $ quest_nesting_material.started = True
    "{b}Quest Unlocked:{/b} Nesting Material"
    s "Two: a piece of her favorite prey."
    s "Dapplefeather wasn't picky. Anything should suffice."
    $ quest_favorite_prey.started = True
    "{b}Quest Unlocked:{/b} Favorite Prey"
    s "Finally: a crocus. Her favorite flower."
    s "I think I've seen some growing around camp."
    $ quest_crocus.started = True
    "{b}Quest Unlocked:{/b} Crocuses"
    t "Is that all?"
    s "Yes. If you get those things for me, I can handle all the digging myself."
    t "Are you sure?"
    s "I'm not dead yet, Talonclaw. I haven't completely lost my strength."
    t "I'll start heading towards camp, then. I'll be back when everything is gathered."
    s "Okay. Sounds good."
    s "Thank you, Talonclaw."
    s "... You know, Dapplefeather really loved you."
    s "I know that, wherever she is, she's grateful for your help, too."
    t "..."
    show screen gameUI with fade
    "Click the {b}'?!'{/b} button to access your Quest list."
    "Click the {b}Camp{/b} button to travel back to camp."
    call screen gameUI

