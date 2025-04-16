screen stat(name, current, max):
    text "[name]: [current]/[max]"
    bar value AnimatedValue(current, max):
        xalign 0.5
        xsize 300

screen player_stats():
    zorder 1
    frame:
        yalign 1.0
        vbox:
            use stat("Health", player.health, player.health_max)
            null height 15
            use stat("Energy", player.energy, player.energy_max)
            null height 15
            text "Money: $[money]"

screen enemy_stats():
    frame:
        xalign 1.0
        vbox:
            use stat("Health", enemy.health, enemy.health_max)
