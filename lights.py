from gpiozero import LED
from time import sleep
lights = LED(20)
lights.on()
sleep(5)
lights.off()
