label player_turn:

    if enemy.health <= 0:
        $ victories += 1
        hide placeholder boy with dissolve
        "You defeated the enemy!"
        jump combat

    $ player_attack = renpy.random.randint(1, 5)
    $ player_heal = renpy.random.randint(1, 5)

    menu:
        "Choose your action."

        "{color=#EE4B2B}Attack [player_attack]\n{color=#add8e6}Energy -1" if player.energy >= 1:
            $ enemy.health -= player_attack
            $ player.energy -= 1

            show placeholder boy at shake, center

            "You dealt [player_attack] damage to the enemy."

            jump player_turn

        "{color=#af0}Heal [player_heal]\n{color=#add8e6}Energy -2" if player.energy >= 2:
            $ player.health += player_heal
            $ player.energy -= 2

            "You healed [player_heal] health."

            jump player_turn

        "End Turn":
            jump enemy_turn
