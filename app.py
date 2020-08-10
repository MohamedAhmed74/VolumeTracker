from flask import Flask, render_template

VolumeTracker = Flask(__name__)


@VolumeTracker.route('/')
def index():
    return render_template('index.html')
