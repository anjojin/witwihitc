label bs_1:
    $ currently_in = "bury"
    t "Some eulogy."
    show burial site bg with fade
    show side sun sitting
    play music "music/ES_A Friend Like You - Headlund.mp3" loop
    s "I only said what's already been on every cat in ThunderClan's mind."
    t "I had a few thoughts about the part where you condemned our warrior ancestors to an eternity of suffering and torment ..."
    hide side sun sitting
    show side sun rising
    s "Think you're funny?"
    s "I'm not in the mood to laugh right now, Talonclaw."
    t "I'm sorry. But, as you yourself pointed out, the bodies are quite literally beginning to pile up around camp."
    t "Everycat is already going through a hard enough time. The warriors are looking to you for words of comfort; words of inspiration."
    t "Did your speech have to be quite so ... upsetting?"
    s "Upsetting?"
    hide side sun sitting
    show side sun rising
    s "{i}Upsetting{/i} was exactly my intention."
    s "With each day that passes, more and more of our Clanmates' lives are stolen away."
    s "Now, Spottedlight is gone, and you expect me not to be upset about it?"
    t "I didn't mean --"
    hide side sun rising
    show side sun standing
    s "I know exactly what you meant."
    s "Were you even paying enough attention to notice that Briarstar didn't show up to the vigil?"
    s "Or, did not even care enough to look?"
    t "..."
    t "I noticed, Sunshadow."
    s "Then, you should be angry!"
    s "You say cats need words of comfort -- well, where are the cats whose job it is to comfort us?"
    s "To protect us?"
    t "Come on. You can't blame all this on Briarstar."
    t "Spottedlight was her Clanmate, too."
    t "If there was anything she could've done to prevent this, I'm sure she would've done it."
    hide side sun standing
    show side sun sitting
    s "..."
    s "Tell me this, then, Talonclaw."
    menu: 
        s "Why do you think this famine happened, in the first place?"
        "The Moonpool running dry.":
            jump bs1_wc_moonpool
        "The greencough outbreak.":
            jump bs1_wc_greencough
        "Overpopulation.":
            jump bs1_wc_overpopulation
        "The harsh weather.":
            jump bs1_wc_leafbare

label bs1_wc_moonpool:
    t "Believe what you will, but you can't deny that things really started falling apart after we lost our connection to StarClan."
    hide side sun sitting
    show side sun rising
    s "Am I really expected to believe that the power of our warrior ancestors is contained within a little pool of water?"
    s "If that's the case, why worship them at all?"
    s "What happens when the Moonpool freezes over? Or when twolegs decide to fill it in with dirt?"
    s "No. What happens in the land of the living -- that's what really matters."
    s "Last newleaf alone, ThunderClan had four new litters of kits, none of which were their queens' first."
    s "Our family trees are so large, cats can't even keep track of their own kin."
    s "Not to mention all the downtrodden rogues and strays Briarstar's taken in."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Spottedlight, I believe that puts us at sixteen."
    jump bs1_sun_lament

label bs1_wc_greencough:
    t "The medicine cats say that this greencough strain is one of the deadliest that the forest has seen in moons."
    hide side sun sitting
    show side sun rising
    s "And how do outbreaks spread?"
    s "Last newleaf alone, ThunderClan had four new litters of kits, none of which were their queens' first."
    s "Our family trees are so large, cats can't even keep track of their own kin."
    s "Not to mention all the downtrodden rogues and strays Briarstar's taken in."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Spottedlight, I believe that puts us at sixteen."
    jump bs1_sun_lament

label bs1_wc_overpopulation:
    t "I think every cat in ThunderClan is already well aware of your opinions on this matter, Sunshadow."
    hide side sun sitting
    show side sun rising
    s "It's not an opinion. It's simple fact."
    s "Last newleaf alone, ThunderClan had four new litters of kits, none of which were their queens' first."
    s "Our family trees are so large, cats can't even keep track of their own kin."
    s "Not to mention all the downtrodden rogues and strays Briarstar's taken in."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "Hn. Well, if your theory is true, at least the hard times shouldn't last much longer."
    t "By my last head count, I believe our ranks are down to sixteen, now."
    jump bs1_sun_lament

label bs1_wc_leafbare:
    t "Say what you will, but you can't deny that we've never lived through a leafbare this harsh before."
    t "Not to mention the drought earlier this greenleaf."
    hide side sun sitting
    show side sun rising
    s "ShadowClan, WindClan, and RiverClan have all endured the exact same conditions that we have, and yet they haven't experienced nearly as much hardship."
    s "Last newleaf alone, ThunderClan had four new litters of kits, none of which were their queens' first."
    s "Our family trees are so large, cats can't even keep track of their own kin."
    s "Not to mention all the downtrodden rogues and strays Briarstar's taken in."
    s "With our dens overflowing, it's no wonder the Clan couldn't sustain itself."
    t "I think every cat in ThunderClan is already well aware of your opinions, Sunshadow."
    s "Yeah. Every cat who's left."
    s "How many are there, now?"
    t "... With the loss of Spottedlight, I believe that puts us at sixteen."

label bs1_sun_lament:
    t "That's counting your new kits."
    s "Sixteen cats ..."
    s "And I suspect at least a few of those won't make it to the end of leaf-bare."
    t "Stop it."
    t "Don't do that."
    t "ThunderClan is strong. We can survive this if we just --"
    s "Just what?"
    s "Stick together? Be the best warriors we can be?"
    s "Spottedlight believed that, too. Look at all the good it did her!"
    t "What {i}are{/i} we supposed to do, then, Sunshadow?"
    t "Start a revolution?"
    t "Go back in time and stop ThunderClan from becoming overpopulated?"
    hide side sun rising
    show side sun sitting
    s "..."
    s "I'll tell you what {i}I'm{/i} going to do."
    s "I'm going to bury my mate."
    s "She's getting a proper ThunderClan sendoff -- all the rites, all the rituals."
    s "Nothing withheld."
    t "Sunshadow."
    s "What?"
    t "You can't be serious."
    s "Do I seem unserious to you?"
    t "We're practically one bad day away from all of ThunderClan joining the body pile."
    t "We barely have enough energy to keep everyone fed, let alone perform an elaborate grave-digging ritual in the middle of leaf-bare."
    t "Forgive me if I'm not overwhelmed with sympathy."
    s "See, that, Talonclaw, is an appeal to logic. To reason."
    s "But those things don't matter anymore. Nothing makes sense and it hasn't for a long time."
    s "My mate is dead. Let me freeze, for all I care. The worms can eat us both."
    t "Don't say things like that."
    s "Why not?"
    s "Suddenly overwhelmed with sympathy?"
    menu:
        t "What about ..."
        "Your Clanmates?":
            jump bs1_warrior_code
        "Your kits?":
            jump bs1_kits
        "Me?":
            jump bs1_me

label bs1_warrior_code:
    $ talon_clan_bonus += 1
    t "There's a whole denful of cats back at camp waiting for you to put them to work."
    t "The warriors look up to you. Some of them practically hang on your every word."
    t "Is this really the sort of example you want to be setting for them?"
    hide side sun sitting
    show side sun rising
    s "You mean the example of doing right by the cats I love?"
    s "Resisting fear? Standing up against the unfairness of our sitation?"
    s "Yes, Talonclaw. That's {i}exactly{/i} the kind of example I want to be setting."
    t "The Warrior Code clearly states that keeping the Clan fed must always be our top priority, even at the expense of --"
    s "The Warrior Code also states that our leaders are supposed to care for ThunderClan's young and old, living each life with pride and dignity."
    s "Does that sound like Briarstar to you?"
    t "..."
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
    t "Just ... Come on, Sunshadow. Come back to camp with me."
    t "Get some food in your belly. Warm your paws. I can cover your hunting patrols for the day."
    jump bs1_kit_quiz

label bs1_kits_unfair:
    t "It isn't fair to them."
    t "And I know how much that must hurt. Because it isn't fair to you, either."
    t "And it especially isn't fair to Spottedlight."
    hide side sun sitting
    show side sun rising
    s "..."
    t "StarClan, I still remember when the two of you were just a couple of feather-brained apprentices ..."
    t "Remember when you got that sting on your muzzle, trying to pick those flowers to impress her?"
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
    t "Every cat does."
    t "But we can't give that to her, Sunshadow."
    t "Not while our Clanmates are counting on us to keep them alive."
    t "And I think Spottedlight would agree."
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
    t "If we hurry, maybe we can be done by sundown."
    t "We might even have a little energy left over to hunt for the Clan."
    s "..."
    s "You're a good friend, Talonclaw."
    t "... Yeah. I know."
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
    t "That, and I secretly have psychic powers. But keep it under wraps."
    s "*Snrk*"
    t "Ha! See? I made you laugh!" 
    t "Don't ever say I haven't achieved the impossible."
    s "I would never say that."
    t "..."
    s "..."
    t "Come back to camp with me, Sunshadow."
    t "Get some food in your belly. Warm your paws. I can take over your duties for the day."
    s "I ..."
    s "I can't."
    t "Why?"
    hide side sun sitting
    show side sun rising
    s "Look at the sky. The vultures are already starting to circle."
    s "How can I walk away knowing that, as soon as I do, they'll carry her off and I'll never see her again?"
    s "I know that it's pointless and I know that it's foolish. But I just ..."
    s "Oh, StarClan, Talonclaw."
    s "She wanted to take our kits to the creek."
    s "In greenleaf, she said."
    s "When everything got better, we were supposed to go swimming."
    s "Do you think they'll even remember what she smells like?"
    s "Will I?"
    t "..."
    t "Let me help you."
    s "What?"
    t "Let me help you bury Spottedlight."
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
    s "Spottedlight wasn't picky. Anything should suffice."
    $ quest_favorite_prey.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Favorite Prey"
    s "Finally: a crocus. Her favorite flower."
    s "I think I've seen some growing around camp."
    $ quest_crocus.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Crocuses"
    t "Is that all?"
    s "Yes. If you get those things for me, I can handle all the digging by myself."
    t "Are you sure?"
    s "I'm not dead yet, Talonclaw. I haven't completely lost my strength."
    t "... I guess I can start heading back towards camp, then."
    t "I'll come back to this part of the territory when I have everything gathered."
    s "... Thank you, Talonclaw."
    s "Spottedlight really loved you, you know."
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
    if quest_harbringer_final.started or quest_favorite_prey.cancelled or quest_favorite_prey.failed:
        s "Talonclaw! You're here!"
        s "You know, you really had me worried for a second, there. I was starting to believe you wouldn't show."
        t "Of course I showed."
        hide side sun_m standing 
        show side sun_m rising
        s "Yes. Of course. I see that, now ..."
        s "I'm sorry. I shouldn't have doubted. It's just, these days, it's so rare to find a cat you can truly depend on."
        t "... Sunshadow, I --"
        hide side sun_m rising
        show side sun_m sitting
        s "Say, how did the patrols go today?"
        s "I wish I could say I was too preoccupied to think about them, but, alas ... you know how I worry."
        s "Did the warriors manage to organize themselves okay without me?"
        t "Yes, but --"
        s "Ha! What did I tell you, Talonclaw? It all works out."
        s "Oh! And, would you look at this? The grave is finally ready."
        s "Around sunhigh, a few buzzards started circling, but I managed to scare them off."
        s "They'll think twice before bothering my mate again!"
        t "... Your paws are bleeding."
        s "Oh. Are they?"
        hide side sun_m sitting
        show side sun_m standing
        s "Ha! Well, would you look at that? They are."
        s "It's funny, I'm completely numb to the pain." 
        s "Maybe I should get frozen more often."
        t "... Sunshadow, there's something I have to tell you."
        s "Alright. But first, did you manage to get all the things I asked for?"
        if quest_favorite_prey.cancelled or quest_favorite_prey.failed:
            t "I don't think that's important right now."
            s "... Oh, no."
            s "You didn't, did you?"
            s "What was it, huh?"
            s "Briarstar needed you on the hunting patrol? A kitten got stuck up in a tree somewhere?"
            t "No! What? No!"
            if eaten_prey:
                s "Don't lie! I can smell that you've eaten!"
                s "Too hungry to save that prey for Spottedlight?"
            t "Listen, if you would just let me explain --"
        else:
            t "Yes, but --"
            s "Good. Give them here. Let's begin before I lose my nerve."
            t "Sunshadow, if you would just listen to me --"
        s "The love of my life is about to be buried, Talonclaw! What could possibly be more important than --"
        jump bs2_abrupt
    else:
        hide side sun_m sitting 
        show side sun_m rising
        if talon_sun_bonus<0:
            s "... What are you doing here?"
            s "Come to insult my family?"
            s "Or, worse, try to talk me into turning tail and fleeing back to camp with you like a good little warrior?"
        else:
            s "Talonclaw."
            s "What are you doing here?"
            s "Come to talk me into coming back to camp with you like a good little warrior?"
        t "Sunshadow."
        t "You look ... awful." 
        s "I am awful."
        s "Now, answer my question."
        s "{i}What are you doing here?{/i}"
        t "..."
        t "... I wish I didn't have to be the one to tell you this."
        hide side sun_m rising
        show side sun_m sitting        
        s "When have you ever wanted to be 'the one' to do anything?"
        t "You might want to sit down for this."
        s "I'm already sitting."
        t "Sunshadow, something ... uh, s-something ..."
        hide side sun_m sitting 
        show side sun_m standing
        s "StarClan, out with it. What's the great tragedy? Did Briarstar skip you for the hunting patrol?"
        s "Was there a kitten stuck up a tree that you couldn't save somewhere?"
        t "Sunshadow ..."
        s "Look around you, Talonclaw! Look at what's been happening for the past four moons!"
        s "The love of my life is cold and gray at my paws! Whatever you have to say, I think I can handle --"
        jump bs2_abrupt

label bs2_abrupt:
    stop music 
    t "Sunshadow, two of your kits are dead."
    hide side sun_m standing
    show side sun_m sitting
    s "..."
    t "Your daughters. Willowkit and Featherkit."
    t "They were weakened by their mother's loss."
    t "There ... There was nothing we could do."
    s "..."
    t "... StarClan, Sunshadow, I'm sorry."
    t "I'm so, so incredibly sorry."
    t "You have no idea how badly I wish there was something I could say to make this any better."
    t "To take away even a fraction of the pain you must be feeling."
    t "But ... there isn't."
    t "And I can't."
    t "So I'm just ... sorry."
    s "..."
    s "......."
    s "........................"
    s "... What about the others?"
    t "What?"
    s "The other three? Stormkit, Wolfkit, and Starlingkit."
    s "Are they doing alright?"
    t "I ..."
    t "Yes."
    t "I think so."
    s "Are they healthy?"
    t "Healthy enough."
    s "They have enough to eat, now?"
    t "..."
    t "......."
    t "... Yes, Sunshadow."
    t "They have enough to eat, now."
    hide side sun_m sitting
    show side sun_m rising
    play audio "sfx/inhale.mp3"
    s "... {i}*Inhale*{/i}"
    play audio "sfx/exhale.mp3"
    s "... {i}*Exhale*{/i}"
    if quest_harbringer_final.started:
        hide side sun_m sitting
        show side sun_m standing
        s "Come to the grave with me, Talonclaw."
        t "What?"
        s "Come to the grave with me."
        s "We're going to bury my mate."
        jump bs2_ending
    else:
        jump bs2_nonending

label bs2_nonending:
    s "Something's shifted."
    s "Can you sense it?"
    s "That churning in the air?"
    t "Sunshadow --"
    s "Go back to camp, Talonclaw."
    t "But --"
    s "Go back to camp."
    s "You can't feel it."
    s "You never have."
    t "..."
    play sound "sfx/quest_unlocked.mp3"
    $ quest_harbringer.started = False
    $ quest_harbringer.completed = True
    "{b}Quest Completed:{/b} Harbringer"
    call screen gameUI

label bs2_ending:
    play music "music/ES_Whispers of the Wasteland - Victor Lundberg.mp3"
    "{b}Begin Illustration Here{/b}"
    s "We are gathered here today to mourn the passing of Spottedlight."
    s "She was a loving mate, sister, daughter, mother, and friend to everyone in ThunderClan."
    s "An honorable warrior who served her fellow Clanmates until her very last breath."
    s "It is time, now, to perform the burial rites that were taught to us by our warrior ancestors ..."
    s "... and which have since been used to exalt countless generations of ThunderClan cats."
    s "A vigil has been held, and the proper materials have been collected by those who cared for her."
    s "Crocuses."
    s "Nesting materials."
    s "And, finally, a piece of prey."
    s "StarClan, please accept these offerings such that they may ease Spottedlight's journey into Silverpelt ..."
    s "... As well as replenish the spirits of the living who are here to mourn her."
    s "For we, too, have a long journey ahead."
    s "The journey to remake a new ThunderClan."
    s "With I, as leader."
    t "Sunshadow, what are you --"
    s "And Talonclaw as my deputy."
    t "..."
    s "It's alright, darling. You can rest now."
    s "I'll keep our family safe."
    s "Under my care, our kits will never get sick. They will never go hungry."
    s "They will never want for anything."
    s "Losing you is going to be the worst thing that ever happens to them."
    s "Oh, my love. Can you sense that feeling in the air?"
    s "The restlessness, the anticipation? Green things turning over in the dirt?"
    s "Soon, it will be newleaf."
    s "The hard times will be over."
    s "The ground will thaw."
    s "And the primroses will be in bloom ..."
    scene black with fade
    s "Nothing can stop what happens now."
    "{b}END GAME{/b}"
    $ MainMenu(confirm=False)()
