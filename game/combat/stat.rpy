init python:
    class Stat():
        def __init__(self, stat: dict = {}) -> None:
            self.health = self.health_max = stat.get("health", 0)
            self.energy = self.energy_max = stat.get("energy", 0)

            self.attack = 0
            self.attack_min = stat.get("attack_min", 0)
            self.attack_max = stat.get("attack_max", 0)

            self.heal = 0
            self.heal_min = stat.get("heal_min", 0)
            self.heal_max = stat.get("heal_max", 0)

        def turn(self) -> None:
            self.attack = renpy.random.randint(self.attack_min, self.attack_max)
            self.heal = renpy.random.randint(self.heal_min, self.heal_max)

        def apply_heal(self) -> None:
            if self.health + self.heal >= self.health_max:
                self.health = self.health_max
            else:
                self.health += self.heal
