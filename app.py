import os
from flask import Flask,redirect
from multiprocessing import Value
import random

# Initiate a counter named 'counter'
counter = Value('i', 0)

# Open a 'test-stacks.txt' file with a list of test stacks
file = open("test-stacks.txt", "r")

# Read the test stacks file into a list called 'stacks'
with open('test-stacks.txt') as f:
    stacks = f.read().splitlines()

# Start the app
app = Flask(__name__)

# If the url has path '/' (no path)
@app.route('/')
def hello():
    with counter.get_lock():
            # Create a string called 'url' as a connection of 'https://', stack name and '.grafana.net'
            url = f'https://{stacks[counter.value]}.grafana.net/d/f5ebfb7e-f3ec-45b2-acb1-d3e64539725d/login-service-dashboard?orgId=1&from=now-7d&to=now'
            # Increase counter by 1
            counter.value += 1
    # Redirect to the url
    print("A participant was redirected to", url)
    return redirect(url, code=302) 

if __name__ == '__app__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
