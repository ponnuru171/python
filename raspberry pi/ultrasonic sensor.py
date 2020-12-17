import RPi.GPIO as GPIO
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

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = (pulse_end_time) - (pulse_start_time)
      distance = round(pulse_duration * 17150, 2)
      print("Distance:",distance,"cm")
"""VCC Connects to Pin 2 (5v)
Trig Connects to Pin 7 (GPIO 4)
Echo Connects to R1 (1k Ω)
R2 (2k Ω) Connects from R1 to Ground
Wire from R1 and R2 connects to Pin 11
GND connects to Pin 6 (Ground)
    """