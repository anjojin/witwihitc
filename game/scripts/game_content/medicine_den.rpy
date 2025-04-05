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
        l "What are you doing here?"
        l "I swear to StarClan, Talonclaw, if I tell you once, I've told you a thousand times --"
        t "But I need to talk to you."
        l "Hn. You hear that, dying cats back there? It's an emergency. Talonclaw needs to talk to me."
        l "Okay, then. Go ahead and talk."
        jump locust_menu1

label md3_herbs:
    show locust_hunch_night with easeinright
    l "Talonclaw? What are you doing in the medicine den?"
    l "I swear to StarClan, if I tell you once, I've told you a thousand times --"
    t "Relax. I come bearing gifts."
    show screen md_herbs with fade
    show screen gameUI
    l "Hn ... Is that all?"
    if quest_miracle_worker.started:
        t "Nope."
        t "Take a look."
        t "Catmint."
        l "Wh - How - How in StarClan's name did you --"
        t "Guess I got lucky."
        l "Give it here."
        t "Not so fast."
        t "Remember when you told me earlier that, if I found catmint, I could do whatever I wanted with it?"
        l "... You didn't think I was serious, did you?"
        l "You're not honestly planning to line your nest with it?"
        t "Just give me one leaf. That's all I need."
        l "What for?"
        t "... I haven't decided, yet."
        l "{i}*Koff Koff*{/i} Ha!"
        l "Can you believe that? He's playing with life and death, and he hasn't decided why."
        t "I'm going to give it to somecat who needs it!"
        t "I just ... haven't decided who."
        l "You're a regular hero, Talonclaw."
        l "You want to feel the weight of your Clanmates' lives in your paws, you can be my guest."
        l "StarClan knows I could use a break from it."
        l "Here's your leaf. Make your choice wisely."
        l "Hey, what do you know? I'm feeling lighter already ..."
        show screen sickden with fade
        show locust_hunch_night
        play sound "sfx/game_tip.mp3"
        "Click on the {b}sick den entrance{/b} to access cats in the sick den."
        jump locust_menu
    else:
        l "Well, I suppose it frees up my paws for tomorrow ..."
        l "... Thank you, Talonclaw."
        t "Don't mention it."
        jump locust_menu

label md3_clover:
    t "Hello? Locustleaf?"
    t "Listen, I know you don't want me in here, but I have something to tell you. It's important."
    t "It's about ..."
    show cloverpaw_sit_center with easeinleft
    t "... Cloverpaw?" 
    c "Hey."
    t "What are you ...?"
    c "You can hold off on the whole 'concerned, contrite Clanmate' thing."
    c "I already did the messy part for you."
    t "You ... turned yourself in?"
    c "Figured I might as well. No getting around the inevitable."
    c "Think I'll get points in StarClan for it?"
    t "Don't say things like that. You still have a good shot at beating this."
    t "Locustleaf is the most talented medicine cat in the forest. He'll do everything he can to --"
    c "Yeah, alright. You can save your breath, Talonclaw."
    c "Don't you get it? You don't have to feel bad anymore."
    c "I ... I don't want any cat to feel bad."
    c "I live my whole life trying to protect my friends, make them laugh, only for it to end on a downer?"
    c "That's so depressing."
    c "No, if I had it my way, I'd end it with a joke a joke."
    c "Speaking of which ..."
    c "Hey, Talonclaw, do you know why see-through graves never took off?"
    t "Uh ... Why?"
    c "It {i}remains to be seen.{/i}"
    c "Hahahahaha!"
    play audio "sfx/ES_Female, Single - Epidemic Sound.mp3"
    c "{i}*Cough* *Cough* *Cough*{/i}"
    play sound "sfx/rustle.mp3"
    play audio "sfx/impact.mp3"
    hide cloverpaw_sit_center with fade
    t "..."
    show locust_hunch_night with easeinright
    l "*Snrk* ... 'remains to be seen.' Clever."
    t "Is she going to be alright?"
    l "Why do cats always ask me that question?"
    l "If I knew the answer, there wouldn't need to be a medicine cat, would there?"
    l "Maybe she'll get better. Maybe she won't. It's in the paws of StarClan now."
    t "Come on, Locustleaf. Don't be like that."
    t "You'll take care of her, won't you?"
    hide locust_hunch_night
    l "..."
    show locust_loaf_night
    l "... Of course I will."
    l "I would never forgive myself if I didn't."
    t "Good."
    t "Because I would never forgive you, either."
    hide locust_loaf_night
    show locust_hunch_night
    l "I would never forgive {i}you{/i} if you did."
    t "Heh."
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
        "That's it":
            jump md3_end

label md3_clover2:
    $ already_cloverpaw = True
    t "Do you think Cloverpaw did the right thing?"
    t "What if she's really fine, but she ends up catching something serious from one of the cats inside?"
    l "It's worth the risk."
    l "The apprentices are vital to the future of this Clan."
    l "The potential for any contagion among them is far too serious to be left unaddressed."
    t "I know ..."
    l "Don't worry. I'll be sure to keep her separated from those whose symptoms are more advanced."
    l "... Though, I am tempted to send her in just to liven things up in there."
    l "The other patients could use a healthy dose of her courage."
    jump locust_menu

label md3_kits:
    $ already_kits = True
    t "... I still can't believe the kittens are gone."
    t "They barely even got to live."
    l "... My mentor believed that they stay kits forever up in StarClan. But I disagree."
    l "I like to think they grow and train and make mistakes. Just like the living."
    t "Think that's what this famine is?"
    t "Just one big mistake from StarClan?"
    l "I've seen apprentices with less common sense."
    t "..."
    jump locust_menu

label md3_catmint:
    $ already_catmint = True
    t "Here."
    hide locust_hunch_night
    show locust_lay_night
    l "... Great. It's a catmint leaf. What about it?"
    t "It's for you."
    t "I want you to have it."
    l "What is this, a joke?"
    l "You ask me for my own herbs, just to give them back to me?"
    t "What happened to that talk from earlier, about a medicine cat being worth a dozen warriors?"
    t "Who's saved more lives than you, Locustleaf?"
    l "..."
    hide locust_lay_night
    show locust_hunch_night
    l "Give the herbs to Maplebreeze."
    t "What?"
    l "You say I've saved lives. Well, not nearly enough of them."
    l "Maplebreeze is still young. She has her whole life ahead of her."
    l "She's the one who deserves these herbs. Not me."
    t "Locustleaf ..."
    t "How selfless of you."
    l "Tch. It's only logical. She's far more of an asset to ThunderClan than I am, at this stage."
    l "Besides. Like I said earlier. I'm not sick."
    t "... Of course."
    jump locust_menu

label md3_pouncetail:
    $ already_pouncetail = True
    if quest_gather_herbs.cancelled:
        l "By the way, how did your search for catmint go?"
        l "Manage to find anything?"
        t "... I decided to spend my time hunting, instead."
        l "Ha. Finally, he wisens up."
        l "It's like I always say. Leave the medical work to the medicine cats."
        l "You warriors wouldn't last a day in our paws, anyway."
    t "Where is Maplebreeze?"
    l "Recovering in the sick den, with the rest of the patients."
    t "Could I ... possibly see them?"
    t "I need to do a favor for Briarstar."
    l "Absolutely not. The sick den is for medicine cats and patients only."
    l "Unless you intend on staying back there."
    t "Please? I swear, I'll be in and out. Like I wasn't even there."
    t "What if news of her deputy is the push Briarstar finally needs to start being a leader again?"
    hide locust_hunch_night
    show locust_loaf_night
    l "Hmph. Something tells me no matter what I say, I won't be able to convince you what a mouse-brained idea this is."
    l "And StarClan knows I won't be able to stop you by force."
    l "So go ahead and risk your life, if that's what you want to do so badly."
    l "And if you end up back in my den because of it, don't say I didn't warn you."
    show screen sickden with fade
    play sound "sfx/game_tip.mp3"
    "Click on the {b}sick den entrance{/b} to access cats in the sick den."
    jump locust_menu

label md3_flipcloud:
    $ already_flipcloud = True
    t "I took Redpaw and Fawnpaw out earlier today. They miss their father."
    t "How is he doing?"
    l "... Somehow, I get the sense that, if I tell you the truth, I'll have two apprentices in my den tomorrow, pestering me to see him."
    l "So, for now, I'll just say 'he's fine.'"
    l "He misses his kits. He speaks of them often."
    t "You really want me to lie to the apprentices?"
    l "Not a complete lie. That last part is true."
    l "If you know what's good for them, that should be enough for you."
    jump locust_menu

label md3_cough:
    $ already_cough = True
    l "{i}*Cough* *Cough* *Cough*{/i}"
    t "I can't believe you aren't taking this cough more seriously, Locustleaf."
    t "You, more than any cat, should understand how important your health is to the future of the Clan."
    l "Have you seen what I do all day? The cats I work around?"
    l "Avoiding greencough isn't an option for me. If I cured myself, I would just catch it again from one of my patients."
    l "What good would that serve?"
    t "A lot!"
    t "You were just saying earlier how much medicine cats' lives are worth!"
    l "{i}*Cough* *Cough*{/i}"
    l "In case you hadn't noticed, Talonclaw ..."
    l "... I'm old."
    hide locust_hunch_night
    show locust_lay_night
    l "My body is failing in all sorts of ways, which compound by the day."
    l "Just this morning, I lost all the feeling in my back left paw."
    l "Who knows what'll be the next to go?"
    l "I don't want to waste a single moment of my remaining time worrying about the inevitable."
    l "Not even medicine cats can cheat death."
    hide locust_lay_night
    show locust_hunch_night
    l "If we could, this job would be a whole lot less interesting."
    jump locust_menu

label md3_future:
    $ already_future = False
    t "Locustleaf, you've seen more tragedy this leafbare than any cat."
    t "Do you think it changes who you are inside? As in, permanently?"
    t "Will ThunderClan ever go back to the way it was?"
    hide locust_hunch_night
    show locust_loaf_night
    l "..."
    l "I've been a medicine cat for a long time, Talonclaw. I've seen cats die in every possible way."
    l "But, with this latest outbreak, things are different."
    l "Cats don't fight to get out of the medicine den, anymore."
    l "They don't have that froth in their mouth to rejoin their Clanmates, their loved ones."
    l "No, with these ones, it's like they just ... slip away."
    l "Quick as falling asleep."
    t "That's terrible."
    l "It's pathetic. The whole lot of them are cowards."
    hide locust_loaf_night
    show locust_lay_night
    l "They think they can just give up on ThunderClan? That, just because they're dying, their Clan is over?"
    l "Mouse-dung. A warrior's most important job isn't to hunt for the Clan, or even protect it."
    l "It's to believe in it."
    l "As long as ThunderClan exists, it will need cats to believe."
    l "And, as long as THunderClan exists, cats will always have something to believe in."
    l "But not if we stop --"
    hide locust_lay_night
    show locust_hunch_night
    l "N-Not if we stop --"
    l "-- {i}*Wheeze* *Cough*{/i}"
    l "E-Excuse me ..."
    t "Is there anything I can get you?"
    l "No. It's alright."
    l "Nothing can stop what happens now."
    l "I do think living through this has changed who we are. And more change is coming."
    l "There isn't any way around it."
    l "But I'm not worried."
    l "ThunderClan will come out the other side of this -- damanged, sure, but alive."
    l "As long as cats still believe."
    l "Don't let the spark die out, Talonclaw."
    t "..."
    jump locust_menu

label md3_end:
    l "Good."
    l "Now, I think you know what I'm about to say, so why don't you go ahead and do it without me having to say it?"
    t "... Good night, Locustleaf."
    l "Good night."
    l "Let's hope we don't see each other tomorrow."
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
        "{b}Flipcloud,{/b} Redpaw and Fawnpaw's father. What would you like to do?"
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
    t "It's Talonclaw, Flipcloud. I have some herbs for you."
    fl "You're gonna have to pick something smaller, Redpaw ... That carp is way too big for you ..."
    t "These will make you feel better. Here, eat them."
    fl "You're growing up so quick, Redpaw ..."
    fl "Growing ... So ..."
    "Flipcloud laps up the herbs in a daze."
    hide sd_maple
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
    t "Have some catmint, Maplebreeze. I just gathered it earlier today."
    m "Oh, Talonclaw ... No."
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