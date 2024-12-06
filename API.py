from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/time')
def get_time():
    now = datetime.now().strftime("%H:%M:%S")
    return jsonify({"current_time": now})

@app.route('/date')
def get_date():
    today = datetime.now().strftime("%Y-%m-%d")
    return jsonify({"current_date": today})

@app.route('/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/status')
def status():
    return jsonify({"status": "API is running smoothly."})

if __name__ == '__main__':
    app.run(debug=True)