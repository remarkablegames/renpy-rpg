init python:
    from math import ceil

default wins = 0

label win:

    $ wins += 1

    hide placeholder boy with dissolve

    "You defeated the enemy!"

    $ rewards = ceil(wins / 10)

    jump reward
