init python:
    from math import floor

label shop:

    $ config.menu_include_disabled = True

    menu:
        "Would you like to buy something from the shop?"

        "Learn “Heal” (-$1)" if not player.has_skill("heal") and money >= 1:
            $ money -= 1
            $ player.toggle_skill("heal", True)

            "You learned “Heal”."

            jump shop

        "Learn “Energize” (-$3)" if not player.has_skill("energize") and money >= 3:
            $ money -= 3
            $ player.toggle_skill("energize", True)

            "You learned “Energize”."

            jump shop

        "Learn “Enrage” (-$5)" if not player.has_skill("enrage") and money >= 5:
            $ money -= 5
            $ player.toggle_skill("enrage", True)
            $ player.attack_max = player.attack_min

            "You learned “Enrage”."

            jump shop

        "Get a reward (-$[floor(wins * 1.5)])" if money >= floor(wins * 1.5):
            $ money -= floor(wins * 1.5)
            $ rewards += 1
            $ config.menu_include_disabled = False

            jump reward

        "Leave":
            $ config.menu_include_disabled = False

            jump combat
