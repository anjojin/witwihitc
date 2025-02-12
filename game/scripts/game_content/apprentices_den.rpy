label app_den_empty:
    $ final_game_screen = False
    $ quick_menu = True
    scene apprentices_den with fade
    show screen gameUI
    l "It feels so empty in here, with Shimmerpaw and Sootpaw gone ..."
    $ final_game_screen = True
    call screen gameUI