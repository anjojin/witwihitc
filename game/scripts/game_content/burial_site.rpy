label bs_1:
    $ currently_in = "bury"
    t "Some eulogy."
    show burial site bg with fade
    show side sun sitting
    play music "music/ES_A Friend Like You - Headlund.mp3" loop
    s "I only said what's been on every ThunderClan cat's mind."
    t "I had a few thoughts about the part where you condemned our warrior ancestors to an eternity of suffering and torment ..."
    hide side sun sitting
    show side sun rising
    s "Think you're funny?"
    s "I'm not in the mood to laugh right now, Talonclaw."
    t "I'm sorry. But, as you yourself pointed out, the bodies are quite literally beginning to pile up around camp."
    t "Forgive me if I'm not overwhelmed with sympathy."
    hide side sun rising
    show side sun sitting
    s "Well, I can tell you one thing right now. My Dapplefeather is not going on the pile."
    s "She's going to get a proper ThunderClan burial. All the rites. All the rituals."
    s "Nothing withheld."
    t "Sunshadow."
    s "What?"
    t "You can't be serious."
    s "Do I seem unserious to you?"
    t "We're practically one bad day away from all of ThunderClan joining the pile."
    t "We barely have enough energy to keep everyone fed, let alone perform an elaborate grave-digging ritual in the middle of leaf-bare."
    s "See, that, Talonclaw, is an appeal to logic. To reason."
    s "But those things don't matter anymore. Nothing makes sense and it hasn't for a long time."
    s "My mate is dead. Let me freeze, for all I care. These burial rites can be for the both of us."
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
    $ talon_clan_bonus += 1
    t "The Warrior Code clearly states that keeping the Clan fed must always be our top priority, even at the expense of --"
    s "StarClan, that's the problem with you, Talonclaw."
    s "Our friends and family drop like flies, and yet still, you think the rules are what's most important?"
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
    t "Believe what you will, but you can't deny that things got worse after we lost our connection to StarClan."
    hide side sun sitting
    show side sun rising
    s "Am I really expected to believe that the power of our warrior ancestors is contained within a little pool of water?"
    s "If that's the case, why worship them at all?"
    s "What happens when the Moonpool freezes? Or when twolegs decide to fill it in with gravel?"
    s "No. There's a simpler explanation in the land of the living."
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Briarstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Dapplefeather, I believe that puts us at sixteen."
    jump bs1_sun_lament

label bs1_wc_greencough:
    t "The medicine cats say that this greencough strain is one of the deadliest that the forest has seen in moons."
    hide side sun sitting
    show side sun rising
    s "And how do outbreaks spread?"
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Briarstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the sickness spread as fast as it did."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Dapplefeather, I believe that puts us at sixteen."
    jump bs1_sun_lament

label bs1_wc_overpopulation:
    t "I think every cat in ThunderClan is already well aware of your opinions on this matter, Sunshadow."
    hide side sun sitting
    show side sun rising
    s "It's not an opinion. It's simple fact."
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Briarstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "Hn. Well, if your theory is true, the hard times shouldn't last much longer."
    t "By my last head count, I believe our ranks are down to sixteen."
    jump bs1_sun_lament

label bs1_wc_leafbare:
    t "Say what you will, but you can't deny that we've never lived through a leafbare this harsh before."
    t "Not to mention the drought earlier this greenleaf."
    hide side sun sitting
    show side sun rising
    s "ShadowClan, WindClan, and RiverClan have all endured the exact same conditions that we have. And yet, they have not suffered nearly as much."
    s "Why? Because they've managed their Clan sizes."
    s "This past newleaf alone, we've had four new litters of kits, plus all downtrodden rogues and strays Briarstar's taken in."
    s "By my calculations, that put ThunderClan's greenleaf population well past eighty."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Dapplefeather, I believe that puts us at sixteen."

label bs1_sun_lament:
    t "That's counting your new kits."
    hide side sun rising
    show side sun sitting
    s "Sixteen cats ..."
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
    t "You really think that your peace of mind is worth more than the lives of those kits?"
    t "You think they'll be happy growing up knowing that their father chose a lifeless corpse over them?"
    jump bs1_kit_quiz

label bs1_kits_irrational:
    t "It's just not rational to throw your life away over a cat who's already gone."
    t "I'm sorry, Sunshadow. I know how much you loved her. But doing this won't bring her back."
    t "What happens to Dapplefeather's body won't make a difference in the lives of your kits."
    t "What happens to {i}you,{/i} will."
    t "Just ... Come on, Sunshadow. Come back to camp with me. Get some food in your belly. Warm your paws. I can cover your hunting patrols for the day."
    jump bs1_kit_quiz

label bs1_kits_unfair:
    t "It isn't fair to them."
    t "And I know how much that must hurt. Because it isn't fair to you, either."
    t "And it especially isn't fair to Dapplefeather."
    hide side sun sitting
    show side sun rising
    s "..."
    t "StarClan, I still remember when the two of you were just a couple of feather-brained apprentices ..."
    t "Remember when you got that massive sting on your muzzle, trying to pick those flowers to impress her?"
    s "... I had to eat all my food pre-chewed for a week."
    t "And you deserved it, too! Don't you know a wasp's nest when you see one?"
    s "Ha!"
    t "Heh."
    hide side sun rising
    show side sun sitting
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
    hide side sun sitting
    show side sun rising
    menu:
        s "My kits. Since you care so much about them, tell me their names."
        "Willowkit, Wolfkit, Stormkit, Starlingkit, and Featherkit":
            jump bs1_kits_correct
        "Willowkit, Wolfkit, Stormkit, Bluekit, and Dapplekit":
            jump bs1_kits_incorrect1
        "Willowkit, Spottedkit, Shadekit, Starlingkit, and Featherkit":
            jump bs1_kits_incorrect2

label bs1_kits_correct:
    $ talon_sun_bonus += 1
    t "Willowkit, Wolfkit, Stormkit, Starlingkit, and Featherkit."
    t "And now, you look like a fool."
    s "..."
    jump sun_ultimatum

label bs1_kits_incorrect1:
    t "Willowkit, Wolfkit, Stormkit, Bluekit, and ... Dapplekit?"
    jump bs1_sun_furious

label bs1_kits_incorrect2:
    t  "Willowkit, Spottedkit ... Shadekit ... Starlingkit, and Featherkit?"
    jump bs1_sun_furious

label bs1_sun_furious:
    $ talon_sun_bonus -= 2
    hide side sun rising
    show side sun standing
    s "..."
    s "Get out."
    t "Sunshadow --"
    s "You have some nerve, lecturing me about my family."
    s "To think I once considered you their kin."
    s "That {i}she{/i} considered you their kin."
    t "Please, Sunshadow, just --"
    s "{i}Out.{/i} Now. You don't deserve to be here."
    s "This is a sacred place. You're polluting the air with your scent."
    t "..."
    show screen gameUI with fade
    play sound "sfx/game_tip.mp3"
    "Click the {b}'?!'{/b} button to access your Quest list."
    play sound "sfx/game_tip.mp3"
    "Click the {b}Camp{/b} button to travel back to camp."
    call screen gameUI

label bs1_me:
    t "What about me?"
    t "You're my best friend, Sunshadow. The closest thing I have to kin."
    t "If I lost you ..."
    hide side sun sitting
    show side sun rising
    s "It's not that simple."
    s "If you ever lost your mate, I would be devastated for you."
    s "I would be there for you the same way I'm asking you to be here for me, now."
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
    t "... Then let me help you."
    s "What?"
    t "If there's nothing I can do to stop you, then at least let me help you."
    t "If we hurry, maybe we can be done by dark."
    t "We might even have a little energy left over to hunt for the Clan."
    s "..."
    s "You're a good cat, Talonclaw."
    t "... Whatever."
    t "Just tell me what you need."
    jump bs1_quest

label bs1_leave_to_it:
    $ talon_sun_bonus -= 2
    t "Fine. See what I care."
    t "While you're doing that, I'll be out working to feed the sick and the starving."
    t "You know, the cats whose fates can still actually be changed."
    s "..."
    show screen gameUI with fade
    play sound "sfx/game_tip.mp3"
    "Click the {b}'?!'{/b} button to access your Quest list."
    play sound "sfx/game_tip.mp3"
    "Click the {b}Camp{/b} button to travel back to camp."
    call screen gameUI


label bs1_sun_relent:
    $ talon_sun_bonus += 1
    hide side sun rising
    show side sun sitting
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
    hide side sun sitting
    show side sun rising
    s "Look at the sky. The vultures are already circling."
    s "How can I walk away knowing that, as soon as I do, they'll carry her off and I'll never see her again?"
    s "I know that it's pointless and I know that it's foolish. But I just ..."
    s "Oh, StarClan, Talonclaw. She wanted to take our kits to the creek. In greenleaf, she said."
    s "When everything got better, we were supposed to go swimming."
    s "Do you think they'll even remember what she smells like?"
    s "Will I?"
    t "..."
    t "Let me help you."
    s "What?"
    t "Let me help you bury Dapplefeather."
    s "But I thought you said --"
    t "Forget what I said."
    t "Just tell me what you need."
    s "Talonclaw, I --"
    t "I know."
    t "Get on with it."
    s "..."
    jump bs1_quest

label bs1_quest:
    $ burial_rites = True
    hide side sun rising
    show side sun standing
    s "There are three things."
    s "One: a scrap of moss from her nest."
    $ quest_nesting_material.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Nesting Material"
    s "Two: a piece of her favorite prey."
    s "Dapplefeather wasn't picky. Anything should suffice."
    $ quest_favorite_prey.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Favorite Prey"
    s "Finally: a crocus. Her favorite flower."
    s "I think I've seen some growing around camp."
    $ quest_crocus.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Crocuses"
    t "Is that all?"
    s "Yes. If you get those things for me, I can handle all the digging myself."
    t "Are you sure?"
    s "I'm not dead yet, Talonclaw. I haven't completely lost my strength."
    t "I'll start heading towards camp, then. I'll be back when everything is gathered."
    s "Okay. Sounds good."
    s "... Thank you, Talonclaw."
    s "Dapplefeather really loved you, you know."
    s "I know that, wherever she is, she's grateful for your help, too."
    t "..."
    show screen gameUI with fade
    play sound "sfx/game_tip.mp3"
    "Click the {b}'?!'{/b} button to access your Quest list."
    play sound "sfx/game_tip.mp3"
    "Click the {b}Camp{/b} button to travel back to camp."
    call screen gameUI

label bs2:
    stop music fadeout 0.5
    play music "music/ES_A Friend Like You - Headlund.mp3" loop
    scene burial site night with fade
    show side sun_m sitting
    show screen gameUI
    s "{i}*Pant* *Pant*{/i}"
    t "Sunshadow."
    show side sun_m standing
    if quest_harbringer_final.started or quest_favorite_prey.cancelled:
        s "Talonclaw! You made it!"
        s "You had me worried for a second, there. I was starting to think you wouldn't show."
        hide side sun_m standing 
        show side sun_m rising
        s "The grave is finally ready."
        s "A few buzzards started circling around sunhigh, but I gave 'em a good scare. I don't think they'll bother us anymore."
        t "Your paws are bleeing ..."
        s "Are they?"
        hide side sun_m rising
        show side sun_m standing
        s "Oh. Ha! What do you know? They are."
        s "That's funny. I couldn't feel it at all."
        s "Maybe I should freeze more often."
        t "Sunshadow, I have to tell you something."
        s "Sure. But first, did you get the things I asked you for?"
        if quest_favorite_prey.cancelled:
            t "I don't think that's important right now."
            s "... Oh, no. You didn't, did you?"
            s "What was it, huh? They needed you on the hunting patrol? A kitten was stuck up in a tree somewhere?"
            t "No! What? No! Would you just listen?"
        else:
            t "Yes, I did, but --"
            s "Good. Give them here."
            s "Let's begin before I lose my nerve."
            t "Sunshadow, if you would just listen to me --"
        s "The love of my life is about to be buried, Talonclaw! What could possibly be more important than --"
        jump bs2_abrupt
    else:
        if talon_sun_bonus<0:
            s "What are you doing here?"

label bs2_abrupt:
    t "Your kits are dead."
    hide side sun_m standing
    show side sun_m sitting
    s "..."
    t "Two of your daughters. Willowkit and Featherkit."
    t "They were weakened by their mother's loss. Her sickness took them before anything could be done to stop it."
    t "I'm so sorry, Sunshadow."
    t "I wish there was something I could say that would make this any better."
    t "To take away the pain you must be feeling."
    t "But there isn't."
    t "I'm just ... sorry."
    s "..."
    s "... What about the others?"
    s "Stormkit, Wolfkit, and Starlingkit?"
    s "Are they alright?"
    t "Yes."
    s "Are they healthy?"
    t "Yes."
    s "Is there enough food to go around?"
    t "..."
    t "......."
    t "... Yes, Sunshadow."
    t "There's enough food to go around."
    hide sun_m sitting
    show sun_m rising
    s "... {i}*Inhale*{/i}"
    hide side sun_m sitting
    show side sun_m standing
    s "... {i}*Exhale*{/i}"
    if quest_harbringer_final.started:
        s "Come to the grave with me, Talonclaw."
        t "What?"
        s "Come to the grave with me."
        s "We're going to bury my mate."
        jump bs2_ending

label bs2_ending:
    "{b}Begin Illustration Here{/b}"
    s "We are gathered here today to mourn the passing of Dapplefeather."
    s "She was a loving mate, sister, daughter, mother, and friend to everyone in ThunderClan."
    s "She touched countless lives, x, y z ..."
    s "... And yet, in spite of it all ..."
    s "... Dapplefeather's life was just getting started."
    s "She had a bright future ahead."
    s "A future filled with x,y,z"
    s "Dapplefeather used the last of her strength to bring five new lives into the world."
    s "One might think that was when her future was cut short."
    s "But it actually x"
    s "Every x, y, z."
    s "Now, the ones she left behind are here to help ease her journey into Silverpelt."
    s "With these offerings, [] all who gather here may []."
    s "Crocuses, to []."
    s "Bedding, to keep us warm."
    s "And, finally, a piece prey to embolden us along our journey."
    s "The journey to create a new ThunderClan."
    s "A ThunderClan with no []."
    s "With I as the leader, and Talonclaw as my deputy."
    t "Sunshadow, what are you --"
    s "It's alright, Talonclaw."
    s "..."
    s "You can rest now, darling."
    s "Watch over Willowkit and Featherkit for me."
    s "I'll keep the rest of our family safe."
    s "Our kits will never get sick. They will never go hungry."
    s "Losing you is going to be the worst thing that ever happens to them."
    s "Can you sense that feeling in the air?"
    s "The restlessness, the anticipation? Green things, turning over in the dirt?"
    s "Nothing can stop what happens now."
    s "Soon, it will be newleaf."
    s "The hard times will be over."
    s "And the [] will be in bloom ..."






