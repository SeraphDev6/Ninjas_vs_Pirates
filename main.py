from character_generator import *

player = new_player()
while player.health > 0:
    player.enemy=new_enemy()
    player.enemy.enemy=player
    print(f"{player.enemy} {player.enemy.name} appeared!")
    print("Prepare to battle!")
    while player.enemy.health > 0 and player.health >0:
        player.increment_turns()
        player.enemy.increment_turns()
    if player.health > 0:
        player.enemies_defeated+=1
        print(f"Defeated {player.enemy.name}")
print(f"Well fought {player} {player.name}. You defeated {player.enemies_defeated} enemies!")


