import servomotor
import socket
import RPi.GPIO as GPIO
from PCA9685 import PCA9685
import time

host = '192.168.2.16'
port = 55555
buffsize = 1024
x = 90
y = 40
pwm = PCA9685()
pwm.setPWMFreq(50)
pwm.setRotationAngle(1,x)
pwm.setRotationAngle(0,y)
mess = ''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print("Server is listening !!!")

while True:
  client, address = server.accept()
  print("Connected with {}".format(str(address)))
  mess = client.recv(buffsize).decode("utf-8")
  command = mess
  if command == 'R':
    if x > 0:
      x -= 5
      print("RIGHT")
      pwm.setRotationAngle(1,x)
      time.sleep(0.1)
    else:
      print("Out of Angle")
  if command == 'L':
    if x < 180:
      x += 5
      print("LEFT")
      pwm.setRotationAngle(1,x)
      time.sleep(0.1)
    else:
      print("Out of Angle")
  if command == 'D':
    if y < 80:
      y += 5
      print("DOWN")
      pwm.setRotationAngle(0,y)
      time.sleep(0.1)
    else:
      print("Out of Angle")
  if command == 'U':
    if y > 0:
      y -= 5
      print("UP")
      pwm.setRotationAngle(0,y)
      time.sleep(0.1)
    else:
      print("Out of Angle")
