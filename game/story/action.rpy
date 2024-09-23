label action:

    if enemy.health <= 0:
        $ victories += 1
        "You defeated the enemy!"
        jump combat

    $ player_attack = renpy.random.randint(1, 5)
    $ player_heal = renpy.random.randint(1, 5)

    menu:
        "What do you want to do?"

        "Attack [player_attack], Energy -1" if player.energy >= 1:
            $ enemy.health -= player_attack
            $ player.energy -= 1

            show placeholder boy at shake, center

            "You dealt [player_attack] to the enemy."

            jump action

        "Heal [player_heal], Energy -2" if player.energy >= 2:
            $ player.health += player_heal
            $ player.energy -= 2

            "You healed [player_heal] HP."

            jump action

        "End Turn":
            jump end_turn
