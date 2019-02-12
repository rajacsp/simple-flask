import os
from flask import Flask, render_template, g
import sys
import logging


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
