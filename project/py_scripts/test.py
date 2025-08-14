from time import sleep 
from servo_system import Servo_Movement
from servo import Servo
from machine import Pin, PWM

servo_motors = Servo_Movement(20)

def testing():
    print("Testing: FORWARD - SLOW")
    sleep(1)
    servo_motors.forward_slow()
    

testing()