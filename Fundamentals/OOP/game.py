from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.__init__ import BattleOver

class Game:
    def __init__(self):
        self.ninja1 = Ninja("Ninja")
        self.pirate1 = Pirate("Pirate")

    def play(self):
        while BattleOver.death == False:
            self.ninja1.attack(self.pirate1)
            self.pirate1.attack(self.ninja1)


if __name__ == "__main__":
    game = Game()
    game.play()
