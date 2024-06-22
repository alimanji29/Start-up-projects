from random import randint

L= ["rock", "paper", "scissors"]

while True:
    Aliakber = L[randint(0,2)]
    Player = input("rock, paper or scissors? ")
    if Player == Aliakber:
        print("TIE")
    elif Player == "rock":
        if Aliakber == "paper":
            print("HAHA, YOU LOSE")
        else:
            print("Good job, you win")
    elif Player == "paper":
        if Aliakber == "scissors":
            print("HAHA, YOU LOSE")
        else: 
            print("You win")
    elif Player == "scissors":
        if Aliakber == "rock":
            print("HAHA, YOU LOSE")
        else:
            print("You win")
    else:
        print("check your spelling buddy")

    play_again= input("Do you want to play again? (y/n) ")
    if play_again != "y":
        break