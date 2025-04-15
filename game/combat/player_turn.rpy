label player_turn:

    $ config.menu_include_disabled = False

    if player.health <= 0:
        jump lose

    if enemy.health <= 0:
        jump win

    $ player.turn()
    $ config.menu_include_disabled = True

    menu:
        "Choose your action."

        "Attack {color=#ee4b2b}[player.attack]{/color},
        Energy {color=#add8e6}[emoji.one]{/color}" if player.energy >= 1:
            $ player.energy -= 1
            $ enemy.health -= player.attack

            show placeholder boy at shake, center

            "You dealt [player.attack] damage to the enemy."

            jump player_turn

        "Heal {color=#af0}[player.heal]{/color},
        Energy {color=#add8e6}[emoji.two]{/color}" if player.energy >= 2:
            $ player.energy -= 2
            $ player.apply_heal()

            "You healed [player.heal] health."

            jump player_turn

        "End Turn":
            jump enemy_turn
