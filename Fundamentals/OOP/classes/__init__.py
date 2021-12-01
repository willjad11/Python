import random
import math


class BattleOver:
    def __init__(self):
        pass

    death = False

class Stats:

    def __init__( self , name):
        self.name = name
        self.strength = (random.randint(0,10))
        self.speed = (random.randint(0,10))
        self.health = (math.floor(random.randint(70,100)))

    def dodge(self):
        dodge = (random.randint(math.floor(self.speed/4),self.speed+1))
        if dodge >= self.speed:
            print("Dodged the attack!")
        print({dodge})

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")


    def attack (self,player):
        attackid = random.randint(0,2)
        attacks ={
            0:(4,0,9,2),
            1:(2,5,9,3),
            2:(2,10,7,9)
        }
        def death(self, player):
            if self.health <= 0:
                print(f"{self.name} has died! {player.name} wins!")
                BattleOver.death = True
            else:
                return False
        
        if death(self, player) == False and BattleOver.death == False:
            strength_div,strength_add,crit_check,dmg_mult = attacks[attackid]
            attack_name = player.attack_names[attackid]

            damage_done = (random.randint(math.floor(self.strength / strength_div), self.strength + 1)) + strength_add
            player.health -= damage_done
            print(f"{self.name} hit {player.name} with a {attack_name} for {damage_done} damage!")
            if (random.randint(0,10+1)) >= crit_check:
                player.health -= (damage_done *dmg_mult)
                print(f"{self.name} crit for an extra " + str(math.floor(damage_done * dmg_mult)),"damage!")
            print(f'{player.name} has {player.health} health!')
            print("----------------------------")
            return self,player.health
    
