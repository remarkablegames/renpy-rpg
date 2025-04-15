init python:
    class Emoji:
        def __init__(self) -> None:
            self.emojis = {
                "1": "1️⃣",
                "2": "2️⃣",
            }

        def get(self, key) -> str:
            """
            Get emoji.
            """
            return self.emojis[str(key)]

default emoji = Emoji()
