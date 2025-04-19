screen select_enemy():
    imagebutton:
        idle "placeholder/placeholder boy.png"
        hover "placeholder/placeholder boy hover.png"
        at center
        action Jump("select_enemy_end")

label select_enemy:

    window hide

    show screen select_enemy

    pause

label select_enemy_end:

    hide screen select_enemy

    $ player.energy -= player.skills["attack"].energy
    $ enemy.health -= player.attack

    show placeholder boy at shake

    "You dealt [player.attack] damage to the enemy."

    if enemy.health > 0 and "stun" in player.skills["attack"].tags and renpy.random.random() < 0.2:
        $ enemy.stunned = True

        show placeholder boy at shake

        "You stunned the enemy!"

    jump player_turn
