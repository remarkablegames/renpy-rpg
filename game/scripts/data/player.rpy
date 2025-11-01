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

                "life_force": Skill(
                    callback=self.action_life_force,
                    label_active="Energy {color=[colors.energy]}+1{/color}, Health {color=[colors.heal]}-[player.health_max // 4]",
                    label_disabled="{color=[gui.insensitive_color]}Energy +1, Health -[player.health_max // 4]",
                ),

                "rage": Skill(
                    callback=self.action_rage,
                    energy=1,
                    label_active="Attack {color=[colors.attack]}x2{/color}, Energy [emojis.get(player.skills['rage'].energy)]",
                    label_disabled="{color=[gui.insensitive_color]}Attack x2, Energy [player.skills['rage'].energy]",
                ),
            }

        def has_skill(self, skill: str) -> bool:
            return self.skills.get(skill).enabled

        def toggle_skill(self, skill: str, is_enabled: bool) -> None:
            self.skills.get(skill).enabled = is_enabled

        def display_menu(self) -> None:
            """
            Display menu for player.
            """
            narrator("Choose your action.", interact=False)
            action = renpy.display_menu(self.get_menu_choices())
            action()

        def get_menu_choices(self) -> list:
            """
            Get display menu choices for player.
            """
            choices = []

            for skill in self.skills.values():
                if skill.enabled:
                    if skill.callback == self.action_life_force:
                        skill_label = skill.label_active if self.health > self.health_max // 4 else skill.label_disabled
                    elif self.energy >= skill.energy:
                        skill_label = skill.label_active
                    else:
                        skill_label = skill.label_disabled

                    choices.append((skill_label, skill.callback))

            return choices + [("End Turn", self.end_turn)]

        def action_attack(self) -> None:
            """
            Player attack enemy.
            """
            attack_skill = self.skills["attack"]
            energy_cost = attack_skill.energy

            if self.energy < energy_cost:
                narrator("You don’t have enough energy.")
                renpy.jump("player_turn")
            else:
                renpy.jump("player_attack")

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

        def action_life_force(self) -> None:
            """
            Player convert health to energy.
            """
            health_cost = self.health_max // 4

            if self.health <= health_cost:
                narrator("You don’t have enough health.")
            else:
                self.health -= health_cost
                self.energy += 1

            renpy.jump("player_turn")

        def action_rage(self) -> None:
            """
            Player increase attack multiplier.
            """
            energy_cost = self.skills["attack"].energy

            if self.energy < energy_cost:
                narrator("You don’t have enough energy.")
            else:
                self.energy -= energy_cost
                self.attack_multiplier *= 2

            renpy.jump("player_turn")

        def end_turn(self) -> None:
            """
            Player end turn.
            """
            self.attack_multiplier = 1

            renpy.jump("enemy_turn")

default player = Player(
    health=15,
    energy=2,
    attack_min=1,
    attack_max=3,
    heal_min=2,
    heal_max=5,
)
