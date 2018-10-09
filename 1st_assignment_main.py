# 완성되지 않은 코드입니다

#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################
from car import Car
import time

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        self.car.steering.center_alignment()
        for speed, distance in [[30,15], [50,20], [70,25]]:
            self.car.accelerator.go_forward(speed)
            while self.car.distance_detector.get_distance() > distance:
                continue
            self.car.accelerator.stop()
            self.car.accelerator.go_backward(speed)
            time.sleep(4)
            self.car.accelerator.stop()
        self.car.drive_parking()

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()