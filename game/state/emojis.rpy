init python:
    class Emojis:
        def __init__(self) -> None:
            self.emojis = {
                "1": "1️⃣",
                "2": "2️⃣",
            }

        def get(self, key) -> str:
            return self.emojis.get(str(key))

default emojis = Emojis()
