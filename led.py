# Pin assignments
import  RPi.GPIO as GPIO
LED_PIN = 7
BUTTON_PIN = 17
# Setup GPIO module and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)
# Set LED pin to OFF (no voltage)
GPIO.output(LED_PIN, GPIO.LOW)
try:
    # Loop forever
    while 1:
         # Detect voltage on button pin
         if GPIO.input(BUTTON_PIN) == 1:
              # Turn on the LED
              GPIO.output(LED_PIN, GPIO.HIGH)
         else:
               # Turn off the LED
               GPIO.output(LED_PIN, GPIO.LOW)
except KeyboardInterrupt:
    print('hecho')
finally:
    GPIO.cleanup()
    