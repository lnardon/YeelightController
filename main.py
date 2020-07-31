# Import os
import os
# Import Yeelight Python Lib
from yeelight import Bulb

#  Create digital bulbs with their IP
bulb = Bulb("192.168.15.3")

# Receives an input from the user and identifies the respective action to take
while True:
    print("Select your action:")
    print("Type 0 and hit enter to exit")
    print("Type 1 and hit enter to turn on")
    print("Type 2 and hit enter to turn off")
    print("Type 3 and hit enter to change the brightness level")
    mode = input('Selected Action: ')

    # For now it only turns on and off the bulb
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