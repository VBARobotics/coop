from gpiozero import Motor, LED
from time import sleep

door = Motor(forward=17, backward=18)
# red = LED(19)
# green = LED(20)

door.stop()
# red.blink(on_time=0.5,off_time=0.5)
door.forward()
sleep(5)
# red.off()
# green.blink()
door.backward()
sleep(5)
# green.off()
door.stop()