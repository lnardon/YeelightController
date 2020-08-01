import os
from flask import Flask, request
from flask_cors import cross_origin
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
@cross_origin()
@app.route('/on')
def on():
    for bulb in bulbs:
        bulb.turn_on()
    return {}

# Turns all the lights off
@app.route('/off')
def off():
    bulbs[1].turn_off()
    for bulb in bulbs:
        bulb.turn_off()
        return {}

# Sets the brightness of all the light based on the header property called brightness
@cross_origin() 
@app.route('/brightness', methods=["POST"] )
def brightness():
    b = int(request.headers.get_all('brightness')[0])
    for bulb in bulbs:
        bulb.set_brightness(b)
        return {}

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
    return {}

app.run(host= '0.0.0.0')