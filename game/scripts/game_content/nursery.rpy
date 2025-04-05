label n1:
    $ nursery_visited = True
    scene nursery bg with fade
    stop music fadeout 0.5
    play music "music/ES_Weightless Steps - Roots and Recognition.mp3" loop
    show screen gameUI
    t "... Hello?"
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    show crowkit with easeinright
    play audio "sfx/kitten1.mp3"
    cr "*Gasp* Batkit! Look who's here!"
    play audio "sfx/ES_Twig, Snap From Branch - Epidemic Sound.mp3"
    show batkit with easeinleft
    ba "Talonclaw!!!"
    play audio "sfx/kitten2.mp3"
    cr "Talonclaw, Talonclaw, Talonclaw!!!"
    ba "What are you doing here? Shouldn't you be out on patrol with the rest of the warriors?"
    cr "Didja bring us any presents?"
    ba "Didja fight off any rogues???"
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
    be "They're a regular pawful, is what they are. But I suppose they keep me young."
    be "I could certainly use more of their energy ..."
    t "How are the newborns doing?"
    be "Ah, yes. Say hello to your Uncle Talonclaw, dears."
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
    t "They're so small."
    be "They may be small, but their appetites certainly aren't."
    be "I'm not a young queen anymore, Talonclaw. My milk won't last forever."
    t "Don't worry. You won't go hungry."
    t "Sunshadow and I will make sure of it."
    be "Hmm ..."
    be "And where is Sunshadow now?"
    t "Er, he's ... out."
    be "Out where? On patrol?"
    t "... Out digging a grave for Dapplefeather."
    be "Tch."
    be "Do you hear that, little ones? Your father must be the biggest fool in all of ThunderClan."
    if quest_crocus.started or quest_crocus.completed:
        t "You could cut him some slack, you know. He's been going through a really hard time."
        be "What type of time have the rest of us been going through?"
    else:
        t "I tried to talk him out of it."
        be "Apparently, not hard enough."
    be "If he wants to freeze to death, he can feel free to do so, but I'm not raising these kits alone."
    t "Don't say things like --"
    stop music
    show featherkit
    play audio "sfx/koff.mp3"
    f "*koff* *koff*"
    hide featherkit
    t "!!!"
    play music "music/ES_A Different Story - Roots and Recognition.mp3" loop
    be "Oh, StarClan. Not this again."
    be "Shh, shhh ... it's alright little one. Settle down."
    t "What's happening? Why is she coughing?"
    be "She may have caught something. She and Willowkit haven't been eating well."
    t "What?!"
    be "I was hoping it was just a temporary shock from their mother's passing. But, now ..."
    t "Do you think it's serious?"
    menu:
        be "I'm not sure ..."
        "Offer to help":
            jump n1_offer_help
        "Decline to help":
            jump n1_decline
label n1_offer_help:
    $ talon_sun_bonus += 1
    t "I-I'll fetch the medicine cat right away!"
    $ quest_medical_opinion.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Medical Opinion"
    t "Locustleaf is in the medicine den. He'll know what to do."
    be "Yes. You're right. It will be good to get his opinion."
    be "Thank you, Talonclaw. Best not to delay."
    be "In kits this young, sickness burns through them quick."
    if quest_crocus.started:
        show screen n_tansy
        call screen gameUI
    else:
        call screen gameUI

label n1_decline:
    t "... It's just a little cough. It can't be all that bad, right?"
    t "No need to get the medicine cats involved in something so minor. Especially since their paws are already so full."
    be "... Yes. You're right. I'm probably just overreacting."
    be "All this death around camp has been making me paranoid."
    t "Don't worry. I'm sure she'll be feeling better in no time."
    be "Yes. I hope you're right."
    be "..."
    t "..."
    be "Well, I suppose you're busy."
    be "Thank you for dropping in. I know the kits appreciate it."
    t "Yes. Best of luck with the little ones."
    t "I'll tell Sunshadow you said hello."
    if quest_crocus.started:
        show screen n_tansy
        call screen gameUI
    else:
        call screen gameUI

label n1_click_tansy:
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
    be "By that time, there may be nothing left."
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
    be "By that time, there may be nothing left."
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
    if quest_check_nursery.started:
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
    t "There are only 14 of us left, now ..."
    hide beetle_curl 
    show beetle_kits_night
    be "What?"
    t "Oh, I'm sorry. I was just thinking out loud ..."
    be "Did you get rid of the catmint?"
    t "Yes. Just like you suggested."
    if got_catmint=="maple":
        t "Maplebreeze seemed very appreciative. I think the herbs will go a long way in supporting her recovery."
    elif got_catmint=="pounce":
        t "I tried giving it to Pouncetail, but ... he didn't really seem to notice."
    elif got_catmint=="flip":
        t "Flipcloud seemed appreciative ... or, at least I think he did."
        t "I hope it helps him get to see his kits again, soon."
    elif got_catmint=="clover":
        be "Who'd you give them to?"
        t "Erm ... a cat who needed them."
    be "Well done. And what about Sunshadow?"
    t "... He didn't exactly take the news well."
    t "But I can't say I blame him."
    be "I take it he didn't come back to camp with you?"
    t "... No."
    t "He didn't."
    if talon_sun_bonus>0:
        be "..."
        t "Listen, Beetle, I know Sunshadow can be kind of a pawful, but he's not really a bad cat."
        t "He wants to be a good father to these kits. I know he does."
        t "He's just ... going through a lot right now."
        t "I mean, can you really blame him for needing to spend some time away from camp right now?"
        t "The wound is still so fresh."
        be "You don't have to defend him to me, Talonclaw."
        be "I've lost kits before. I have sympathy for what he's going through."
        be "As for him wanting to be a good father ..."
        hide beetle_kits_night
        show beetle_curl
        be "... I'll believe it when I see it."
    else:
        be "..."
        t "I don't know how to get through to him."
        t "He's been like this ever since he was a kit. Whenever he sets his mind to something, it's impossible to talk him out of it."
        be "Hmph."
        be "I guess I'll just have to wait for the day he finally sets his mind on being a father, then?"
        t "C'mon, Beetle. You could have a little sympathy."
        t "You've lost kits before, haven't you?"
        be "... Yes."
        be "I have."
        t "So you must know how he feels."
        be "I don't think I've ever truly known how that tom is feeling."
        be "I think he can make other cats feel however he wants them to feel."
        be "But as for him ..."
        be "What's really inside his heart ..."
        hide beetle_kits_night
        show beetle_curl
        be "I have no way of knowing."
    t "StarClan, Beetle."
    t "Do you think ..."
    t "Do you think the other three kits will make it?"
    t "Are they doing well?"
    hide beetle_curl
    show beetle_kits_night
    be "It depends on what you mean by 'make it.'"
    be "Make it out of kithood? Maybe. Only time will tell."
    be "But will things really be any easier for them when they become apprentices?"
    be "Or even warriors?"
    t "Surely, the famine will be over by then!"
    be "Okay. But what comes after the famine?"
    be "Even you aren't so naive, Talonclaw."
    be "I hear you counting your Clanmates' nests under your breath at night."
    be "Think greenleaf is going to stir the cats we've lost from their graves?"
    be "Think the blood is going to water the flowers and make the trees grow?"
    be "No. Things won't move on so easily."
    be "Nothing can stop what happens now."
    be "A change is brewing for ThunderClan, and it sure as StarClan won't be for the better."
    "{b}BEGIN ILLUSTRATION HERE{/b}"
    be "... I just hope that whoever is in charge next is kind to them."
    be "I had hoped that my sons being born here would mean they'd have a better life than mine."
    be "The mighty ThunderClan."
    be "Where a cat can realize his destiny."
    be "Become whoever he's meant to be."
    t "Your sons can still have that life."
    t "We may be going through a rough patch right now, but ThunderClan is still the place that you dreamed about."
    be "... Oh, Talonclaw."
    be "It was never the place that I dreamed about."
    be "I had to give my sons Clan names so cats wouldn't think less of them."
    be "Crowkit's name was supposed to be 'Crawford.' After my father."
    be "He's barely three moons old, now, and, already, he dreams of murder."
    be "And warriors encourage him, because he cats he wants to kill aren't from our Clan."
    be "And when the day comes that he's finally finished his work ..."
    be "When his body finally breaks down ..."
    be "... This Clan will discard him. Just like it does to all the cats who've outlived their usefulness."
    be "At least these kits won't make the same mistake I did."
    be "They won't have to grow up blaming themselves. Wondering just what it is that this place stands for."
    be "In a way, I almost envy them."
    be "They've already gotten all that grief out of the way."
    be "Whatever life throws at them, they'll be ready."
    t "..."
    st "Mew!"
    be "Shh ..."
    be "The kits are hungry again."
    be "Think you could fetch us something to eat?"
    t "... I'm not sure how much is left on the pile."
    t "Would you be open to splitting?"
    be "Sure."
    be "Why not?"
    be "I'm open to anything."
    scene black with fade
    be "After all ..."
    be "... it's the end of the world."
    "{b}END GAME{/b}"
    $ MainMenu(confirm=False)()









