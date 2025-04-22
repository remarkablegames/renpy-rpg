label combat:

    scene bg plain with dissolve

    show screen player_stats

    $ player.energy = player.energy_max

    if wins < 3:
        $ enemies.show()
    else:
        $ enemies.show(2)

    jump player_turn
