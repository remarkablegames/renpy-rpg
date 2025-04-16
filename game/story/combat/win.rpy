init python:
    from math import ceil

default money = 0
default interest = 0
default rewards = 0
default wins = 0

label win:

    $ wins += 1

    hide placeholder boy with dissolve

    "You defeated the enemy!"

    $ interest = ceil(money * 0.2)
    $ money += wins + interest

    "You earned $[wins] + $[interest] (interest)."

    $ rewards += 1

    jump reward
