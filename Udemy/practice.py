import RPi.GPIO as GPIO
import time

LED_PIN = 17
GPIO.setmode(GPIO.BCM)  # use gpio number
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
  # GPIO.HIGH ~ GPIO.LOW : toggle 1
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()  # energy be put off
