init python:
    from typing import Callable

    class Choice:
        def __init__(self, name: str, color: str, value: str, energy: int, callback) -> None:
            self.name = name
            self.color = color
            self.value = value
            self.energy = energy
            self.callback = callback

    class Actions:
        def __init__(self) -> None:
            self.choices = {
                "attack": Choice("Attack", "#ee4b2b", "[player.attack]", 1, self.attack),
                "heal": Choice("Heal", "#af0", "[player.heal]", 2, self.heal),
            }

        def display_menu(self) -> None:
            """
            Display actions menu.
            """
            narrator("Choose your action.", interact=False)
            action = renpy.display_menu(self.__choices())
            action()

        def __choices(self) -> list:
            """
            Get display menu choices.
            """
            player.turn_rng()
            choices = []

            for choice in self.choices.values():
                energy_cost = choice.energy
                if player.energy < energy_cost:
                    label = f"{{color=[gui.insensitive_color]}}{choice.name} {choice.value}, Energy {energy_cost}"
                else:
                    label = f"{choice.name} {{color={choice.color}}}{choice.value}{{/color}}, Energy [emoji.get({energy_cost})]"
                choices.append((label, choice.callback))

            return choices + [("End Turn", self.end_turn)]

        def attack(self) -> None:
            """
            Attack action.
            """
            energy_cost = self.choices["attack"].energy
            if player.energy < energy_cost:
                narrator("You don't have enough energy.")
            else:
                player.energy -= energy_cost
                enemy.health -= player.attack
                renpy.show("placeholder boy", at_list=[shake])
                narrator("You dealt [player.attack] damage to the enemy.")

            renpy.jump("player_turn")

        def heal(self) -> None:
            """
            Heal action.
            """
            energy_cost = self.choices["heal"].energy
            if player.energy < energy_cost:
                narrator("You don't have enough energy.")
            else:
                player.energy -= energy_cost
                player.apply_heal()
                narrator("You healed [player.heal] health.")

            renpy.jump("player_turn")

        def end_turn(self) -> None:
            """
            End turn.
            """
            renpy.jump("enemy_turn")

default actions = Actions()
