from car import Car
import RPi.GPIO as GPIO
import time

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