# git clone https://github.com/Majdawad88/ECET411_PIR.git


import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)

while True:

        PIR_status = GPIO.input(PIR_PIN)
        if PIR_status == 1:
                print('Moved')
        sleep(.1)

