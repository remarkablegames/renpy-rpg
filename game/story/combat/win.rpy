init python:
    from math import ceil

default money = 0
default loot = 0
default interest = 0
default rewards = 0
default wins = 0

label win:

    "You won the battle!"

    $ player.reset()
    $ wins += 1
    $ interest = ceil(money * 0.4)
    $ loot = renpy.random.randint(wins, round(wins * 1.5) + 1)
    $ money += loot + interest

    "You earned $[loot] + $[interest] (interest)."

    if wins % 3 == 1:
        $ rewards += 1

        jump reward

    else:

        jump shop
