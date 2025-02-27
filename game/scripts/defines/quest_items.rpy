# The Quests are listed here.
default quest_nesting_material = Quest(name="Nesting Material", description="Fetch some moss from Dapplefeather's old nest.", cancelled = False, started = False)
default quest_favorite_prey = Quest(name="Favorite Prey", description="Go on a hunting patrol and catch a piece of prey.", cancelled = False, started = False)
default quest_crocus = Quest(name="Crocuses", description="Find a small, purple flower somewhere in camp.", cancelled = False, started = False)
default quest_feed_deputy = Quest(name="Feed the Deputy", description="Catch a piece of prey and deliver it to Pouncetail in the medicine den.")
default quest_medical_opinion = Quest(name="Medical Opinion", description="Visit the medicine den and ask Locustleaf about Featherkit.")

## my_quests contains all quests. This is used for quests_screen.
default my_quests = []
label create_my_quests:
    $ my_quests.append(quest_nesting_material)
    $ my_quests.append(quest_favorite_prey)
    $ my_quests.append(quest_crocus)
    $ my_quests.append(quest_feed_deputy)
    $ my_quests.append(quest_medical_opinion)