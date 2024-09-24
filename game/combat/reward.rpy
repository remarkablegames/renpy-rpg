label reward:

    if not rewards:
        jump combat

    $ reward_attack = renpy.random.randint(1, 2 + wins)
    $ reward_heal = renpy.random.randint(1, 3 + wins)

    menu:
        "Choose a reward (remaining: [rewards])."

        "Increase base attack by {color=#ee4b2b}+[reward_attack]":
            $ player.attack_min += reward_attack
            $ player.attack_max += reward_attack

        "Increase base heal by {color=#af0}+[reward_heal]":
            $ player.heal_min += reward_heal
            $ player.heal_max += reward_heal

        "Recover all health":
            $ player.health = player.health_max

        "Increase max health by {color=#af0}+[reward_heal]" if renpy.random.random() < 0.6:
            $ player.health += reward_heal
            $ player.health_max += reward_heal

        "Increase max energy by {color=#add8e6}+1" if wins > 5 and renpy.random.random() < 1 / wins:
            $ player.energy_max += 1

    $ rewards -= 1

    jump reward
