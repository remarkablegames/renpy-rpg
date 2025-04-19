init python:
    from math import floor

label shop:

    menu:
        "Would you like to buy something from the shop?"

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
