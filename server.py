import servomotor
import socket
import RPi.GPIO as GPIO
from PCA9685 import PCA9685
import time

host = '172.20.10.7'
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
  print(mess)
  command = mess
  print("X: {}".format(x))
  print("Y: {}".format(y))
  if x > 0 and x < 180:
    if command == 'R':
      x -= 5
      print("RIGHT")
    elif command == 'L':
      x += 5
      print("LEFT")
    pwm.setRotationAngle(1,x)
    time.sleep(0.1)
  if y > 0 and y < 80:
    if command == 'D':
      y += 5
      print("DOWN")
    elif command == 'U':
      y -= 5
      print("UP")
    pwm.setRotationAngle(0,y)
    time.sleep(0.1)
