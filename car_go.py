import RPi.GPIO as GPIO
from time import sleep

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

def moveForward(pwm, time):
    print("\tmoveForward")
    GPIO.output(PIN2, MOVE)
    GPIO.output(PIN3, MOVE)
    pwm.start(DC)
    
    sleep(time)
    
    GPIO.output(PIN2, STOP)
    GPIO.output(PIN3, STOP)
    pwm.start(DC)

def moveRight(pwm, time):
    print("\tmoveRight")
    GPIO.output(PIN2, STOP)
    GPIO.output(PIN3, MOVE)
    pwm.start(DC)
    
    sleep(time)
    
    GPIO.output(PIN2, STOP)
    GPIO.output(PIN3, STOP)
    pwm.start(DC)
    
def moveLeft(pwm, time):
    print("\tmoveLeft")
    GPIO.output(PIN2, MOVE)
    GPIO.output(PIN3, STOP)
    pwm.start(DC)
    
    sleep(time)
    
    GPIO.output(PIN2, STOP)
    GPIO.output(PIN3, STOP)
    pwm.start(DC)
    
def stop(pwm):
    print("\tstop")
    pwm.stop()
    GPIO.cleanup()
    
print("Program started")
pwm = setting()
moveForward(pwm, 1)
moveRight(pwm, 1)
moveLeft(pwm, 1)
stop(pwm)
print("Program end")