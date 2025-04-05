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
    fa "Oh, this one was actually pretty tame."
    fa "Usually, it takes twice as long to pull those two apart."
    r "Slowing down lately, Cloverpaw?"
    c "Slowing down? Tch, I was just getting started."
    c "You're lucky Talonclaw showed up when he did, or else I would've shredded you."
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
    scene app_den_bg with fade
    stop music fadeout 1.0
    play music "music/ES_Unbounded Horizons - Victor Lundberg.mp3" loop
    show screen gameUI
    t "It's probably best not to disturb the apprentices right now."
    if quest_babysitting.started:
        t "I'll see them when I'm ready to patrol."
    if quest_crocus.started:
        show screen ad_juniper
    call screen gameUI

label ad3:
    $ apprentice_visited_postp = True
    scene app den night with fade
    stop music fadeout 1.0
    play music "music/ES_The Coldest Water - Headlund.mp3" loop
    show screen gameUI
    if quest_check_clover.started:
        jump ad3_check_clover
    else:
        if quest_report_clover.completed:
            play sound "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
            "The faint voices of the apprentices drift towards the entrance of the den."
            r "Think she'll be alright?"
            fa "Of course she will."
            fa "She's so hard-headed. No way she'd ever let something this stupid kill her."
            r "... You're right."
            r "I'm sure she'll be back to driving us crazy in no time."
            r "Let's just enjoy the peace and quiet while we can."
            t "..."
            call screen gameUI
        if quest_babysitting.cancelled:
            show clover_sit_n with easeinbottom
            t "Cloverpaw?"
            t "What are you doing out here all by yourself?"
            c "... Couldn't sleep."
            c "Where were you earlier?"
            c "We waited by the camp entrance for you for ages, but you never showed."
            t "Ah ... I'm sorry, kitto."
            t "I had to go on an emergency herb hunting trip for Locustleaf."
            if quest_miracle_worker.started:
                menu:
                    c "Did you manage to find what you were looking for?"
                    "Offer Cloverpaw catmint":
                        jump ad3_offer_catmint
                    "Deny":
                        jump ad3_deny
            else:
                jump ad3_deny
        else:
            jump ad4

label ad3_deny:
    t "... No."
    c "Ha. Serves you right."
    c "You shoulda seen how devastated Lilypaw was when she realized you weren't coming."
    c "It was like watching a ..."
    c "Ah ..."
    play audio "sfx/ES_Female, Sneezeing - Epidemic Sound - 0000-1518.mp3"
    c "AH-CHOO!"
    t "You alright?"
    c "*Sniff* Fine."
    c "You'll take us out tomorrow to make up for it, right?"
    t "... We'll see."
    t "But you'll have to get plenty of rest, first."
    c "Fine."
    c "'Night, Talonclaw."
    t "Good night, Cloverpaw."
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide clover_sit_n with fade
    t "..."
    call screen gameUI

label ad3_offer_catmint:
    t "... I did, actually."
    t "I have it here with me. Take a look."
    c "..."
    c "... Is that what I think it is?"
    t "Catmint. Straight from the territory."
    t "It's yours, Cloverpaw."
    c "What do you mean?"
    t "I mean, I want you to have it."
    c "Are you insane? What would you want to do a thing like that for?" 
    c "I'm perfectly healthy!"
    t "I don't know! I mean, I just heard you sneezing earlier, and figured maybe --"
    c "Oh, so he can't even be bothered to take me on patrol, but after hearing me sneeze one time, suddenly, he wants to play the hero."
    c "Get real, Talonclaw. You'd better give those herbs to somecat who actually needs them."
    c "Or else, I might just have to knock the sense back into you myself."
    t "But --"
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide clover_sit_n with fade
    t "... *Sigh*"
    call screen gameUI

label ad3_check_clover:
    play sound "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    "The faint voices of the apprentices drift towards the entrance of the den."
    fa "... Are you {i}sure{/i} you're okay?"
    c "Stars, not this again."
    c "How many times do I have to tell you this? I'm perfectly fi--"
    t "Cloverpaw?"
    c "..."
    t "I know you're in there. Come outside. I want to talk to you."
    c "..."
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    show clover_sit_n with fade
    c "... Go away. I'm busy."
    t "Busy doing what?"
    c "Dying, apparently."
    t "Not funny."
    c "I disagree. What do you want?"
    t "I just ... came to say hello, I guess."
    c "'Hello.'"
    hide clover_sit_n
    show clover_stand_n
    c "There, we said it. Can I go back inside, now? It's freezing."
    t "Not so fast."
    hide clover_stand_n
    show clover_sit_n
    c "..."
    t "How are you holding up?"
    t "Have there been any changes since we last talked?"
    c "Well, I've been communing with my warrior ancestors, and they helped me find the healing power of friendship, so I guess you could say I'm basically cured."
    t "Come on, Cloverpaw."
    t "Talk to me."
    c "I {i}am{/i} talking."
    t "How long do you think you can avoid this?"
    hide clover_sit_n
    show clover_roll_n
    c "Until the sun explodes. Until my teeth fall out."
    c "I'm young. I'm spry. I think I've got a while."
    t "Every cat thinks they've got a while."
    c "Oh, suddenly, he's the lifespan expert."
    c "Remind me of something, Talonclaw: how many family members have you lost in the past five moons?"
    c "Oh, wait. I forgot. You're an orphan."
    c "Pulled that thorn out of your paw early, didn't you?"
    t "Now, you're just being mean."
    c "Sorry. I'm a little bit on edge."
    menu:
        c "I think it's the whole 'I'm dying' of it all."
        "Encouragement":
            jump ad3_reason
        "Empathy":
            jump ad3_empathy
        "Harsh":
            jump ad3_harsh

label ad3_encouraging:
    t "C'mon. Don't be so defeatist."
    t "You can still beat this thing if you face it head-on."
    hide clover_roll_n
    show clover_stand_n
    c "Oh, yeah? You got any spare catmint lying around?"
    jump ad3_cont

label ad3_empathy:
    t "... I'm so sorry, Cloverpaw."
    t "I didn't get the chance to say if before, but I really do feel for you."
    t "I can't even imagine how scared and alone you must be feeling ..."
    hide clover_roll_n
    show clover_stand_n
    c "Yeah? Why don't I cough on you, and it'll give you an idea?"
    jump ad3_cont

label ad3_harsh:
    t "Will you please cut it with the remarks?"
    t "This doesn't just affect you, you know."
    t "There's a whole den of cats in there whose futures could be cut short by your refusal to grow up."
    hide clover_roll_n
    show clover_stand_n
    c "You think I don't know that?"
    c "When I came back from the clearing, all of them had already moved their nests to the other side of the den."
    c "I thought I could at least pretend things were normal for a little while longer, but now I'm going to die {i}and{/i} they all hate me."
    t  "Don't say that."
    jump ad3_cont

label ad3_cont:
    t "I thought we agreed we weren't going to panic until we knew for sure that this was serious."
    hide clover_stand_n 
    show clover_sit_n
    c "Yeah. And, for tonight, that agreement is perfect. Because we still don't know."
    c "But who knows what tomorrow will bring?"
    scene silverpelt with fade
    c "... Can I ask you something kinda pathetic?"
    t "Go for it."
    c "Okay."
    c "Do you ..."
    c "Do you think you could get Briarstar to do my warrior ceremony early?"
    t "... I don't know if Briarstar is up for any kind of ceremony right now."
    t "In fact, I'd be a bit shocked if she even remembers who your mentor is."
    c "Heh."
    c "Figures."
    c "All praise to our glorious leader."
    t "Come on. She may not be all there, but StarClan chose her for a reason."
    c "StarClan must not know what they're doing, then."
    c "... Must be getting awfully crowded up there."
    c "Do you believe in what Sunshadow was saying, earlier?"
    menu:
        c "That they're having as rough a go as we are?"
        "Yes":
            jump ad3_yes
        "No":
            jump ad3_no 
        "I don't know":
            jump ad3_idk

label ad3_yes:
    t "... I do."
    t "The StarClan I knew would have never put ThunderClan through something like this."
    t "They would have sent a prophecy. Or an omen. I don't know. Just ... something."
    t "They wouldn't just sit back and let it happen."
    c "StarClan's let bad things happen before, though, haven't they?"
    c "Other outbreaks. Other accidents. All the wars between the Clans."
    c "Think they were powerless then, too?"
    t "... I guess I'm not sure."
    jump ad3_cont2

label ad3_no:
    t "... I don't."
    t "StarClan, Sunshadow'd probably burst a blood vessel if he heard me saying that. But it's true."
    t "I guess there's just something comforting about believing that there's still a paradise up there, waiting for us."
    t "Especially while there's so much suffering down below."
    c "Why do you think they let this happen, then?"
    t "... I guess I'm not sure."
    jump ad3_cont2

label ad3_idk:
    t "... I guess I don't know."
    jump ad3_cont2

label ad3_cont2:
    t "None of us will never really know, until we join them up there."
    t "It's always been sort of mysterious how they work."
    c "... Do you think StarClan cats get the chance to grow up?"
    c "Like, when kits die, do they stay kits forever, or will they eventually become warriors?"
    t "That's an interesting question, Cloverpaw."
    t "I guess I never really thought about it."
    c "... Will {i}I{/i} ever get the chance to grow up?"
    c "Will I ever master my front paw blow, or will I screw it up for all eternity?"
    c "Will I understand more, when I'm up there?"
    c "Will I be braver?"
    c "Or is this just ... it?"
    c "This is the sad, stupid version of my soul that's going to be beamed up into the sky and preserved forever."
    c "The kits will look up to me at night:"
    c "'Who did that star used to be, Mommy? A great Clan leader? A noble war hero?'"
    c "'Oh, no, little one. That's just Cloverpaw. The apprentice who couldn't quite hack it.'"
    c "'Unless by 'hack it', you mean 'hack up both of her lungs.''"
    stop music fadeout 5.0
    t "..."
    c "Oh, c'mon. You can't deny that that was funny."
    c "Sad and funny."
    t "..."
    t "Crouch down."
    c "What?"
    t "Crouch down and be quiet."
    t "It's time for your warrior ceremony."

label ad3_ending:
    play music "music/ES_Infinite Love - Vendla.mp3"
    "{b}BEGIN ILLUSTRATION HERE{/b}"
    c "But - I thought you said --"
    t "Briarstar doesn't have to know. I doubt it will make much of a difference to her, anyways."
    t "You can tell your friends I took you to her den and had her do it special."
    t "Keep vigil in the clearing tonight."
    c "T-Talonclaw, this is really nice, and all, but I don't know if I really --"
    t "Too late! It's already happening."
    t "Nothing can stop it, now."
    c "But --"
    t "Shh! You're not supposed to talk during your ceremony!"
    c "{i}*Snrk*{/i}"
    c "Okay, okay ... I'm crouching."
    t "Good. Now."
    t "Have you thought of a warrior name that you like?"
    c "Oh, c'mon."
    c "That's totally cheating!"
    t "Don't lie. You've probably had one picked out for moons."
    c "..."
    c "... Cloverfang."
    t "Ohh. {i}Cloverfang.{/i}"
    t "That's a good one."
    t "Alright. Now, close your eyes."
    c "I don't think that's part of the --"
    t "Just trust me."
    c "..."
    c "Okay. They're closed."
    t "Good. Now."
    t "Imagine yourself standing in the shadow of the hightree."
    t "It's a greenleaf day, and the sweat is sticking to your pelt, but you can't tell if it's from the heat, or just the excitement."
    t "Your friends and family are gathered all around you, adorning you with flowers, grooming your fur until it shines."
    t "Finally, Briarstar emerges from her den."
    t "The entire camp falls silent."
    t "She looks down at you and says:"
    b "I, Briarstar, leader of ThunderClan, call upon my warrior ancestors to look down on this apprentice."
    b "She has trained hard to understand the ways of your noble code, and I commend her to you as a warrior in her turn."
    b "Cloverpaw, do you promise to uphold the warrior code and to protect and defend your Clan, even at the cost of your life?"
    c "I do."
    c "I really, really do."
    b "Then by the powers of StarClan, I give you your warrior name."
    b "Cloverpaw, from this moment you will be known as Cloverfang."
    b "StarClan honors your courage, and we welcome you as a full warrior of ThunderClan."
    scene black with fade
    cf "..."
    cf "... I'll fight for it it until my very last breath."
    "{b}END GAME{/b}"
    $ MainMenu(confirm=False)()

label ad4:
    scene app den night with fade
    stop music fadeout 1.0
    play music "music/ES_The Coldest Water - Headlund.mp3" loop
    show screen gameUI
    t "Probably best to let the apprentices rest up."
    if quest_babysitting.completed:
        t "They've had a long day."
    else:
        t "I'm sure they've had a long day."
    call screen gameUI
















