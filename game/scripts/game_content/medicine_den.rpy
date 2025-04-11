label md1:
    $ med_den_visited = True
    stop music fadeout 0.5
    play music "music/ES_Enough by Now - Headlund.mp3" loop
    if not quest_medical_opinion.started or quest_medical_opinion.completed:
        scene med_den_ext with fade
        t "The medicine den."
        t "Locustleaf would have a fit if I went in there without a good reason."
        t "Especially since I'm one of the only healthy warriors left ..."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
        else:
            call screen gameUI
    
    else:
        scene med_den_bg with fade
        show screen gameUI
        show locustleaf with moveinright
        show maplebreeze with moveinleft
        m "{i}*Wheeze*{/i} I-I'm not ... {i}*Wheeze*{/i} I'm not that sick, Locustleaf ... {i}*Wheeze*{/i} Honest ..."
        m "These herbs should go to ... {i}*Wheeze*{/i} somecat who really ... {i}*Wheeze*{/i} needs them ..."
        l "Shut up and eat your catmint."
        t "Locustleaf!"
        l "Talonclaw?"
        l "What do I always say? The medicine den is for emergencies, only!"
        t "But it {i}is{/i} an emergency!"
        t "Featherkit's gotten sick, and --"
        m "*Gasp* Oh, no! Will she be alright?"
        l "Stay out of this, Maplebreeze."
        l "Featherkit ... she's one of Sunshadow's new litter, right?"
        l "Has she stopped eating?"
        t "Yes."
        l "And developed a cough?"
        t "Yes! Now, come on, we need to hurry! Do you have anything I can --"
        stop music
        l "She'll be dead by sundown."
        m "*Gasp*"
        play music "music/ES_Days That Matter - Headlund.mp3" loop
        t "What?!"
        l "I'm sorry. There's nothing I can do."
        l "A cat her age, in these conditions, without a mother, doesn't stand a chance against any sort of cough."
        l "Herbs, or no herbs."
        t "No, no, that can't be right."
        t "She just got sick this morning! There must still be some time to save her!"
        m "{i}Wheeze{/i} ... Yes, Locustleaf, surely there's still something we can --"
        l "Quiet, Maplebreeze!"
        m "..."
        l "... Okay. Maybe, if I had the herbs to spare, I would be more inclined to agree with you."
        l "But, in case you haven't noticed, this den is already filled with the sick and dying, inclduing our own deputy."
        t "But Featherkit's so small -- she'll only need a tiny scrap of catmint!"
        t "Maplebreeze was just saying she didn't need hers!"
        m "Yes ... {i}wheeze{/i}... I'd be happy to spare a little ..."
        l "Maplebreeze is a {i}medicine cat.{/i}"
        l "If these herbs could go towards one starving kit, versus Maplebreeze, who will go on to save dozens of lives..."
        l "Well, I'll let you do the math on that one."
        l "Need I remind you how much worse things got for ThunderClan after we lost our last apprentice?"
        t "..."
        t "... What if I could find more?"
        l "Excuse me?"
        t "More catmint. Then, could you spare some for Featherkit?"
        l "Ha! If you find any catmint out there, you could line your nest with it, for all I care."
        l "Better yet, you could find a whole branch and spend the afternoon hitting yourself over the head with it."
        if quest_favorite_prey.started:
            l "It'd probably be a better use of your time."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} Hunting for catmint means Talonclaw will no longer be able to complete the following questline: {b}Burial Rites.{/b}"
            play sound "sfx/game_tip.mp3"
            menu:
                "How would you like to proceed?"
                "Stick with burying Dapplefeather":
                    jump md1_give_up
                "Switch to finding catmint":
                    jump md1_accept_challenge

        elif quest_feed_deputy.started:
            l "It'd probably be a better use of your time."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} hunting for catmint means Talonclaw will no longer be able to complete the following quest: {b}Feed the Deputy.{/b}"
            play sound "sfx/game_tip.mp3"
            menu:
                "How would you like to proceed?"
                "Stick with hunting for Pouncetail":
                    jump md1_give_up
                "Switch to finding catmint":
                    jump md1_accept_challenge

        elif quest_babysitting.started:
            l "It'd probably be a better use of your time."
            play sound "sfx/game_tip.mp3"
            "{b}Game Tip:{/b} hunting for catmint means Talonclaw will no longer be able to complete the following quest: {b}Babysitting.{/b}"
            play sound "sfx/game_tip.mp3"
            menu:
                "How would you like to proceed?"
                "Stick with patrolling with the apprentices":
                    jump md1_accept_challenge
                "Switch to finding catmint":
                    jump md1_give_up
        else:
            menu:
                l "It'd probably be a better use of your time."
                "Challenge Accepted":
                    jump md1_accept_challenge
                "Give Up":
                    jump md1_give_up

label md1_accept_challenge:
    $ quest_gather_herbs.started = True
    if quest_favorite_prey.started:
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Questline Cancelled:{/b} Burial Rites"
        if quest_crocus.started:
            $ quest_crocus.started = False
            $ quest_crocus.cancelled = True
        $ quest_favorite_prey.started = False
        $ quest_favorite_prey.cancelled = True
        if quest_nesting_material.started:
            $ quest_nesting_material.started = False
            $ quest_nesting_material.cancelled = True
    if quest_feed_deputy.started:
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Quest Cancelled:{/b} Feed the Deputy"
        $ quest_feed_deputy.started = False
        $ quest_feed_deputy.cancelled = True
    if quest_babysitting.started:
        play sound "sfx/ES_Error 04 - Epidemic Sound.mp3"
        "{b}Quest Cancelled:{/b} Babysitting"
        $ quest_babysitting.started = False
        $ quest_babysitting.cancelled = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Collect Catmint"
    t "Fine! I will, then!"
    t "... N-Not the branch thing. The catmint thing."
    t "I'm going to find catmint, and I'm going to save Featherkit's life, and I'm going to make everything better!"
    l "..."
    l "... Heh. Heh."
    l "Hahaha! Ahahaha!"
    jump md1_end

label md1_give_up:
    t "..."
    t "... How can this be happening?"
    t "Why would StarClan take her so young?"
    l "Oh, don't be so dramatic."
    l "Sometimes kits die. It's just a fact of life. Especially in big litters."
    t "There's no need to say something so cruel!"
    t "You couldn't possibly understand how it feels to be completely powerless to save someone you love!"
    l "... {i}I{/i} couldn't possibly understand?"
    l "... Heh. Heh."
    l "Hahaha! Ahahaha!"
    jump md1_end

label md1_end:
    play audio "sfx/ES_Male 03 - Epidemic Sound.mp3" 
    l "{i}*Koff* *Koff* *Koff*{/i}"
    t "Are you alright?!"
    l "{i}*Gasp*{/i} I-I'm fine."
    l "Get out."
    l "{i}*Choke* *Wheeze*{/i}"
    t "Locustleaf --"
    l "I said, get OUT!!!"
    l "{i}*Koff* *Koff* *Koff*{/i}"
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Medical Opinion"
    $ quest_medical_opinion.started = False
    $ quest_medical_opinion.completed = True
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Grim Tidings"
    $ quest_grim_tidings.started = True
    call screen gameUI

label md1_click_berries:
    $ herbs_clicked += 1
    if herbs_clicked == 5:
        $ botanist.grant()
    play audio "sfx/plant_error.mp3"
    t "I wonder if these berries are edible. Locustleaf would probably know."
    t "... And would probably have my head on a pike in the middle of camp if I wasted his time with such a mouse-brained question."
    hide screen md_berries
    call screen gameUI

label md2:
    if quest_medical_opinion.started:
        jump md1
    elif nursery_visited==False:
        jump md1
    elif nursery_visited==True and not quest_medical_opinion.started and not quest_medical_opinion.completed:
        stop music fadeout 0.5
        play music "music/ES_Enough by Now - Headlund.mp3" loop
        scene med_den_ext with fade
        t "I really hope I'm right about Featherkit ..."
        t "If her cough turns out to be serious, Beetle can always fetch Locustleaf herself."
        t "The medicine den is only a few paces away from the nursery, after all."
        t "I'm a warrior. It's my job to hunt for the Clan. Not worry about kits with the sniffles."
        t "Yup. Definitely not worried."
        t "Definitely not ..."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
        else:
            call screen gameUI
    else:
        stop music fadeout 0.5
        play music "music/ES_Enough by Now - Headlund.mp3" loop
        scene med_den_ext with fade
        t "I doubt Locustleaf wants to see me back so soon ..."
        if quest_gather_herbs.started:
            t "I'll follow up with him when I get the catmint, like I promised."
        else:
            t "I hope he's doing okay."
            t "If we lost him ..."
            t "{i}*Shudder*{/i}"
            t "Probably best not to think about things like that."
            t "Locustleaf is the most talented medicine cat in the forest. I know he'll be fine."
            t "He has to."
        if quest_crocus.started:
            show screen md_berries
            call screen gameUI
        else:
            call screen gameUI

label md3:
    $ already_cloverpaw = False
    $ already_kits = False
    $ already_catmint = False
    $ already_pouncetail = False
    $ already_flipcloud = False
    $ already_cough = False
    $ already_future = False
    $ med_den_visited_postp = True
    stop music fadeout 0.5
    play music "music/ES_Enough by Now - Headlund.mp3" loop
    scene int med den night with fade
    show screen gameUI
    if quest_report_clover.started:
        jump md3_clover
    if quest_gather_herbs.completed or quest_gather_herbs.failed:
        jump md3_herbs
    else:
        show locust_hunch_night with easeinright
        l "{i}*Koff* *Koff*{/i}"
        l "Who's there?"
        l "Reveal yourself! I can hear your pawsteps!"
        t "It's just me, Locustleaf."
        hide locust_hunch_night
        show locust_loaf_night
        l "... Talonclaw."
        l "I should've known it was you. No other warrior has quite such a ... distinctive smell."
        l "What are you doing in the medicine den? Don't the words 'emergencies only' mean anything to you?"
        t "I need to talk to you about something."
        hide locust_loaf_night
        show locust_hunch_night
        l "Hn. You hear that, sick and dying patients? It's an emergency. Talonclaw needs to talk to me about something."
        l "Go ahead and talk, then."
        jump locust_menu1

label md3_herbs:
    show locust_hunch_night with easeinright
    l "{i}*Koff* *Koff*{/i}"
    l "Who's there?"
    l "Reveal yourself! I can hear your pawsteps!"
    t "It's just me, Locustleaf."
    hide locust_hunch_night
    show locust_loaf_night
    l "... Talonclaw."
    l "I should've known it was you. No other warrior has quite such a ... distinctive smell."
    l "What are you doing in the medicine den? Don't the words 'emergencies only' mean anything to you?"
    t "I come bearing gifts."
    show screen md_herbs with fade
    show screen gameUI
    l "Hn ... Is that all?"
    if quest_miracle_worker.started:
        t "Nope."
        t "Take a look."
        t "Catmint. Fresh from the territory."
        l "Wh --"
        l "How --"
        l "How in StarClan's name did you ...?"
        t "I don't know. Guess I got lucky?"
        l "Give it here."
        t "Not so fast."
        t "Remember when you told me earlier that, if I found catmint, I could do whatever I wanted with it?"
        l "... You didn't think I was serious, did you?"
        l "You're not honestly planning to line your nest with it?"
        t "One leaf. That's all I ask for."
        l "What for?"
        t "... I haven't decided, yet."
        l "{i}*Koff Koff*{/i} Ha!"
        l "Can you believe that? He's playing with the lives of his Clanmates, and he hasn't yet decided why."
        t "I'm not going to throw it away! It'll go to a cat who needs it!"
        t "I just ... haven't decided who."
        l "You're a regular hero, Talonclaw."
        l "You know what? If you really want to feel the weight of your Clanmates' lives in your paws, you can be my guest."
        l "StarClan knows I could use a break from it."
        l "Here's your leaf. Make your choice wisely."
        l "Hey, what do you know? I'm feeling lighter already ..."
        show screen sickden with fade
        show locust_hunch_night
        play sound "sfx/game_tip.mp3"
        "Click on the {b}sick den entrance{/b} to access cats in the sick den."
        jump locust_menu
    else:
        l "Well, I suppose it frees up my paws a bit ..."
        l "... Thank you, Talonclaw."
        t "Don't mention it."
        jump locust_menu

label md3_clover:
    t "... Hello? Locustleaf?"
    t "Are you home?"
    t "Listen, I know you don't any cats disturbing you, but I have to tell you something."
    t "It's about ..."
    show cloverpaw_sit_center with easeinleft
    t "... Cloverpaw?" 
    c "Hey."
    t "What are you ...?"
    t "I mean, are - are you feeling, er --"
    c "Relax. You can hold off on the whole 'concerned, contrite Clanmate' thing."
    c "The messy part is already over with."
    t "You ..."
    t "You turned yourself in?"
    c "Sure. Why not? Figured I might as well, right?"
    c "Maybe they'll give me points in StarClan for being such a good little sprite."
    t "Hey, c'mon. Don't say things like that."
    t "Locustleaf is the most talented medicine cat in the forest. It'll be a long time before you see StarCl --"
    c "Yeah, yeah, alright. You can save your breath, Talonclaw."
    c "Don't you get it, yet?"
    c "You don't have to feel bad about me, anymore!"
    c "... I don't want any cat to feel bad about me."
    c "I live my whole life trying to make my friends laugh, only for it to be cut short on a downer?"
    c "That's so ... depressing."
    c "No, if I had my way, everything would end with a joke."
    c "Speaking of which ..."
    c "Hey, Talonclaw, do you know why see-through graves never took off?"
    t "Uh ..."
    t "Why, Cloverpaw?"
    c "It {i}remains to be seen.{/i}"
    c "Hahahahaha!"
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide cloverpaw_sit_center with fade
    t "..."
    show locust_hunch_night with easeinright
    l "*Snrk* ... 'remains to be seen.'"
    l "Clever."
    t "Is she going to be alright?"
    l "Why do cats always ask me that question?"
    l "If I knew the answer, my job would be a whole lot less interesting."
    play audio "sfx/quest_unlocked.mp3"
    $ quest_report_clover.started = False
    $ quest_report_clover.completed = True
    "{b}Quest Completed:{/b} Report Cloverpaw"
    jump locust_menu

label locust_menu:
    menu:
        l "Now, was there anything else you wanted to say, or are you still here just to waste my time?"
        "Cloverpaw" if quest_report_clover.completed and not already_cloverpaw:
            jump md3_clover2
        "Kits" if quest_check_nursery.completed and not already_kits:
            jump md3_kits
        "Catmint" if quest_miracle_worker.started and not already_catmint:
            jump md3_catmint
        "Pouncetail" if quest_feed_deputy.started and not already_pouncetail:
            jump md3_pouncetail
        "Flipcloud" if quest_babysitting.completed and not already_flipcloud:
            jump md3_flipcloud
        "Cough" if med_den_visited and not already_cough:
            jump md3_cough
        "ThunderClan's Future" if not already_future:
            jump md3_future
        "That's it":
            jump md3_end

label md3_clover2:
    $ already_cloverpaw = True
    t "You'll take care of Cloverpaw, won't you?"
    l "Of course I will."
    l "What kind of medicine cat would I be, if I didn't?"
    t "Do you think we did the right thing?"
    t "What if Cloverpaw's really fine, but she ends up catching something serious from one of the cats inside?"
    hide locust_hunch_night
    show locust_loaf_night
    l "It's worth the risk. The apprentices are far too vital to this Clan for any potential contagion among them to be left unaddressed."
    t "I know, but still ..."
    l "Don't worry. I know what I'm doing."
    l "She'll be kept well away from the cats who are really in trouble."
    l "... Though, I am tempted to send her into the sick den, just to liven things up in there."
    l "The other patients could use a dose of her wit."
    hide locust_loaf_night
    show locust_hunch_night
    jump locust_menu

label md3_kits:
    $ already_kits = True
    t "... I still can't believe Featherkit and Willowkit are gone."
    t "They barely even got to live! No apprenticeship, no warrior names ..."
    t "We won't even know what color their eyes were supposed to be."
    hide locust_hunch_night
    show locust_lay_night
    l "... Sunshadow's eyes are copper."
    l "Spottedlight's were hazel."
    l "So, according to everything I've seen and studied in my time as a medicine cat ..."
    l "... The kits' eyes likely would've been some shade of orange or green."
    l "If it helps at all."
    t "... Y'know, oddly enough, it does."
    t "Thanks, Locustleaf."
    l "Don't mention it."
    jump locust_menu

label md3_catmint:
    $ already_catmint = True
    t "Here."
    l "... It's a catmint leaf. What about it?"
    t "I want you to have it. For your cough."
    l "What is this, some kind of joke?"
    l "You ask me for my own herbs, just to give them back to me a second later?"
    t "What happened to that talk from earlier, about a medicine cat being worth a dozen warriors?"
    t "Who's saved more lives than you, Locustleaf?"
    l "..."
    hide locust_hunch_night
    show locust_lay_night
    l "Give the herbs to Maplebreeze."
    t "What?"
    l "You say I've saved lives. Well, not nearly enough of them."
    l "Maplebreeze is still young. She has her whole life ahead of her."
    l "She's the one who deserves these herbs. Not me."
    t "Locustleaf ..."
    t "How kind of you."
    l "Tch. It's only logical."
    l "She a far greater asset to ThunderClan than I am."
    hide locust_lay_night
    show locust_hunch_night
    l "Besides. I'm not sick."
    t "... Of course."
    jump locust_menu

label md3_pouncetail:
    $ already_pouncetail = True
    if quest_gather_herbs.cancelled:
        l "By the way, how did your catmint search go?"
        l "Manage to find anything?"
        t "... I decided to spend my time hunting, instead."
        l "Ha. Finally, he wisens up."
        l "It's like I always say. Leave the medical work to the medicine cats."
        l "You warriors wouldn't last a day in our paws, anyway."
    t "... Say, whatever happened to Maplebreeze?"
    l "She's recovering in the sick den, with the rest of the patients."
    t "Oh."
    t "Could I ... possibly go back there to see them?"
    l "Absolutely not. Unless you intend on staying back there forever."
    t "Please? I swear, I'll be in and out."
    t "I just need to do a favor for Briarstar."
    t "What if this is what she needs to finally start being a leader again?"
    hide locust_hunch_night
    show locust_loaf_night
    l "... Something tells me no matter what I say, I won't be able to convince you what a mouse-brained idea this is."
    l "And StarClan knows I won't be able to stop you by force."
    l "So go ahead and risk your life, if that's what you want to do so badly."
    l "And if you end up back in my den because of it, don't say I didn't warn you."
    show screen sickden with fade
    play sound "sfx/game_tip.mp3"
    "Click on the {b}sick den entrance{/b} to access cats in the sick den."
    jump locust_menu

label md3_flipcloud:
    $ already_flipcloud = True
    t "I took Redpaw and Fawnpaw out hunting, earlier today. They wouldn't stop talking about Flipcloud."
    t "Can I ask how he's doing?"
    l "... Well, you just did."
    l "And somehow I get the sense that, if I tell you the truth, I'll have two apprentices in my den tomorrow, pestering me nonstop about him."
    l "So, for now, I'll just say ..."
    l "He's fine."
    l "He misses his kits. Speaks of them often."
    t "... You really want me to lie to these apprentices?"
    l "It's not a complete lie. That last part is true."
    l "And, if you know what's good for the apprentices, that will be enough for you."
    jump locust_menu

label md3_cough:
    $ already_cough = True
    l "{i}*Cough* *Cough* *Cough*{/i}"
    t "I can't believe you aren't taking this cough more seriously, Locustleaf."
    t "You, more than any cat, should understand how important your health is to the future of the Clan."
    l "{i}*Ahem*{/i} Have you seen what I do all day? The cats I work around?"
    l "Avoiding greencough isn't exactly an option for me."
    l "Even if I did manage to cure myself, I would just catch it again from one of my patients."
    l "What good would that serve?"
    t "A lot!"
    t "You were just saying earlier how important medicine cats are! How much their lives are worth"
    l "{i}*Cough* *Cough*{/i}"
    l "In case you hadn't noticed, Talonclaw ..."
    hide locust_hunch_night
    show locust_lay_night
    l "... I'm old."
    l "My body is failing in all sorts of ways, all of which compound by the day."
    l "Just this morning, I lost all the feeling in my left paw."
    l "My eyesight is going."
    l "Who knows what'll be next?"
    l "My pelt? My teeth? my brain?"
    l "I don't want to waste a single moment of the time I have left worrying about the inevitable."
    l "Not even medicine cats can cheat death."
    hide locust_lay_night
    show locust_hunch_night
    l "If we could, this job would be a whole lot less interesting."
    jump locust_menu

label md3_future:
    $ already_future = False
    t "Locustleaf, you've seen more tragedy this leafbare than any cat."
    t "Do you think ... Do you think it changes who you are on the inside?"
    t "Will ThunderClan ever go back to the way it was?"
    hide locust_hunch_night
    show locust_loaf_night
    l "..."
    l "I'll be frank with you, Talonclaw."
    l "I've been a medicine cat for a long time. I've seen warriors die in every possible way."
    l "But, with this latest outbreak, things are ... different."
    l "Cats don't fight, anymore."
    l "They don't have that froth in their mouth to get out of the medicine den and rejoin their Clanmates. Their loved ones."
    l "This latest crop just ... slip away."
    l "Quick as falling asleep."
    t "That's ..."
    t "That's terrible."
    l "It's pathetic, is what it is. The whole lot of them are cowards."
    hide locust_loaf_night
    show locust_lay_night
    l "They think they can just give up on ThunderClan? Just like that?"
    l "That, just because they're dying, their Clan is over?"
    l "Mouse-dung. Now's the time we need them more than ever."
    l "A warrior's top job isn't to hunt for his Clan, or even protect it."
    l "It's to believe in everything it stands for."
    l "As long as ThunderClan exists, it will need cats to believe in it."
    l "And, as long as THunderClan exists, cats will always have something to believe in."
    l "But not if we stop --"
    hide locust_lay_night
    show locust_hunch_night
    l "N-Not if we stop --"
    l "-- {i}*Wheeze* *Cough*{/i}"
    t "Is there anything I can get you?"
    l "{i}*Cough*{/i} N-No."
    l "It's alright ..."
    l "Nothing can stop what happens now."
    l "All of our insides have changed, in a physical and literal sense, and even more change is on the way. No way around it."
    l "But, as for me ... I'm not worried."
    l "ThunderClan will come out the other side of this -- damanged, sure, but alive."
    l "As long as the warriors still believe."
    l "Don't let the spark die out, Talonclaw."
    t "..."
    jump locust_menu

label md3_end:
    l "Good."
    l "Now, I think you know what I'm about to say, so why don't you go ahead and do it without me having to say it?"
    t "... Good night, Locustleaf."
    l "Good night, Talonclaw."
    l "I hope we don't see each other again for a long, long time."
    hide locust_hunch_night with fade
    call screen gameUI

label sickden:
    hide screen sickden
    stop music fadeout 0.5
    play music "music/ES_Enough by Now - Headlund.mp3" loop
    scene sickden with fade
    show screen gameUI
    play sound "sfx/game_tip.mp3"
    "Click on the cat you want to interact with."
    call screen sick_cats

label sd_flipcloud:
    hide screen sick_cats
    menu:
        "{b}Flipcloud,{/b} father of Redpaw and Fawnpaw. What would you like to do?"
        "Offer catmint":
            jump flip_offer
        "Cancel":
            jump sickden_cancel

label sd_maplebreeze:
    menu:    
        "{b}Maplebreeze,{/b} ThunderClan's young medicine cat. What would you like to do?"
        "Offer catmint":
            jump maple_offer
        "Cancel":
            jump sickden_cancel

label sd_pouncetail:
    menu:    
        "{b}Pouncetail,{/b} ThunderClan's deputy. What would you like to do?"
        "Offer catmint" if quest_miracle_worker.started:
            jump pounce_offer
        "Offer prey" if quest_feed_deputy.started:
            jump pounce_prey
        "Cancel":
            jump sickden_cancel

label sickden_cancel:
    play sound "sfx/game_tip.mp3"
    "Click on the cat you want to interact with."
    call screen sick_cats

label flip_offer:
    hide screen sick_cats
    show flipcloud
    fl "Redpaw? Is that you?"
    t "It's Talonclaw, Flipcloud."
    t "I have some herbs here, for you."
    fl "You're gonna have to pick something smaller, Redpaw ... That carp is way too big ... It'll make you sick."
    t "Here. Eat up."
    fl "You're growing up so quick, Redpaw ..."
    fl "Growing ... So ..."
    "Flipcloud confusedly laps up the herbs."
    hide sd_flipcloud
    $ gave_herbs = "flip"
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Miracle Worker"
    $ quest_miracle_worker.started = False
    $ quest_miracle_worker.completed = True
    if quest_harbringer.completed:
        t "I bet Beetle will want to hear hear who I gave the herbs to, considering she's the one who gave me the idea."
        t "StarClan knows she could use some good news, right now."
        play audio "sfx/quest_unlocked.mp3"
        "{b}Quest Unlocked:{/b} Follow Up with Beetle"
        $ quest_followup_beetle.started = True
    call screen gameUI

label maple_offer:
    hide screen sick_cats
    show sd_maple
    t "Have some catmint, Maplebreeze!"
    t "I just gathered it earlier today."
    m "Oh, Talonclaw ..."
    m "That's very kind of you, but there are cats in this den far worse off than I."
    m "What about Sunshadow's kits?"
    t "... All the cats in this den need you to help them get better."
    t "Now, quiet down. Locustleaf says you have to rest your voice."
    m "..."
    "Maplebreeze reluctantly laps up the herbs."
    hide sd_maple
    $ gave_herbs = "maple"
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Miracle Worker"
    $ quest_miracle_worker.started = False
    $ quest_miracle_worker.completed = True
    if quest_harbringer.completed:
        t "I bet Beetle will want to hear hear who I gave the herbs to, considering she's the one who gave me the idea."
        t "StarClan knows she could use some good news, right now."
        play audio "sfx/quest_unlocked.mp3"
        "{b}Quest Unlocked:{/b} Follow Up with Beetle"
        $ quest_followup_beetle.started = True
    call screen gameUI

label pounce_offer:
    hide screen sick_cats
    show pouncetail
    "You drop the herbs near Pouncetail's mouth."
    p "..."
    "He doesn't seem to be eating them."
    p "..."
    "His chest rises and falls."
    hide pouncetail
    $ gave_herbs = "pounce"
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Miracle Worker"
    $ quest_miracle_worker.started = False
    $ quest_miracle_worker.completed = True
    if quest_harbringer.completed:
        t "I bet Beetle will want to hear who I gave the herbs to, considering she's the one who gave me the idea."
        t "StarClan knows she could use some good news, right now."
        play audio "sfx/quest_unlocked.mp3"
        "{b}Quest Unlocked:{/b} Follow Up with Beetle"
        $ quest_followup_beetle.started = True
        $ quest_miracle_worker.started = False
    call screen gameUI

label pounce_prey:
    show pouncetail
    "You drop the prey near Pouncetail's mouth."
    p "..."
    "He doesn't seem to be eating it."
    p "..."
    "His chest rises and falls."
    hide pouncetail
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Feed the Deputy"
    $ quest_feed_deputy.started = False
    $ quest_feed_deputy.completed = True
    t "I guess I should probably report back to Briarstar, now ..."
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Follow Up with Briarstar"
    $ quest_followup_briar.started = True
    call screen gameUI

label locust_menu1:
    menu:
        l "What is it that's so vitally important?"
        "Cloverpaw" if quest_report_clover.completed and not already_cloverpaw:
            jump md3_clover2
        "Featherkit and Willowkit" if quest_check_nursery.completed and not already_kits:
            jump md3_kits
        "Catmint" if quest_miracle_worker.started and not already_catmint:
            jump md3_catmint
        "Pouncetail" if quest_feed_deputy.started and not already_pouncetail:
            jump md3_pouncetail
        "Flipcloud" if quest_babysitting.completed and not already_flipcloud:
            jump md3_flipcloud
        "Cough" if med_den_visited and not already_cough:
            jump md3_cough
        "ThunderClan's Future" if not already_future:
            jump md3_future