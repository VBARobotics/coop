import gpiozero
from time import sleep
RELAY_PIN = 18

# Triggered by the output pin going high: active_high=True
# Initially off: initial_value=False

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=True, initial_value=False)

relay.off() # switch off

relay.on() # switch on

print(relay.value) # see if on or off
