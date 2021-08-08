from character_generator import *

player = new_player()
while player.health > 0:
    player.enemy=new_enemy()
    player.enemy.enemy=player
    print(f"{player.enemy} {player.enemy.name} appeared!")
    print("Prepare to battle!")
    while player.enemy.health > 0:
        player.increment_turns()
        player.enemy.increment_turns()
    print(f"Defeated {player.enemy.name}")



