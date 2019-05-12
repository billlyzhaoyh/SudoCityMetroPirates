from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from evaluate_route import transit_cost,drive_cost
from vehicle_footprints import VEHICLE_FOOTPRINTS

import googlemaps
import json

app = Flask(__name__)

@app.route('/')
def homepage():
     return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    license_plate='YA52 MPV'
    startLocation = request.form.get('start')
    endLocation = request.form.get('end')

    if startLocation is not None and endLocation is not None :

        now = datetime.now()

        modes = ['driving','walking','bicycling','transit']
        gmaps = googlemaps.Client(key='AIzaSyB6iXjFokaVryqlrrv7TzD_sUruUbirE4A')
        drive = gmaps.directions(startLocation,endLocation,mode=modes[0],departure_time=now,region='uk')
        walk=gmaps.directions(startLocation,endLocation,mode=modes[1],departure_time=now,region='uk')
        bicycle=gmaps.directions(startLocation,endLocation,mode=modes[2],departure_time=now,region='uk')
        transit=gmaps.directions(startLocation,endLocation,mode=modes[3],departure_time=now,region='uk')

        car_distance = drive[0]['legs'][0]['distance']['value'];
        car_time = drive[0]['legs'][0]['duration']['text'];

        #carbon_drive,tree_drive=drive_cost(car_distance, license_plate)
        carbon_drive=0
        tree_drive=0

        walking_distance = walk[0]['legs'][0]['distance']['value'];
        walking_time = walk[0]['legs'][0]['duration']['text'];

        cycling_distance = bicycle[0]['legs'][0]['distance']['value'];
        cycling_time = bicycle[0]['legs'][0]['duration']['text'];

        



        
        stepsList = []

        steps = transit[0]['legs'][0]['steps']
        for step in steps:
            distance = step['distance']['value']

            try:
                travelMode = step['transit_details']['line']['vehicle']['type']
            except:
                travelMode = step['travel_mode']


            stepsList.append({'distance': distance, 'travelMode': travelMode})

        transit_distance = transit[0]['legs'][0]['distance']['value'];
        transit_time = transit[0]['legs'][0]['duration']['text'];

        carbon_transit,tree_transit=transit_cost(stepsList, VEHICLE_FOOTPRINTS)

        result = {
            'driving': {'distance': car_distance, 'time': car_time, 'co2': carbon_drive,'tree':tree_drive},
            'transit': {'distance': transit_distance, 'time': transit_time, 'co2': carbon_transit,'tree':tree_transit},
            'cycling': {'distance': cycling_distance, 'time': cycling_time, 'co2': 0},
            'walking': {'distance': walking_distance, 'time': walking_time, 'co2': 0}
        }
        return render_template('result.html', start = startLocation, end = endLocation, result = result)
    else:
        return render_template('index.html', message = "Route not found.")

