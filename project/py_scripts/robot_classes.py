from machine import Pin, PWM
import time 
from time import sleep
from servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic


class Servo_Movement:
    def __init__(self, servo_left_pin, servo_right_pin, debug = False):
        self.servo_left_pin = servo_left_pin
        self.left_wheel = Servo(PWM(Pin(servo_left_pin)))
        self.servo_right_pin = servo_right_pin
        self.right_wheel = Servo(PWM(Pin(servo_right_pin)))
        self.__debug = debug

    def forward(self):
        if self.__debug:
            print("Servo moving: FORWARD")
        self.left_wheel.set_duty(2500)
        self.right_wheel.set_duty(500)

    def forward_slow(self):
        if self.__debug:
            print("Servo moving: FORWARD - SLOW")
        self.left_wheel.set_duty(1700)
        self.right_wheel.set_duty(1300)

    def turn_right(self):
        if self.__debug:
            print("Servo moving: TURNING - RIGHT")

        self.left_wheel.set_duty(1700)
        self.right_wheel.set_duty(1700)

#        self.right_wheel.set_angle(0)
#        time.sleep(1)
#        self.right_wheel.set_angle(90)
#        time.sleep(2)

    def turn_left(self):
        if self.__debug:
            print("Servo moving: TURNING - LEFT")

        self.left_wheel.set_duty(1300)
        self.right_wheel.set_duty(1300)

#        self.left_wheel.set_angle(180)
#        time.sleep(1)
#        self.left_wheel.set_angle(90)
#        time.sleep(2)

    def backward(self):
        if self.__debug:
            print("Servo moving: BACKWARD")
        self.left_wheel.set_duty(500)
        self.right_wheel.set_duty(2500)

    def backward_slow(self):
        if self.__debug:
            print("Servo moving: BACKWARD - SLOW")
        self.left_wheel.set_duty(1300)
        self.right_wheel.set_duty(1700)


    def self_destruct(self):
        # this is literally just the stop function 
        #its just named that because i thought it was funny
        if self.__debug:
            print("Servo: STOPPING")
        self.left_wheel.set_duty(1500)
        self.right_wheel.set_duty(1500)

servo_motors = Servo_Movement(20, 18)

def movement_testing():
    print("Testing: FORWARD - SLOW in 3 SECONDS")
    sleep(3)
    print("Testing: FORWARD - SLOW")
    sleep(1)
    servo_motors.forward_slow()
    sleep(1)
    print("INTERMISSION")

    print("Testing: BACKWARD - SLOW")
    sleep(3)
    print("Testing: BACKWARD - SLOW")
    sleep(1)
    servo_motors.backward_slow()
    sleep(1)
    print("INTERMISSION")

    print("Testing: TURN - LEFT in 3 SECONDS")
    sleep(3)
    print("Testing: TURN - LEFT")
    sleep(1)
    servo_motors.turn_left()
    sleep(1)
    print("INTERMISSION")

    print("Testing: TURN - RIGHT in 3 SECONDS")
    sleep(3)
    print("Testing: TURN - RIGHT")
    sleep(1)
    servo_motors.turn_right()
    sleep(1)
    print("INTERMISSION")

    print("STOPPING")
    sleep(1)
    servo_motors.self_destruct


class ULTRAKILL:
    def __init__ (self, range_a, range_b, debug = False):
        self.__range_a = range_a
        self.__range_b = range_b
        self.__debug = debug

    def distance(self):
        self.__range_a.distance_mm (id=[0, 0, 0, 0])
        self.__range_b.distance_mm (id=[0, 0, 1, 0])

    def dist_front(self):
        return int(self.__range_b.distance_mm)

    def dist_side(self):
        return int(self.__range_a.distance_mm)


sensor_output_fr = ULTRAKILL.dist_front
sensor_output_si = ULTRAKILL.dist_side
sensor_output_both = sensor_output_fr, sensor_output_si

def ultrasonic_testing():
    while True:
        servo_motors.forward()
        print(f"Sensor Outputs: {sensor_output_both}")
    if 




class Colour_Sensor:
    def __init__ (self,   debug = False):
        ...
