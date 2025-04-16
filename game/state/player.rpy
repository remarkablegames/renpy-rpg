init python:
    from typing import Callable

    class Skill:
        def __init__(self, **kwargs) -> None:
            self.name = kwargs.get("name")
            self.color = kwargs.get("color")
            self.value = kwargs.get("value")
            self.energy = kwargs.get("energy")
            self.callback = kwargs.get("callback")


    class Player(RPGCharacter):
        def __init__(self, **kwargs) -> None:
            super().__init__(
                health=15,
                energy=2,
                attack_min=1,
                attack_max=3,
                heal_min=2,
                heal_max=5,
            )

            self.skills = {
                "attack": Skill(
                    name="Attack",
                    color="[colors.attack]",
                    value="[player.attack]",
                    energy=1,
                    callback=self.action_attack,
                ),

                "heal": Skill(
                    name="Heal",
                    color="[colors.heal]",
                    value="[player.heal]",
                    energy=2,
                    callback=self.action_heal,
                ),
            }

        def display_menu(self) -> None:
            """
            Combat display menu.
            """
            narrator("Choose your action.", interact=False)
            action = renpy.display_menu(self.get_menu_choices())
            action()

        def get_menu_choices(self) -> list:
            """
            Get display menu choices.
            """
            self.turn_rng()
            choices = []

            for choice in self.skills.values():
                energy_cost = choice.energy
                if player.energy < energy_cost:
                    label = f"{{color=[gui.insensitive_color]}}{choice.name} {choice.value}, Energy {energy_cost}"
                else:
                    label = f"{choice.name} {{color={choice.color}}}{choice.value}{{/color}}, Energy [emojis.get({energy_cost})]"
                choices.append((label, choice.callback))

            return choices + [("End Turn", self.end_turn)]

        def action_attack(self) -> None:
            """
            Attack action.
            """
            energy_cost = self.skills["attack"].energy
            if player.energy < energy_cost:
                narrator("You don't have enough energy.")
            else:
                player.energy -= energy_cost
                enemy.health -= player.attack
                renpy.show("placeholder boy", at_list=[shake])
                narrator("You dealt [player.attack] damage to the enemy.")

            renpy.jump("player_turn")

        def action_heal(self) -> None:
            """
            Heal action.
            """
            energy_cost = self.skills["heal"].energy
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

default player = Player()
