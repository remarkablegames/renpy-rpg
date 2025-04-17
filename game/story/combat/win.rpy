init python:
    from math import ceil

default money = 0
default interest = 0
default rewards = 0
default wins = 0

label win:

    hide placeholder boy with dissolve

    "You defeated the enemy!"

    $ wins += 1
    $ interest = ceil(money * 0.2)
    $ money += renpy.random.randint(wins, wins + 3) + interest

    "You earned $[money] + $[interest] (interest)."

    if wins % 3 == 1:
        $ rewards += 1

        jump reward

    else:

        jump shop
