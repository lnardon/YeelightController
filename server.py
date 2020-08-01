import os
from flask import Flask, request
from yeelight import *

app = Flask(__name__)

# Clears the terminal every load
os.system('cls' if os.name == 'nt' else 'clear')

# Gets all the lights in the network
raw_bulbs = discover_bulbs()
bulbs = []
for bulb in raw_bulbs:
    # Creates digital bulbs with their IP
    bulbs.append(Bulb(bulb['ip']))


# API_ROUTES
# LAN ONLY
# Turns all the lights on
@app.route('/on')
def on():
    for bulb in bulbs:
        bulb.turn_on()

# Turns all the lights off
@app.route('/off')
def off():
    for bulb in bulbs:
        bulb.turn_off()

# Sets the brightness of all the light based on the header property called brightness 
@app.route('/brightness', methods=["POST"] )
def brightness():
    b = int(request.headers.get_all('brightness')[0])
    for bulb in bulbs:
        bulb.set_brightness(b)

# Blinks all the light in a green color once 
@app.route('/flow')
def flow():
    transitions = [HSVTransition(120, 100, duration=75)]

    flow = Flow(
        count=1,
        transitions=transitions
    )
    for bulb in bulbs:
        bulb.start_flow(flow)

app.run()