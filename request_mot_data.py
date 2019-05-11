"""
Example Python script for getting MOT data (carbon emission in particular)
from the ``vehicleenquiry.service.gov.uk`` website.
"""
import json

# Third-party libraries; these will need to be installed separately
import requests
from six.moves import urllib


#: URL template for the ``dvlasearch`` POST requests
DVLASEARCH_URL_TEMPLATE = (
    'https://dvlasearch.appspot.com/DvlaSearch?apikey={}&licencePlate={}'
)

#: POST request header for the ``dvlasearch.co.uk`` website
DVLASEARCH_HEADERS = {'accept': 'application/json'}

#: JSON name
CO2_EMISSIONS = 'co2Emissions'

#: Unit suffix of the CO2 field of the JSON response
CO2_SUFFIX = ' g/km'


def get_carbon_emission(licence_plate, api_key):
    """
    Return the carbon emission for the vehicle with the given licence plate.

    Parameters
    ---------
    licence_plate : str
        Licence plate of the vehicle
    api_key : str
        API token used for the ``dvlasearch.co.uk`` website.

    Returns
    -------
    co2_emission : float
        CO2 emission in units of g/km

    Raises
    ------
    KeyError
        If the API token or the licence plate is invalid.
    """
    # Replace special characters in the licence plate string
    licence_plate = urllib.parse.quote(licence_plate)
    # Normalise API key string TODO
    full_url = DVLASEARCH_URL_TEMPLATE.format(api_key, licence_plate)
    response = requests.get(full_url, headers=DVLASEARCH_HEADERS).text
    emission_g_km = json.loads(response)[CO2_EMISSIONS]
    return float(emission_g_km.replace(CO2_SUFFIX, ''))

