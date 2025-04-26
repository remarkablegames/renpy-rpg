# Should the user be allowed to rollback the game? If set to False, the user cannot interactively rollback.
define config.rollback_enabled = False

# To customize levels, see `game/story/data/levels.json`.

init python:
    class Game:
        pass

    game = Game()

    # Enemy names that are mapped to their respective images. E.g., name "Boy 1" becomes image "boy_1".
    game.enemies = ["Boy", "Girl", "Guy"]
