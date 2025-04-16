label combat_start:

    scene bg plain with dissolve

    show placeholder boy with dissolve

    show screen player_stats
    show screen enemy_stats

    $ player.energy = player.energy_max
    $ enemy.health = enemy.health_max = round(5 * (wins + 1) * (1 + renpy.random.random()))

    $ enemy.attack_min = round(wins * (1 + renpy.random.random())) + 1
    $ enemy.attack_max = enemy.attack_min + wins + 1

    $ enemy.heal_min = round(wins * (1 + renpy.random.random())) + 1
    $ enemy.heal_max = enemy.heal_min + wins + 1

    jump player_turn
