default prey_caught = 0
default training_with = []
default hunting_patrols = ["hunting_1", "hunting_2", "hunting_3", "hunting_4", "hunting_5", "hunting_6", "hunting_7", "hunting_8", "hunting_9", "hunting_10", "hunting_11", "hunting_12", "hunting_13", "hunting_14", "hunting_15", "hunting_16"]
default patrol_counter = 0
default red_hunting_chance = 15
default clover_hunting_chance = 15
default fawn_hunting_chance = 14
default lily_hunting_chance = 13
default talon_clan_bonus = 0
default talon_sun_bonus = 0
default talon_chance = 0
default patrol_max = 0
default prey_potential = 0

label shuffle_patrols:
    $ patrol_max = renpy.random.randint(6,10)
    if quest_babysitting.started:
        $ patrol_max += 4
    return 


label patrol_select:
    python:
        if patrol_counter <= patrol_max:
            renpy.random.shuffle(hunting_patrols)
            pause_time = renpy.random.randint(1,2)
            patrol_counter += 1 
            renpy.pause(pause_time, hard = True)
            renpy.jump(hunting_patrols.pop(0)) 
        else:
            renpy.jump("patrol_hard_over")