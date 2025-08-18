from machine import Pin, PWM
from project.lib.servo import Servo
import time
from project.lib.PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

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
        timevar = int(0)

        while timevar < 1: 
            self.right_wheel.set_duty(1300)
            self.left_wheel.set_duty(1700)
            timevar = int(timevar + 1)
            time.sleep(0)
            self.right_wheel.set_duty(1500)
            self.left_wheel.set_duty(1500)
            print(timevar)
            time.sleep(1.4)
            if self.right_wheel.set_duty(1200) and self.left_wheel.set_duty(1800):
                self.right_wheel.set_duty(1500)
                self.left_wheel.set_duty(1500)
        

    def turn_left(self):
        if self.__debug:
            print("Servo moving: TURNING - LEFT")

        timevar = int(0)

        while timevar < 1: 
            self.right_wheel.set_duty(1800)
            self.left_wheel.set_duty(1200)
            timevar = int(timevar + 1)
            time.sleep(0)
            self.right_wheel.set_duty(1500)
            self.left_wheel.set_duty(1500)
            print(timevar)
            time.sleep(1.4)
            if self.right_wheel.set_duty(1800) and self.left_wheel.set_duty(1200):
                self.right_wheel.set_duty(1500)
                self.left_wheel.set_duty(1500)

    def backward(self):
        if self.__debug:
            print("Servo moving: BACKWARD")
        self.left_wheel.set_duty(500)
        self.right_wheel.set_duty(2500)

    def backward_slow(self):
        if self.__debug:
            print("Servo moving: BACKWARD - SLOW")
        self.left_wheel.set_duty(1200)
        self.right_wheel.set_duty(1800)


    def self_destruct(self):
        # this is literally just the stop function 
        #its just named that because i thought it was funny
        if self.__debug:
            print("Servo: STOPPING")
        self.left_wheel.set_duty(1500)
        self.right_wheel.set_duty(1500)

class ULTRAKILL:
    def __init__ (self, range_a, range_b, debug = False):
        self.__range_a = range_a
        self.__range_b = range_b
        self.__debug = debug

    def distance(self):
        self.__range_a.distance_mm (id=[0, 0, 0, 0])
        self.__range_b.distance_mm (id=[1, 0, 0, 0])

    def dist_front(self):
        return int(self.__range_b.distance_mm)

    def dist_side(self):
        return int(self.__range_a.distance_mm)

class Colour_sensor:
    def __init__ (self,   debug = False):
        ...