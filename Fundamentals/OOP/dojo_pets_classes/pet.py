from dojo_pets_classes import ninja

class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    energy = 10
    health = 100

    def sleep(self, owner):
        print(f"The {self.type} {self.name} sleeps next to {ninja.first_name}")
        self.energy += 25
        print(f"{self.name}'s energy level is {Pet.energy}")

    def eat(self, owner):
        print(f"The {self.type} {self.name} happily eats next to {owner.first_name}.")
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy level is {Pet.energy}")
        print(f"{self.name}'s health level is {Pet.health}")

    def play(self, owner):
        print(f"The {self.type} {self.name} plays excitedly near {owner.first_name}")
        self.health += 5
        print(f"{self.name}'s health level is {Pet.health}")

    def noise(self, owner):
        print(f"The {self.type} {self.name} barks at {owner.first_name}")


class SecondPet( Pet ):
    def __init__(self, name, type):
        super().__init__(name, type)
    
    energy = 10
    health = 100
