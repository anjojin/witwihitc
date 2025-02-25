default prey_caught = 0
default training_with = ["hunting_red", "hunting_lily", "hunting_fawn", "hunting_clover"]
default hunting_patrols = ["hunting_1", "hunting_2", "hunting_3"]
default patrol_counter = 0

label shuffle_patrols:
    $ renpy.random.shuffle(hunting_patrols)
    return 


label patrol_select:
    $ pause_time = renpy.random.randint(1,5)
    python:
        if patrol_counter <= 2:
            patrol_counter += 1 
            renpy.pause(pause_time, hard = True)
            renpy.jump(hunting_patrols.pop(0)) 
        else: 
            renpy.jump("patrol_over")