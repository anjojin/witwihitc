label ld1:
    $ leaders_visited = True
    scene leaders_entrance_day with fade
    show screen gameUI
    stop music fadeout 0.5    
    play music "music/ES_La Vuelta a Lerida - Vendla.mp3" loop
    if quest_crocus.started:
        t "Hmm ... if I were a crocus, where would I be?"
        t "These tree roots seem like as good of a place to grow as any."
        t "Though, how anything manages grow in the middle of a leafbare like this one is beyond me ..."
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        show briarstar_standing with fade
        b "Talonclaw."
        t "Oh!"
        b "I thought I heard somecat talking out here."
        t "I'm so sorry to disturb you, Briarstar. I was just searching around the leader's den for crocuses."
        t "If you're wondering why, it's because --"
        b "No need to explain yourself."
        b "Please. Come inside. You can continue your search there."
        t "That's very kind of you, Briarstar, but you really don't have to --"
        b "It's really no trouble. Follow me."
        b "Your paws must be freezing."
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        hide briarstar_standing with fade
        t "If you insist ..."
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        jump ld1_inside

    else:
        t "The leaders' den."
        t "At the start of the famine, Briarstar used to give these incredible speeches from up here."
        t "'I have seven lives left,' she said, 'and I'll give every last one of them helping my Clan!'"
        t "... Rumor has it she's down to her last two, now."
        t "And I can't remember the last time I saw her give a speech."
        t "Come to think of it, I can't remember the last time I saw her at all ..."
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        show briarstar_standing with fade
        b "Talonclaw."
        t "Oh!"
        b "I thought I heard somecat talking out here."
        t "I'm so sorry to disturb you, Briarstar. I don't know what I was --"
        b "No need to explain yourself. I understand perfectly."
        b "Sometimes, there's a certain comfort in hearing one's own thoughts spoken aloud."
        t "Er ... Yes. I suppose so."
        b "Why don't you step inside my den for a moment?"
        b "Your paws must be freezing."
        t "That's very kind of you, Briarstar, but you really don't have to --"
        b "Please. I insist."
        b "Follow me."
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        hide briarstar_standing with fade
        t "... Okay?"
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        jump ld1_inside

label ld1_inside:
        scene leaders_den_bg with fade
        stop music fadeout 2.0
        play music "music/ES_Little Light - Wanderer's Trove.mp3" loop
        show briarstar
        if not quest_crocus.started:
            b "I hope this moss is soft enough for your liking."
            t "... Of course it is, Briarstar. Thank you."
            t "What a fascinating den you have."
            t "I can see why you spend so much time in it."
            b "Oh. Yes."
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
        b "..."
        b "Talonclaw?"
        t "Yes?"
        if quest_crocus.started:
            b "I must apologize. I'm afraid I invited you in here with an ulterior motive, unrelated to your foraging."
        else:
            b "I must apologize. I'm afraid I invited you in here with an ulterior motive, unrelated to your body temperature."
        b "... I have to ask you for a favor."
        t "Oh! That's alright, Briarstar." 
        t "What is it?"
        b "On your hunt today, can you be sure to bring something substantial back for Pouncetail?"
        if quest_crocus.started or quest_crocus.completed:
            jump ld1_talonclaw_sunshadow
        if quest_gather_herbs.started:
            b "If he stands any chance at beating greencough, it's imperative that he keeps his strength up."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} Hunting for Pouncetail means Talonclaw will no longer be able to complete the following quest: {b}Gather Herbs.{/b}"
            play sound "sfx/game_tip.mp3"
            menu:
                "How would you like to proceed?"
                "Stick with gathering herbs":
                    jump ld1_decline
                "Switch to hunting for Pouncetail":
                    jump ld1_accept
        else:
            menu:
                b "If he stands any chance at beating greencough, it's imperative that he keeps his strength up."
                "Accept":
                    jump ld1_accept
                "Decline":
                    jump ld1_decline

label ld1_accept:
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Feed the Deputy"
    $ quest_feed_deputy.started = True
    $ talon_clan_bonus += 2
    if quest_gather_herbs.started:
        $ quest_gather_herbs.started = False
        $ quest_gather_herbs.cancelled = True
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Quest Cancelled:{/b} Gather Herbs"
    t "Sure, Briarstar. No problem."
    t "I'll make sure Pouncetail gets what he needs."
    b "You're a good cat, Talonclaw. I only pray that it helps him recover."
    b "StarClan knows ThunderClan can't afford to lose another deputy. Especially so soon after Squirrelpelt ..."
    t "Yes. Of course."
    t "And ... I'm so sorry for your loss."
    t "You and Squirrelpelt were together for moons. His passing must have been devastating."
    b "..."
    b ".........."
    t "I'm sorry. Did I say something wrong?"
    b "... No."
    b "It's okay."
    b "I suppose I am ... {i}devastated.{/i}"
    b "I'm not sure."
    b "I try not to feel anything too strongly, these days."
    t "... When was the last time you ate something, Briarstar?"
    b "..."
    b "You have more pressing things to worry about."
    t "You're our leader. The Clan is counting on you to --"
    b "Prey should go to cats who don't have more than one life to lose."
    b "That's my final opinion on the matter."
    t "..."
    b "Come and find me after you've visited Pouncetail. I'd like to know how he's doing."
    t "Wait, but, while I have your ear, there were a few other Clan matters I wanted to speak to you --"
    b "I hope you stay well, Talonclaw."
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide briarstar with fade
    t "..."
    call screen gameUI

label ld1_decline:
    t "I'm sorry, Briarstar. Hunting's been poor lately."
    t "There's no guarantee that I'll bring anything back to camp today, let alone have enough to spare for Pouncetail."
    t "Even if I did, the medicine cats would have a fit if I broke their quarantine."
    t "They're pretty strict about keeping the sick cats away from the healthy ones."
    b "..."
    b "... Of course."
    b "How foolish of me."
    b "I wasn't aware that cats were being quarantined, at all."
    t "... Locustleaf implemented the policy a few moons ago."
    b "A few moons ago?"
    b "My apologies. I seem to be losing track of time ..."
    t "... When was the last time you ate something, Briarstar?"
    b "..."
    b "You have more pressing matters to worry about."
    t "You're our leader. The Clan is counting on you to --"
    b "Prey should go to cats who don't have more than one life to lose."
    b "That's my final opinion on the matter."
    t "..."
    b "I'll be retreating deeper into my quarters. Feel free to stay here as long as you'd like."
    b "I hope you stay well, Talonclaw."
    t "Wait, but, while I have your ear, there were a few other Clan matters I wanted to speak to you --"
    b "I hope you stay well, Talonclaw."
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide briarstar with fade 
    t "..."
    call screen gameUI

label ld1_talonclaw_sunshadow:
        b "If he stands any chance against greencough, it's imperative that he keeps his strength up."
        t "... I'm sorry, Briarstar. I'm actually not sure if I'll be able to hunt for the Clan today."
        t "I agreed to help with a burial ceremony for Spottedlight."
        if quest_crocus.started:
            t "That's what the crocuses are for."
        b "Oh."
        b "..."
        b "Is this because of Sunshadow's speech?"
        t "You heard that from the leader's den?"
        b "Yes. Your friend is a very gifted orator."
        b "Even though you know how I hate the vigils, I must admit I was ... roused by his words."
        b "I can see why the other warriors think so highly of him."
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
    t "... You know, you could show a little more gratitude towards."
    t "Without him out there organizing the patrols, rationing the prey, and giving the warriors something to believe in every day ..."
    t "... This Clan might very well just fall apart."
    t "StarClan knows you aren't doing it any favors."
    b "..."
    b "... You are loyal to him."
    t "Yes."
    b "More loyal to him than you are to your own Clan."
    b "Watch your back, Talonclaw."
    b "Loyalty like that is often rewarded with betrayal."
    t "..."
    b "I'll be moving deeper into my quarters."
    b "Feel free to stay in my den as long as you'd like."
    b "I hope you find what you're looking for, Talonclaw."
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide briarstar with fade
    t "..."
    if quest_crocus.started:
        show screen ld_mushroom
    call screen gameUI

label ld1_click_mushroom:
    $ herbs_clicked += 1
    if herbs_clicked == 5:
        $ botanist.grant()
    play audio "sfx/plant_error.mp3"
    t "I don't think this is what Sunshadow is looking for."
    hide screen ld_mushroom
    call screen gameUI
    
label ld1_switch:
    t "... You're right."
    t "I'm sorry, Briarstar. I don't know what's gotten into me."
    t "I'll make sure to get Pouncetail what he needs."
    if quest_crocus.started:
        $ quest_crocus.started = False
        $ quest_crocus.cancelled = True
    $ quest_favorite_prey.started = False
    $ quest_favorite_prey.cancelled = True
    if quest_nesting_material.started:
        $ quest_nesting_material.started = False
        $ quest_nesting_material.cancelled = True
    $ quest_feed_deputy.started = True
    play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
    "{b}Questline Cancelled:{/b} Burial Rites"
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Feed the Deputy"
    b "Thank you, Talonclaw. You're a good cat. Loyal to your friend. That's something to be admired."
    b "I hope, once all this is over, the two of you can dig a truly lavish grave together."
    t "Thank you, Briarstar."
    t "Oh -- and while I have your ear, there were a few other Clan matters I wanted to speak to you about."
    t "Sunshadow's been organizing all the patrols, and I think it might be helpful if --"
    b "Thank you, Talonclaw. That will be all."
    b "Come and find me after you've visited Pouncetail. I'd like to know how he's doing."
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide briarstar with fade
    t "..."
    call screen gameUI

label ld_2:
    scene leaders_entrance_day with fade
    show screen gameUI
    stop music fadeout 0.5
    play music "music/ES_La Vuelta a Lerida - Vendla.mp3" loop
    t "I doubt Briarstar wants to see me back so soon."
    if quest_feed_deputy.started:
        t "I'll come back once I've made sure that Pouncetail's eaten something."
    call screen gameUI

label ld3:
    if quest_feed_deputy.completed or quest_feed_deputy.cancelled or quest_feed_deputy.failed:
        jump ld3_feed_dep
    else:
        stop music fadeout 0.5
        play music "music/ES_La Vuelta a Lerida - Vendla.mp3" loop
        scene ld ext night with fade
        show screen gameUI
        t "I don't think Briarstar wants to see me right now."
        if quest_feed_deputy.started:
            t "I'll see her after I deliver Pouncetail's meal to him in the medicine den, just like I promised."
        call screen gameUI

label ld3_feed_dep:
    stop music fadeout 0.5
    play music "music/ES_Little Light - Wanderer's Trove.mp3" loop
    scene leaders int night with fade
    show briar_night_lay
    b "Talonclaw."
    b "You're back already?"
    t "Um ... Already?"
    t "Briarstar, it's been hours since we last talked."
    t "The entire day has nearly passed."
    b "Has it?"
    b "Oh. Would you look at that?"
    b "It's dark outside."
    b "Night's fallen so quick ..."
    b "Tell me, Talonclaw, do the days feel any longer to you?"
    b "We've already passed the solstice, and yet, nothing seems to have changed."
    t "The nights are getting shorter in their own time, even if it's not enough for us to notice yet."
    t "Trust in StarClan. Better times are on their way."
    b "..."
    b "... Did you visit Pouncetail?"
    if quest_feed_deputy.completed:
        jump ld3_feed_dep_complete
    else:
        t "... No."
        t "I'm sorry."
        t "I really tried my best to, because I know how important this is, but other things just kept coming up, and --"
        b "Talonclaw."
        b "It's okay."
        b "Really."
        b "You don't need to justify yourself to me."
        t "But ... aren't you angry?"
        t "I failed to do what you asked of me."
        t "Aren't you wondering why?"
        b "I don't really ... {i}wonder{/i} things, anymore."
        b "I find that {i}wondering{/i}, more often than not, originates from a place of fear ..."
        b "... And, well, I can't quite remember how it feels to be afraid."
        b "I've forgotten how to do it."
        b "The racing heartbeat ..."
        b "The flood of metal over the tongue ..."
        b "I can conjure it up in words, but somehow I can't quite manage to inhabit it for real."
        t "... You're just exhausted."
        t "We all are."
        t "Maybe looking ahead to the future would help."
        t "Have you given any thought to who's going to be next in line to lead the Clan?"
        t "Sunshadow seems like a natural choice. All the warriors look up to him so much, already."
        if talon_sun_bonus<0:
            t "But, I'd be happy to talk through other options, as well, if you're interested ..."
        b "..."
        b "... You're right, Talonclaw."
        b "I am ..."
        b "... {i}exhausted.{/i}"
        b "That's exactly right."
        b "I've been searching for that term for moons, but could never quite find it."
        b "{i}'Exhausted' ...{/i}"
        b "You know, you really have a way with words."
        b "I can see why you and Sunshadow are friends."
        t "Briarstar --"
        b "Please excuse me, Talonclaw."
        t "But --"
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        hide briar_night_lay with fade
        t "..."
        call screen gameUI

label ld3_feed_dep_complete:
    t "Yes."
    t "I brought him a fresh meal, like you asked, but ..."
    t "... I don't think he ate it."
    t "In fact, I don't think he noticed my presence, at all."
    b "Hmm."
    b "Yes. It makes sense."
    b "Squirrelpelt was like that, too. Towards the end."
    t "... It might be time to seriously consider choosing a new deputy, Briarstar."
    t "Have you given any thought to it?"
    t "Who's going to be next in line to lead the Clan?"
    b "..."
    hide briar_night_lay
    show briar_night_sit
    stop music fadeout 5.0
    b "... What do you think about me attending the vigils, again?"
    b "I've spent the whole day thinking about what I'm going to say at Pouncetail's."
    t "That's ..." 
    t "That's wonderful."
    t "Your Clanmates will be happy to see you again."
    b "It {i}isn't{/i} wonderful."
    b "Not at all ..."
    b "I fear that all the time I've spent alone in my den has weakened my facility for language ..."
    b "No matter how I try, I just can't seem to come up with the right words to honor Pouncetail's memory ..."
    b "I can't appear before the warriors like this."
    b "... Perhaps you could help me, Talonclaw?"
    t "Help you, how?"
    b "I'll deliver what I have eulogy, and whenever I pause, you can suggest the word that you think best ..."
    b "..."
    b "..............."
    t "... Fits?"
    b "See? You're already a natural."
    b "Let's begin."
    b "Ahem ..."
    jump briar_eulogy_start

label briar_eulogy_start:
    play music "music/ES_The Narrow Path - Daniel Kaede.mp3"
    $ eulogy_mistakes = 0
    b "Pouncetail was my apprentice."
    b "I was with him from his sixth moon until he graduated early, on his tenth."
    b "Four moons may not seem like a very long time to form a connection with a cat, but it's a period of my life I still look back on very fondly."
    menu:
        b "Though I hate to say it, because '... ... ...', I learned from Pouncepaw just as much as I had to teach him."
        "'it's embarrassing'":
            jump briar_eulogy_incorrect
        "'I hate cliches'":
            jump briar_eulogy_cont1
        "'it's only half-true'":
            jump briar_eulogy_incorrect

label briar_eulogy_cont1:
    menu:
        b "Even now, when I look into his face, I just see that plucky young cat who never seemed to ..."
        "'... give up on what was right.'":
            jump briar_eulogy_incorrect
        "'... stop fighting.'":
            jump briar_eulogy_incorrect
        "'... run out of things to say.'":
            jump briar_eulogy_cont2

label briar_eulogy_cont2:
    b "I can still picture that greenleaf so clearly."
    b "The stench of growth."
    b "The oppressive heat."
    menu:
        b "The '...' coating our pelts in a film."
        "'sweat'":
            jump briar_eulogy_cont3
        "'salt'":
            jump briar_eulogy_incorrect
        "'rain'":
            jump briar_eulogy_incorrect

label briar_eulogy_cont3:
    menu:
        b "I used to think, what does '...' exist for, if not for cats like him?"
        "'the future'":
            jump briar_eulogy_cont4
        "'ThunderClan'":
            jump briar_eulogy_incorrect
        "'the Warrior Code'":
            jump briar_eulogy_incorrect

label briar_eulogy_cont4:
    b "When he spoke of his plans, his eyes would shimmer like he could see the moons unfurling right in front of his paws."
    b "He wanted to catch a lizard one day, he said."
    b "He wanted to know what they tasted like."
    menu:
        b "Now, Pouncetail ..."
        "'has passed away.'":
            jump briar_eulogy_incorrect
        "'is dead.'":
            jump briar_eulogy_cont5
        "'has joined his warrior ancestors.'":
            jump briar_eulogy_incorrect

label briar_eulogy_cont5:
    b "And, try as I might, I can't come up with an explanation as to why."
    b "I know some of you may think I've failed you as a leader."
    menu:
        b "That it was my '...' that caused this famine."
        "'lack of foresight'":
            jump briar_eulogy_cont6
        "'poor decision making'":
            jump briar_eulogy_incorrect
        "'inflexibility'":
            jump briar_eulogy_incorrect

label briar_eulogy_cont6:
    b "I've only ever tried to do what was best for every cat under my leadership."
    b "But maybe, there was something else I could have done ..."
    b "Something more ..."
    b "Something differently ..." 
    b "... that would have stopped any of this from happening."
    b "I don't know."
    b "I'm not sure if that's true."
    b "Maybe it isn't."
    b "But what I do know is ..."
    b "Pouncetail will never know the taste of lizard, now."
    b "And, if that was because of me, then I hope he knows that I didn't do it on purpose."
    stop music fadeout 5.0
    b "I would've caught a lizard for him."
    b "I would've hunted down every last lizard in the forest."
    hide briar_night_sit
    show briar_night_lay
    if eulogy_mistakes == 0:
        $ silver_tongue.grant()
    "{b}BEGIN ILLUSTRATION HERE{/b}"
    b "..."
    t "..."
    t "... That's it?"
    t "That's all you have to say?"
    t "Nothing about who's going to take over as deputy?"
    t "Who's next in line to lead the Clan?"
    play music "music/ES_A Subtle Reflection - Daniel Kaede.mp3" loop
    b "... I'm very tired, Talonclaw."
    t "Great StarClan."
    t "You have no idea, do you?"
    t "Cats are dying out there, Briarstar! They need answers!"
    t "If you're not going to lead them, the least you can do is put someone in power who will!"
    t "It's your duty!"
    b "..."
    b "'Duty.'"
    b "Yes. It makes sense that you would be concerned with duty."
    b "After all ..."
    b "You've never died."
    b "Not even once."
    b "When you don't know how it feels to die, your mind develops this remarkable propensity for torturing itself over vague concepts."
    b "'Duty' being one of them."
    b "But I've left all of that behind with my old body."
    b "I've left it behind seven times over."
    b "I don't have any illusions about where I'm going when all of this is over, Talonclaw."
    b "I know how I'll be remembered."
    b "'The leader who destroyed ThunderClan with her naivete.'"
    b "'Who gave shelter to dozens and couldn't even be bothered to regret it.'"
    b "'Who was never worried enough.'"
    b "None of you could see just how terrified I was when those first snows hit."
    b "When all of this began."
    b "How could I possibly lead these cats, I thought, when I'm just as sick and scared as they are?"
    b "The simple answer was, I couldn't."
    b "Now, Squirrelpelt is dead, and so are all but one of our kits."
    b "And I finally understand just how little point there is to worrying about things that can't be changed."
    b "Nothing can stop what happens now, Talonclaw."
    b "If Sunshadow wants ThunderClan next, he can take it."
    b "He can take all the pain and the heartbreak that comes with it, too."
    b "As for me, I'll be a blade of grass ..."
    b "A cough in the wind ..."
    scene black with fade
    b "A moonbeam ..."
    "{b}END GAME{/b}"
    $ MainMenu(confirm=False)()

label briar_eulogy_incorrect:
    $ eulogy_mistakes += 1
    if eulogy_mistakes==5:
        jump briar_eulogy_end
    else:
        b "Hmm ... No, I don't think that's quite what I was looking for."
        b "Let's keep going."
    jump briar_eulogy_cont1

label briar_eulogy_end:
    stop music fadeout 5.0
    b "..."
    b "... Thank you Talonclaw."
    t "... That's it?"
    t "Is that all you have to say?"
    b "No. It isn't."
    b "But thank you, anyway."
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide briar_night_sit with fade
    t "..."
    play sound "sfx/quest_unlocked.mp3"
    $ quest_feed_deputy.started = False
    $ quest_feed_deputy.completed = True
    "{b}Quest Completed:{/b} Feed the Deputy"
    call screen gameUI

label ld4:
    stop music fadeout 0.5
    play music "music/ES_La Vuelta a Lerida - Vendla.mp3" loop
    scene ld ext night with fade
    show screen gameUI
    t "I don't think Briarstar wants to see me right now."
    if quest_feed_deputy.started:
        t "I'll see her after I deliver Pouncetail his prey in the medicine den, like I promised."
    call screen gameUI