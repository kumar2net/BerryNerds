import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)

def blink():
    while True:
        print("LED ON")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.4)
        
        print("LED OFF")
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.4)
    
def destroy():
        print("  LED SHUTDOWN BY KEYBOARDINTERRUPT")
        GPIO.output(18,GPIO.HIGH)
        GPIO.cleanup()
        
        
if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()
        
