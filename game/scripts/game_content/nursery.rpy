label n1:
    $ nursery_visited = True
    scene nursery bg with fade
    stop music fadeout 0.5
    play music "music/ES_Weightless Steps - Roots and Recognition.mp3" loop
    show screen gameUI
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    play audio "sfx/kitten1.mp3"
    cr "... What's this?"
    cr "Do I smell ... a rogue? On ThunderClan's territory???"
    show crowkit with easeinright
    cr "Reveal yourself, outsider, and come face-to-face with the terrifying power of ..."
    cr "*Gasp*"
    cr "Batkit, come out! Look who's here!"
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    show batkit with easeinleft
    ba "Talonclaw!!!"
    play audio "sfx/kitten2.mp3"
    cr "Talonclaw, Talonclaw, Talonclaw!!!"
    t "Haha! Hey, kittos!"
    t "What are you two playing?"
    ba "'Warrior and Rogue!' It's a game Crowkit made up."
    ba "We're supposed to take turns being the warrior and the rogue, but Crowkit totally cheats and takes longer than he should."
    cr "Do not!"
    ba "Do, too!"
    cr "Do not!!!"
    play audio "sfx/growl.mp3"
    be "Boys, stop pestering him."
    cr "But - But --"
    be "But nothing. Talonclaw probably has a lot to do today. Leave the grownup cats to talk in peace."
    play audio "sfx/kitten3.mp3"
    cr "Aww ..."
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    hide crowkit with moveoutright
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    hide batkit with moveoutleft
    play audio "sfx/slideup.mp3"
    show beetle_kits with easeinbottom
    be "Sorry about that. They never mind their manners."
    t "It's alright. They're good kits."
    be "They're a regular pawful, is what they are."
    be "I have no idea where they get their energy ..."
    be "Certainly not from me."
    t "It'll make them great assets to the Clan."
    t "Have you given any thought to who you hope will mentor them?"
    t "I can try putting in a good word with Briarstar!"
    t "The first time I was given an apprentice --"
    be "Talonclaw."
    be "It's really alright."
    be "You don't have to pretend to be interested in my children."
    be "I know who it is you're really here to see."
    t "..."
    be "Say hello to your Uncle Talonclaw, dears."
    show starlingkit
    show stormkit
    show willowkit
    show wolfkit
    show featherkit
    play audio "sfx/mews.mp3" volume 0.75
    wo "Mew!"
    st "Mrow!"
    w "Eep!"
    f "..."
    sta "Zzz ..."
    stop audio
    hide starlingkit
    hide stormkit
    hide willowkit
    hide wolfkit
    hide featherkit
    t "Wow ... wouldja look at that?"
    t "They're so ..."
    t "Small."
    be "Hmph. Their appetites certainly beg to differ."
    t "Do you have enough to feed them?"
    be "I get one tiny scrap of prey to share with my sons every day, and now there are five motherless kits quite literally sucking my belly dry every night."
    be "How would you like me to answer that question?"
    t "Don't worry. Sunshadow and I are here to help, now."
    t "We'll take extra hunting patrols, give up on rations ..."
    t "Even beg for twoleg scraps, if we have to."
    t "These kits will not go hungry under our watch."
    be "Hmm ..."
    be "And where is Sunshadow now?"
    t "Er ..."
    t "He's ..."
    t "... Out."
    be "Out where?"
    be "On patrol?"
    t "... Out digging a grave for Spottedlight."
    be "Tch."
    be "Do you hear that, little ones?"
    be "Your father must be the biggest fool in all of ThunderClan."
    if quest_crocus.started or quest_crocus.completed:
        t "You could cut him a little slack, you know."
        t "You know how much he loved Spottedlight. He's going through a really hard time."
        be "And what type of time are the rest of us going through?"
    else:
        t "I tried to talk him out of it."
        be "Apparently, not hard enough."
    t "..."
    be "If he wants to freeze to death, he can feel free to do so, but I'm not raising these kits on my own."
    be "More hungry mouths are the last thing I need."
    t "Don't say things like --"
    stop music
    show featherkit
    play audio "sfx/koff.mp3"
    f "*koff* *koff*"
    hide featherkit
    t "!!!"
    play music "music/ES_A Different Story - Roots and Recognition.mp3" loop
    be "Oh, StarClan. Not this again."
    t "Again?!"
    be "Shh, shhh ... it's alright little one. Settle down."
    t "What's happening? Why is she coughing?"
    be "... Featherkit developed a little cold just this morning."
    be "She and Willowkit haven't been eating well."
    t "You said they all had healthy appetites!"
    be "They did!"
    be "At least, at first ..."
    t "Do you think it's serious?"
    be "I can't say for sure."
    be "I've seen symptoms like this in young kits who lost their mothers ..."
    be "They never recovered from the shock. They just kept getting weaker and weaker until they eventually ..."
    menu:
        be "Should somecat alert Locustleaf?"
        "Offer to help":
            jump n1_offer_help
        "Decline to help":
            jump n1_decline
label n1_offer_help:
    $ talon_sun_bonus += 1
    t "I-I'll fetch him right away!"
    $ quest_medical_opinion.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Medical Opinion"
    be "Thank you, Talonclaw."
    be "Best not to delay."
    be "I hate to be morbid, but in kits this young, sickness burns through them quick."
    if quest_crocus.started:
        show screen n_tansy
        call screen gameUI
    else:
        call screen gameUI

label n1_decline:
    t "... It's just a little cough. It can't be all that bad, right?"
    t "No need to get the medicine cats involved in something so minor."
    t "Their paws are full enough, already."
    be "..."
    be "... You're right."
    be "I'm probably just being paranoid."
    be "All this death around camp has put me on edge."
    t "Don't worry. I'm sure it'll all work itself out."
    be "I hope you're right."
    t "..."    
    be "..."
    be "Well, I suppose you're busy."
    be "Thank you for dropping in. I know the kits appreciate it."
    t "Yes. Best of luck with the little ones."
    t "I'll tell Sunshadow you said hello."
    be "Don't bother."
    be "If he really wants help with these kits ... I can tell him, myself."
    if quest_crocus.started:
        show screen n_tansy
        call screen gameUI
    else:
        call screen gameUI

label n1_click_tansy:
    $ herbs_clicked += 1
    if herbs_clicked == 5:
        $ botanist.grant()
    play audio "sfx/plant_error.mp3"
    t "It's purple, and it's a flower ... but it's not quite a crocus."
    t "I'd better keep looking."
    hide screen n_tansy
    call screen gameUI

label n2:
    scene nursery bg with fade
    show beetle_kits
    stop music fadeout 0.5
    play music "music/ES_A Different Story - Roots and Recognition.mp3" loop
    show screen gameUI
    if quest_medical_opinion.started:
        show willowkit
        play audio "sfx/koff.mp3"
        w "*koff* *koff*"
        hide willowkit
        be "Oh, no ... Don't you start now, too."
        be "Don't worry, darlings. Help is coming."
        be "Just hang in there a little while longer ..."
        call screen gameUI
    elif quest_grim_tidings.started:
        be "Did you talk to --"
        t "Yes. I just got back from the medicine den."
        be "What did he say?"
        $ nursery_visited_prep2 = True
        menu:
            t "He said ..."
            "Truth":
                jump n2_truth
            "White lie":
                jump n2_white_lie
    else:
        show willowkit
        show wolfkit
        show featherkit
        play audio "ES_Boy, 3 Years Old, Coughing 01 - Epidemic Sound.mp3"
        w "*koff* *koff*"
        hide willowkit
        be "..."
        call screen gameUI

label n2_truth:
    t "... He said he doesn't like Featherkit's chances."
    t "You should probably separate her from her siblings, just in case she's contagious."
    be "Separate them how? You want me to move her to the medicine den all by herself?"
    be "Why don't I just go ahead and throw her onto the body pile, while I'm at it?"
    t "... I'm sorry."
    t "Locustleaf said she might still have a shot, if she gets catmint."
    if quest_gather_herbs.started:
        t "I'm going out to find some, now."
    be "These days, it seems like every cat's in need of catmint ..."
    jump n2_confront

label n2_confront:
    t "Should we let Sunshadow know?"
    be "... No."
    be "I don't want to frighten him."
    t "He's Featherkit's father. I think he has the right to be frightened."
    be "If he's Featherkit's father, then why isn't he here with her right now?"
    be "Why am I the one caring for his sick daughter, while he's out running a fool's errand who-knows-where?"
    be "You can tell him whatever you'd like, Talonclaw, but know this -- whatever happens to Featherkit, I am not taking the blame for it."
    t "What are you talking about?"
    t "Who would blame you?"
    t "What's happening to Featherkit is a terrible act of chance. It isn't like --"
    be "I'm an ex-loner, Talonclaw."
    be "From the way Sunshadow's been talking, I might as well have stolen the food right out of these kittens' mouths."
    be "You know it's true."
    menu:
        t "Come on. That's not fair ..."
        "Sunshadow doesn't think that way.":
            jump n2_sun_defend
        "Sunshadow has a point.":
            jump n2_sun_point
        "I was an outsider, too.":
            jump n2_outsider

label n2_sun_defend:
    $ talon_sun_bonus += 1
    t "Sunshadow has nothing against you. I know for a fact he's grateful for your help."
    t "He's just ... concerned about how many newcomers Briarstar let into the Clan when our resources were already stretched thin."
    t "That's all."
    be "What makes Sunshadow and these so-called 'newcomers' any different?"
    be "His body takes up just as much space in the warriors' den as mine does."
    be "We eat the same food, drink the same water, bring back the same amount of prey."
    be "And, now, when both of us are starving, somehow I'm the one to blame, and he isn't?"
    be "Don't be a fool, Talonclaw. Sunshadow's beliefs aren't so rational. They never have been."
    be "These past few moons have been madness. Cats are terrified. They want an explanation."
    be "And when terrified cats want an explanation, they won't stop looking for one until they find it."
    t "... How will they know when that happens?"
    be "They won't feel afraid anymore."
    be "By the time that happens, there may be nothing left."
    t "..."
    jump n2_finish

label n2_outsider:
    t "I used to be an outsider, too. Do you think Sunshadow would blame {i}me{/i} for his daughter's illness?"
    t "He's my best friend. He's practically my brother. I know for a fact that he would never --"
    be "Talonclaw."
    be "It doesn't matter."
    t "What do you mean, 'it doesn't matter?' Of course it matters!"
    be "It won't protect you."
    be "None of it will."
    be "These past few moons have been madness. Cats are terrified. They want an explanation."
    be "And when terrified cats want an explanation, they won't stop looking for one until they find one."
    t "... How will they know when they've found one?"
    be "They won't feel afraid anymore."
    be "By the time that happens, there may be nothing left."
    t "..."
    jump n2_finish

label n2_sun_point:
    t "Sunshadow just believes -- accurately -- that it was foolish of Clan leadership not to exercise a bit more {i}foresight{/i} into --"
    be "Foresight? Do you hear yourself?"
    t "Half of the ThunderClan this greenleaf were newborns, elders, or too sick to hunt! Briarstar should have known better."
    be "Briarstar gave me a place to stay when rogues drove me out of my home."
    be "She gave me the chance to provide a better life for my kits."
    be "You're telling me you really buy into this jargon? That the weak are a burden and the Clan should belong to the strong?"
    t "Look at the other Clans. Look at what happens in nature. It's been proven over and over again."
    t "Sometimes, you need to trim the fat to keep everything in balance."
    be "That's the problem with cats like you. You think that you'll always belong to the 'strong' category."
    be "One day, you're going to be weak, Talonclaw."
    be "What will become of you, then?"
    be "Do you think you'll be a special case?"
    be "Think that cats like {i}Sunshadow{/i} are going to protect you?"
    be "No. I'd practice getting on your paws, now, and start begging for mercy."
    be "When the time finally comes, you'll be grateful for the experience."
    t "..."
    jump n2_finish

label n2_white_lie:
    $ talon_clan_bonus += 2
    t "He said that Featherkit will be fine, as long as she gets the herbs she needs."
    if quest_gather_herbs.started:
        t "I'm going out to fetch her some, now."
    be "Good. You should hurry. It's not just Featherkit, anymore."
    be "Willowkit's developed a wheeze now, too."
    t "W-What? Already? I was only gone a few moments!"
    t "Should we quarantine them? Separate them from the rest of their siblings?"
    be "Separate them how? You want me to move them to the medicine den all by themselves?"
    be "Why don't I just go ahead and throw them onto the body pile, while I'm at it?"
    t "... I'm sorry."
    be "...*Sigh*"
    be "It's alright."
    be "Once they get their herbs, it's all going to be better, right?"
    t "... Yes. It's all going to be better."
    show willowkit
    show wolfkit
    show featherkit
    play audio "sfx/koff.mp3"
    w "*rasp* *wheeze*"
    be "Whatever you end up doing, you'd better do it fast."
    be "I'm not sure how much longer any of it will matter."
    "{b}Quest Completed:{/b} Grim Tidings"
    $ quest_grim_tidings.started = False
    $ quest_grim_tidings.completed = True
    call screen gameUI

label n2_finish:
    show willowkit
    show wolfkit
    show featherkit
    play audio "sfx/koff.mp3"
    w "*rasp* *wheeze*"
    hide willowkit
    t "Oh, no. Willowkit's started now, too?"
    be "... You should leave."
    be "Whatever you end up doing, you'd better do it fast."
    be "I'm not sure how much longer any of it will matter."
    play audio "sfx/quest_unlocked.mp3"
    "{b}Quest Completed:{/b} Grim Tidings"
    $ quest_grim_tidings.started = False
    $ quest_grim_tidings.completed = True
    call screen gameUI

label n3:
    $ nursery_visited_postp = True
    scene nursery bg night with fade
    stop music fadeout 0.5
    play music "music/ES_Asheville Lament - American Legion.mp3" loop
    show screen gameUI
    show beetle_curl with easeinbottom
    if got_catmint:
        jump n3_catmint
    elif quest_check_nursery.started:
        jump n3_check
    else:
        jump n3_no_check

label n3_no_check:
    t "Hello?"
    be "..."
    be "Talonclaw."
    t "What's going on?"
    t "Where are Crowkit and Batkit?"
    be "..."
    hide beetle_curl
    show beetle_kits_night
    be "... I sent them outside."
    be "So they wouldn't see it happen."
    jump n3_continue

label n3_catmint:
    t "Beetle!"
    t "I got it!"
    t "Just like I said I would"
    t "The cat ..."
    t "... mint."
    be "..."
    t "... Is something wrong?"
    t "You should be excited."
    be "..."
    hide beetle_curl
    show beetle_kits_night 
    be "... I'm sorry, Talonclaw."
    jump n3_continue

label n3_check:
    be "Talonclaw --"
    t "Tell me it's not what I think it is."    
    t "Tell me I'm not too late."
    be "..."
    hide beetle_curl
    show beetle_kits_night
    be "... I take it you must have run into one of my kits."

label n3_continue:
    t "No."
    t "{i}No.{/i}"
    if quest_gather_herbs.completed:
        if got_catmint:
            t "How long has it been? There might still be time!"
            t "I have the catmint right here! Maybe -- if we give it to them -- they can still --"
            be "Talonclaw."
            be "I'm sorry."
            t "Where are they now?"
            jump n3_cont_2
    elif not nursery_visited:
            t "This can't be happening."
            t "I - I didn't even know that any of the kits were sick!"
    else:
        be "... Featherkit left first, and her sister followed shortly after."
    be "It happened quick. They went out like little embers."
    be "Nothing the medicine cats could do, they said."
    t "..."
    t "... Where are Featherkit and Willowkit now?"
    jump n3_cont_2

label n3_cont_2:
    be "Where do you think? I moved them outside."
    t "Already?!"
    t "In this cold?"
    be "They won't feel it anymore, Talonclaw."
    be "They're sleeping with the other little ones, now."
    be "In the elder's den."
    t "... This is all my fault."
    if nursery_visited:
        if not quest_medical_opinion.completed:
            t "I should have taken their sickness more seriously. Maybe if Locustleaf had known earlier, he --"
        else:
            if quest_gather_herbs.completed:
                t "Maybe if I had been faster gathering the catmint, they --"
            elif quest_gather_herbs.failed:
                t "Maybe if I had managed to find the catmint, they --"
            else:
                t "I should have tried harder to save them. Maybe if I had been brave enough to look for catmint, they --"
    else:
        t "I should have checked on them earlier. Maybe if I had been here, they could've --"
    be "What good is that, now?"
    be "The shame. The responsibility. It won't make any difference."
    t "..."
    be "Somecat needs to break the bad news to your friend."
    t "Oh, StarClan. Sunshadow."
    t "He's going to be devastated. He didn't even know that they were sick."
    be "He'll understand."
    t "How can you say that?"
    be "For the sakes of these three kits, he'll have to understand."
    if quest_gather_herbs.completed or quest_gather_herbs.failed:
            be "It's up to Sunshadow to fight for his family, now."
            be "No more passing the blame."
            be "No more running away to dig graves."
            t "..."
            if got_catmint:
                t "... What do I do with the catmint, now?"
                be "Give it to somecat who needs it."
                be "I'm sure you can think of a few."
                be "It's not too late for you to save a life tonight."
                play sound "sfx/quest_unlocked.mp3"
                $ quest_miracle_worker.started = True
                "{b}Quest Unlocked:{/b} Miracle Worker"
                t "..."
            be "Don't look at me like that, Talonclaw."
            be "So guilty."
            be "So full of remorse."
            be "We did everything we could."
            t "But it still wasn't enough."
            t "We couldn't save them."
            be "Sometimes, that's just the way things are."
            be "It doesn't change the fact that you gave everything you had to give."
            be "Willowkit and Featherkit both know that. And they'll be grateful when you see them again in StarClan."
            be "Until then, we have to keep trying for the ones that are still here."
            t "Even though it hurts?"
            be "Even though it hurts."
            t "..."
    else:
        be "You know, it's funny."
        be "For how much the two of you claim to care about this little family, I was the only one who watched those two kits take their final breaths."
        t "..."
        be "I'm not going through this alone anymore, Talonclaw."
        be "Now, it's your and Sunshadow's turns."
        be "I've already grieved more than my share."
        t "..."
    play sound "sfx/quest_unlocked.mp3"
    $ quest_check_nursery.started = False
    $ quest_check_nursery.completed = True
    "{b}Quest Completed:{/b} Check Nursery"
    play sound "sfx/quest_unlocked.mp3"
    if quest_favorite_prey.completed:
        $ quest_harbringer_final.started = True
    else:
        $ quest_harbringer.started = True
    "{b}Quest Unlocked:{/b} Harbringer"
    call screen gameUI

label n4:
    scene nursery bg night with fade
    stop music fadeout 0.5
    if quest_followup_beetle.started:
        jump n4_ending
    else:
        play music "music/ES_Asheville Lament - American Legion.mp3" loop
        show screen gameUI
        show beetle_curl with easeinbottom
        be "..."
        call screen gameUI

label n4_ending:
    play music "music/ES_A Sign of Solace - Daniel Kaede.mp3" loop
    show screen gameUI
    show beetle_curl with easeinbottom
    t "One, two, three kits ..."
    t "Plus eleven makes fourteen ..."
    hide beetle_curl 
    show beetle_kits_night
    be "Did you say something?"
    t "Oh, no. I'm sorry. I was just thinking out loud ..."
    t "I just came back to say that I followed your advice. I gave the catmint away."
    if got_catmint=="maple":
        t "Maplebreeze seemed very appreciative. I think the herbs will go a long way in supporting her recovery."
        be "Picking the medicine cat ... how {i}logical{/i} of you."
    elif got_catmint=="pounce":
        t "I figured it might help Pouncetail get better, but ... he didn't really seem to notice."
        be "Hm. Seems like we'll be getting a change in leadership soon, after all ..."
    elif got_catmint=="flip":
        t "Flipcloud seemed appreciative ... or, at least I think he did. It was sort of hard to tell."
        t "I just hope it helps him see his kits again, soon."
        be "I hope so, too. He was always the most doting father ... I'm surprised those two apprentices aren't spoiled rotten."
    elif got_catmint=="clover":
        be "Who'd you give it to?"
        t "Erm ... a cat who needed it."
        be "That hardly narrows it down."
        t "..."
    be "And what about Sunshadow?"
    be "Did you break the news?"
    t "Yes."
    be "How did he take it?"
    t "... How do you think he took it?"
    be "Hard, I presume?"
    t "Yes. Very hard."
    t "Can you blame him?"
    be "I take it he didn't come back to camp with you, then?"
    t "... No."
    t "He didn't."
    if talon_sun_bonus>0:
        be "..."
        t "Listen, Beetle, I know Sunshadow is a lot to handle, but he's not really a bad cat."
        t "He wants to be a good father to these kits. I know he does."
        t "He's just ... going through a lot right now."
        be "You don't have to defend him to me, Talonclaw."
        be "I've lost kits before. I have sympathy for what he's going through."
        be "I just hope he exercises caution."
        be "Even though I'll never understand it ... cats in this Clan do listen to what he has to say."
        be "I have a feeling he's going to try to make his pain all of ThunderClan's problem."
        be "Play the 'poor, sympathetic single father' role."
        t "You mean, you don't really believe he cares about his kits?"
        be "..."
        hide beetle_kits_night
        show beetle_curl
        be "... I'll believe it when I see it."
    else:
        be "..."
        t "I don't know how to get through to him."
        t "He's been like this ever since he was a kit."
        t "Whenever he sets his mind to something, it's impossible to talk him out of it."
        be "Hmph."
        be "I guess I'll just have to wait for the day he finally sets his mind on being a father, then?"
        t "C'mon, Beetle. You could have a little sympathy."
        t "You've lost kits before, haven't you?"
        be "... Yes."
        be "I have."
        t "So then, you must understand how he feels."
        be "..."
        hide beetle_kits_night
        show beetle_curl
        be "I don't think I've ever truly understood what that cat is feeling."
        be "I think he can make other cats feel however he wants them to feel."
        be "But as for him ..."
        be "What's truly inside his heart ..."
        be "I have no way of knowing."
    t "..."
    t "... Do you think they'll make it?"
    t "The other three kits?"
    be "Hmm ..."
    hide beetle_curl
    show beetle_kits_night
    be "I guess that answer depends on what exactly it is you mean by 'make it.'"
    be "Will they make it out of kithood?"
    be "Maybe. Only time will tell. They're awfully fragile at this age."
    be "But ... will things really be any easier for them when they become apprentices?"
    be "Or even warriors?"
    t "Surely, the famine will be over by then!"
    be "Okay. But, what comes after the famine?"
    be "Even you aren't so naive, Talonclaw."
    be "I hear you counting your Clanmates' nests under your breath at night."
    be "Think that greenleaf is going to stir the dead from their graves?"
    be "That the blood is going to water the trees and make the flowers grow?"
    be "No."
    be "Nothing can stop what happens now."
    be "Something big is brewing for ThunderClan, and StarClan knows it won't be for the better."
    "{b}BEGIN ILLUSTRATION HERE{/b}"
    be "... I can only hope that whoever is in charge next is kind to them."
    be "I had hoped that my sons being born here would afford them a better life than mine."
    be "The mighty ThunderClan."
    be "Where a cat can realize his destiny."
    be "Become whoever he's meant to be."
    t "Your sons can still have that life."
    t "We may be going through a rough patch right now, but ThunderClan is still the place you always dreamed about."
    be "... Oh, Talonclaw."
    be "It was never the place I always dreamed about."
    be "My sons are only three moons old, and, already, they dream of murder."
    be "I see those little claws, those little teeth, and know they'll be stained with the blood of our family, one day."
    be "And, when their bodies finally break down ..."
    be "When their claws break and their teeth fall out and they've hunted their last piece of prey ..."
    be "... Then this Clan will discard them. Just like it does all the cats who've outlived their usefulness."
    be "Why else do you think the elder's den was the first to go in the famine?"
    be "The weak have to die to feed the strong."
    t "That's a rather defeatist attitude, isn't it?"
    t "ThunderClan may not be perfect, but we have these rules and principles for a reason. They're better than the alternative."
    be "... You still don't get it, do you?"
    be "That's good. You should try to keep it that way."
    be "One day, the fantasy will crumble, and you'll be forced to see things the way they really are."
    be "Just like I did."
    be "I'd tell you to get ready, but there wouldn't be any point."
    be "It's a heartbreak you can't really prepare for."
    t "..."
    be "In a way, these kits are the lucky ones."
    be "They already understand what it means to be a ThunderClan warrior."
    be "They were born into it."
    be "Whatever violence gets throws at them, they'll be ready to face it."
    be "Teeth, and claws."
    t "..."
    st "Mew!"
    be "Oh."
    be "The kits are hungry again."
    be "Talonclaw, could you fetch us something to eat?"
    t "... I'm not sure how much is left on the pile."
    t "Would you be open to splitting?"
    be "Sure."
    be "Why not share a meal with a traitor?"
    be "After all ..."
    scene black with fade
    be "... it's the end of the world."
    "{b}END GAME{/b}"
    $ MainMenu(confirm=False)()









