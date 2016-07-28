import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.IN) ## Setup GPIO Pin 7 to OUT
inp = GPIO.input(7)

while True:
    if GPIO.input(17):
        print "button pressed"
