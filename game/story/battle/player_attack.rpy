screen select_enemy():
    text "Select enemy:"

    for enemy_index, enemy in enumerate(enemies.enemies):
        if enemy.health > 0:
            imagebutton:
                focus_mask True
                idle f"enemies/{enemy.image}.png"
                hover f"enemies/{enemy.image} hover.png"
                at position(enemies.xalign_position(enemy))
                action Call("player_attack_end", enemy, enemy_index)

label player_attack:

    window hide

    if enemies.count_alive() == 1:
        call player_attack_end(enemies.get_alive())

        jump player_turn

    show screen select_enemy

    pause

label player_attack_end(enemy = None, enemy_index = 0):

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
        $ renpy.hide_screen(f"enemy_stats{enemy_index}")

    elif "stun" in player.skills["attack"].tags and renpy.random.random() < 0.2:
        $ enemy.stunned = True
        $ renpy.show(enemy.image, at_list=[shake])

        "You stunned the enemy!"

    return
