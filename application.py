from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

import googlemaps
import json

app = Flask(__name__)

@app.route('/')
def homepage():
     return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    startLocation = request.form.get('start')
    endLocation = request.form.get('end')

    if startLocation is not None and endLocation is not None :

        now = datetime.now()

        gmaps = googlemaps.Client(key='AIzaSyB6iXjFokaVryqlrrv7TzD_sUruUbirE4A')
        transit_direction = gmaps.directions(startLocation,
                                             endLocation,
                                             mode="transit",
                                             departure_time=now)

        print(transit_direction.routes)

        return json.dumps(transit_direction)
    else :
        return 'FAIL'

