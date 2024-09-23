label enemy_turn:

    $ enemy.turn()

    if enemy.health < enemy.health_max and coinflip():
        "Enemy healed [enemy.heal] health."
        $ enemy.apply_heal()

    else:
        "Enemy dealt [enemy.attack] damage to you."
        show placeholder boy with vpunch
        $ player.health -= enemy.attack

    $ player.energy = player.energy_max

    jump player_turn
