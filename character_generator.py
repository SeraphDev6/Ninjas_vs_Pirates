from character import *
from random import choice

classes={"ninja":Ninja,"nirate":Pirate}

def new_player():
    name = input("What is your name? > ").capitalize()
    char_class=""
    while char_class=="":
        attempt= input("Are you a ninja, or a pirate? > ").lower()
        if attempt in classes:
            char_class = classes[attempt]
        else:
            print("You can only choose between ninja and pirate!")
    player = char_class(name,player=True)
    status=""
    while status=="":
        answer = input("Would you rather be strong, fast, or hearty? > ").lower()
        if answer == "strong":
            status=answer
            player.strength += 1
        elif answer == "fast":
            status=answer
            player.speed += 1
        elif answer == "hearty":
            status=answer
            player.max_health += 5
            player.health += 5
        else:
            print("That wasn't one of the options!")
    print(f"Starting as {player.name}, the {status} {attempt}")
    return player

ninja_names=["blarg"]
pirate_names=["blargf"]
def new_enemy():
    enemy_class=choice(list(classes.values()))
    name= choice(ninja_names) if enemy_class==Ninja else choice(pirate_names)
    return enemy_class(name)
