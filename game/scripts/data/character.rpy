init python:
    class RPGCharacter():
        def __init__(self, **kwargs) -> None:
            self.name = kwargs.get("name", "")
            self.image = kwargs.get("image", self.name.replace(" ", "_").lower())

            self.health = self.health_max = kwargs.get("health", 0)
            self.energy = self.energy_max = kwargs.get("energy", 0)

            self.attack = 0
            self.attack_min = kwargs.get("attack_min", 0)
            self.attack_max = kwargs.get("attack_max", 0)
            self.attack_multiplier = kwargs.get("attack_multiplier", 1)

            self.heal = 0
            self.heal_min = kwargs.get("heal_min", 0)
            self.heal_max = kwargs.get("heal_max", 0)

            self.stunned = False

        def turn_rng(self) -> None:
            """
            Generate random numbers for turn.
            """
            self.attack = round(renpy.random.randint(self.attack_min, self.attack_max) * self.attack_multiplier)
            self.heal = renpy.random.randint(self.heal_min, self.heal_max)

        def perform_attack(self, target) -> None:
            """
            Attack character.
            """
            renpy.sound.play("sound/punch.ogg", relative_volume=0.5)
            target.health -= self.attack

        def perform_heal(self, overheal=False) -> None:
            """
            Heal character.
            """
            renpy.sound.play("sound/potion.ogg", relative_volume=0.5)
            if not overheal and self.health + self.heal >= self.health_max:
                self.health = self.health_max
            else:
                self.health += self.heal

        def reset(self) -> None:
            """
            Reset stats.
            """
            self.attack_multiplier = 1
            self.stunned = False

            if self.health > self.health_max:
                self.health = self.health_max
