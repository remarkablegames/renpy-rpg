init python:
    import json

    class Levels:
        def __init__(self) -> None:
            self.levels = json.load(renpy.file("story/data/levels.json"))

        def get(self, level: int) -> dict:
            """
            Get level data.
            """
            try:
                return self.levels[str(level)]

            except KeyError:
                level = { "enemies": [] }

                enemies_count = 1 if wins < 3 else 2

                while enemies_count > 0:
                    girl = renpy.random.random() < 0.5
                    attack_min = round(wins * (1 + renpy.random.random())) + 1
                    heal_min = round(wins * (1 + renpy.random.random())) + 1

                    level["enemies"].append({
                        "name": "Girl" if girl else "Boy",
                        "image": "girl" if girl else "boy",
                        "health": round(5 * (wins + 1) * (1 + renpy.random.random())),
                        "attack_min": attack_min,
                        "attack_max": attack_min + wins + 1,
                        "heal_min": heal_min,
                        "heal_max": heal_min + wins + 1,
                    })

                    enemies_count -= 1

                return level

default levels = Levels()
