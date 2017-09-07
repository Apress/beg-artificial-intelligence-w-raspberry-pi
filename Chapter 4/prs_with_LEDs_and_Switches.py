import RPi.GPIO as GPIO
import time
from random import randint

# Setup GPIO pins
# Set the BCM mode
GPIO.setmode(GPIO.BCM)

# Outputs
GPIO.setup( 4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# Ensure all LEDs are off to start
GPIO.output( 4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)

# Inputs
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

global player
player = 0

# Setup the callback functions
def rock(channel):
    global player
    player = 1  # magic number 1 = rock, pin 12
    
def paper(channel):
    global player
    player = 2  # magic number 2 = paper pin 16
    
def scissors(channel):
    global player
    player = 3  # magic number 3 = scissors pin 21
    
def quit(channel):
    exit()      # pin 20, immediate exit from the game

# Add event detection and callback assignments
GPIO.add_event_detect(12, GPIO.RISING, callback=rock)
GPIO.add_event_detect(16, GPIO.RISING, callback=paper)
GPIO.add_event_detect(21, GPIO.RISING, callback=scissors)
GPIO.add_event_detect(20, GPIO.RISING, callback=quit)

# computer random pick
computer = randint(1,3)
 
while True:

    if player == computer:
        # This is a tie condition
        GPIO.output(27,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(27, GPIO.LOW)
        player = 0
    elif player == 1:
        if computer == 2:
            # Player loses, paper covers rock
            GPIO.output(17,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(17, GPIO.LOW)
            player = 0
        else:
            # Player wins, rock dulls scissors
            GPIO.output(4,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(4, GPIO.LOW)
            player = 0
    elif player == 2:
        if computer == 3:
            # Player loses, scissors cuts paper
            GPIO.output(17,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(17, GPIO.LOW)
            player = 0
        else:
            # Player wins, paper covers rock
            GPIO.output(4,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(4, GPIO.LOW)
            player = 0
    elif player == 3:
        if computer == 1:
            # Player loses, rock dulls scissors
            GPIO.output(17,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(17, GPIO.LOW)
            player = 0
        else:
            # Player wins, scissors cuts paper
            GPIO.output(4,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(4, GPIO.LOW)
            player = 0
   
    # another random pick for the computer
    computer = randint(1,3)

   
    
