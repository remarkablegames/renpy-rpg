screen stat(name, current, max):
    text "[name]: [current]/[max]"
    bar value AnimatedValue(current, max):
        xalign 0.5
        xsize 300

screen player_stats():
    frame:
        yalign 1.0
        vbox:
            use stat("Health", player.health, player.health_max)
            null height 15
            use stat("Energy", player.energy, player.energy_max)

screen enemy_stats():
    frame:
        xalign 1.0
        vbox:
            use stat("Health", enemy.health, enemy.health_max)
