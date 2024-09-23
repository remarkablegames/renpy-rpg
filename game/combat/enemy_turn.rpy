label enemy_turn:

    $ enemy_attack = renpy.random.randint(1 + victories, 5 + victories)
    $ enemy_heal = renpy.random.randint(1 + victories, 5 + victories)

    if enemy.health < enemy.health_max and coinflip():
        "Enemy healed [enemy_heal] health."
        $ enemy.health = enemy.health_max if enemy.health + enemy_heal >= enemy.health_max else enemy.health + enemy_heal

    else:
        "Enemy dealt [enemy_attack] damage to you."
        show placeholder boy with vpunch
        $ player.health -= enemy_attack

    $ player.energy = player.energy_max

    jump player_turn
