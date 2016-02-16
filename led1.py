#!/usr/bin/python/
import os                   # what is this?
import time                 # why import this?
import RPi.GPIO as GPIO		# Import lib to interface with GPIO pin on rpi2

GPIO.setmode(GPIO.BOARD)    # Is this needed to access GPIO?
GPIO.setwarnings(False)
				# Prepare the pins	
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

# Setup variables for user input
led_choice = 0
count = 0

os.system('clear')

print ("Which LED you want to blink?")
print ("1: Red?")
print ("2: Green?")
print ("3: Yellow?")
print ("4: All?")
led_choice = input("Make your choice: ")

if led_choice == 1:
    os.system('clear')
    print ("You choose the red LED")
    count = input("How many times you want it to blink?: ")
    while count > 0:
        GPIO.output(7,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(7,GPIO.LOW)
        time.sleep(1)
        count = count - 1

if led_choice == 2:
    os.system('clear')
    print ("You choose the green LED")
    count = input("How many times you want it to blink?: ")
    while count > 0:
        GPIO.output(11,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(11,GPIO.LOW)
        time.sleep(1)
        count = count - 1

if led_choice == 3:
    os.system('clear')
    print ("You choose the yellow LED")
    count = input("How many times you want it to blink?: ")
    while count > 0:
        GPIO.output(13,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(13,GPIO.LOW)
        time.sleep(1)
        count = count - 1

if led_choice == 4:
    os.system('clear')
    print ("You choose all LEDs")
    count = input("How many times you want them all to blink?: ")
    while count > 0:
        GPIO.output(7,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(7,GPIO.LOW)

        GPIO.output(11,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(11,GPIO.LOW)

        GPIO.output(13,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(13,GPIO.LOW)

        count = count - 1

GPIO.cleanup()


    
