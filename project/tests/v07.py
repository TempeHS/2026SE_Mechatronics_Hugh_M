
from robot_classes import ULTRAKILL, Servo_Movement
import time

servo_motors = Servo_Movement(20, 18)
ultrasonic = ULTRAKILL([0, 0, 0, 0], [0, 0, 1, 0])

sensor_output_fr = ultrasonic.dist_front
sensor_output_si = ultrasonic.dist_side

def ultrasonic_testing():
    
    while True:
        print(f"OUTPUTS//FRONT: {sensor_output_fr}")
        print(f"OUTPUTS//SIDE: {sensor_output_si}")
        time.sleep(0.5)
        if ultrasonic.dist_front() < 0: 
            servo_motors.self_destruct()
            servo_motors.turn_left()
            print("WALL DETECTED: TURNING...")
        else:
            servo_motors.forward_slow()


ultrasonic_testing()