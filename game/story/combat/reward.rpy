label reward:

    if not rewards:
        jump shop

    $ reward_attack = renpy.random.randint(1, 2 + wins)
    $ reward_heal = renpy.random.randint(1, 3 + wins)

    menu:
        "Choose your reward (remaining: [rewards])."

        "Reroll rewards (-$[wins * 2])" if money >= wins * 2:
            $ money -= wins * 2

            jump reward

        "Increase attack by {color=[colors.attack]}+[reward_attack]":
            $ player.attack_min += reward_attack
            $ player.attack_max += reward_attack

        "Increase heal by {color=[colors.heal]}+[reward_heal]" if player.has_skill("heal"):
            $ player.heal_min += reward_heal
            $ player.heal_max += reward_heal

        "Increase max health by {color=[colors.heal]}+[reward_heal * 2]" if renpy.random.random() < 0.5:
            $ player.health += reward_heal * 2
            $ player.health_max += reward_heal * 2

        "Increase max energy by {color=[colors.energy]}+1" if not wins % 3 and renpy.random.random() < 0.5:
            $ player.energy_max += 1

        "Recover all health" if player.health < player.health_max:
            $ player.health = player.health_max

    $ rewards -= 1

    jump reward
