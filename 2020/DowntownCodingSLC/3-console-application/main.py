#!/usr/bin/env python
# * coding: utf8 *
"""
Utility Provider

Usage:
  main.py utilities at <street> <zone> --key <api_key> [[--gas --water --electric] | --all]

Options:
  <street>   a quoted street address
  <zone>     a Utah zip code or city
  <api_key>  a developer.api.mapserv.utah.gov api key
"""

#: pros
#: - script arguments are documented, descriptive, and simple to understand
#: cons
#: - dependencies are still not easily installable

import json

import requests
from colorama import Fore, init
from docopt import docopt

init(autoreset=True)


def get_coordinates(street, zone, key):
    '''geocodes an address address
    returns a coordinate tuple
    '''

    request = requests.get(
        f'https://api.mapserv.utah.gov/api/v1/geocode/{street}/{zone}',
        timeout=5,
        headers={'referer': 'https://downtown-coding-slc.org'},
        params={'apikey': key}
    )

    response = request.json()

    if request.status_code != 200:
        print('address not found', response)

        return None, None

    match = response['result']
    location = match['location']
    x = location['x']
    y = location['y']

    print(f'address location: {Fore.MAGENTA}{x}, {y}\n')

    return x, y


def arcgis_online_query(service_url, where, geometry, outfields):
    request = requests.get(
        service_url,
        # timeout=15,
        params={
            'where': where,
            'geometry': json.dumps(geometry),
            'geometryType': 'esriGeometryPoint',
            'spatialRel': 'esriSpatialRelIntersects',
            'outFields': ','.join(outfields),
            'returnGeometry': False,
            'f': 'json'
        }
    )

    return request.json()


def get_fiber_providers(x, y):
    response = arcgis_online_query(
        'https://services1.arcgis.com/99lidPhWCzftIe9K/arcgis/rest/services/BroadbandService/FeatureServer/0/query',
        'transtech=50', {
            'x': x,
            'y': y,
            'spatialReference': {
                'wkid': 26912
            }
        }, ['UTProvCode']
    )

    providers = [provider['attributes']['UTProvCode'] for provider in response['features']]

    print(f'Fiber internet is available from {Fore.CYAN}{", ".join(providers)}')


def get_gas_provider(x, y):
    response = arcgis_online_query(
        'https://services1.arcgis.com/99lidPhWCzftIe9K/arcgis/rest/services/UtahNaturalGasServiceAreas_Approx/FeatureServer/0/query',
        None, {
            'x': x,
            'y': y,
            'spatialReference': {
                'wkid': 26912
            }
        }, ['Name']
    )

    providers = [provider['attributes']['Name'] for provider in response['features']]

    print(f'Gas is provided by {Fore.CYAN}{", ".join(providers)}')


def get_electricity_provider(x, y):
    response = arcgis_online_query(
        'https://services1.arcgis.com/99lidPhWCzftIe9K/arcgis/rest/services/ElectricalService/FeatureServer/0/query',
        None, {
            'x': x,
            'y': y,
            'spatialReference': {
                'wkid': 26912
            }
        }, ['PROVIDER']
    )

    providers = [provider['attributes']['PROVIDER'] for provider in response['features']]

    print(f'Electricity is provided by {Fore.CYAN}{", ".join(providers)}')


def get_water_provider(x, y):
    response = arcgis_online_query(
        'https://services1.arcgis.com/99lidPhWCzftIe9K/arcgis/rest/services/RetailCulinaryWaterServiceAreas/FeatureServer/0/query',
        None, {
            'x': x,
            'y': y,
            'spatialReference': {
                'wkid': 26912
            }
        }, ['DWNAME']
    )

    providers = [provider['attributes']['DWNAME'] for provider in response['features']]

    print(f'Water is provided by {Fore.CYAN}{", ".join(providers)}')


if __name__ == '__main__':
    options = docopt(__doc__)

    print(f'{Fore.YELLOW}{options}')

    x, y = get_coordinates(options['<street>'], options['<zone>'], options['<api_key>'])
    get_fiber_providers(x, y)

    if options['--all'] or options['--gas']:
        get_gas_provider(x, y)
    if options['--all'] or options['--electric']:
        get_electricity_provider(x, y)
    if options['--all'] or options['--water']:
        get_water_provider(x, y)
