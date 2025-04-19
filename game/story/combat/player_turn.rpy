label player_turn:

    if enemy.health <= 0:
        jump win

    if player.health <= 0:
        jump lose

    $ player.display_menu()
