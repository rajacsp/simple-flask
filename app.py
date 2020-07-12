import os
from flask import Flask, render_template, make_response
import sys
import logging
from time import time
import json
from random import random

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():

    countries = [
        ["India", "Asia"],
        ["Canada", "North America"]
    ]

    return render_template('index.html', countries=countries)


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    Temperature = random() * 100
    Humidity = random() * 55

    data = [time() * 1000, Temperature, Humidity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


@app.route('/highchart', methods=["GET", "POST"])
def main():
    return render_template('graph.html')
