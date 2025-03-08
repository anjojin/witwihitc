label ld1:
    $ leaders_visited = True
    scene leaders_entrance_day with fade
    show screen gameUI
    stop music fadeout 0.5
    play music "ES_La Vuelta a Lerida - Vendla.mp3" loop
    
    if quest_crocus.started:
        t "Hmm ... if I were a crocus, where would I be?"
        t "These tree roots seem like as good of a place as any to grow."
        t "Though, how anything manages grow these days is beyond me ..."
        show briarstar_standing with fade
        b "Talonclaw."
        t "Oh!"
        b "I thought I heard somecat talking out here."
        t "I'm so sorry to disturb you, Briarstar. I was just searching around the leader's den for crocuses."
        t "If you're wondering why, it's because --"
        b "No need to explain yourself."
        b "Please. Come inside. You can continue your search there."
        t "Are you certain? I'd hate to impose."
        b "It's really no trouble. Follow me."
        b "Your paws must be freezing."
        hide briarstar_standing with fade
        t "..."
        jump ld1_inside

    else:
        t "The leaders' den."
        t "Rumor has it Briarstar is on her last two lives. At the gathering in greenleaf, she was so proud to report that she had all nine ..."
        t "I can't remember the last time I saw her eating a piece of prey."
        t "Come to think of it, I can't remember the last time I saw her at all ..."
        show briarstar_standing with fade
        b "Talonclaw."
        t "Oh!"
        b "I thought I heard somecat talking out here."
        t "I'm so sorry to disturb you, Briarstar. I don't know what I was --"
        b "No need to explain yourself."
        b "Sometimes, there's a certain comfort to hearing your thoughts spoken aloud."
        b "Why don't you step inside my den for a moment? Your paws must be freezing."
        t "That's very kind of you, but you really don't have to --"
        b "Please. I insist. Follow me."
        hide briarstar_standing with fade
        t "... Okay?"
        jump ld1_inside

label ld1_inside:
        scene leaders_den_bg with fade
        show briarstar
        b "It stays quite warm in here all year round, so sometimes, peculiar things will grow."
        b "Mostly mushrooms and other fungi; though, once, the most precious white lily blossomed in that corner right over there."
        t "Is that what you named your daughter after?"
        b "Hm?"
        t "Your daughter? Lilypaw?"
        b "... Oh. Yes. I suppose it is."
        b "That's funny. All these moons since she was born, and I'm just now making that connection."
        b "I just always knew I felt a strong connection to the name 'Lily'."
        t "It must have been a sign from StarClan."
        b "Yes. It must have."
        b "Thank you, Talonclaw."
        b "For helping me discover something new about myself."
        t "... Happy to help."
        b "Talonclaw?"
        t "Yes?"
        if quest_crocus.started:
            b "I must apologize. I'm afraid I invited you in here with an ulterior motive, unrelated to your foraging."
        else:
            b "I must apologize. I'm afraid I invited you in here with an ulterior motive, unrelated to your body temperature."
        b "... I have to ask you for a favor."
        t "Oh! That's alright, Briarstar." 
        t "What is it?"
        b "On your hunt today, can you be sure to bring back something substantial for Pouncetail?"
        if quest_crocus.started or quest_crocus.completed:
            jump ld1_talonclaw_sunshadow
        menu:
            b "If he stands any chance at beating greencough, it's imperative that he keeps his strength up."
            "Accept":
                jump ld1_accept
            "Decline":
                jump ld1_decline

label ld1_accept:
    "{b}Quest Unlocked:{/b} Feed the Deputy"
    $ quest_feed_deputy.started = True
    $ talon_clan_bonus += 2
    t "Sure, Briarstar. No problem."
    t "I'll make sure Pouncetail gets what he needs."
    b "You're a good cat, Talonclaw. I only pray that it helps him recover."
    b "StarClan knows ThunderClan can't afford to lose another deputy. Especially so soon after Squirrelpelt's death."
    t "Yes. Of course. I'm so sorry for your loss."
    t "You and Squirrelpelt were together for moons. His passing must have been devastating."
    b "..."
    b ".........."
    t "I'm sorry. Did I say something wrong?"
    b "... No."
    b "It's okay."
    b "I suppose I am ... {i}devastated.{/i}"
    b "I'm not sure."
    b "I try not to feel things too strongly, these days."
    t "... When was the last time you ate something, Briarstar?"
    b "..."
    b "You have more pressing things to worry about."
    t "You're our leader. The Clan needs you --"
    b "Prey should go to cats who don't have more than one life to lose."
    b "That's my final opinion on the matter."
    t "..."
    b "Come and find me after you've visited Pouncetail. I'd like to know how he's doing."
    t "Oh --"
    hide briarstar with fade
    t "... kay."
    call screen gameUI

label ld1_decline:
    t "I'm sorry, Briarstar. Hunting's been poor."
    t "There's no guarantee that I'll bring anything back to camp today, let alone have enough to spare for Pouncetail."
    t "Even if I did, the medicine cats would have a fit if I broke their quarantine."
    t "They're pretty strict about keeping the sick cats away from the healthy ones."
    b "..."
    b "... Of course."
    b "How foolish of me."
    b "I wasn't aware that cats were being quarantined."
    t "... Locustleaf implemented the policy a few moons ago."
    b "A few moons ago?"
    b "My apologies. I seem to be losing track of time ..."
    t "... When was the last time you ate something, Briarstar?"
    b "..."
    b "You have more pressing things to worry about."
    t "You're our leader. The Clan needs you --"
    b "Prey should go to cats who don't have more than one life to lose."
    b "That's my final opinion on the matter."
    t "..."
    b "I'll be retreating deeper into my quarters. Feel free to stay here as long as you'd like."
    b "I hope you stay well, Talonclaw."
    t "Thank --"
    hide briarstar with fade 
    t "... you."
    call screen gameUI

label ld1_talonclaw_sunshadow:
        b "If he stands any chance against greencough, it's imperative that he keeps his strength up."
        t "... I'm sorry, Briarstar. I'm actually not sure if I'll be able to hunt for the Clan today."
        t "I agreed to help with a burial ceremony for Dapplefeather."
        t "That's what the crocuses are for."
        b "Oh."
        b "..."
        b "Is this because of Sunshadow's speech?"
        t "You heard that from the leader's den?"
        b "Yes. Your friend is a very gifted orator."
        b "Even though you know how I hate the vigils, I must admit I was ... roused by his words."
        b "But rousing words aren't enough to fill empty bellies."
        b "Pouncetail is the deputy of this Clan. ThunderClan can't afford to lose another." 
        b "Especially not so soon after Squirrelpelt's passing."
        menu:
            b "Please, Talonclaw. I know you care for Sunshadow, but are his needs really most important right now?"
            "Stick with helping Sunshadow":
                jump ld1_stick_sunshadow
            "Switch to helping Briarstar":
                jump ld1_switch    
            
label ld1_stick_sunshadow:
    $ talon_sun_bonus +=1
    t "Sunshadow just lost the love of his life."
    t "He needs me."
    b "Talonclaw, there's not a cat left in ThunderClan who hasn't lost something. Who doesn't {i}need{/i} something."
    b "Squirrelpelt's body is rotting in the elders' den right now, alongside those of several of our kits."
    b "If that was all we paid attention to, ThunderClan would never catch another piece of prey."
    t "I'm sorry. I can't just abandon my friend."
    b "..."
    b "... You are loyal to him."
    b "More loyal to him than you are to your own Clan."
    b "Watch your back, Talonclaw."
    b "Loyalty like that is often rewarded with betrayal."
    t "..."
    b "I'll be moving deeper into my quarters. Feel free to stay in my den as long as you'd like."
    b "I hope you find what you're looking for, Talonclaw."
    t "Thank --"
    hide briarstar with fade
    t "... you."
    if quest_crocus.started:
        show screen ld_mushroom
    call screen gameUI

label ld1_click_mushroom:
    t "I don't think this is what Sunshadow is looking for."
    hide screen ld_mushroom
    call screen gameUI
    
label ld1_switch:
    t "... You're right."
    t "I'm sorry, Briarstar. I don't know what's gotten into me."
    t "I'll make sure to get Pouncetail what he needs."
    $ quest_crocus.started = False
    $ quest_crocus.cancelled = True
    $ quest_favorite_prey.started = False
    $ quest_favorite_prey.cancelled = True
    $ quest_nesting_material.started = False
    $ quest_nesting_material.cancelled = True
    $ quest_feed_deputy.started = True
    "{b}Questline Cancelled:{/b} Burial Rites"
    "{b}Quest Unlocked:{/b} Feed the Deputy"
    b "Thank you, Talonclaw. You're a good cat. Loyal to your friend. That's something to be admired."
    b "I hope, once all this is over, the two of you can dig a truly lavish grave together."
    t "Thank --"
    b "Come and find me after you've visited Pouncetail. I'd like to know how he's doing."
    hide briarstar with fade
    t "... you."
    call screen gameUI

label ld_2:
    scene leaders_entrance_day with fade
    show screen gameUI
    stop music fadeout 0.5
    play music "ES_La Vuelta a Lerida - Vendla.mp3" loop
    t "I doubt Briarstar wants anycat disturbing her right now."
    if quest_feed_deputy.started:
        t "I'll come back when I've made sure that Pouncetail's eaten something."
    call screen gameUI

