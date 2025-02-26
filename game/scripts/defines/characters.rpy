define s = Character("Sunshadow", callback = name_callback, cb_name = 'sun', color="#7c490f", image="sun")
define s_unknown = Character("Sunshadow", color="#7c490f")
image side sun sitting = At("char/sun_sitting.png", sprite_highlight('sun'))
image side sun rising = At("char/sun_rising.png", sprite_highlight('sun'))
image side sun standing = At("char/sun_standing.png", sprite_highlight('sun'))

define t = Character("Talonclaw", color = "#3d3c72", callback = name_callback, cb_name = 'talon')
image talon = At("char/lark pixel.png", sprite_highlight('talon'))

define b = Character("Briarstar", callback=name_callback, cb_name='briar', color="#6b0e5a")
image briarstar = At("char/briarstar.png", sprite_highlight('briar'))
image briarstar_standing = At("char/briarstar_standing.png", sprite_highlight('briar'))

define f = Character("Fawnpaw", callback=name_callback, cb_name='fawn', color="#9f5d16")
image fawnpaw_ad1 = At("char/fawnpaw ad1.png", sprite_highlight('fawn'))

define r = Character("Redpaw", callback=name_callback, cb_name='red', color="#9f1616")
image redpaw_ad1 = At("char/redpaw ad1.png", sprite_highlight('red'))

define c = Character("Cloverpaw", callback=name_callback, cb_name='clover', color="#274f23")
image cloverpaw_ad1 = At("char/cloverpaw ad1.png")

define l = Character("Lilypaw", callback=name_callback, cb_name='lily', color="#4f233c")
image lilypaw_entrace = At("char/lilypaw entrance.png")
image lilypaw_ad1 = At("char/lilypaw ad1.png")