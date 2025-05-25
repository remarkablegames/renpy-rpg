init python:
    class Enemies:
        def __init__(self) -> None:
            self.enemies = []
            self.count = 0

        def generate(self) -> None:
            """
            Generate enemies.
            """
            enemies = levels.get(wins)["enemies"]

            self.enemies = []
            self.count = len(enemies)

            for enemy in enemies:
                self.enemies.append(RPGCharacter(**enemy))

        def show(self) -> None:
            """
            Show enemies.
            """
            self.generate()

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

            xalign_position = 0.5

            if count == 2:
                if index == 0:
                    xalign_position = 0.25
                elif index == 1:
                    xalign_position = 0.75
            elif count == 3:
                if index == 0:
                    xalign_position = 0.1
                elif index == 2:
                    xalign_position = 0.9

            return xalign_position

        def count_alive(self) -> int:
            """
            Get alive enemies.
            """
            count = 0
            for enemy in self.enemies:
                if enemy.health > 0:
                    count += 1
            return count

        def get_alive(self) -> RPGCharacter:
            """
            Get alive enemy.
            """
            for enemy in self.enemies:
                if enemy.health > 0:
                    return enemy

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

                if enemy.heal and enemy.health < enemy.health_max and renpy.random.random() < 0.5:
                    narrator(f"{enemy.name} healed {enemy.heal} health.")
                    enemy.perform_heal()
                else:
                    narrator(f"{enemy.name} dealt {enemy.attack} damage to you.")
                    renpy.with_statement(vpunch)
                    enemy.perform_attack(player)

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
