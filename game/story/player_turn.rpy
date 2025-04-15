label player_turn:

    if player.health <= 0:
        jump lose

    if enemy.health <= 0:
        jump win

    $ actions.display_menu()
