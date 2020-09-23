import RPi.GPIO as GPIO
import time
import sys
import traceback

GPIO.setmode(GPIO.BOARD)

def main():
    LED_PIN = 18
    SWITCH_PIN = 16

    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.wait_for_edge(SWITCH_PIN, GPIO.RISING, bouncetime=200)
    GPIO.output(LED_PIN, not GPIO.input(LED_PIN))
     

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        GPIO.cleanup()
    except Exception as e:
        print("Some error occured")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)
        GPIO.cleanup()
