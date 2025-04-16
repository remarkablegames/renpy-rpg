init python:
    from math import ceil

default gold = 0
default wins = 0

label win:

    $ wins += 1

    hide placeholder boy with dissolve

    "You defeated the enemy!"

    $ gold += wins + abs(enemy.health)

    "You earned $[wins] + $[abs(enemy.health)] (bonus)."

    $ rewards = ceil(wins / 10)

    jump reward
