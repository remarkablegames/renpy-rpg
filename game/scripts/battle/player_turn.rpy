label player_turn:

    $ player.turn_rng()

    jump player_turn_menu

label player_turn_menu:

    if enemies.dead():
        jump win

    elif player.health <= 0:
        jump lose

    $ player.display_menu()
