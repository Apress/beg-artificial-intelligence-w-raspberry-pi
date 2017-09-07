# LEDtest.py by D. J. Norris  Jan, 2017
# Uses Prolog with Python type functions
import time
import RPi.GPIO as GPIO
from pyswip import Functor, Variable, Query, call

# Setup Python like functions for Prolog statements
assertz = Functor(“assertz”, 1)
father = Functor(“father”, 2)

# Add facts to a dynamic database
call(assertz(father(“michael”,”john”)))
call(assertz(father(“michael”,”gina”)))

# Setup an iterative query session
X = Variable()
q = Query(father(“michael”,X))
while q.nextSolution():
    print “Hello,”, X.value
    if X.value == “john”:          # Lite LED #4 if john is a child of michael
        GPIO.output(4,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(4,GPIO.LOW)
    if X.value == “gina”:          # Lite LED #17 if gina is a child of michael
        GPIO.output(17,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(17,GPIO.LOW)

