screen select_enemy:
    text "Select enemy:"

    for enemy in enemies.enemies:
        if enemy.health > 0:
            imagebutton:
                focus_mask True
                idle f"enemies/{enemy.image}.png"
                hover f"enemies/{enemy.image} hover.png"
                at position(enemies.xalign_position(enemy))
                action Call("player_attack_end", enemy)

label player_attack:

    window hide

    $ enemies_alive = enemies.alive()
    if len(enemies_alive) == 1:
        call player_attack_end(enemies_alive[0])
        jump player_turn

    show screen select_enemy
    pause

label player_attack_end(enemy=None):

    hide screen select_enemy

    if not enemy:
        jump player_turn_menu

    $ player.energy -= player.skills["attack"].energy
    $ player.perform_attack(enemy)
    $ renpy.show(enemy.image, at_list=[shake])

    "You dealt [player.attack] damage to [enemy.name]."

    if enemy.health <= 0:
        $ renpy.hide(enemy.image)
        $ renpy.with_statement(dissolve)
        $ renpy.hide_screen(f"enemy_stats{enemies.enemies.index(enemy)}")

    elif "stun" in player.skills["attack"].tags and renpy.random.random() < 0.2:
        $ enemy.stunned = True
        $ renpy.show(enemy.image, at_list=[shake])

        "You stunned the enemy!"

    return
