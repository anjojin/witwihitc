label nursery_first:
    $ final_game_screen = False
    $ quick_menu = True
    $ nursery_visited = True
    scene nursery_bg with fade
    show screen gameUI
    show lark
    show brightpoppy laying 
    b "Oh! Larkpaw!"
    b "Come in quickly! Don't let the cold air in! I just got the kits warmed up!"
    l "Ah! Sorry!"
    hide brightpoppy laying
    show brightpoppy standing
    b "*Sigh* It's alright. Just try to be more mindful next time."
    l "No, really. I'm sorry. I --" 
    b "Larkpaw, it's really alright!"
    b "You're an apprentice. I'm sure you have a lot on your mind."
    l "Sorr -- Er, thanks, Brightpoppy."
    l "How are the kits doing? Is there anything I can help you with?"
    b "I think we're okay! Creekkit and Applekit just went down for their nap. Flykit is the only one who's still up."
    l "I hope they haven't been giving you too much trouble!"
    b "Oh, nothing I can't handle. Though, things have been difficult ever since their father passed on."
    b "If only StarClan had inflicted that bee sting onto a different cat ..."
    b "As well as that bee allergy."
    b "I'm sorry. Is that terrible to say?"
    l "Not at all!"
    l "I think it's perfectly natural to want your kits to have a father in their lives."
    b "You're such a reassuring presence, Larkpaw. Thank you."
    l "Of course."
    b "Oh, look! It seems like Flykit wants to join us."
    hide brightpoppy standing
    show brightpoppy side
    show flykit
    "Flykit scampers over."
    b "Flykit! Look who's here! Come say hello!"
    f "Hello!"
    f "Are you Larkpaw?"
    l "Yes, I am!"
    f "Are you the one my mommy says isn't a real SunClan cat?"
    l "..."
    b "..."
    l "Uh ..."
    b "Hahahaha!"
    b "Oh, Flykit. You know that mommy was only joking when she said that!"
    b "Larkpaw is as just as SunClan as any of us, in spite of his, ehm, heritage ..."
    f "Oh."
    f "Then, how come you also said that Larkpaw's mommy is a feather-brained, two-timing traitor who's going to burn in the Place of No Stars forever?"
    b "..."
    l "..."
    b "Eheh ... Kits ... Where do they get it from?"
    l "Sounds like they get it from their parents."
    menu:
        f "Why is everyone so quiet all of a sudden?"
        "Passive":
            jump passive
        "Aggressive":
            jump aggressive
        "Passive-Aggressive":
            jump passive_aggressive

label passive:
    $ clan_rep += 10
    b "Flykit, can you let Mommy talk to Larkpaw alone for a second?"
    f "But --"
    b "Please?"
    f "..."
    hide flykit
    hide brightpoppy side
    show brightpoppy standing
    "Flykit scampers off."
    b "..."
    l "... Well, uh, it was great checking in with you, Brightpoppy."
    l "I'm glad to see that the kits are doing well."
    b "Yes ... They're full of energy."
    l "I bet ..."
    b "..."
    l "..."
    b "Larkpaw ... I'm sorry."
    b "You're clearly a thoughtful young cat."
    l "Thanks --"
    b "-- And I shouldn't judge you based on your family when you're so obviously nothing like them."
    l "..."
    l "... I'll try not to let the cold air in on my way out."
    b "You do that."
    $ final_game_screen = True
    call screen gameUI


label aggressive:
    $ clan_rep -= 10
    $ bright_aggressive = True
    l "Hey, Flykit?"
    f "Yeah?"
    l "What's that on your paws?"
    f "Huh?"
    "{b}FLICK!{/b}"
    b "Flykit!"
    f "WAHHHH!!!"
    b "How dare you?"
    l "How dare {i}you?{/i} Acting like you're my friend to my face, meanwhile you insult my family behind my back!"
    b "Oh, grow up! Everyone in this Clan insults your family. It's practically impossible not to!"
    b "Maybe if you didn't act like such boorish rogues and embarrass yourselves all the time, you could actually earn the respect of your Clanmates."
    l "My family are not {i}boorish rogues.{/i}"
    b "No? Then why did your mother break the Warrior Code?"
    b "Why is your brother embarrassed to be seen with you?"
    b "As for your father -- have you ever even met him?"
    l "You're one to talk about fatherhood, considering what happened to your {i}mate!{/i}"
    b "{i}*Gasp!*{/i}"
    l "Yeah! That's right!"
    l "I bet he's having a great time up in StarClan without having to worry aobut any irritating, flea-brained pests buzzing in his ear!"
    l "And I'm not talking about bees."
    b "If you ever know anything, Larkpaw, know this -- you may be a part of this Clan, but you will never truly belong here."
    l "Is that supposed to make me feel something?"
    l "Because it doesn't!"
    l "I don't feel anything at all!"
    b "Get out."
    l "I was just about to!"
    b "..."
    $ final_game_screen = True
    call screen gameUI

label passive_aggressive:
    b "Flykit, go back to playing."
    f "But --"
    b "Now."
    f "..."
    hide flykit
    hide brightpoppy side
    show brightpoppy standing
    "Flykit scampers off."
    b "..."
    b "... Listen, I'm sorry."
    l "It's okay."
    l "Kits can't help but to be honest."
    l "Unlike some cats in this Clan."
    b "Hehe, uh, yes ... A-And they have such active imaginations!"
    l "I bet."
    b "Um ..."
    b "H-Hey, Larkpaw, now that you mention it, I just remembered that the nursery actually could use some more of --"
    l "Sorry. I was just leaving."
    l "Late for training."
    b "Wait, b-but --"
    b "Don't let the cold air in on your way out!!"
    l "Sorry, what was that? I couldn't hear you!"
    scene nursery_bg with fade
    "{b}WHOOSH!!{/b}"
    $ final_game_screen = True
    call screen gameUI

label nursery_revisit:
    $ final_game_screen = False
    $ quick_menu = True
    scene nursery_bg with fade
    show screen gameUI
    show lark
    if bright_aggressive:
        show brightpoppy side
        show flykit
        f "What was the mean cat saying about Daddy, Brightpoppy?"
        b "... Nothing, Flykit. Nothing at all."
        b "Come nap with your siblings."
        $ final_game_screen = True
        call screen gameUI
    else:
        show brightpoppy laying
        b "..."
        $ final_game_screen = True
        call screen gameUI

