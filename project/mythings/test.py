from time import sleep 
from servosystem import Servo_Movement
from servo import Servo
from machine import Pin, PWM

servo_motors = Servo_Movement(20, 18)

def testing():
    print("Testing: FORWARD - SLOW")
    sleep(1)
    servo_motors.forward_slow()
    

testing()