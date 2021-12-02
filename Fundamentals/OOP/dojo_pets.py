from dojo_pets_classes import ninja
from dojo_pets_classes import pet

ninjapet = pet.Pet("Fido", "Dog")
ninjapet2 = pet.SecondPet("Jingles", "Cat")
ninjaman = ninja.Ninja("Jaden", "Willeiksen", 10, "Pet Food", ninjapet)

ninjaman.feed(ninjapet)
ninjaman.walk(ninjapet)
ninjaman.bathe(ninjapet)

ninjaman.feed(ninjapet2)
ninjaman.walk(ninjapet2)