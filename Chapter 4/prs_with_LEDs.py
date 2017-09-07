import RPi.GPIO as GPIO
import time
from random import randint

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
 
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
        GPIO.output(27,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(27, GPIO.LOW)
    elif player == "rock":
        if computer == "paper":
            print("You lose ", computer, "covers", player)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(17, GPIO.LOW)
        else:
            print("You win ", player, "dulls", computer)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(4, GPIO.LOW)
    elif player == "paper":
        if computer == "scissors":
            print("You lose ", computer, "cuts", player)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(17, GPIO.LOW)
        else:
            print("You win ", player, "covers", computer)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(4, GPIO.LOW)
    elif player == "scissors":
        if computer == "rock":
            print("You lose ", computer, "dulls", player)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(17, GPIO.LOW)
        else:
            print("You win ", player, "cuts", computer)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(4, GPIO.LOW)
    else:
        print("Invalid input. Please reenter")
    
    # Reset player = False to continue looping    
    player = False

    computer = inputList[randint(0,2)]
