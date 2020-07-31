from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "id": "Flask ID"
    }

app.run()