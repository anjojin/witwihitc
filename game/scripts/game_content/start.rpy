label start:
    call create_my_quests
    
    jump lark_dream

    label lark_dream:
        yarrowstar_unknown "{i}The world is ending.{/i}"
        show starclan_bg with fade
        ""
        l "What's going on?"
        l "Where am I?"
        yarrowstar_unknown "{i}Nothing can stop what happens now.{/i}"
        l "Am I dreaming? Who's there?"
        yarrowstar_unknown "{i}No teeth, no claws, no teeth, no claws, no teeth, no claws, no teeth, no claws, no teeth, no claws, no teeth, no claws, no teeth, no claws ...{/i}"
        l "..."
        l "Is this ..."
        l "Am I in StarClan?"
        yarrowstar_unknown "..."
        l "I am, aren't I?"
        l "Haha! So - So this must mean I'm destined for greatness, right?"
        l "This is amazing. What do you have for me? A prophecy? A quest? Do I have special powers?"
        l "C'mon! I'm ready to get my destiny started!"
        yarrowstar_unknown "..."
        l "... Hello?"
        l "Why won't you answer?"
        yarrowstar_unknown "..."
        yarrowstar_unknown "{i}........{/i}"
        show yarrowstar with fade
        yarrowstar ""
        l "Woah ..."
        yarrowstar "{i}You shouldn't be here.{/i}"
        yarrowstar "{i}Not yet.{/i}"
        l "What? No, t-that can't be true!"
        l "Listen, I know I'm still in training, but I can handle whatever needs to be done! No matter what, I swear, I can find a way!"
        yarrowstar "{i}Nothing can stop what happens now.{/i}"
        l "What are you saying?"
        yarrowstar "{i}Larkpaw.{/i}"
        l "You're not making any sense!"
        yarrowstar "Larkpaw."
        sh "Larkpaw! Incoming!"
        "{i}BAP!!!{/i}"
        jump wake_up

label wake_up:
    show apprentices_den with fade
    $ currently_in = "apprentices"
    l "..."
    l "Ugh ..."
    show shimmerpaw den with fade
    sh "Welcome back to the land of the living."
    l "Did ... Did you just hit me in the back of the head with a moss-ball?"
    sh "I've got a better question: do {i}you{/i} know that you talk in your sleep?"
    sh "Like, really really loudly?"
    menu:
        l "..."
        "Tell Shimmerpaw about the dream":
            jump tell_dream
        "Stay quiet":
            jump stay_quiet

label tell_dream:
    $ shimmer_knows_dream = True
    l "Not funny, Shimmerpaw."
    sh "I'm not joking! You really were talking! It practically --"
    l "Not about the talking, mouse-brain! About waking me up."
    l "For your information, I was in the middle of a dream. A really special one."
    l "There was a white cat, with stars in her pelt ..."
    l "She told me that the world was going to end."
    sh "Hmm ..."
    sh "Sometimes I get weird dreams after eating something funny."
    menu:
        sh "Maybe you should go and see the medicine cat about it?"
        "Let it go":
            jump let_go
        "Stand your ground":
            jump stand_ground

label let_go:
    $ shimmerpaw_rel += 5
    l "... I guess that squirrel you caught yesterday did taste a little suspicious."
    sh "How so?"
    l "Well, if {i}you{/i} could catch it, there must have been something wrong with it."
    sh "Mm. Maybe it's been flavored by all of my dust that you've been eating during training lately."
    l "Heh."
    jump shimmerpaw_options
    

label stand_ground:
    l "Could you lose the humor? This is serious!"
    l "When was the last time any cat in this Clan had a dream about a starry cat?"
    sh "For your information, I {i}was{/i} being serious. If this dream of yours really came from StarClan, then {color=#0a5151}Frondfoot{/color} is the cat who would wanna know about it."
    menu:
        l "..."
        "Let it go":
            jump let_go_2
        "Double down":
            jump double_down

label let_go_2:
    l "... Fine."
    sh "... 'And, I'm sorry for being such a huge jerk, Shimmerpaw?'"
    l "..."
    l "Whatever."
    sh "Apology accepted."
    $ quest_find_frondfoot.started = True
    "{b}Quest Unlocked:{/b} Find Frondfoot."
    jump shimmerpaw_options

label double_down:
    $ shimmerpaw_rel -= 10
    l "Well ... you didn't sound serious!"
    sh "StarClan almighty. If this is how our chosen one is acting after one weird dream, then the whole Clan is doomed."
    l "You think it'll really come down to that?"
    sh "No, mouse-brain."
    sh "What has gotten into you today?"
    sh "Ugh. And, would you look at the time? Now, I'm late."
    l "Late for what?"
    sh "Training. And now that stupid question made me extra late."
    sh "See you, Larkpaw."
    scene apprentices_den with fade
    l "Hmph. Whatever." 
    l "Who needs her, anyway?"
    l "..."
    jump camp_prompt

label stay_quiet:
    l "Sorry ..."
    sh "It's alright. You must've been having some dream, huh?" 
    sh "Do you remember it at all? Was it scary? Did it feel real?"
    sh "*Gasp* Was {i}I{/i} there??"
    l "Uh ... Sure!"
    sh "Really?"
    l "Yeah!" 
    l "As punishment for your bad attitude and flagrant disrespect for the warrior code, StarClan turned you into a skunk and you were exiled from SunClan for your horrible stench."
    sh "Wow ..." 
    sh "What do you think it could mean?"
    l "I actually don't think the meaning could possibly be any more clear."
    sh "Anyways ..."

label shimmerpaw_options:
    $ seen_brother = False
    $ seen_mentor = False
    $ ask_train = False
    menu:
        sh "Got a plan for the day?"
        "Where's my brother?":
            $ seen_brother = True
            jump seen_brother
        "Where's Rainwhisker?":
            $ seen_mentor = True
            jump seen_mentor
        "Wanna train together?":
            $ ask_train = True
            jump ask_shimmer_train

label seen_brother:
    $ lark_knows_sootpaw_clearing = True
    sh "I'm pretty sure Sootpaw got up early to train."
    l "Ugh. Of course. Why do I even bother asking?"
    l "Hey, think if we told him that there was a suboptimally-marked border at the bottom of a cliff, he'd jump down it?"
    sh "Eh, lay off him. More room in the apprentices' den for us."
    sh "Once {i}you{/i} get out of here, then I'll really start getting some decent sleep."
    jump shimmerpaw_options_2

label seen_mentor:
    sh "Y'know, I'm really not sure."
    sh "Hmm, what a predicament, huh? How ever will we find her?" 
    sh "Oh, I know! Let me go ahead and tap into the super special psychic connection I have with your mentor, whom I otherwise rarely ever see or talk to."
    sh "Hmm .... Oh ... Oh, this is interesting ..."
    sh "According to my psychic intuitions and proclivities, it seems like {color=#0b2e69}Rainwhisker{/color} is ..."
    sh "... Up your butt."
    l "Real mature."
    l "Where do you even get these stupid jokes from?"
    sh "Hmm ... Let me think on that one ..."
    sh "From up your butt?"
    l "StarClan almighty."
    jump shimmerpaw_options_2

label shimmerpaw_options_2:
    menu:
        sh "Anything else?"
        "Where's my brother?" if not seen_brother:
            $ seen_brother = True
            jump seen_brother
        "Where's Rainwhisker?" if not seen_mentor:
            $ seen_mentor = True
            jump seen_mentor
        "Wanna train together?" if not ask_train:
            $ ask_train = True
            jump ask_shimmer_train
        "That's it.":
            jump thats_it

label ask_shimmer_train:
    sh "Sure, why not? I got nothing better to do."
    "{b}Quest Unlocked:{/b} Train with Shimmerpaw."
    $ quest_shimmerpaw_training.started = True
    $ quest_shimmerpaw_training.abandoned = False
    l "Don't you have to check in with Prickleheart?"
    sh "Nope. I managed to dodge her today."
    sh "Nothing that a well-timed excuse about your poor, dead mother can't get you out of."
    sh "Thanks again, Mom!"
    l "You know, you really could stand to take your training a little more seriously."
    sh "Oh, come on. Don't even start."
    sh "My mentor's name is literally {i}Prickleheart.{/i} I don't even know how {color=#787878}Flickerstar{/color} managed to come up with something that horrible."
    l "Yeah, well, at least she sort of cares about you."
    l "Sometimes, it feels like {color=#0b2e69}Rainwhisker{/color} couldn't give a rat's tail whether I lived or died."
    sh "Well, then, this is perfect."
    sh "We both get to screw over our horrible mentors for the day."
    l "Heh. Yeah. I guess."
    $ training_with = "Shimmerpaw"
    jump shimmerpaw_options_2


label thats_it:
    sh "Well, considering my plans to sleep in have already been thwarted, I guess I might as well get my day started, too."
    sh "Those poppy seeds aren't going to steal themselves from the medicine den, after all."
    l "Should I even ask?"
    sh "Not unless you want to be made an accomplice~!"
    if training_with=="Shimmerpaw":
        sh "Whenever you're ready, I'll catch you on the next training patrol."
    else:
        sh "Good luck with finding your mentor, or your brother, or whatever it is you end up doing."
    sh "Seeya!"
    scene apprentices_den with fade
    l "StarClan help her ..."
    jump camp_prompt


label camp_prompt:
    l "I should probably check out what's happening around camp."
    $ final_game_screen = True
    show screen gameUI 
    "Click the {b}'?!'{/b} button to access your Quest list."
    "Click the {b}Camp{/b} button to go on patrol, or travel to different parts of the camp."
    call screen gameUI

label nursery:
    "You are now in the nursery."

label clearing: 
    "You are now in the clearing."