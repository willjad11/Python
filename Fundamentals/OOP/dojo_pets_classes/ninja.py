class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self, pet):
        print(f"The famous ninja {self.first_name} {self.last_name} walks {pet.name}")
        pet.play(self)

    def feed(self, pet):
        print(f"The famous ninja {self.first_name} {self.last_name} feeds {pet.name} 1 treat and some {self.pet_food}")
        pet.eat(self)
        self.treats -= 1
        print(f"{self.treats} treats are left")

    def bathe(self, pet):
        print(f"The famous ninja {self.first_name} {self.last_name} bathes {pet.name}")
        pet.noise(self)
