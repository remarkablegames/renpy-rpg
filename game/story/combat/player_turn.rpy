label player_turn:

    if enemies.dead():
        jump win

    if player.health <= 0:
        jump lose

    $ player.display_menu()
