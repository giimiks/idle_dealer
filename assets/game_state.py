import json

from dataclasses import dataclass

@dataclass
class GameState:
    background: str = "purple"

    def reset(self):
        self.background ="purple"

    def save(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load(cls, filename: str):
        try:
            with open(filename, "rb") as file:
                data = json.load(file)
                return cls(**data)
        except FileNotFoundError:
            print("No save file found.")
            return cls()
    