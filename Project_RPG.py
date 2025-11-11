import random
choose = ["1","2"]
player_hp = 50
enemy_hp = 50
number_potions_player = 5
skip_turn_player = False
skip_turn_enemy = False
while True:
    #choix du joueur
    if skip_turn_player:
        print("Vous passez votre tour...")
        skip_turn_player = False
    else:
        player_choice = ""
        while player_choice not in ["1","2"]:
            player_choice = input("Souhaitez-vous attaquer (1) ou boire une potion (2) ? : ")
        if player_choice == "1":
            player_attack = random.randint(5,15)
            enemy_hp -= player_attack
            print(f"\nVous avez inflige {player_attack} points de degat a l'ennemi!")
        elif player_choice == "2" and number_potions_player > 0:
            player_potion_health = random.randint(15,25)
            player_hp += player_potion_health
            number_potions_player -= 1
            skip_turn_player = True
            print(f"\nVous avez recupere {player_potion_health} points de vie!")
        else:
            print("\nVous n'avez plus de potions...\n")
            continue

    if player_hp > 100:
        player_hp = 100
    if enemy_hp <= 0:
        print("\nL'ennemi n'a plus de ponits de vie, tu as gagne!!")
        break

    #choix de l'ennemi
    if skip_turn_enemy:
        print("L'ennemi passe son tour...")
        skip_turn_enemy = False
    else:
        enemy_choice = random.choice(choose)
        if enemy_choice == "1":
            enemy_attack = random.randint(5,15)
            player_hp -= enemy_attack
            print(f"L'ennemi vous a inflige {enemy_attack} points de degat!")
        else:
           enemy_potion_health = random.randint(5,15)
           enemy_hp += enemy_potion_health
           skip_turn_enemy = True
           print(f"l'ennemi a recupere {enemy_potion_health} points de vie!")

    if enemy_hp > 100:
        enemy_hp = 100
    if player_hp <= 0:
        print("\nTu n'as plus de points de vie, tu as perdu!!")
        break

    #Stats
    print(f"\nIl vous reste {player_hp} points de vie et {number_potions_player} potions restantes.")
    print(f"Il reste {enemy_hp} points de vie a l'ennemi.")
    print("--" * 50)
print("\n***Fin du jeu***")