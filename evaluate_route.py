"""
Evaluate a route based on its carbon footprint.
"""
from vehicle_footprints import DEFAULT_FOOTPRINT



def step_cost(step, vehicle_footprints):
    """
    Return the carbon footprint of a single step of a route in grams.
    """
    TRAVEL_MODE = 'travel_mode'

    if step[TRAVEL_MODE] == 'WALKING':
        vehicle_type = step[TRAVEL_MODE]
    elif step[TRAVEL_MODE] == 'TRANSIT':
        vehicle_type = step['transit_details']['line']['vehicle']['type']
    else:
        # Handle unknown vehicle types for robustness
        vehicle_type = 'UNKNOWN'

    per_km_cost = vehicle_footprints.get(vehicle_type, DEFAULT_FOOTPRINT)
    # Convert meters to kilometers
    distance = 1e3 * float(step['distance']['value'])
    # Ignore all other available pieces of data (e.g. duration) for now
    return per_km_cost * distance


def leg_cost_by_steps(leg, vehicle_footprints):
    """
    Returns
    -------
    leg_costs : list of floats
    """
    return [step_cost(step, vehicle_footprints) for step in leg['steps']]


def leg_cost(leg, vehicle_footprints):
    """
    Return the carbon footprint of a single leg of a route in grams.
    """
    return sum(step_cost(step, vehicle_footprints) for step in leg['steps'])



def route_cost(route, vehicle_footprints):
    """
    Return the carbon footprint of the given route.

    Parameters
    ----------
    route : dict
    vehicle_footprints : dict(str, float)
        Carbon footprint of different modes of transportation in units of
        g/km.

    Returns
    -------
    cost : float
        The carbon footprint in units of grams.
    """
    return sum(leg_cost(leg, vehicle_footprints) for leg in route['legs'])

