# This file contains the Predator class

class Predator:

    def __init__(self) -> None:
        self.life : int = 50

    def __str__(self) -> str:
        return '🤖'

    def increase_life(self, damage):
        if self.life < 50:
            self.life += damage

    def decrease_life(self, damage):
        if self.life > 0:
            self.life -= damage
        if self.life < 0:
            self.life = 0

    