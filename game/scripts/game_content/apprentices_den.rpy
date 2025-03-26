label ad1:
    $ apprentice_visited = True
    scene app_den_bg with fade
    stop music fadeout 1.0
    play music "music/ES_Unbounded Horizons - Victor Lundberg.mp3" loop
    show screen gameUI
    t "It's always nice to check up on how the Clan's future warriors are doing."
    menu:
        t "I wonder just what they're up to, in there ..."
        "Eavesdrop":
            jump ad1_eavesdrop
        "Leave them alone":
            jump ad1_leave_alone

label ad1_eavesdrop:
    play sound "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    "You strain your ears, picking up on the apprentices' familiar voices."
    play audio "sfx/meow1.mp3"
    c "StarClan, Redpaw, if I have to hear one more word --"
    r "I'm exercising my free will! I have the right to refuse anything I don't --"
    c "Free will? Are you serious?"
    r "I'm just saying it's not hygenic! What's the problem?"
    c "The problem is that your sister went out of her way to get this snow for you to drink, and now you're letting it go to waste."
    r "I don't want to drink something that's been in another cat's mouth! Is that so wrong?"
    fa "That's why I put it on a leaf, mouse-brain!"
    c "You hear that? That's why she put it on a leaf."
    r "You don't know where that leaf has been!"
    c "It's a {i}leaf!{/i} You're a ThunderClan apprentice, and you're telling me you're afraid of a ..."
    c "Ah ..."
    play audio "sfx/ES_Female, Sneezeing - Epidemic Sound - 0000-1518.mp3"
    c "Ah-CHOO!"
    r "See? Your argument is so stupid, your own body is allergic to it."
    c "Is {i}your{/i} body allergic to my paws in your face?"
    fa "Cloverpaw, wait!!!"
    play audio "sfx/ES_Hiss, Angry - Epidemic Sound.mp3"
    r "AHHHHH!"
    li "EVERYONE STOP FIGHTING!!!"
    li "StarClan, you're all driving me crazy!"
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    show lilypaw_entrace with fade
    li "... Eep!"
    li "T-Talonclaw! Hello!"
    fa "Talonclaw's outside?"
    c "Talonclaw!"
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide lilypaw_entrace with fade
    show cloverpaw_ad1 with easeinright
    show fawnpaw_ad1 with easeinright
    show redpaw_left with easeinleft
    show lilypaw_ad1 with easeinleft
    fa "Talonclaw!!!"
    t "Hey, kittos."
    t "Sounded like some battle in there."
    fa "Oh, this one was actually pretty tame. Usually, it takes twice as long to pull those two apart."
    r "Slowing down lately, Cloverpaw?"
    c "Slowing down? Tch, I was just getting started. You're lucky Talonclaw showed up when he did, or else I would've shredded you."
    r "Right ... that's probably why I won our last three mock-battles, too."
    play audio "sfx/ES_Retro Game, Gun Shot - Epidemic Sound.mp3" volume 0.5
    c "{i}*STOMP*{/i}"
    menu:
        r "Oww!"
        "Side with Redpaw":
            jump ad1_side_red
        "Side with Fawnpaw and Cloverpaw":
            jump ad1_side_clover
        "Stay out of it":
            jump ad1_stayout

label ad1_side_red:
    $ red_hunting_chance -=1
    $ clover_hunting_chance += 1
    t "You probably shouldn't be fetching snow for other cats with all the contagion going around right now, Fawnpaw."
    t "It isn't hygenic."
    r "Hahaha! See? That's exactly what I said!"
    c "Stuff a feather in it, Redpaw."
    t "... It probably isn't the best idea to pick petty fights with your denmates, either, Cloverpaw."
    c "Hmph ..."
    jump ad1_cont

label ad1_side_clover:
    $ fawn_hunting_chance -=1
    $ red_hunting_chance += 1
    t "It isn't nice to refuse a gift from your sister, Redpaw."
    t "Especially when she went out of her way to get it for you in this cold."
    r "Hmph ..."
    c "... That's it? 'Hmph'?"
    c "No, 'I'm sorry, Fawnpaw?'"
    c "No, 'I promise to stop being an arrogant mouse-brain?'"
    t "... It probably isn't the best idea to pick petty fights with your denmates, either, Cloverpaw."
    c "Whuh?"
    jump ad1_cont

label ad1_stayout:
    t "Haha! You guys crack me up." 
    t "This takes me back to my own apprentice days. My denmates used to drive me up the wall."
    jump ad1_cont

label ad1_cont:
    fa "I think we've all just gone a little stir-crazy from being stuck in camp all the time."
    r "Seriously. I haven't had a real training session since Flipcloud moved into the medicine den." 
    fa "Yeah. And my mentor keep ditching me to go on patrol with the other warriors."
    fa "Apparently ThunderClan 'can't afford to have inexperienced hunters scaring off all the prey.'"
    fa "As if there's any prey out there to begin with ..."
    r "Say ... maybe you could take us out later, Talonclaw."
    c "Ooh! Yeah! That'd be awesome!"
    r "It could be just like a regular hunting patrol, only we'd be there to help you."
    fa "We swear, we won't let you down! We've all been practicing."
    r "Yeah. Cloverpaw's made an excellent mock mouse."
    play audio "sfx/ES_Retro Game, Gun Shot - Epidemic Sound.mp3" volume 0.5
    c "{i}*STOMP*{/i}"
    r "Ha. Missed me that time."
    t "I don't know, you guys ..."
    if quest_favorite_prey.started:
        t "I kind of agreed to do this thing for Sunshadow today ..."
    fa "Come on! What have you got to lose?"
    play sound "sfx/game_tip.mp3"
    "{b}Game Tip:{/b} Hunting with the apprentices will {b}increase{/b} the number of opportunities you have at catching prey."
    play sound "sfx/game_tip.mp3"
    "However, it will also {b}decrease{/b} your odds of success."
    play sound "sfx/game_tip.mp3"
    if quest_gather_herbs.started:
            play sound "sfx/game_tip.mp3"
            "It will also mean you can no longer complete the following questline: {b}Gather Herbs{/b}"
            menu:
                "How would you like to proceed?"
                "Stick with finding catmint":
                    jump ad1_no
                "Switch to patrolling with the apprentices":
                    jump ad1_yes
    else:
        menu:
            "Do you accept?"
            "Yes":
                jump ad1_yes
            "No":
                jump ad1_no 

label ad1_yes:
    $ quest_babysitting.started = True
    $ training_with = ["hunting_red", "hunting_lily", "hunting_fawn", "hunting_clover"]
    t "Aw, sure. You guys can come out with me today. Why not?"
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Adult Supervision"
    if quest_gather_herbs.started:
        $ quest_gather_herbs.started = False
        $ quest_gather_herbs.cancelled = True
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Quest Cancelled:{/b} Gather Herbs"
    fa "Yes! Thank you!"
    c "Hahaha! I'm gonna catch so much, we won't be able to carry it all home!"
    r "That's kind of unrealistic, Cloverpaw."
    c "Can you allow joy to exist in your vicinity for, like, one second without getting your melancholy all over it, Redpaw?"
    r "Nyehh."
    t "... Lilypaw? You've been awfully quiet. Do you have anything to say?"
    li "..."
    li "I ..."
    li "I'll do my best."
    t "That's all I can ask for."
    li "{i}*Smile*{/i}"
    t "Alright, then. I'll meet you all on the territory when I'm ready to get started."
    t "Until then, try not to injure each other."
    c "Not making any promises."
    r "Cloverpaw!"
    c "What? I'm just trying to be {i}realistic.{/i}"
    fa "We promise you won't regret this, Talonclaw."
    t "I might be starting to, already ..."
    if quest_crocus.started:
        show screen ad_juniper
    call screen gameUI

label ad1_no:
    t "Ah ... I'm sorry, guys."
    menu:
        t "I can't take you out because ..."
        "... of your mentors":
            jump ad1_mentors
        "... you wouldn't like it":
            jump ad1_polite
        "... it's too risky":
            jump ad1_risk
        "... I'm already committed" if quest_favorite_prey.started or quest_gather_herbs.started:
            jump ad1_committed

label ad1_leave_alone:
    t "Probably best not to disturb them. Especially when there's so much other work to be done."
    t "Maybe I'll run into them later."
    if quest_crocus.started:
        show screen ad_juniper
    call screen gameUI

label ad1_mentors:
    $ talon_clan_bonus += 1
    t "It's just not my place to patrol with you. That's your mentors' jobs."
    r "My mentor has been in the medicine den for moons now, and no cat's assigned me a new one. How is that fair?"
    fa "Even if you were assigned a new one, they probably wouldn't take you out, anyways!"
    fa "No matter how hard you try to prove to them that you're ready!"
    t "I'm sorry, guys. Those are just the rules."
    c "Screw the rules! We're healthy! We want to hunt! ThunderClan isn't fed on technicailities!"
    r "Yeah!"
    jump ad1_no_finish

label ad1_polite:
    $ talon_clan_bonus -= 1
    t "Patrolling isn't all it's cracked up to be."
    t "You should consider all yourselves lucky to get to relax around camp all day while the rest of us freeze our tails off out there."
    c "... What?"
    c "Our Clanmates and kin are dying. We just want to help, and you're telling us it's 'not all it's cracked up to be?'"
    c "How old do you think we are?"
    r "Unbelievable. You know, this is why things never get better. Because cats like you refuse to take our ideas seriously."
    c "This is slander!"
    r "It's an outrage!"
    jump ad1_no_finish

label ad1_risk:
    t "I'm sorry. Prey is scarce enough as it is. You guys may feel like seasoned hunters now, but the truth is, you're still lacking experience."
    c "Well, when are we supposed to get the experience? At this rate, we'll be 20 moons old before we graduate!"
    r "This is completely unfair. How can you say it's too risky when you haven't even given us a chance?"
    c "It's an outrage!"
    r "It's criminal!"
    jump ad1_no_finish

label ad1_committed:
    if quest_favorite_prey.started:
        $ talon_sun_bonus += 1
        t "I'm already committed. I've gotta catch a piece of prey for Dapplefeather before she's buried."
        c "You guys are gonna bury Dapplefeather?"
        c "My sisters haven't been buried yet, and they croaked moons ago. Can you throw them in there, too?"
        r "Why can't we come with you to hunt for Dapplefeather? All you need is one piece of prey, right?"
        jump ad1_risk
    if quest_gather_herbs.started:
        t "I'm already committed. I've gotta look for catmint to help Sunshadow's sick kits."
        c "Sunshadow's kits are sick?"
        fa "My father has been sick for moons. Could you find some catmint for him, too?"
        r "This is ridiculous. You're a warrior, not a medicine cat. You're really going to put your personal needs over the needs of the Clan?"
        c "It's an outrage!"
        r "It's criminal!"
        jump ad1_no_finish

label ad1_no_finish:
    fa "... Lilypaw. You've been quiet."
    fa "Do you have anything to say?"
    li "..."
    li ".........."
    li "I'm tired of the fighting."
    li "I'm going back inside."
    play audio "sfx/slideup.mp3"
    hide lilypaw_ad1 with moveoutleft
    fa "Lilypaw, wait!"
    play audio "sfx/slideup.mp3"
    hide fawnpaw_ad1 with moveoutright
    c "Tch. Whatever. I don't know why I even bother."
    play audio "sfx/slideup.mp3"
    hide cloverpaw_ad1 with moveoutright
    r "... I expected more from you."
    play audio "sfx/slideup.mp3"
    hide redpaw_left with moveoutleft
    t "Tch ..."
    t "Awfully dramatic, those young cats."
    t "One day, they'll know better."
    t "Once somecat actually gets around to teaching them ..."
    if quest_crocus.started:
        show screen ad_juniper
    call screen gameUI

label ad1_click_juniper:
    play audio "sfx/plant_error.mp3"
    t "It's purple, and it's a flower ... but it's not quite a crocus."
    t "I'd better keep looking."
    hide screen ad_juniper
    call screen gameUI

label ad2:
    t "It's probably best not to disturb the apprentices right now."
    if quest_babysitting.started:
        t "I'll see them when I'm ready to patrol."
    if quest_crocus.started:
        show screen ad_juniper
    call screen gameUI
