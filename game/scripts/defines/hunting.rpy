default prey_caught = 0
default training_with = []
default hunting_patrols = ["hunting_1", "hunting_2", "hunting_3"]
default patrol_counter = 0
default red_hunting_chance = 13
default clover_hunting_chance = 13
default fawn_hunting_chance = 12
default lily_hunting_chance = 11
default talon_clan_bonus = 0
default talon_sun_bonus = 0
default talon_chance = 0

label shuffle_patrols:
    $ renpy.random.shuffle(hunting_patrols)
    return 


label patrol_select:
    $ pause_time = renpy.random.randint(1,5)
    $ patrol_max = renpy.random.randint(1,5)
    if quest_babysitting.started:
        $ patrol_max += 4
    python:
        if patrol_counter <= patrol_max:
            patrol_counter += 1 
            renpy.pause(pause_time, hard = True)
            renpy.jump(hunting_patrols.pop(0)) 
        else: 
            renpy.jump("patrol_over")