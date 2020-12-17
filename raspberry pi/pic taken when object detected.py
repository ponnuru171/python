import RPi.GPIO as GPIO
import picamera
from time import sleep
import time

while 1:
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 7
    PIN_ECHO = 11
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print("Waiting for sensor to settle")
    time.sleep(2)
    print("Calculating distance")
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance:", distance, "cm")
    if distance < 30:
        with picamera.PiCamera() as cam:
            cam.resolution = (2592, 1944)
            ts = (time.strftime("%Y %d %b %H.%M.%S"))
            sai = ts + "image.jpg"
            print("ready for the picture")
            sleep(3)
            cam.capture(sai)
            print("picture is taken")
            sleep(2)
    else:
        sleep(5)
        print("object is not in range to capture the picture")
    