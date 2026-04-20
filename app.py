from flask import Flask, jsonify, render_template
import threading
import random as r
import time

app = Flask(__name__)

data = [0]*6

def task(lb, ub, refreshTime, index):
    global data
    while True:
        data[index] = r.randint(lb, ub)
        time.sleep(refreshTime)

def start_threads():
    configs = [
        (10, 20, 10, 0),
        (-10, 10, 20, 1),
        (-100, 0, 8, 2),
        (0, 20, 12, 3),
        (-40, 40, 16, 4),
        (100, 200, 14, 5),
    ]

    for lb, ub, rt, idx in configs:
        t = threading.Thread(target=task, args=(lb, ub, rt, idx), daemon=True)
        t.start()

start_threads()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
