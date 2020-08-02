import os, json
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
# Returns all the available lights on the network
@app.route('/bulbsList')
@cross_origin()
def bulbsList():
  return str(raw_bulbs)

# Turns all the lights on
@app.route('/on')
@cross_origin()
def on():
    for bulb in bulbs:
        bulb.turn_on()
    return {}

# Turns all the lights off
@app.route('/off')
@cross_origin() 
def off():
    for bulb in bulbs:
        bulb.turn_off()
        return {}

# Toggles all the lights
@app.route('/toggle')
@cross_origin() 
def toggle():
    for bulb in bulbs:
        bulb.toggle()
        return {}

# Sets the brightness of all the light based on the header property called brightness
@app.route('/brightness', methods=["POST"] )
@cross_origin() 
def brightness():
    b = int(request.headers.get_all('brightness')[0])
    for bulb in bulbs:
        bulb.set_brightness(b)
        return {}

# Blinks all the light in a green color once 
@app.route('/flow')
@cross_origin() 
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