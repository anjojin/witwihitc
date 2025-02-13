define s = Character("Sunshadow", callback = name_callback, cb_name = 'sun', color="#7c490f", image="sun")
define s_unknown = Character("Sunshadow", color="#7c490f")
image side sun sitting = At("char/sun_sitting.png", sprite_highlight('sun'))
image side sun rising = At("char/sun_rising.png", sprite_highlight('sun'))
image side sun standing = At("char/sun_standing.png", sprite_highlight('sun'))

define t = Character("Talonclaw", color = "#3d3c72", callback = name_callback, cb_name = 'talon')
image talon = At("char/lark pixel.png", sprite_highlight('talon'))

define w = Character("Willowleap", callback=name_callback, cb_name='willow', color="#6b0e5a")
image willowleap = At("char/willowleap.png", sprite_highlight('willow'))

define b = Character("Brightpoppy", callback=name_callback, cb_name='brightpoppy', image="brightpoppy", color="#9f4b16")
image brightpoppy laying = At("char/brightpoppy/brightpoppy laying.png", sprite_highlight('brightpoppy'))
image brightpoppy standing = At("char/brightpoppy/brightpoppy standing.png", sprite_highlight('brightpoppy'))
image brightpoppy side = At("char/brightpoppy/brightpoppy side.png", sprite_highlight('brightpoppy'))

define f = Character("Flykit", callback=name_callback, cb_name = 'flykit', color = "#627610")
image flykit = At("char/flykit.png", sprite_highlight('flykit'))
