label cl1:
    $ currently_in = "clearing"
    scene clearing bg with fade
    play sound "sfx/camp_click.mp3"
    show screen gameUI
    stop music fadeout 0.5
    play music "music/ES_Dreams of a Life - Damon Greene.mp3"
    if burial_rites:
        t "Okay. Nesting materials, prey, and crocuses ..."
        t "Nesting materials, I can probably find in the warrior's den."
        t "For crocuses, I'll have to search around camp."
        t "And for prey, I'll have to go on a hunting patrol." 
        t "Let's hope I manage to bring back more than one thing today ... I'd hate for my only catch to go to waste."
        play sound "sfx/game_tip.mp3"
        "The {b}Camp{/b} button can also be used to travel to different parts of camp, or go on patrol."
        play sound "sfx/game_tip.mp3"
        "Talonclaw does not have the strength to patrol more than once per day, so use it wisely."
        show screen freshkill
        call screen gameUI

    else:
        if talon_sun_bonus < 0:
            t "Mouse-brain ..."
            t "Whatever. He'll cool off eventually."
            t "He has to ..."
            t "In the meantime, I should probably see if anyone needs anything around camp."
        else:
            t "I should probably check out what's happening around camp."
        play sound "sfx/game_tip.mp3"
        "The {b}Camp{/b} button can also be used to travel to different parts of camp, or go on patrol."
        play sound "sfx/game_tip.mp3"
        "Talonclaw does not have the strength to patrol more than once per day, so use it wisely."
        show screen freshkill
        call screen gameUI

label click_freshkill:
    hide screen freshkill
    scene empty freshkill day
    show screen gameUI
    t "I hope the freshkill pile fills up soon."
    t "Though, even if it does, the prey never seems to last long ..."
    scene clearing bg with fade
    call screen gameUI

label cl2:
    scene clearing bg with fade
    show screen gameUI
    stop music fadeout 0.5
    play music "music/ES_Dreams of a Life - Damon Greene.mp3"
    t "The clearing is empty. Everycat's already gone out for the day."
    t "I'd better get a move on, myself, while there's still some light to lose."
    show screen freshkill
    call screen gameUI

label cl3:
    $ currently_in = "clearing"
    $ quick_menu = True
    scene clearing bg night with fade
    show screen gameUI
    stop music fadeout 0.5
    play music "music/ES_Dreams of a Life - Damon Greene.mp3"
    if quest_babysitting.completed:
        jump cl3_cloverpaw
    elif not quest_gather_herbs.completed and prey_caught==0:
        t "Oof. StarClan, what a disaster ..."
        t "At least the warriors' hunting patrol made it back alright. Hopefully, they fared better than I did."
        if quest_favorite_prey.completed:
            t "I guess Sunshadow will have to make do without a piece of prey for Dapplefeather, after all."
            t "I wonder how he's doing out there."
            t "Has he completely frozen to death yet, or only halfway-frozen?"
            t "I should probably go check on --"
            jump cl3_crowkit
    elif prey_caught > 0:
        t "Thank you, StarClan, for the lives of this prey. Please guide their spirits to the afterlife, and let their bodies nourish and protect our own ..."
        t "... It looks like the other warriors finished their hunting patrol, too."
        t "Hopefully, they didn't come back empty-pawed."
        if quest_favorite_prey.completed: 
            t "I guess I have everything Sunshadow asked for, now."
            t "I wonder how he's doing out there."
            t "Has he completely frozen to death yet, or only halfway-frozen?"
            t "I should probably go check on --"
            jump cl3_crowkit
    show screen freshkill_night
    call screen gameUI

label cl3_crowkit:
    stop music fadeout 1.0
    show crowkit clearing with fade
    cr "*Sniffle* *Whimper*"
    play music "music/ES_Sweet Scent - Headlund.mp3" loop
    t "Whoa. Crowkit?"
    t "What are you doing outside the nursery all by yourself, kitto?"
    t "Is something wrong?"
    cr "..."
    cr "............"
    cr "... I'm not supposed to tell you."
    t "What do you mean?"
    cr "M-Mama told me not to!"
    cr "I-I wasn't -- I wasn't supposed to --"
    cr "{i}*Sob*{/i}"
    t "Whoa, buddy! Easy! Take a breath."
    cr "But I wasn't supposed to see! Batkit and me were supposed to wait outside! Mama didn't want us to see!"
    cr "I didn't wanna sneak a peek! Batkit dared me to!"
    cr "A-And now -- And now --"
    t "Crowkit, slow down. I can hardly understand you."
    cr "{i}*Whimper*{/i}"
    t "Now, I need you to answer me as clearly as you can."
    t "What is making you so upset?"
    cr "{i}*Sniff*{/i}"
    cr "Guh ...."
    cr "T-The ....."
    cr "The babies, they ......"
    cr "They ......"
    t "..."
    t "Oh, great StarClan."
    $ quest_check_nursery.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Check the Nursery"
    show screen freshkill_night
    call screen gameUI

label cl3_cloverpaw:
    show lilypaw_ad1 with easeinleft
    show redpaw_right with easeinright
    show fawnpaw_right with easeinright
    show cloverpaw_center with easeinleft
    t "Alright. Patrol is over."
    t "Redpaw, Fawnpaw, Lilypaw, all of you go back to the apprentices' den."
    fa "Hey, you can't tell us what to do!"
    t "I can, and I will. Go back to your den now, Fawnpaw. That's an order."
    fa "... I hope you feel better, Cloverpaw."
    hide fawnpaw_right with moveoutright
    hide redpaw_right with moveoutright
    hide lilypaw_ad1 with moveoutleft
    hide cloverpaw_center
    show cloverpaw_sit_center
    c "..."
    c "... Why are you looking at me like that?"
    t "Like what?"
    c "Like I could drop dead at any moment."
    c "I swear to StarClan, all of you are overreacting. I'm fine. It's just a little cough."
    t "Yeah. How many times have I heard that speech before?"
    t "And how many of those cats are still 'perfectly fine' today?"
    c "..."
    t "How long has this been going on?"
    c "... I guess training started getting kinda hard a few days ago."
    c "My first sneeze was just last night."
    t "Have any of your denmates started showing any symptoms?"
    c "Are you serious?"
    c "One cough and you already think it's dangerous for me to be around my friends?"
    t "It's not personal, Cloverpaw. It's just how sickness spreads."
    c "I would never do anything to hurt the cats I care about."
    t "Then why all the secrecy?"
    t "You must have known you weren't feeling well. Why not speak up about it earlier?"
    c "..."
    c "... I've seen cats do it like you say."
    c "Good, upstanding Clanmates who ran straight to the medicine den at the first sign of trouble."
    c "That was what my sister did."
    c "She said I shouldn't visit her."
    c "It was a risk, she said. I might get infected, she said."
    c "... That was the last time I ever saw her."
    c "Cats who go into the medicine den ... They don't come back out again."
    c "I don't want to die in the medicine den, Talonclaw."
    c "I don't want to die at all."
    t "..."
    c "... Except, now, I guess I probably won't have a choice, right?"
    c "You're going to tell Locustleaf what happened, and I'll be dragged away like a naughty kit who escaped the nursery."
    c "It's kinda funny, if you think about it. I'll get to see Fawnpaw and Redpaw's dad before they do. Haha --"
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    menu:
        c "{i}*Cough* *Cough* *Cough*{/i}"
        "Report Cloverpaw":
            jump cl3_report
        "Don't report Cloverpaw":
            jump cl3_spare
    call screen gameUI

label cl3_report:
    $ report_clover = True
    $ talon_clan_bonus += 1
    t "... I'm sorry, Cloverpaw."
    t "I don't mean to sabotage your future. But it's a matter of Clan safety."
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    c "{i}*Cough* *Cough*{/i} ..."
    c "... Yeah. That's what I figured you'd say."
    hide cloverpaw_sit_center with fade
    t "Whuh?"
    t "Where does she think she's going?"
    t "{i}*Sigh*{/i} ... Of course. When has Cloverpaw ever made anything easy for anyone?"
    t "Still, nothing stopping me from telling Locustleaf what happened."
    $ quest_report_clover.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Report Cloverpaw"
    jump cl3_clover_end

label cl3_spare:
    $ report_clover = False
    $ talon_clan_bonus -= 1
    t "..."
    t "... Keep your voice down."
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    c "{i}*Cough*{/i} ... Whuh?"
    t "Don't cough so loud. You'll make the warriors suspicious."
    c "You mean ... you aren't going to turn me in?"
    t "I don't 'mean' anything."
    t "I'm just think that {i}maybe{/i} we should wait a few days before we make a big decision. Just to see if this cough gets any worse."
    t "And if it does, mark my words, kitto, you're going straight to the medicine den. No exceptions."
    t "But, for now ..."
    t "We'll wait and see."
    c "..."
    c "... Wow, Talonclaw."
    c "I don't know what to say."
    t "How about 'thank you?'"
    c "Thank you."
    c "I ... I really owe you one."
    hide cloverpaw_sit_center with fade
    t "..."
    t "Somehow, I can't tell if that was the bravest thing I've ever done, or the stupidest."
    t "I should probably visit the apprentice's den later to check how she's doing."
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Check on Cloverpaw"
    jump cl3_clover_end

label cl3_clover_end:
    t "... StarClan, what a nightmare this has turned into."
    if prey_caught==0:
        t "And we didn't even bring back any prey to show for it, either."
        t "That's the last time I ever let the apprentices talk me into anything."
        t "At least the warriors' hunting patrol made it back alright. Hopefully, they fared better than we did."
        if quest_favorite_prey.completed:
            t "I guess Sunshadow will have to make do without a piece of prey for Dapplefeather, after all."
            t "I wonder how he's doing out there."
            t "Has he completely frozen to death yet, or only halfway-frozen?"
            t "I should probably go check on --"
            jump cl3_crowkit
    if prey_caught>0:
        t "I don't know if that was even worth the prey we brought back."
        if quest_favorite_prey.completed: 
            t "I guess I have everything Sunshadow asked for, now."
            t "I wonder how he's doing out there."
            t "Has he completely frozen to death yet, or only halfway-frozen?"
            t "I should probably go check on --"
            jump cl3_crowkit
    show screen freshkill_night
    call screen gameUI

label cl3_freshkill:
    hide screen freshkill_night
    scene freshkill meager with fade
    t "Seems like the warriors managed to bring a few kills back ... but it isn't much."
    play sound "sfx/game_tip.mp3"
    if prey_caught > 1:
        if quest_feed_deputy.started:
            menu:
                "You have 1 freshkill set aside for Pouncetail. Contribute your remaining {b}[prey_caught - 1]{/b} prey to the pile?"
                "Yes":
                    jump cl3_yes
                "No":
                    jump cl3_1
        elif quest_favorite_prey.completed:
            menu:
                "You have 1 freshkill set aside for Dapplefeather. Contribute your remaining {b}[prey_caught - 1]{/b} prey to the pile?"
                "Yes":
                    jump cl3_yes
                "No":
                    jump cl3_1
    elif prey_caught > 0:
            menu:
                "Contribute {b}[prey_caught]{/b} prey to the pile?"
                "Yes":
                    jump cl3_yes
                "No":
                    jump cl3_1
    else:
        "You have nothing to contribute to the pile."
        jump cl3_1


label cl3_yes:
    play audio "sfx/ES_Small, Place Down On Others, Pile 01 - Epidemic Sound.mp3"
    scene freshkill full with fade
    "You contributed your prey."

label cl3_1:
    scene clearing bg night with fade
    t "..."
    show screen clanmates
    call screen gameUI

label cl3_clanmates:
    menu:
        "It seems like your clanmates are having a discussion. Would you like to listen in?"
        "Yes":
            jump cl3_eavesdrop
        "No":
            jump cl3_no

label cl3_eavesdrop:
    scene clanmates bg with fade
    hide screen clanmates
    show raven_sit
    show moth_sit
    show cloud_stand
    r "I swear, it was like a whole squirrel in there, or something. It was as long as my tail."
    mo "It was probably a pellet. An owl pellet."
    r "What in StarClan's name is that?"
    mo "It's a puked-up amalgamation of all the bits that owls can't digest."
    cl "Can we eat them?"
    r "Ew. Are you crazy?"
    hide cloud_stand
    show cloud_sit
    cl "Only joking. Di-jest, Di-jest."
    r "{i}*Groan*{/i}"
    cl "Hahaha!"
    hide raven_sit
    show raven_stand
    r "Boo! Hiss!"
    mo "It's kinda scary, isn't it? An owl that close to camp?"
    hide cloud_stand
    show cloud_sit
    cl "It seemed like it was eating well. Maybe we should follow its example."
    r "Wanna grow a pair of wings, Cloudheart? It might help you on your journey to become leader."
    hide moth_sit
    show moth_stand
    mo "Whoa. Cloudheart wants to be leader?"
    r "Why are you so surprised? Pouncetail's on the way out, and so is Briarstar."
    cl "Raven's exaggerating. It was only an idea."
    cl "Besides, it's not like I could even go to the Moonpool to receive my nine lives, anyways."
    mo "Oh, yeah. What do you plan to do about that?"
    cl "I'm not sure. I wasn't really serious, anyway. Who would even wanna be the leader right now?"
    cl "How can you turn ThunderClan around from a mess like this one?"
    hide raven_stand
    show raven_sit
    r "Yeah, well, whatever you do, it'd be better than nothing. Which is what our current leader is doing."
    r "A whole lotta nothing."
    mo "... You could do a lot worse than nothing, too."
    mo "Whatever cat ends up taking over, I just feel sorry for them."
    mo "It'll take a lot to earn ThunderClan's trust again."
    cl "..."
    r "..."
    scene clearing bg night with fade
    call screen gameUI

label cl3_no:
    t "I have better things to do than listen to petty gossip."
    call screen gameUI