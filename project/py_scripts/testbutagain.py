from time import sleep
from machine import Pin, PWM
from robot_classes import Servo_Movement

servo_motors = Servo_Movement(20, 18)

def testing():
    print("Testing: FORWARD - SLOW in 3 SECONDS")
    sleep(3)
    print("Testing: FORWARD - SLOW")
    sleep(1)
    servo_motors.forward_slow()
    sleep(1)

    print("Testing: FORWARD in 3 SECONDS")
    sleep(3)
    print("Testing: FORWARD ")
    sleep(1)
    servo_motors.forward()
    sleep(1)

    print("Testing: BACKWARD - SLOW")
    sleep(3)
    print("Testing: BACKWARD - SLOW")
    sleep(1)
    servo_motors.backward_slow()
    sleep(1)

    print("Testing: BACKWARD in 3 SECONDS")
    sleep(3)
    print("Testing: BACKWARD")
    sleep(1)
    servo_motors.backward()
    sleep(1)

    print("Testing: TURN - LEFT in 3 SECONDS")
    sleep(3)
    print("Testing: TURN - LEFT")
    sleep(1)
    servo_motors.turn_left()
    sleep(1)

    print("Testing: TURN - RIGHT in 3 SECONDS")
    sleep(3)
    print("Testing: TURN - RIGHT")
    sleep(1)
    servo_motors.turn_right()
    sleep(1)

testing()