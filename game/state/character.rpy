init python:
    class RPGCharacter():
        def __init__(self, **kwargs) -> None:
            self.health = self.health_max = kwargs.get("health", 0)
            self.energy = self.energy_max = kwargs.get("energy", 0)

            self.attack = 0
            self.attack_min = kwargs.get("attack_min", 0)
            self.attack_max = kwargs.get("attack_max", 0)

            self.heal = 0
            self.heal_min = kwargs.get("heal_min", 0)
            self.heal_max = kwargs.get("heal_max", 0)

        def turn_rng(self) -> None:
            """
            Generate random numbers for turn.
            """
            self.attack = renpy.random.randint(self.attack_min, self.attack_max)
            self.heal = renpy.random.randint(self.heal_min, self.heal_max)

        def perform_heal(self) -> None:
            """
            Heal character.
            """
            if self.health + self.heal >= self.health_max:
                self.health = self.health_max
            else:
                self.health += self.heal
