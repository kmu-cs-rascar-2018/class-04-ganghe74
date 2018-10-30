#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
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
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        self.car.steering.center_alignment()
        self.car.accelerator.go_forward(100)
        
        line_detector = self.car.line_detector
        
        while line_detector.is_in_line():
            line = line_detector.read_digital()
            degree = [-20 if line[1] else -35, -5 if line[2] else -10, 0, 5 if line[2] else 10, 20 if line[3] else 35]
            degree = [x*y for x, y in zip(line, degree)]
            self.car.steering.turn(90 + sum(degree))

        self.car.drive_parking()

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()