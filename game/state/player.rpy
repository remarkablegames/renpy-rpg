init python:
    class Skill:
        def __init__(self, **kwargs) -> None:
            self.name = kwargs.get("name")
            self.color = kwargs.get("color")
            self.value = kwargs.get("value")
            self.energy = kwargs.get("energy")
            self.callback = kwargs.get("callback")
            self.enabled = kwargs.get("enabled", False)

    class Player(RPGCharacter):
        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)

            self.skills = {
                "attack": Skill(
                    name="Attack",
                    color="[colors.attack]",
                    value="[player.attack]",
                    energy=1,
                    callback=self.action_attack,
                    enabled=True,
                ),

                "heal": Skill(
                    name="Heal",
                    color="[colors.heal]",
                    value="[player.heal]",
                    energy=2,
                    callback=self.action_heal,
                ),
            }

        def has_skill(self, skill: str) -> bool:
            return self.skills.get(skill).enabled

        def toggle_skill(self, skill: str, is_enabled: bool) -> None:
            self.skills.get(skill).enabled = is_enabled

        def display_menu(self) -> None:
            """
            Display menu.
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

            for skill in self.skills.values():
                if not skill.enabled:
                    continue

                energy_cost = skill.energy

                if self.energy < energy_cost:
                    label = f"{{color=[gui.insensitive_color]}}{skill.name} {skill.value}, Energy {energy_cost}"
                else:
                    label = f"{skill.name} {{color={skill.color}}}{skill.value}{{/color}}, Energy [emojis.get({energy_cost})]"

                choices.append((label, skill.callback))

            return choices + [("End Turn", self.end_turn)]

        def action_attack(self) -> None:
            """
            Attack action.
            """
            energy_cost = self.skills["attack"].energy
            if self.energy < energy_cost:
                narrator("You don't have enough energy.")
            else:
                self.energy -= energy_cost
                enemy.health -= self.attack
                renpy.show("placeholder boy", at_list=[shake])
                narrator("You dealt [player.attack] damage to the enemy.")

            renpy.jump("player_turn")

        def action_heal(self) -> None:
            """
            Heal action.
            """
            energy_cost = self.skills["heal"].energy
            if self.energy < energy_cost:
                narrator("You don't have enough energy.")
            else:
                self.energy -= energy_cost
                self.apply_heal()
                narrator("You healed [player.heal] health.")

            renpy.jump("player_turn")

        def end_turn(self) -> None:
            """
            End turn.
            """
            renpy.jump("enemy_turn")

default player = Player(
    health=15,
    energy=2,
    attack_min=1,
    attack_max=3,
    heal_min=2,
    heal_max=5,
)
