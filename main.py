# Import os / sys
import os
import sys
import json
# Import Yeelight Python Lib
from yeelight import Bulb
from yeelight import discover_bulbs

raw_bulbs = discover_bulbs()
bulbs = []
for bulb in raw_bulbs:
    bulbs.append(Bulb(bulb['ip']))
#  Create digital bulbs with their IP
bulb = Bulb("192.168.15.3")

# print(str(sys.argv[1]))   Get args from terminal for future feature to be implemented

# Receives an input from the user and identifies the respective action to take
while True:
    print("Select your action:")
    print("Type 0 and hit enter to exit")
    print("Type 1 and hit enter to turn on")
    print("Type 2 and hit enter to turn off")
    print("Type 3 and hit enter to change the brightness level")
    mode = input('Selected Action: ')

    # For now it only turns the bulb on and off and adjusts the brightness
    if mode == '0':
        exit()
    elif mode == '1':
        bulb.turn_on()
    elif mode == '2':
        bulb.turn_off()
    elif mode == '3':
        print("Type the value of the desired brightness")
        brightness = input('Value Between 1 & 100: ')
        bulb.set_brightness(int(brightness))
    else:
        print("Invalid Action")
    os.system('cls' if os.name == 'nt' else 'clear')