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
        SPEED = 40
        self.car.steering.center_alignment()
        self.car.accelerator.go_forward(SPEED)
        
        line_detector = self.car.line_detector
        preLine = [0,0,0,0,0]

        while True:
            if self.car.distance_detector.get_distance() < 30: # 장애물 만나면
                print("Obstacle Detected")
                self.car.steering.turn(90-35) # 좌회전
                while line_detector.is_in_line(): # 라인에서 벗어나길 기다린다.
                    continue
                print("out mainline")
                while not line_detector.is_in_line(): # 가이드라인에 들어가길 기다린다.
                    continue
                print("meet guideline")
                self.car.steering.turn(90+35) # 우회전
                while line_detector.is_in_line(): # 가이드라인에서 벗어나길 기다린다.
                    continue
                print("out guideline")
                while not line_detector.is_in_line(): # 라인에 들어가길 기다린다.
                    continue
                print("meet mainline")
            if not line_detector.is_in_line(): # 라인을 벗어나면 (급커브)
                print("Curve")
                self.car.accelerator.stop()
                self.car.steering.turn(90 + preLine[0] * 35 + preLine[4] * -35)
                self.car.accelerator.go_backward(SPEED)
                time.sleep(0.5)
                self.car.accelerator.stop()
                self.car.steering.turn(90 + preLine[0] * -35 + preLine[4] * 35)
                self.car.accelerator.go_forward(SPEED)
                time.sleep(0.5)

            line = line_detector.read_digital()
            degree = [-20 if line[1] else -35, -5 if line[2] else -10, 0, 5 if line[2] else 10, 20 if line[3] else 35]
            degree = [x*y for x, y in zip(line, degree)]
            self.car.steering.turn(90 + sum(degree))

            preLine = line

        self.drive_parking()

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
