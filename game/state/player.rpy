init python:
    class Skill:
        def __init__(self, **kwargs) -> None:
            self.label_active = kwargs.get("label_active", "")
            self.label_disabled = kwargs.get("label_disabled", "")
            self.energy = kwargs.get("energy", 0)
            self.callback = kwargs.get("callback")
            self.enabled = kwargs.get("enabled", False)
            self.tags = kwargs.get("tags", [])

    class Player(RPGCharacter):
        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)

            self.skills = {
                "attack": Skill(
                    callback=self.action_attack,
                    enabled=True,
                    energy=1,
                    label_active="Attack {color=[colors.attack]}[player.attack]{/color}, Energy [emojis.get(player.skills['attack'].energy)]",
                    label_disabled="{color=[gui.insensitive_color]}Attack [player.attack], Energy [player.skills['attack'].energy]",
                ),

                "heal": Skill(
                    callback=self.action_heal,
                    energy=2,
                    label_active="Heal {color=[colors.heal]}[player.heal]{/color}, Energy [emojis.get(player.skills['heal'].energy)]",
                    label_disabled="{color=[gui.insensitive_color]}Heal [player.heal], Energy [player.skills['heal'].energy]",
                ),

                "energize": Skill(
                    callback=self.action_energize,
                    label_active="Energy {color=[colors.energy]}+1{/color}, Health {color=[colors.heal]}-[player.health_max // 4]",
                ),

                "rage": Skill(
                    callback=self.action_enrage,
                    energy=1,
                    label_active="Attack {color=[colors.attack]}+100%{/color}, Energy [emojis.get(player.skills['rage'].energy)]",
                    label_disabled="{color=[gui.insensitive_color]}Attack +100%, Energy [player.skills['rage'].energy]",
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
                if skill.enabled:
                    skill_label = skill.label_disabled if self.energy < skill.energy else skill.label_active
                    choices.append((skill_label, skill.callback))

            return choices + [("End Turn", self.end_turn)]

        def action_attack(self) -> None:
            """
            Attack enemy.
            """
            energy_cost = self.skills["attack"].energy

            if self.energy < energy_cost:
                narrator("You don’t have enough energy.")
            else:
                self.energy -= energy_cost
                enemy.health -= self.attack
                renpy.show("placeholder boy", at_list=[shake])
                narrator("You dealt [player.attack] damage to the enemy.")

            renpy.jump("player_turn")

        def action_heal(self) -> None:
            """
            Heal player.
            """
            heal_skill = self.skills["heal"]
            energy_cost = heal_skill.energy

            if self.energy < energy_cost:
                narrator("You don’t have enough energy.")
            else:
                self.energy -= energy_cost
                self.perform_heal(overheal="overheal" in heal_skill.tags)
                narrator("You healed [player.heal] health.")

            renpy.jump("player_turn")

        def action_energize(self) -> None:
            """
            Decrease health and increase energy.
            """
            health_cost = self.health_max // 4
            self.health -= health_cost
            self.energy += 1
            narrator(f"You gained 1 energy and lost {health_cost} health.")

            renpy.jump("player_turn")

        def action_enrage(self) -> None:
            """
            Increase attack multiplier.
            """
            energy_cost = self.skills["attack"].energy

            if self.energy < energy_cost:
                narrator("You don’t have enough energy.")
            else:
                self.energy -= energy_cost
                self.attack_multiplier += 1.0

            renpy.jump("player_turn")

        def end_turn(self) -> None:
            """
            End turn.
            """
            self.attack_multiplier = 1.0

            renpy.jump("enemy_turn")

default player = Player(
    health=15,
    energy=2,
    attack_min=1,
    attack_max=3,
    heal_min=2,
    heal_max=5,
)
