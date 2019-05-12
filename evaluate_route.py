"""
Evaluate a route based on its carbon footprint.
"""
from vehicle_footprints import DEFAULT_FOOTPRINT
from request_mot_data import get_carbon_emission



def transit_cost(steplist, vehicle_footprints):
    """
    Return the carbon footprint of a single step of a route in grams.
    """
    total_footprint=0
    carbon_foronetree=60
    for leg in steplist:
        leg_type = leg['travelMode']
        per_km_cost = vehicle_footprints.get(leg_type, DEFAULT_FOOTPRINT)
        distance = 1e-3 * leg['distance']
        footprint=distance*per_km_cost
        total_footprint=total_footprint+footprint
    total_footprint=round(total_footprint)
    days_to_absorb=round(total_footprint/carbon_foronetree)
    return total_footprint,days_to_absorb

def drive_cost(distance, licence_plate):
    """
    Return the carbon footprint of a single step of a route in grams.
    """
    #default api key
    api='xGJSAEmF0FMRVlFs'
    per_km_cost=get_carbon_emission(licence_plate, api)
    total_footprint=per_km_cost*distance*1e-3
    carbon_foronetree=60
    total_footprint=round(total_footprint)
    days_to_absorb=round(total_footprint/carbon_foronetree)
    return total_footprint,days_to_absorb


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

