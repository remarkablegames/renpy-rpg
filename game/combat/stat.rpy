init python:
    class Stat():
        def __init__(self, stat: dict = {}) -> None:
            self.health = self.health_max = stat.get("health", 0)
            self.energy = self.energy_max = stat.get("energy", 0)

        def random_health(self, minimum: int, maximum: int) -> None:
            self.health = self.health_max = renpy.random.randint(minimum, maximum)
