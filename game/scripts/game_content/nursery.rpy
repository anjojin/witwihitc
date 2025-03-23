label n1:
    $ nursery_visited = True
    scene nursery bg with fade
    stop music fadeout 0.5
    play music "music/ES_View of the Park - Roots and Recognition.mp3" loop
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
    ba "Anything to eat???"
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
    be "Five tiny, little miracles."
    be "Stormkit looks so much like her mother, don't you think?"
    t "Yes. She's beautiful."
    t "They all are."
    be "Their father should be here to enjoy this moment. Have you seen Sunshadow anywhere?"
    t "Er, Sunshadow is ... out."
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
    be "Crowkit and Batkit already give me enough to worry about."
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
    be "She caught a little cold just this morning. She and Willowkit haven't been eating well."
    t "What?!"
    be "I was hoping it was just a temporary shock from their mother's passing. But, now ..."
    t "Do you think it's serious?"
    menu:
        be "I'm not sure. She's progressing rather quickly ..."
        "Offer to help":
            jump n1_offer_help
        "Decline to help":
            jump n1_decline
label n1_offer_help:
    $ talon_sun_bonus += 1
    t "I-I'll fetch the medicine cat!"
    $ quest_medical_opinion.started = True
    play sound "sfx/quest_unlocked.mp3"
    "{b}Quest Unlocked:{/b} Medical Opinion"
    t "Locustleaf is in the medicine den right now. He'll know what to do."
    be "Yes. You're right. It will be good to get his opinion."
    be "Thank you, Talonclaw. Best not to delay."
    be "I hate to be morbid, but in kits this young, sickness burns through them quick."
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
        be "Don't worry, girls. Help is coming."
        be "Just hang in there a little while longer ..."
        call screen gameUI
    if quest_medical_opinion.completed and not nursery_visited_prep2:
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
    be "These days, it seems like everycat's in need of catmint ..."
    jump n2_confront

label n2_confront:
    t "Should we let Sunshadow know?"
    be "... No."
    be "I don't want to frighten him."
    t "He's Featherkit's father. I think he has the right to be frightened."
    be "If he's Featherkit's father, then why isn't he here with her right now?"
    be "Why am I the one caring for his sick daughter, while he's out running a fool's errand?"
    be "You can tell him whatever you'd like, Talonclaw, but know this -- whatever happens to Featherkit, I am not taking the blame."
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
    be "Don't be a fool, Talonclaw. Sunshadow's beliefs aren't so logical. They never have been."
    be "These past few moons have been madness. Cats are terrified. They want an explanation."
    be "And when terrified cats want an explanation, they won't stop looking for one until they find it."
    t "... How will they know when that happens?"
    be "They won't feel afraid anymore."
    be "How many cats are going have to get hurt before that happens?"
    be "Who knows? I'm not sure it even matters."
    be "By that time, there may be nothing left."
    t "..."
    jump n2_finish

label n2_outsider:
    t "I used to be an outsider, too. Do you think Sunshadow blames me for his daughter's illness?"
    t "He's my best friend. He's practically my brother. I know for a fact that he would never --"
    be "Talonclaw."
    be "It doesn't matter."
    t "What do you mean, 'it doesn't matter?' Of course it matters!"
    be "I mean, you might not be as protected as you think."
    be "These past few moons have been madness. Cats are terrified. They want an explanation."
    be "And when terrified cats want an explanation, they won't stop looking for one until they find one."
    t "... How will they know when they've found one?"
    be "They won't feel afraid anymore."
    be "How many cats are going have to get hurt before that happens?"  
    be "Who knows? I'm not sure it even matters."
    be "By that time, there may be nothing left."
    t "..."
    jump n2_finish

label n2_sun_point:
    t "Sunshadow just believes -- accurately -- that it was foolish of Clan leadership not to exercise a bit more {i}foresight{/i} into --"
    be "Foresight? Do you hear yourself?"
    t "Half of the new cats this greenleaf were newborns, elders, or too sick to hunt! Briarstar should have known better."
    be "You buy into this jargon? That the weak are a burden and the Clan should belong to the strong?"
    t "Look at the other Clans. Look at what happens in nature. It's been proven over and over again."
    t "Sometimes, you need to trim the fat to keep everything in balance."
    be "That's the problem with cats like you. You think that you'll always belong to the 'strong' category."
    be "One day, you're going to be weak, Talonclaw."
    be "What will become of you, then?"
    be "Do you think you'll be a special case?"
    be "Think that cats like {i}Sunshadow{/i} are going to protect you?"
    be "No. I'd practice getting on your paws, now, and start begging for mercy."
    be "When the time finally comes, you'll be grateful for  the experience."
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
    call screen gameUI