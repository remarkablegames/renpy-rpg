init python:
    class Enemies:
        def __init__(self) -> None:
            self.enemies = []
            self.count = 0

        def generate(self, count: int = 1) -> None:
            """
            Generate enemies.
            """
            self.enemies = []
            self.count = count

            while count > 0:
                enemy = RPGCharacter()
                enemy.image = "girl" if count > 1 else "boy"
                enemy.name = enemy.image.capitalize()

                enemy.health = enemy.health_max = round(5 * (wins + 1) * (1 + renpy.random.random()))

                enemy.attack_min = round(wins * (1 + renpy.random.random())) + 1
                enemy.attack_max = enemy.attack_min + wins + 1

                enemy.heal_min = round(wins * (1 + renpy.random.random())) + 1
                enemy.heal_max = enemy.heal_min + wins + 1

                self.enemies.append(enemy)

                count -= 1

        def show(self, count: int = 1) -> None:
            """
            Show enemies.
            """
            self.generate(count)

            for enemy_index, enemy in enumerate(self.enemies):
                xalign_position = self.xalign_position(enemy)
                renpy.show_screen(f"enemy_stats{enemy_index}", enemy, xalign_position)
                renpy.show(enemy.image, at_list=[position(xalign_position)])

            renpy.with_statement(dissolve)

        def dead(self) -> bool:
            """
            Whether enemies are dead.
            """
            for enemy in self.enemies:
                if enemy.health > 0:
                    return False

            return True

        def xalign_position(self, enemy: RPGCharacter) -> float:
            """
            Get enemy xalign position.
            """
            count = self.count
            index = self.enemies.index(enemy)

            if index == 0 and count == 2:
                xalign_position = 0.25
            elif index == 1 and count == 2:
                xalign_position = 0.75
            else:
                xalign_position = 0.5

            return xalign_position

        def turn(self) -> None:
            """
            Enemy turn.
            """
            for enemy in self.enemies:
                if enemy.health <= 0:
                    continue

                if enemy.stunned:
                    narrator(f"{enemy.name} is stunned!")
                    continue

                enemy.turn_rng()

                if enemy.health < enemy.health_max and renpy.random.random() < 0.5:
                    narrator(f"{enemy.name} healed {enemy.heal} health.")
                    enemy.perform_heal()
                else:
                    narrator(f"{enemy.name} dealt {enemy.attack} damage to you.")
                    renpy.with_statement(vpunch)
                    player.health -= enemy.attack

                    if player.health <= 0:
                        renpy.jump("lose")

            self.end_turn()

        def end_turn(self) -> None:
            """
            Enemy end turn.
            """
            for enemy in self.enemies:
                enemy.stunned = False

default enemies = Enemies()
