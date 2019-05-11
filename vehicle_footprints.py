#: Carbon footprint of unknown vehicles in g/km
DEFAULT_FOOTPRINT = 200.0

#: CO2 emission of various types of vehicles in g/km.
#: Expected vehicle types are listed here:
#: developers.google.com/maps/documentation/directions/intro#VehicleType
VEHICLE_FOOTPRINTS = {
    'BUS': 68.0,
    'RAIL': 14.0,
    'METRO_RAIL': 43.0,
    'SUBWAY': 43.0,
    # TRAM
    'MONORAIL': 14.0,
    'HEAVY_RAIL': 14.0,
    'COMMUTER_TRAIN': 14.0,
    'HIGH_SPEED_TRAIN': 14.0,
    'LONG_DISTANCE_TRAIN': 14.0,
    'BUS': 68.0,
    'INTERCITY_BUS': 68.0,
    # TROLLEYBUS
    # SHARE_TAXI
    # FERRY
    # CABLE_CAR
    # GONDOLA_LIFT
    # FUNICULAR
    'OTHER': DEFAULT_FOOTPRINT,
    # 'walking' is here too for convenience
    'WALKING': 0.0,
}

