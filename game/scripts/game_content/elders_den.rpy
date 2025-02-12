label elders_den_first:
    $ final_game_screen = False
    $ quick_menu = True
    $ elders_visited = True
    scene elders_den_bg with fade
    show screen gameUI
    l "The elders' den. Flickerstar is probably headed here soon."
    l "Plus, maybe even my mother, Willowleap, if I can finally get the evidence I need to declare her medically insane."
    l "But, for now, it's quiet."
    l "... Really quiet."
    l "Kinda peaceful, even."
    l "..."
    l "Do I hear pawsteps?"
    show willowleap with fade
    w "Ah! Larkpaw!"
    l "{i}Woah, she got here sooner than I thought.{/i}"
    w "What are you doing in the elders' den?"
    l "What are {i}you{/i} doing in the elders' den?"
    w "Tch. That mouse-brain, {color=#7e1a1a}Nettlebreeze{/color}, ordered me to clear all the snow out of the nests."
    w "Can you believe that? Not one stinkin' elder in this Clan, and this is how she wants me to spend my time. It'll probably all be melted by sunhigh!"
    w "I know for a fact this is only because I spoke out against her on patrol, the other day."
    w "It's not my fault that I'm a natural-born leader!"
    w "Every cat in this Clan knows that I would make a better deputy than her. They're just too scared to say it."
    w "Whose choice was it to put her in charge, anyway?"
    l "... Flickerstar's."
    w "Oh, yeah."
    w "Speaking of which -- I'm glad I ran into you, kit. Your mom needs a favor."
    l "What is it?"
    w "I have it on good authority that there's going to be a SwiftClan patrol at the border later today."
    w "I need you to send over a message for me. It's about your father."
    l "Sure, Ma. What is it?"
    w "Tell them that Willowleap says:"
    w "'Emberflame, you may be the deputy now, but it doesn't change the fact that you're a **** stinkin' ***** **** deadbeat *** **** ****** with the breath of a ****.'"
    l "..."
    l "........"
    w "Did you get all that, or do you need me to say it again?"
    l "StarClan, Ma. I didn't even know half those words existed, 'till now."
    jump willowleap_options

label willowleap_options:
    $ already_criticized = False
    $ already_questioned_morality = False
    $ already_questioned_practicality = False
    menu:
        w "Well, it's all true. That mangy rat deserves every single syllable."
        "Criticize":
            jump criticize
        "Question Morality":
            jump question_morality
        "Question Practicality":
            jump question_practicality 

label criticize:
    $ already_criticized = True
    l "Seems rather petty and vindictive, even for you, Ma."
    w "Well, somecat has to speak up. It's disgusting, what's happening over there."
    w "How could they possibly make that cat their deputy after he broke the code and had a half-Clan relationship?"
    w "They shouldn't even let him take an apprentice, if that's the kind of example he's setting!"
    l "Do you even hear yourself right now?"
    w "Oh, please. It's completely different for me."
    w "I'm an excellent role model."
    l "Uh-huh ..."
    jump willowleap_options_2


label question_morality:
    $ already_questioned_morality = True
    l "I thought you never wanted to hear from Emberflame again."
    w "Oh, I don't."
    w "That dirtstripe can turn up dead in a ditch, for all I care."
    w "But, seeing as he {i}isn't{/i} dead in a ditch just yet, I want to make sure he isn't enjoying himself too much without me."
    l "How mature and well-adjusted of you."
    w "Ah, forget it. You're too young. You couldn't possibly understand."
    w "You'll know better once you grow up and have an ill-begotten fling of your own."
    l "Let's hope that never happens."
    jump willowleap_options_2

label question_practicality:
    $ already_questioned_practicality = True
    l "Can't you get some cat who was actually {i}assigned{/i} to the border patrol to do this?"
    w "Not a chance in StarClan. This is a family matter!" 
    w "The only cats allowed to insult my ex-suitor are myself and his own bastard children."
    l "Why don't you get Sootpaw to do it, then?"
    w "Ooh, there's an idea. Bring him along, too. Twice the guilt trip."
    jump willowleap_options_2


label willowleap_options_2:
    menu:
        w "So, are you gonna help me, or what?"
        "Criticize" if not already_criticized:
            jump criticize
        "Question Morality" if not already_questioned_morality:
            jump question_morality
        "Question Practicality" if not already_questioned_practicality:
            jump question_practicality 
        "Agree to help":
            jump agree_to_help
        "Refuse to help":
            jump refuse_to_help

label agree_to_help:
    $ willowleap_rel += 10
    l "Ehh ... Just how important is it that this 'message' get delivered to Emberflame?"
    w "More important than anything in the entire world."
    l "... *Sigh*"
    l "Fine. I'll do it."
    w "Really?"
    l "But if this ends in SwiftClan declaring war against SunClan, I'm not taking the fall!"
    w "Oh, please. That group of softpaws couldn't even declare war on a family of rabbits."
    l "Maybe if I wasn't half SwiftClan, I wouldn't let you boss me around so much ..."
    w "You're a good son, Larkpaw."
    l "Pfft. Alright."
    scene elders_den_bg with fade
    l "Guess I'm doing this, now ..."
    $ quest_willowleap_message.started = True
    $ quest_willowleap_message.abandoned = False
    "{b}Quest Unlocked:{/b} A Family Matter."
    $ final_game_screen = True
    call screen gameUI

label refuse_to_help:
    l "I'm not your little errand boy anymore, Ma. You're going to have to find someone else to instigate your familial conflicts."
    menu:
        w "Oh, {i}wow.{/i} Look at this, everybody. Larkpaw is an apprentice for two moons and, suddenly, he's too good for his poor old mother."
        "Stand your ground":
            jump stand_ground_willowleap
        "Relent":
            jump apologize_willowleap

label stand_ground_willowleap:
    $ willowleap_rel -= 10
    l "Yep! Sure am!"
    w "Tch ..."
    l "I gotta run now, Ma. Good luck cleaning out the elders' den."
    w "Pah. I'll show you where you can shove your good luck."
    scene elders_den_bg with fade
    l "Such a good role model, indeed ..."
    $ final_game_screen = True
    call screen gameUI

label apologize_willowleap:
    $ willowleap_rel += 10
    l "... Ah, c'mon, Ma. You know that's not true."
    l "I'm never too good for you."
    w "... You mean it?"
    l "Of course."
    w "You're a good kit, Larkpaw."
    w "Now, get out there and terrorize your father, before it gets too dark!"
    l "Wait, but --"
    w "No buts! You're losing daylight!"
    scene elders_den_bg with fade
    l "Ugh ... This is why I should never say anything nice."
    $ quest_willowleap_message.started = True
    "{b}Quest Unlocked:{/b} A Family Matter."
    $ final_game_screen = True
    call screen gameUI

label elders_den_revisit:
    $ final_game_screen = False
    $ quick_menu = True
    scene elders_den_bg with fade
    show willowleap
    show screen gameUI
    w "Clean the snow out of the nests ... who does that cat think she is?"
    l "Best leave her to it."
    $ final_game_screen = True
    call screen gameUI