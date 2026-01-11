# Should the user be allowed to rollback the game? If set to False, the user cannot interactively rollback.
define config.rollback_enabled = False


init python:
    def tooltip_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "tooltip")]

    config.custom_text_tags["tooltip"] = tooltip_tag


# To customize enemies: `game/scripts/data/enemies.json`
# To customize levels: `game/scripts/data/levels.json`
