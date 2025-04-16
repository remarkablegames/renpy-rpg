label shop:

    $ config.menu_include_disabled = True

    menu:
        "Would you like to buy something from the shop?"

        "Learn “Heal” (-$[wins])" if not player.has_skill("heal") and money >= wins:
            $ money -= wins
            $ player.toggle_skill("heal", True)

            "You learned “Heal”."

            jump shop

        "Leave":
            $ config.menu_include_disabled = False

            jump combat
