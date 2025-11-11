import random
print("***Rock,Paper,Scissors...***\n")
continuer = "o"
choose = ["rock", "paper", "scissors"]
while continuer == "o":
    player = input("Enter rock, paper or scissors : ")
    if not player in choose:
        continue
    else:
        computer = random.choice(choose)
        print(f"You choose {player}")
        print(f"The computer choose {computer}")
        if player == computer:
            print("Tie...")
        elif player == "rock":
            if computer == "scissors":
                print("You won!")
            else:
                print("You lost!")
        elif player == "paper":
            if computer == "rock":
                print("You won!")
            else:
             print("You lost!")
        elif player == "scissors":
            if computer == "paper":
                print("You won!")
            else:
             print("You lost!")
    continuer = input("Continue ? o/n : ")
    print("--" * 50)
    if continuer != "o":
        print("\n***Fin du jeu***")
        break