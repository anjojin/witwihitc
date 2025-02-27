label nursery_first:
    $ nursery_visited = True
    scene nursery bg with fade
    show screen gameUI
    t "... Hello?"
    show crowkit with easeinright
    cr "*Gasp* Batkit! Look who's here!"
    show batkit with easeinleft
    ba "Talonclaw!!!"
    cr "Talonclaw, Talonclaw, Talonclaw!!!"
    ba "What are you doing here? Shouldn't you be out on patrol with the rest of the warriors?"
    cr "Didja bring us any presents?"
    ba "Anything to eat???"
    be "Boys, stop pestering him."
    cr "But - But --"
    be "But nothing. Talonclaw probably has a lot to do today. Leave the grownup cats to talk in peace."
    cr "Aww ..."
    hide crowkit with moveoutright
    hide batkit with moveoutleft
    show beetle_kits with easeinbottom
    be "Sorry about that. They never mind their manners."
    t "It's alright. They're good kits."
    be "They're a regular pawful, is what they are, but they keep me young."
    t "How are the newborns doing?"
    be "Ah, yes. Say hello to your Uncle Talonclaw, dears."
    show starlingkit
    show stormkit
    show willowkit
    show wolfkit
    show featherkit
    wo "Mew!"
    st "Mrow!"
    w "Eep!"
    f "..."
    sta "Zzz ..."
    hide starlingkit
    hide stormkit
    hide willowkit
    hide wolfkit
    hide featherkit
    t "Wow ... look at that."
    t "Five little miracles."
    be "Don't you think Stormkit looks so much like her mother?"
    t "Yes. She's beautiful."
    t "They all are."
    be "Their father should be here for this. Where is Sunshadow?"
    t "He's ... out."
    be "Out where?"
    t "... Digging Dapplefeather's grave."
    be "Tch. Do you hear that, little ones?"
    be "Your father is the biggest fool in all of ThunderClan."
    if quest_crocus.started or quest_crocus.completed:
        t "You could cut him some slack, you know. He's going through a hard time."
        be "And what type of time are the rest of us going through?"
    else:
        t "I tried to talk him out of it."
        be "Apparently, not hard enough."
    be "If he wants to freeze to death, he can feel free to do so, but I'm not raising these kits alone."
    be "Crowkit and Batkit already give me enough to worry about."
    t "Don't say things like --"
    show featherkit
    f "*koff* *koff*"
    hide featherkit
    t "!!!"
    be "Oh, StarClan. Not again."
    be "Shh, shhh ... it's alright little one. Settle down."
    t "What's happening? Why is she coughing?"
    be "She caught a little cold just this morning. She and Willowkit haven't been eating well."
    t "What?!"
    be "I was hoping it was just the temporary shock from their mother's passing. But, now ..."
    be "This could be more serious than I thought. Talonclaw, can you visit Locustleaf in the medicine den and get his opinion for me?"
    t "Y-Yes! Of course!"
    $ quest_medical_opinion.started = True
    "{b}Quest Unlocked:{/b} Medical Opinion"
    be "Good. And don't delay."
    be "In kits this young, sickness moves quick."
    if quest_crocus.started:
        show screen n_tansy
        call screen gameUI
    else:
        call screen gameUI

label n1_click_tansy:
    t "It's purple, and a flower ... but not quite a crocus."
    hide screen n_tansy
    call screen gameUI
