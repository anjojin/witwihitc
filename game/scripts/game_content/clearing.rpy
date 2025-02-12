label clearing_first:
    $ final_game_screen = False
    $ quick_menu = True
    $ clearing_visited = True
    scene clearing_bg with fade
    show screen gameUI
    show lark
    show sootpaw

    l "Sootpaw?"
    l "What are you doing out here?"
    if lark_knows_sootpaw_clearing:
        l "I thought you got up early to train with Nettlebreeze."
        s "I did. And now, I'm sorting through all the prey in the freshkill pile."
    else:
        s "Nettlebreeze asked me to sort through all the prey in the freshkill pile."
    s "I can't believe how many cats in this Clan leave their half-eaten scraps around to rot!"
    menu:
        s "I mean, how hard is it to show a little decency and clean up after yourself?"
        "Offer to help":
            jump offer_help
        "Leave him to it":
            jump leave_soot

label offer_help:
    l "Need any help?"
    s "Eh ... that's okay. I was actually just finishing up."
    menu:
        s "As soon as this putrid squirrel gets buried, I'll finally be able to move onto alphebetizing Nettlebreeze's feather collection."
        "Insist on helping":
            jump insist_help
        "Leave it alone":
            jump leave_soot

label insist_help:
    l "Oh, perfect. So, I can bury the squirrel, and you can go do ... whatever lame thing you just said."
    s "I'd really rather you didn't."
    l "Why not? What's the big deal?"
    l "I think I can handle digging a hole and sticking some crowfood in it."
    s "It {i}is{/i} a big deal. It's a task that requires a great deal of precision, and --"
    menu:
        "{i}Really{/i} insist":
            jump really_insist
        "Back off":
            jump back_off

label leave_soot:
    l "You're a real hero, brother."
    s "Thanks, but I'm just doing my part."
    s "Maintaining a hygenic environment is vital for the health and longetivity of any prosperous Clan."
    l "Wow. Where'd you hear that?"
    s "Nettlebreeze."
    l "Of course."
    jump sootpaw_clearing_options

label really_insist:
    l "Why are you being so weird? Just let me do it!"
    "You snatch the squirrel away from Sootpaw and stalk across camp to bury it."
    s "Larkpaw!"
    "You hastily scoop a small hole with your paw and drop the squirrel inside."
    s "Stop, stop!!"
    l "What?"
    s "Are you blind? You're doing it all wrong!"
    menu:
        s "How am I going to explain myself to Nettlebreeze?"
        "Apologize":
            jump soot_apologize_prey
        "Defend yourself":
            jump defend_soot_prey

label soot_apologize_prey:
    l "Oh. I'm sorry. I didn't know."
    s "Of couse you didn't."
    s "You never know anything."
    l "..."
    s "..."
    s "... *Sighhhh*"
    s "Whatever. It's fine."
    s "Just ... let me fix it."
    "Sootpaw carries the squirrel across camp, where a collection of freshly-overturned dirt mounds lines the walls in neat rows."
    "He digs a small hole and methodically covers the remains with dirt."
    "Your irregular hole sticks out among the pristine lines."
    jump sootpaw_clearing_options

label defend_soot_prey:
    $ sootpaw_rel -= 10
    $ clan_rep -= 10
    l "Well, how was I supposed to know?!"
    s "You weren't. That's why I said I would do it."
    l "I was only trying to help!"
    s "Oh, well, {i}great{/i} job helping, Larkpaw! I really owe you one."
    s "Why do you even wanna be involved so badly, anyway? Trying to take credit for my idea?"
    l "StarClan, Sootpaw, self-obsessed much?"
    s "It's true, isn't it? You always do this!! Trying to cling to the back of my hard work to score a few measley goodwill points around the Clan."
    s "Well, I'm sorry, but it's not my fault they all hate you!"
    l "..."
    l "Wow."
    l "You don't hold back, do you, Sootpaw?"
    s "I ..."
    s "Just ... give me the stupid squirrel."
    s "At this rate, I'll be lucky to be finished with Nettlebreeze's feather collection by sunhigh."
    "Sootpaw snatches the squirrel from the hole you made and carries it to a collection of freshly overturned dirt mounds across camp."
    "Once he's finished his task, he stalks off towards the leader's den without another word."
    l "Dirtstripe ..."
    $ final_game_screen = True
    call screen gameUI


label back_off:
    l "Fine. StarClan." 
    l "Just bury the stupid squirrel, then, if you're so in love with it."
    s "It's only a task, Larkpaw."
    s "You don't need to take everything so personally."
    l "Tch ..."
    jump sootpaw_clearing_options

label sootpaw_clearing_options:
    $ already_soot_nettlebreeze = False
    $ already_soot_dream = False
    $ already_soot_willow = False
    $ already_soot_training = False
    $ already_soot_bright = False
    menu:
        s "Now, was there something specific you wanted to talk to me about? Because I have a lot to do today."
        "About Nettlebreeze ..." if not already_soot_nettlebreeze:
            jump soot_clearing_nettle
        "About Willowleap ..." if quest_willowleap_message.started and not already_soot_willow:
            jump soot_clearing_willow
        "About Brightpoppy ..." if bright_aggressive and not already_soot_bright:
            jump soot_clearing_bright
        "I had this dream ..." if not already_soot_dream:
            jump soot_clearing_dream
        "Wanna train together?" if not already_soot_training:
            jump soot_ask_training

label soot_clearing_nettle:
    $ already_soot_nettlebreeze = True
    l "You sure are thick with Nettlebreeze these days, huh?"
    s "My mentor holds me to a high standard, and I always try to push myself to meet that standard."
    s "Don't you and Rainwhisker experience the same?"
    l "I'm pretty sure Rainwhisker forgot my name yesterday."
    s "Ha. I'm sorry. I wish the two of you had a better relationship."
    l "Couldn't you report her to Nettlebreeze for negligence, or something?"
    s "Nettlebreeze says she paired the two of you because she thought Rainwhisker could help 'settle your caustic personality.'"
    s "Her words, not mine."
    l "I thought Flickerstar was the one making the pairings."
    s "Um ... yes. Right. Of course Flickerstar is the one making all the important decisions in the Clan."
    s "Just like he organizes all the patrols. And grooms between his own toes."
    jump sootpaw_clearing_options_2


label soot_clearing_willow:
    $ already_soot_willow = True
    l "Get this: Ma asked me to deliver a message to a SwiftClan border patrol later today."
    s "Really? Oh, StarClan. It must be because Emberflame just made deputy."
    s "What did she want you to say?"
    l "I don't think I can repeat it so close to the nursery ..."
    s "Ha! Classic. That cat never changes."
    s "If only she could channel all that spiteful energy into something productive, like hunting. SunClan would never go hungry again."
    s "That's funny that she tried to drag you into it." 
    s "Can you imagine how juvenile you'd have to be to agree to something like that?"
    l "Eheheh ... No ... I couldn't possibly ..."
    s "Just try to ignore her. Whenever she gets like this, Nettlebreeze always makes her do some menial chore until she calms down."
    s "What was it this time? StarClan, it's on the tip of my tongue ..."
    l "Clearing the snow out of the elder's den."
    s "Ha! Clearing the snow out of the elder's den. That's perfect."
    s "That oughta keep her occupied for a while."
    jump sootpaw_clearing_options_2

label soot_clearing_bright:
    $ already_soot_bright = True
    l "Y'know, I just paid Brightpoppy a visit in the nursery."
    s "Oh, no. Was it bad?"
    l "She's probably already started using me as a villain in her kit stories."
    s "Haha. I wouldn't take it personally."
    s "Maybe you can even view this as a learning experience. I didn't want to say anything, but being so antagonistic towards your Clanmates really isn't --"
    l "It wasn't just me, mouse-brain. She went after our whole family."
    l "You, and Willowleap, and --"
    s "Me? She mentioned me?"
    l "Yeah."
    s "What did she say?!"
    l "She said you were embarrassed to be related to us."
    s "Oh."
    s "Thank StarClan. I thought it was gonna be something bad!"
    l "Guess you can't be too offended when it's true, huh?"
    s "..."
    jump sootpaw_clearing_options_2


label soot_clearing_dream:
    $ already_soot_dream = True
    $ soot_knows_dream = True
    l "Um ..."
    l "Yes, there is something, actually ..."
    l "Any chance we could do this somewhere a bit more private?"
    s "How come? Is it serious?"
    l "No, no ... Well, maybe yes?"
    l "I'm not sure."
    s "What is this about, Larkpaw?"
    l "Okay. Don't freak out, but I had this dream last night ..."
    l "... And I think it might have been a vision. From StarClan."
    s "Whoa. What?"
    l "There was a pure white she-cat with stars in her fur."
    l "The way she spoke ... it seems like the Clans might be in danger."
    s "Larkpaw, this is ..."
    s "I have to report this to Nettlebreeze at once."
    l "Wait, what?"
    l "You mean you believe me?"
    s "Of course I believe you! Why wouldn't I?"
    if shimmer_knows_dream:
        l "It's just -- Shimmerpaw was being kind of a jerk about it earlier, and --"
        s "Wait, {i}Shimmerpaw{/i} knows about this?"
        s "Who else have you told?"
        if frond_knows_dream:
            l "No one!"
            l "Well ... I guess Frondfoot. But he doesn't count, right?"
            s "Larkpaw ..."
        else:
            l "No one! Just you and Shimmerpaw. Honest."
            s "Larkpaw ..."
    s "This could potentially be a matter of Clan security. It's beyond you, or I, or any other cat in this Clan."
    menu:
        s "We need to let Flickerstar and Nettlebreeze know, so that they can decide how to handle it."
        "Agree":
            jump soot_clearing_agree
        "Question intentions":
            jump soot_question_intentions
        
label soot_clearing_agree:
    l "Okay. You're right."
    l "This information is too important to keep between us."
    s "I'm glad you agree."
    l "I think I saw Flickerstar in the leader's den, earlier."
    l "Wanna go tell him right now?"
    s "Ehm ..."
    l "What?"
    s "Well ..."
    s "Don't you think it would be better if {i}I{/i} was the one to tell them?"
    menu:
        s "I'm very close with Clan leadership. I think they might take it better, coming from me."
        "Agree":
            jump soot_clearing_agree_2
        "Question intentions":
            jump soot_question_intentions

label soot_question_intentions:
    $ sootpaw_rel -= 10
    $ leadership_knows_dream = True
    l "... Why do you want to be involed so badly?"
    l "I'm the one who had the dream, not you."
    s "I know that, Larkpaw. But, like I said, this is bigger than either one of us."
    s "There could potentially even be others who received --"
    l "There are no others. The starry cat was talking directly to me."
    s "You can't know that for sure."
    l "... Ohh. Okay. I know what's going on here."
    l "You're jealous of me, aren't you?"
    s "Don't be ridiculous, Larkpaw."
    l "Haha! You totally are! Oh, StarClan, this is too good!"
    l "The deputy's perfect apprentice, jealous of his own brother."
    s "Oh, grow up!"
    l "What's the matter? Mad you're just a side character?"
    s "I'm just thinking logically, Larkpaw! If StarClan were to choose anyone in this Clan, why would it be --"
    l "Me, and not you?"
    s "... I was going to say 'an inexperienced apprentice.'"
    l "Ha."
    l "No, you weren't."
    s "..."
    s "I'm telling Nettlebreeze about this."
    s "Whether you like it, or not."
    if quest_sootpaw_training.started:
        s "And you can forget about training, later, too."
    l "Fine!"
    s "Fine."
    l "Great!"
    s "Great."
    scene clearing_bg with fade
    l "Dirtstripe ..."
    $ final_game_screen = True
    if quest_sootpaw_training.started:
        $ quest_sootpaw_training.started = False
        $ quest_sootpaw_training.cancelled = True
    call screen gameUI

label soot_clearing_agree_2:
    $ sootpaw_rel += 10
    $ clan_rep += 10
    $ leadership_knows_dream = True
    l "Yeah ... Yeah, I guess that makes sense."
    if clan_rep<0:
        l "Nettlebreeze doesn't seem to like me much, anyways."
        s "Nonsense. She just hasn't bothered to get to know you."
        s "But all of that's about to change."
    l "... Thanks, Sootpaw."
    l "Sometimes, it feels like you're the only one in this Clan who takes me seriously."
    s "Yes. Well. You are my kin."
    s "That has to count for something, right?"
    l "Heh. Look at you, getting all emotional."
    s "I'll arrange a meeting with Nettlebreeze as soon as I have some spare time."
    if quest_sootpaw_training.started:
        s "Of course, it may eat into the time I set aside to train with you later."
        s "Think you can find something else to do this afternoon?"
        l "I'll manage."
        s "I'm glad to hear it."
    else:
        l "Sounds good. Let me know what she says."
    s "..."
    l "..."
    s "... Hey, Larkpaw?"
    l "Yeah?"
    s "When I talk to Clan leadership, I need to make sure I have all my facts in order."
    s "Are you sure there's nothing about this dream you're leaving out?"
    l "Oh, uh ... No, I'm pretty sure I told you everything I know."
    s "So, she didn't ... mention any other cats?"
    s "Nothing about your blood, or your family?"
    l "... No, Sootpaw."
    l "She didn't say anything about you."
    s "..."
    s "Of course."
    s "Just trying to make sure I have all my facts straight."
    s "After the meeting is over, I'll meet you back here in the clearing."
    $ quest_sootpaw_reporting.started = True
    "{b}Quest Unlocked:{/b} Followup with Sootpaw."
    s ""

label soot_ask_training:
    $ already_soot_training = True
    l "Wanna train together, later?"
    s "I guess I have a bit of time between massaging Flickerstar's joints and picking up Nettlebreeze's prey."
    l "It's my lucky day."
    s "Where are you at in your training? Have you reached the belly rake, or are you still mastering the front-paw-blow?"
    l "Uh ..."
    s "Hmm. We'll start with the basics."
    if quest_shimmerpaw_training.started:
        menu:
            "{b}Warning:{/b} You have already agreed to training with Shimmerpaw. Would you like to switch to training with Sootpaw instead?"
            "Yes": 
                $ quest_sootpaw_training.started = True
                $ quest_shimmerpaw_training.started = False
                $ quest_shimmerpaw_training.cancelled = True
                "{b}Quest Unlocked:{/b} Train with Sootpaw."
            "No":
                l "Ah, mouse-dung. I forgot I have to train with Shimmerpaw later."
                s "Shimmerpaw, huh? Sounds educational."
                s "Try not to let her talk you into doing anything stupid."
                s "You'd be surprised how many grown warriors end up in Flickerstar's den with the excuse that it was Shimmerpaw's idea."
    s "Whenever you're ready, you can head off on a training patrol. I'll meet you then."
    jump sootpaw_clearing_options_2

label sootpaw_clearing_options_2:
    menu:    
        s "Anything else?"
        "About Nettlebreeze ..." if not already_soot_nettlebreeze:
            jump soot_clearing_nettle
        "About Willowleap ..." if quest_willowleap_message.started and already_soot_willow:
            jump soot_clearing_willow
        "About Brightpoppy ..." if bright_aggressive and not already_soot_bright:
            jump soot_clearing_bright
        "I had this dream ..." if not already_soot_dream:
            jump soot_clearing_dream
        "Wanna train together?" if not already_soot_training:
            jump soot_ask_training
        "That's it":
            jump end_soot_clearing

label end_soot_clearing:


