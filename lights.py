#!/usr/bin/python

import gpiozero
from time import sleep
RELAY_PIN = 18

# Triggered by the output pin going high: active_high=True
# Initially off: initial_value=False

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

relay.off() # switch off
sleep(1)
relay.on() # switch on
sleep(2)

print(relay.value) # see if on or off
