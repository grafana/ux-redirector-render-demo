import os
from flask import Flask,redirect
from multiprocessing import Value
import random

counter = Value('i', 0)

file = open("test-stacks.txt", "r")

with open('test-stacks.txt') as f:
    stacks = f.read().splitlines()

app = Flask(__name__)

@app.route('/')
def hello():
    # out = random.randrange(9)
    # return redirect(stacks[out], code=302)
    with counter.get_lock():
            url = f'https://{stacks[counter.value]}.grafana.net'
            out = counter.value
            counter.value += 1
    return redirect(url, code=302) 

if __name__ == '__app__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)