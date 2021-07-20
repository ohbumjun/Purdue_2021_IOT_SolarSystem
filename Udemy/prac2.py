# 0 : power off
# 1 : power on
import RPi.GPIO as GPIO
import time

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
# GPIO.output(LED_PIN, GPIO.HIGH) : 켜놓고 시작

state = int(input("Enter 0 to power off the LED, 1 to power on the LED : "))
if state == 0:
    GPIO.output(LED_PIN, GPIO.LOW)
elif state == 1:
    GPIO.output(LED_PIN, GPIO.HIGH)
else:
    print("Wrong state value :" + str(state))
    exit

time.sleep(2)
GPIO.cleanup()

# if :
# -state is 0 => power off the LED
#           1 => power on the LED
# otherwise   => cleanup GPIOs and exit
