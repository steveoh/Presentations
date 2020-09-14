#!/usr/bin/env python
# * coding: utf8 *
'''
main.py - A script that extracts spatial data for an address
'''

#: pros
#: - no documentation required, run the script and it does what you last left it to do
#: cons
#: - hard coded values
#: - difficult to share - api key is unique to user
#: - dependencies are not easily installable

from dotenv import load_dotenv
import requests
import locale
from os import getenv
import sys

locale.setlocale(locale.LC_ALL, '')
load_dotenv()
KEY = getenv('AGRC_API_KEY')

request = requests.get(
    'http://api.mapserv.utah.gov/api/v1/geocode/123 south main street/slc', timeout=5, params={'apikey': KEY}
)

response = request.json()

if request.status_code != 200:
    print('address not found')

    sys.exit()

match = response['result']
location = match['location']
x = location['x']
y = location['y']

print(f'address is at {x}, {y}')

request = requests.get(
    'http://api.mapserv.utah.gov/api/v1/search/sgid10.boundaries.counties/name',
    timeout=5,
    params={
        'apikey': KEY,
        'geometry': f'point:[{x},{y}]'
    }
)

response = request.json()

if request.status_code != 200:
    print('county not found')

    sys.exit()

result = response['result'][0]
name = result['attributes']['name']

print(f'address is in {name} county')

request = requests.get(
    'http://api.mapserv.utah.gov/api/v1/search/sgid10.cadastre.landownership/owner',
    timeout=5,
    params={
        'apikey': KEY,
        'geometry': f'point:[{x},{y}]'
    }
)

response = request.json()

if request.status_code != 200:
    print('owner not found')

    sys.exit()

result = response['result'][0]
owner = result['attributes']['owner']

print(f'the land is owned by a {owner} entity')

request = requests.get(
    'http://api.mapserv.utah.gov/api/v1/search/sgid10.cadastre.parcels_saltlake_lir/total_mkt_value,bldg_sqft,floors_cnt,built_yr',
    timeout=5,
    params={
        'apikey': KEY,
        'geometry': f'point:[{x},{y}]'
    }
)

response = request.json()

if request.status_code != 200:
    print('parcel not found')

    sys.exit()

result = response['result'][0]
market_value = locale.currency(float(result['attributes']['total_mkt_value']), grouping=True)
square_feet = int(result['attributes']['bldg_sqft'])
number_of_floors = int(result['attributes']['floors_cnt'])
year_built = result['attributes']['built_yr']

print(
    f'the structure was built in {year_built} worth {market_value} with {square_feet:,} square feet across {number_of_floors} floors'
)

request = requests.get(
    'http://api.mapserv.utah.gov/api/v1/search/sgid10.raster.usgs_dem_10meter/feet',
    timeout=5,
    params={
        'apikey': KEY,
        'geometry': f'point:[{x},{y}]'
    }
)

response = request.json()

if request.status_code != 200:
    print('elevation not found')

    sys.exit()

result = response['result'][0]
elevation = float(result['attributes']['feet'])

print(f'the elevation is {elevation:,.2f} feet')
