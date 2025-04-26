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

screen enemy_stats0(enemy, xalign_position = 0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Health", enemy.health, enemy.health_max)

screen enemy_stats1(enemy, xalign_position = 0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Health", enemy.health, enemy.health_max)

screen enemy_stats2(enemy, xalign_position = 0.5):
    frame:
        xalign xalign_position
        vbox:
            use stat("Health", enemy.health, enemy.health_max)
