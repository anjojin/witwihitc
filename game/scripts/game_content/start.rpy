label start:
    call create_my_quests from _call_create_my_quests

    jump sun_speech

    label sun_speech:
        play music "music/ES_A Hard Truth - Wanderer's Trove.mp3" loop
        play audio "ambience/ES_Bieszczady Forest, Winter, Silence - Epidemic Sound.mp3" loop
        s_unknown "They say our ancestors are suffering."
        show start bg with fade
        s sitting "You know, when the Moonpool first ran dry, I could hardly believe it."
        s "I mean, it was unthinkable. Our most sacred space, reduced to a pit of dust and driftwood for the crows to play in."
        s "How could StarClan, in its endless power and wisdom, possibly allow anything like it to happen?"
        s "How could they not have warned us?"
        s "..."
        s rising "... It's been nearly four moons, since then." 
        s "I haven't been back to the Moonpool, but it's probably covered in ice and snow, now."
        s "Just like the rest of the forest is."
        s "In the time that has passed since then, ThunderClan has undergone a tremendous transformation."
        s "We have all borne witness things that go beyond description."
        s "Kits, shriveled to husks like leaves on the vine."
        s "Loved ones lost to sickness, their bodies ravaged by flies."
        s "The bitter cold. The stench of death."
        s sitting "And, of course, the unending hunger."
        s "Nearly a whole leaf-bare has passed without so much as a shrew's tail for ThunderClan to eat."
        s "Our bodies have failed us. Our leadership has failed us."
        s "Logic. Reason. The warrior code."
        s "... And now, just when I thought the worst was over, my mate has abandoned us, too."
        show dapplefeather bg with fade
        s_unknown "My Spottedlight. Only seventy-two moons old."
        s_unknown "Just yesterday, she delivered our first litter."
        s_unknown "Willowkit, Wolfkit, Stormkit, Starlingkit, and Featherkit."
        s_unknown "They haven't even opened their eyes yet and, already, their mother is gone."
        s_unknown "Our kits will grow up with no memory of her face."
        hide dapplefeather bg
        s sitting "..."
        s "Of course, it was only a matter of time."
        s "Spottedlight's body was sick and weakened by the hunger, as so many of ours are now."
        s "I was in the nursery with her, as she died. Smoothing her fur down as she spasmed in her nest."
        s "When she finally went, I didn't look away."
        s "Didn't scream."
        s "No, instead, all I could do was wonder ..."
        s rising "... {i}Does this mean Spottedlight is in StarClan, now?{/i}"
        s "Has her suffering ended? Has she reached any kind of peace, or salvation?"
        s standing "... Or, are our warrior ancestors all starving up there, too?"
        scene sunset clouds with fade
        s_unknown "To my Spottedlight, if you can hear me, I have only this to say:"
        s_unknown "I hope you're in pain."
        s_unknown "I hope you can still feel the agony of your children, of the Clanmates you've left behind."
        s_unknown "I hope you feel it so strongly, it suffocates you."
        s_unknown "I hope the hunger never goes away."
        s_unknown "Because, if it does ..."
        s_unknown "If it's true that, after all these moons, StarClan is still lush and warm and overflowing with prey ..."
        s_unknown "Then it means that, all this time, they could've been helping us."
        s_unknown "They just chose not to."
        s_unknown "And, if that's true, then I won't stop until every last speck of light is clawed from the sky, myself."
        s_unknown "I'll always remember this feeling."
        s_unknown "The hunger and the cold. Even as the weather warms, it will never go away."
        s_unknown "StarClan, what a waste."
        s_unknown "What a collosal waste ..."
        s_unknown "..."
        stop music fadeout 0.5
        play sound "sfx/rustle.mp3"
        play audio "sfx/impact.mp3"
        scene black with fade
        jump bs_1