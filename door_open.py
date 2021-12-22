from gpiozero import Motor
from time import sleep

door = Motor(forward=18, backward=17)

door.stop()
door.forward()
sleep(30)
door.stop()
