from random import randint
 
# List the input options
inputList = ["paper", "rock", "scissors"]
 
# Random computer pick
computer = inputList[randint(0,2)]
 
# Initially set player = False
player = False
 
while player == False:

    player = raw_input("paper, rock, scissors?")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose ", computer, "covers", player)
        else:
            print("You win ", player, "dulls", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose ", computer, "cuts", player)
        else:
            print("You win ", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose ", computer, "dulls", player)
        else:
            print("You win ", player, "cuts", computer)
    else:
        print("Invalid input. Please reenter")
    
    # Reset player = False to continue looping    
    player = False

    computer = inputList[randint(0,2)]
