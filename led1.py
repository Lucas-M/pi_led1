import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
# Setup variables for user input
led_choice = 0
count = 0

os.system('clear')

print "Which LED you want to blink?"
print "!: Red?"
print "2: Green?"
print "3: Yellow?"
print "4: All?"
led_choice = inp9ut("Make your choice: ")

if led_choice == 1:
    os.system('clear')
    print "You choose the red LED"
    count = input("How many times you want it to blink?: ")
    while count > 0:
        GPIO.output(7,GPIO.HIGH)
        time.sleep(1)
        count = count - 1


    
