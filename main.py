# Import Yeelight Python Lib
from yeelight import Bulb

#  Create digital bulbs with their IP
bulb = Bulb("192.168.15.3")

# Receives an input from the user and identifies the respective action to take
print("Select your action:")
print("Type 1 and hit enter no turn on")
print("Type 2 and hit enter no turn off")
mode = input('Selected Action: ')

# For now it only turns on and off the bulb
if mode == '1':
    bulb.turn_on()
elif mode == '2':
    bulb.turn_off()
else:
    print("Action Ignored")