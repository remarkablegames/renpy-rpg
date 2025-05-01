label shop:

    python:
        config.menu_include_disabled = True
        reward_cost = max(wins, 3)

        has_heal = "{s}" if player.has_skill("heal") else ""
        has_overheal = "{s}" if "overheal" in player.skills["heal"].tags else ""
        has_heavy_attack = "{s}" if "stun" in player.skills["attack"].tags else ""
        has_life_force = "{s}" if player.has_skill("life_force") else ""
        has_rage = "{s}" if player.has_skill("rage") else ""

    menu:
        "What do you want to buy?"

        "[has_heal]Learn “Heal” (-$1)
        {tooltip}Heal yourself for 2 energy" if not has_heal and money >= 1:
            $ money -= 1
            $ player.toggle_skill("heal", True)

            "You learned “Heal”."

            jump shop

        "[has_overheal]Upgrade “Heal” to “Overheal” (-$5)
        {tooltip}Heal beyond max health" if has_heal and not has_overheal and money >= 5:
            $ money -= 5
            $ player.skills["heal"].tags.append("overheal")
            $ player.skills["heal"].label_active = player.skills["heal"].label_active.replace("Heal", "Overheal")
            $ player.skills["heal"].label_disabled = player.skills["heal"].label_disabled.replace("Heal", "Overheal")

            "You upgraded “Heal” to “Overheal”."

            jump shop

        "[has_heavy_attack]Upgrade “Attack” to  “Heavy Attack” (-$5)
        {tooltip}Attack with a 20%% chance to stun the enemy" if not has_heavy_attack and money >= 5:
            $ money -= 5
            $ player.skills["attack"].tags.append("stun")
            $ player.skills["attack"].label_active = player.skills["attack"].label_active.replace("Attack", "Heavy Attack")
            $ player.skills["attack"].label_disabled = player.skills["attack"].label_disabled.replace("Attack", "Heavy Attack")

            "You upgraded “Attack” to “Heavy Attack”."

            jump shop

        "[has_life_force]Learn “Life Force” (-$3)
        {tooltip}Convert health to energy" if not player.has_skill("life_force") and money >= 3:
            $ money -= 3
            $ player.toggle_skill("life_force", True)

            "You learned “Life Force”."

            jump shop

        "[has_rage]Learn “Rage” (-$7)
        {tooltip}Double your attack for 1 energy" if not player.has_skill("rage") and money >= 7:
            $ money -= 7
            $ player.toggle_skill("rage", True)
            $ player.attack_min = player.attack_max

            "You learned “Rage”."

            jump shop

        "Get a reward (-$[reward_cost])
        {tooltip}Upgrade a stat or skill" if money >= reward_cost:
            $ money -= reward_cost
            $ rewards += 1
            $ config.menu_include_disabled = False

            jump reward

        "Battle":
            $ config.menu_include_disabled = False

            jump combat
