from math import ceil
from move_list import *
from random import choice

class Character:
    def __init__(self,name,strength,speed,health,moves,player):
        self.name=name
        self.player=player
        self.strength = strength
        self.speed = speed
        self.health = health*5
        self.max_health=health*5
        self.moves=moves
        self.player=player
        self.cooldown=0
        self.current_move=None
        self.enemy=None
        self.enemies_defeated = 0
    def display_health(self):
        bars=max(ceil((self.health*10)/self.max_health),0)
        if self.player:
            return ("|"+"#"*bars+"."*(10-bars)+"|")
        else:
            return ("|"+"."*(10-bars)+"#"*bars+"|")
    def increment_turns(self):
        if self.health > 0:
            self.cooldown -= self.speed
            if self.cooldown <= 0:
                if self.current_move == None:
                    self.choose_move()
                else:
                    getattr(self,self.current_move)()
            else:
                print(f"{self.name} is preparing {self.current_move}, Charged {self.moves[self.current_move]-self.cooldown}/{self.moves[self.current_move]} Energy!")
    def choose_move(self):
        if self.enemy.health >0:
            if self.player:
                print(f"{self.name} : {self.display_health()} vs {self.enemy.display_health()} : {self.enemy.name}")
                print("Available Moves:")
                for move in self.moves:
                    print(f"{move}, takes {self.moves[move]} energy.")

                move_choice=""
                while move_choice=="":
                    attempt = input("Which move do you want to use?").capitalize()
                    if attempt in self.moves:
                        move_choice = attempt
                    else:
                        print("That's not a valid move!")
                self.current_move=move_choice
                self.cooldown+=self.moves[move_choice]
            else:
                self.current_move=choice(list(self.moves.keys()))
                self.cooldown += self.moves[self.current_move]
        else: self.current_move =None
    def Attack(self):
        damage = self.strength
        self.enemy.health -= damage
        print(f"{self.name} attacked dealing {damage} damage!")
        self.choose_move()
class Ninja(Character):
    def __init__(self,name,moves=ninja_moves,player=False):
        super().__init__(name,4,6,4,moves,player)
    def Shuriken(self):
        damage = self.speed*2
        self.enemy.health -= damage
        print(f"{self.name} threw a shuriken dealing {damage} damage!")
        self.choose_move()
    def Meditate(self):
        damage = self.max_health//5
        self.health = min(self.health+damage,self.max_health)
        print(f"{self.name} calmed their mind and body, healing themselves for {damage} health!")
        self.choose_move()
    def Assasinate(self):
        damage = self.enemy.max_health - self.enemy.health
        self.enemy.health -= damage
        print(f"{self.name} used thier finishing move: Death Blow of 1000 Demon Deaths. It dealt {damage} damage!")
        self.choose_move()
    def __str__(self):
        return "Ninja"
class Pirate(Character):
    def __init__(self,name,moves=pirate_moves,player=False):
        super().__init__(name,4,4,6,moves,player)
    def Swashbuckle(self):
        damage = self.strength * 3
        self.enemy.health -= damage
        print(f"{self.name} sliced and slashed with their saber, dealing {damage} damage!")
        self.choose_move()
    def Drink(self):
        damage = self.max_health//4
        self.health = min(self.health+damage,self.max_health)
        print(f"{self.name} drank an entire keg of rum, healing(?) themselves for {damage} health!")
        self.choose_move()
    def Cannon(self):
        damage = 9999
        self.enemy.health -= damage
        print(f"{self.name} used thier finishing move: Shoot 'em with a cannon!! It dealt a ridiculous amount damage!")
        self.choose_move()
    def __str__(self):
        return "Pirate"