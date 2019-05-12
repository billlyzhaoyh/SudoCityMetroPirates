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

        stepsList = []

        steps = transit_direction[0]['legs'][0]['steps']
        for step in steps:
            distance = step['distance']['value']

            try:
                travelMode = step['transit_details']['line']['vehicle']['type']
            except:
                travelMode = step['travel_mode']


            stepsList.append({'distance': distance, 'travelMode': travelMode})

        print(  stepsList)

        return render_template('result.html', start = startLocation, end = endLocation, stepsList = stepsList)
    else :
        return render_template('index.html', message = "Route not found.")

