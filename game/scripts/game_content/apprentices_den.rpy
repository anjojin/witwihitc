label ad1:
    $ apprentice_visited = True
    scene app_den_bg with fade
    stop music fadeout 1.0
    show screen gameUI
    t "It's always nice to check up on how the apprentices are doing."
    t "I wonder what they're up to, in there ..."
    menu:
        t "Focusing hard on their training, I'm sure."
        "Eavesdrop":
            jump ad1_eavesdrop
        "Leave them alone":
            jump ad1_leave_alone

label ad1_eavesdrop:
    "You strain your ears, picking up on the familiar sound of the apprentices' voices."
    c "StarClan, Redpaw, if I have to hear one more word --"
    r "I'm exercising my own free will! I don't have to do anything I don't --"
    c "Free will? Are you serious?"
    r "It's not hygenic! That's all I'm saying! What's the problem?"
    c "The problem is that your sister went out of her way to get this snow for you to drink, and now you're letting it go to waste."
    r "I don't want to drink something that's been in another cat's mouth! That's all!"
    fa "That's why I put it on a leaf, mouse-brain!"
    c "You hear that? That's why she put it on a leaf."
    r "You don't know where that leaf has been!"
    c "I'll show you where that leaf has been!"
    fa "Cloverpaw, wait!!!"
    r "AHHHHH!"
    li "EVERYONE STOP FIGHTING!!!"
    li "StarClan, you're all driving me crazy!"
    fa "Lilypaw, where are you going?"
    li "Someplace where I can hear myself think! StarClan knows it isn't in here!"
    r "We were just fooling around ..."
    c "Buzzkill."
    show lilypaw_entrace with fade
    li "... Eep!"
    li "T-Talonclaw! Hello!"
    fa "Talonclaw's outside?"
    c "Talonclaw!"
    hide lilypaw_entrace with fade
    show cloverpaw_ad1 with easeinright
    show fawnpaw_ad1 with easeinright
    show redpaw_ad1 with easeinleft
    show lilypaw_ad1 with easeinleft
    fa "Talonclaw!!!"
    t "Hey, kittos."
    t "Sounded like quite the argument in there."
    fa "This one was actually pretty tame. It usually takes way longer to separate them."
    r "Slowing down lately, Cloverpaw?"
    c "Slowing down? Tch, I was just getting started. You're lucky Talonclaw showed up when he did, or else I would've shredded him."
    r "Right ... that's probably the reason I won our last three mock-battles, too."
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
    t "... It probably isn't the best idea to pick petty fights with your denmates, either."
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
    fa "Yeah. And my mentor keep ditching me to go on patrol alone."
    fa "Apparently ThunderClan 'can't afford inexperienced hunters scaring off all the prey.'"
    fa "As if there's any prey out there to begin with ..."
    r "Say ... maybe you could take us out later, Talonclaw."
    c "Ooh! Yeah! That'd be awesome!"
    r "It could be just like a regular hunting patrol, only we'd be there to help you."
    fa "We swear, we won't let you down! We've all been practicing our moves."
    r "Yeah. Cloverpaw's made an excellent mock mouse."
    c "{i}*STOMP*{/i}"
    r "Ha. Missed me that time."
    t "I don't know, you guys ..."
    if quest_favorite_prey.started:
        t "I kind of agreed to do this thing for Sunshadow today, and it's really important."
    fa "Come on! What do you have to lose?"
    "{b}Game Tip:{/b} Hunting with the apprentices will {b}increase{/b} your number of opportunities at catching prey."
    "However, it will also {b}decrease{/b} your chances of success."
    menu:
        "Do you accept?"
        "Yes":
            jump ad1_yes
        "No":
            jump ad1_no 

label ad1_yes:
    $ quest_babysitting.started = True
    $ training_with = ["hunting_red", "hunting_lily", "hunting_fawn", "hunting_clover"]
    t "Aw, what the hey? I'll take you guys out with me. Why not?"
    "{b}Quest Unlocked:{/b} Babysitting"
    fa "Yes! Thank you!"
    c "Hahaha! I'm gonna catch so much prey, we're not gonna be able to carry it all home!"
    r "That's kind of unrealistic, Cloverpaw."
    c "Shut it."
    t "... Lilypaw? You've been awfully quiet. Do you have anything to say?"
    li "..."
    li "I ..."
    li "I'll do my best."
    t "That's all I can ask for."
    li "{i}*Smile*{/i}"
    t "Alright, then. I'll meet you all on the territory when I'm ready to get started."
    t "Try not to injure each other until then."
    c "Not making any promises."
    r "Cloverpaw!"
    c "What? I'm just trying to be more {i}realistic.{/i}"
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
        "... of Dapplefeather" if quest_favorite_prey.started:
            jump ad1_dapplefeather

label ad1_leave_alone:
    t "Probably best not to disturb them. Especially when there's so much other work to be done."
    t "Maybe I'll run into them later."
    if quest_crocus.started:
        show screen ad_juniper
    call screen gameUI

label ad1_mentors:
    $ talon_clan_bonus += 1
    t "Your mentors decide when to train you. It's not my place to take you out."
    r "My mentor has been in the medicine den for moons now, and no cat's assigned me a new one. How is that my fault?"
    fa "Even if you were assigned a new one, they probably wouldn't take you out, anyways!"
    fa "No matter what you do to prove you're ready!"
    t "I'm sorry, guys. Those are the rules."
    c "Screw the rules! We're healthy! We want to hunt! This Clan isn't fed on technicailities!"
    r "Yeah!"
    jump ad1_no_finish

label ad1_polite:
    $ talon_clan_bonus -= 1
    t "Patrolling isn't all it's cracked up to be."
    t "You should consider yourself lucky to relax around camp all day while the rest of us are out there freezing our tails off."
    c "... Really?"
    c "Our Clanmates and kin are dying. All we want is to help, and you're telling us it's 'not all it's cracked up to be?'"
    c "Unbelievable. How old do you think we are?"
    r "This is why things never get better. No one ever takes our ideas seriously."
    jump ad1_no_finish

label ad1_risk:
    t "Prey is scarce enough as it is. You guys may feel like seasoned hunters now, but the truth is, you're still lacking experience."
    c "Well, when are we supposed to get the experience? At this rate, we'll be graduating at 20 moons old!"
    r "This is completely unfair. How can you say it's too risky when you haven't even given us a chance?"
    jump ad1_no_finish

label ad1_dapplefeather:
    $ talon_sun_bonus += 1
    t "I'm already committed. I've gotta catch a piece of prey for Dapplefeather before she's buried."
    c "You guys are burying Dapplefeather?"
    c "My sisters still haven't been buried, and they croaked moons ago. Can you throw them in there, too?"
    r "Why can't we come with you to hunt for Dapplefeather? All you need is one piece of prey, right?"
    jump ad1_risk

label ad1_no_finish:
    fa "... Lilypaw. You've been quiet."
    fa "Do you have anything to say?"
    li "..."
    li ".........."
    li "I'm tired of the fighting."
    hide lilypaw_ad1 with moveoutleft
    fa "Lilypaw, wait!"
    hide fawnpaw_ad1 with moveoutright
    c "Tch. Whatever. I don't know why I even bother."
    hide cloverpaw_ad1 with moveoutright
    hide redpaw_ad1 with moveoutleft
    t "..."
    if quest_crocus.started:
        show screen ad_juniper
    call screen gameUI

label ad1_click_juniper:
    t "It's purple, and it's a flower ... but it's not quite a crocus."
    t "I'd better keep looking."
    hide screen ad_juniper
    call screen gameUI
