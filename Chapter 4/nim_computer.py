import random
print "NIM GAME"


player1 = raw_input("Enter your name: ")
player2 = "Computer"
howMany = 0
gameover=False
global stickNumber
stickNumber = 21

def moveComputer():
    removedNumber = random.randint(1,3)
    global stickNumber
    while (removedNumber < stickNumber) or (stickNumber <= 4):
        if stickNumber >= 4:
            stickNumber -= removedNumber
            return stickNumber
        elif (stickNumber == 3) or (stickNumber == 2) or (stickNumber == 1):
            stickNumber = 1
            return stickNumber


def moveHuman():
    global stickNumber
    global howMany
    stickNumber -= howMany
    return stickNumber

def humanLegalMove():
    global howMany
    global stickNumber
    legalMove=False
    while not legalMove:
        print("It's your turn, ",player1)
        howMany=int(input("How many sticks do you want to remove?(from 1 to 3) "))
        if  howMany>3 or howMany<1:
            print("Enter a number between 1 and 3.")
        else:
            legalMove=True
    while (howMany >= stickNumber):
        print("The entered number is greater than or equal to the number of sticks remaining.")
        howMany=int(input("How many sticks do you want to remove?"))
        return howMany

def checkWinner(player):
    global stickNumber
    if stickNumber == 1:
        print(player," wins.")
        global gameover
        gameover = True
        return gameover

def resetGameover():
    global gameover
    global stickNumber
    gameover = False
    stickNumber = 21
    howMany = 0
    return gameover

def game():
    while gameover == False:
        print("It's ",player2,"turn. The number of sticks left: ", moveComputer())
        checkWinner(player2)
        if gameover == True:
            playAgain()  
        humanLegalMove()        
        print("The number of sticks left: ", moveHuman())
        checkWinner(player1)
        if gameover == True:
            playAgain()

def playAgain():
    answer = raw_input("Do you want to play again?(y/n)")
    resetGameover()
    if answer=="y":
        game()
    else:
        print("Thanks for playing the game")
        exit()   

game()
playAgain()
