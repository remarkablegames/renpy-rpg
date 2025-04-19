init python:
    from math import floor

label shop:

    menu:
        "What would you like to do?"

        "Upgrade “Attack” to  “Heavy Attack” (-$5)" if player.has_skill("attack") and "stun" not in player.skills["attack"].tags and money >= 5:
            $ money -= 5
            $ player.skills["attack"].tags.append("stun")
            $ player.skills["attack"].label_active = player.skills["attack"].label_active.replace("Attack", "Heavy Attack")
            $ player.skills["attack"].label_disabled = player.skills["attack"].label_disabled.replace("Attack", "Heavy Attack")

            "You upgraded “Attack” to “Heavy Attack”."

            jump shop

        "Learn “Heal” (-$1)" if not player.has_skill("heal") and money >= 1:
            $ money -= 1
            $ player.toggle_skill("heal", True)

            "You learned “Heal”."

            jump shop

        "Upgrade “Heal” to “Overheal” (-$5)" if player.has_skill("heal") and "overheal" not in player.skills["heal"].tags and money >= 5:
            $ money -= 5
            $ player.skills["heal"].tags.append("overheal")
            $ player.skills["heal"].label_active = player.skills["heal"].label_active.replace("Heal", "Overheal")
            $ player.skills["heal"].label_disabled = player.skills["heal"].label_disabled.replace("Heal", "Overheal")

            "You upgraded “Heal” to “Overheal”."

            jump shop

        "Learn “Energize” (-$3)" if not player.has_skill("energize") and money >= 3:
            $ money -= 3
            $ player.toggle_skill("energize", True)

            "You learned “Energize”."

            jump shop

        "Learn “Rage” (-$5)" if not player.has_skill("rage") and money >= 5:
            $ money -= 5
            $ player.toggle_skill("rage", True)
            $ player.attack_min = player.attack_max

            "You learned “Rage”."

            jump shop

        "Get a reward (-$[floor(wins * 1.5)])" if money >= floor(wins * 1.5):
            $ money -= floor(wins * 1.5)
            $ rewards += 1

            jump reward

        "Battle":
            jump combat
