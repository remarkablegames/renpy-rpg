label end_turn:

    $ enemy_attack = renpy.random.randint(1 + victories, 5 + victories)
    $ enemy_heal = renpy.random.randint(1 + victories, 5 + victories)
    $ coinflip = renpy.random.choice([True, False])

    if coinflip:
        "Enemy dealt [enemy_attack] damage."
        show placeholder boy with vpunch
        $ player.health -= enemy_attack
    else:
        "Enemy healed [enemy_heal] HP."
        $ enemy.health += enemy_heal

    $ player.energy = player.energy_max

    jump action
