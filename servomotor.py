import time
import RPi.GPIO as GPIO
from PCA9685 import PCA9685

x = 0
y = 0

def setup():
	global pwm
	pwm = PCA9685()
	pwm.setPWMFreq(50)
	pwm.setRotationAngle(1,90)
	pwm.setRotationAngle(0,40)
	print("Set up servo done !")
def left():
	global x
	if x >= 0 and x <= 180:
		x += 10
		pwm.setRotationAngle(1,x)
		print("move left !!")
def right():
        global x
        if x >= 0 and x <= 180:
                x -= 10
                pwm.setRotationAngle(1,x)
                print("move right !!")
def up():
	global y
	if y >= 0 and y <= 80:
		y -= 10
		pwm.setRotationAngle(0,y)
		print("move up")
def down():
        global y
        if y >= 0 and y <= 80:
                y += 10
                pwm.setRotationAngle(0,y)
                print("move down")
