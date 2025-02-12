# The Quests are listed here.
default quest_shimmerpaw_training = Quest(name="Train with Shimmerpaw", description="Meet Shimmerpaw on a training patrol", cancelled = False, started = False)
default quest_willowleap_message = Quest(name="A Family Matter", description="Go on a border patrol and deliver Willowleap's message.", cancelled = False, started = False)
default quest_sootpaw_training = Quest(name="Train with Sootpaw", description="Meet Sootpaw on a training patrol", cancelled = False, started = False)
default quest_find_frondfoot = Quest(name="Find Frondfoot", description = "Find Frondfoot and tell him about your dream.", cancelled = False, started = False)
default quest_sootpaw_reporting = Quest(name="Follow Up with Sootpaw", description = "After going on patrol, find Sootpaw and talk to him.")

## my_quests contains all quests. This is used for quests_screen.
default my_quests = []
label create_my_quests:
    $ my_quests.append(quest_shimmerpaw_training)
    $ my_quests.append(quest_willowleap_message)
    $ my_quests.append(quest_sootpaw_training)
    $ my_quests.append(quest_find_frondfoot)
    $ my_quests.append(quest_sootpaw_reporting)
