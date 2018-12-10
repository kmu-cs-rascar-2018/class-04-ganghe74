#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
from BUZZER.Buzzer import Buzzer
import time
import threading


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.buzzer = Buzzer()

    def drive_parking(self):
        self.car.drive_parking()
        self.buzzer.finish = True

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        t = threading.Thread(target=self.buzzer.song)
        t.start()

        INITIAL_SPEED = 30
        SPEED = 30
        self.car.steering.center_alignment()
        self.car.accelerator.go_forward(SPEED)
        
        line_detector = self.car.line_detector
        preLine = [0,0,0,0,0]
        
        count = 0
        count_not_obs = 0

        while count <= 2:

            # 신호등 감지
            rgb = self.car.color_getter.get_raw_data()
            if rgb[0] > 700 and rgb[1] < 400 and rgb[2] < 400:
                print("RED DETECTED!!")
                self.car.accelerator.stop()
                self.buzzer.stop = True
                time.sleep(3)
                self.car.accelerator.go_forward(SPEED)
                time.sleep(0.5)

            # 장애물 감지
            distance = self.car.distance_detector.get_distance()
            if 0 < distance < 30:
                time.sleep(0.1)
                if not self.car.distance_detector.get_distance() < 30: # 장애물을 재확인
                    continue
                print("Obstacle Detected")
                SPEED = 40
                self.car.accelerator.go_forward(SPEED)
                self.buzzer.speed = 20 / SPEED
                self.car.steering.turn(90-35) # 좌회전
                while line_detector.is_in_line():
                    continue
                while not line_detector.is_in_line():
                    continue
                self.car.steering.turn(90+35) # 우회전
                while line_detector.is_in_line():
                    continue
                while not line_detector.is_in_line():
                    continue
            else:
                count_not_obs += 1
                if count_not_obs == 8:
                    if SPEED < 70:
                        SPEED += 1
                        print("SPEED", SPEED)
                        self.car.accelerator.go_forward(SPEED)
                        self.buzzer.speed = 20 / SPEED
                    count_not_obs = 0

            # 라인 벗어날 경우 (급커브)
            if not line_detector.is_in_line():
                print("Curve")
                self.car.accelerator.stop()
                self.car.steering.turn(90 + preLine[0] * 35 + preLine[4] * -35)
                self.car.accelerator.go_backward(SPEED)
                while not line_detector.is_in_line():
                    continue
                time.sleep(0.1)
                self.car.accelerator.stop()
                self.car.accelerator.go_forward(SPEED)

            # 라인 트레이싱
            line = line_detector.read_digital()
            degree = [-20 if line[1] else -35, -5 if line[2] else -10, 0, 5 if line[2] else 10, 20 if line[3] else 35]
            degree = [x*y for x, y in zip(line, degree)]
            self.car.steering.turn(90 + sum(degree))
            preLine = line

            # 정지선 카운트
            if [1,1,1,1,1] == line:
                self.car.steering.center_alignment()
                while line_detector.read_digital() == [1,1,1,1,1]:
                    continue
                count += 1
                print("meet end", count)


        self.drive_parking()

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
