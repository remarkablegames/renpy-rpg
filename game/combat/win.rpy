init python:
    import math

label win:

    $ wins += 1

    hide placeholder boy with dissolve

    "You defeated the enemy!"

    $ rewards = math.ceil(wins / 10)

    jump reward
