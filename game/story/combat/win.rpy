init python:
    from math import ceil

default money = 0
default winnings = 0
default interest = 0
default rewards = 0
default wins = 0

label win:

    "You defeated the enemy!"

    $ player.reset()
    $ wins += 1
    $ interest = ceil(money * 0.2)
    $ winnings = renpy.random.randint(wins, round(wins * 1.5) + 1)
    $ money += winnings + interest

    "You earned $[winnings] + $[interest] (interest)."

    if wins % 3 == 1:
        $ rewards += 1

        jump reward

    else:

        jump shop
