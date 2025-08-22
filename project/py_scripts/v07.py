import time
from classes_pt2 import Servo_Movement, Ultrasonic

servo_motors = Servo_Movement(20, 18)
ultrasonic = Ultrasonic([0, 0, 0, 0], [0, 0, 1, 0])

def ultrasonic_testing():
    
    while True:
        print(f"OUTPUT//FRONT: {ultrasonic.dist_front()}")
        time.sleep(0.5)
        if ultrasonic.dist_front() < 40: 
            servo_motors.self_destruct()
            time.sleep(0.5)
            print("WALL DETECTED: TURNING...")
            servo_motors.turn_left()
            time.sleep(0.9)
            
        else:
            servo_motors.forward_slow()


ultrasonic_testing()
