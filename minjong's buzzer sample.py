#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################

from car import Car
import RPi.GPIO as GPIO
import time
import threading

class Buzzer() :
    def __init__(self):
        self.buzzer_pin = 8
        GPIO.setmode(GPIO.BOARD)
        self.scale = [261.6, 293.6, 329.6, 349.2, 391.9, 440.0, 493.8, 523.2]
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        self.list1 = [2, 1, 0, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 1, 1, 2, 1, 0]
        self.list2 = [2, 1, 0, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 1, 1, 2, 1, 0]
        self.speed = 1
        self.len = len(self.list1)
        self.current = 0
        self.finish = False

    def song(self):
        P = GPIO.PWM(self.buzzer_pin, 100)
        P.start(5)
        while True :
            if self.current == self.len-1 :
                self.list1.extend(self.list2)
                self.len = len(self.list1)
            P.ChangeFrequency(self.scale[self.list1[self.current]])
            time.sleep(self.speed)
            self.current += 1
            if self.finish == True :
                break

class myCar(object):
    def __init__(self, car_name):
        self.car = Car(car_name)
        self.buzzer = Buzzer()

    def drive_parking(self):
        self.car.drive_parking()
        self.buzzer.finish = True

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        t = threading.Thread(target=self.buzzer.song)
        t.start()
        a = 0
        self.car.steering.center_alignment()
        self.car.accelerator.go_forward(50)
        time.sleep(1)
        self.buzzer.speed = 0.3
        time.sleep(3)
        self.drive_parking()


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
