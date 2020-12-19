import RPi.GPIO as GPIO
from time import sleep
import keyboard


# Motor Status
STOP = 0
MOVE = 1

# GPIO PIN
PIN1 = 17
PIN2 = 22
PIN3 = 27

DC = 0
HZ = 1

def setting():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN1, GPIO.OUT)
    GPIO.setup(PIN2, GPIO.OUT)
    GPIO.setup(PIN3, GPIO.OUT)
    pwm = GPIO.PWM(PIN1, HZ)
    return pwm

def moveForward(pwm):
    print("\tmoveForward")
    GPIO.output(PIN2, MOVE)
    GPIO.output(PIN3, MOVE)
    pwm.start(DC)
    
   # sleep(time)


def moveRight(pwm):
    print("\tmoveRight")
    GPIO.output(PIN2, STOP)
    GPIO.output(PIN3, MOVE)
    pwm.start(DC)
    
#   sleep(time)
    
#    GPIO.output(PIN2, STOP)
#    GPIO.output(PIN3, STOP)
#    pwm.start(DC)

    
def moveLeft(pwm):
    print("\tmoveLeft")
    GPIO.output(PIN2, MOVE)
    GPIO.output(PIN3, STOP)
    pwm.start(DC)
    
 #   sleep(time)

def stop(pwm):
    print("\tstop")
    GPIO.output(PIN2, STOP)
    GPIO.output(PIN3, STOP)
    pwm.start(DC)
    
    
print("Program started")

pwm = setting()

while True:
#    print(keyboard.read_key())
    if keyboard.is_pressed('w'):
        print("go")
        moveForward(pwm)
    elif keyboard.is_pressed('d'):
        print("right")
        moveRight(pwm)
    elif keyboard.is_pressed('a'):
        print("left")
        moveLeft(pwm)
    elif keyboard.is_pressed('q'):
        break
    else:
        print(keyboard.read_key())
        stop(pwm)

stop(pwm)
GPIO.cleanup()
print("Program end")