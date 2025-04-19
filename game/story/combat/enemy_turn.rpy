label enemy_turn:

    if enemy.stunned:
        "The enemy is stunned!"

        jump enemy_turn_end

    $ enemy.turn_rng()

    if enemy.health < enemy.health_max and renpy.random.random() < 0.5:
        "Enemy healed [enemy.heal] health."
        $ enemy.perform_heal()
    else:
        "Enemy dealt [enemy.attack] damage to you."
        show placeholder boy with vpunch
        $ player.health -= enemy.attack

    jump enemy_turn_end

label enemy_turn_end:

    $ enemy.stunned = False
    $ player.energy = player.energy_max

    jump player_turn
