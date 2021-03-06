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

import locale
import sys
from os import getenv

import requests
from colorama import Fore, init
from dotenv import load_dotenv

locale.setlocale(locale.LC_ALL, '')
load_dotenv()
init(autoreset=True)
KEY = getenv('AGRC_API_KEY')

request = requests.get(
    'https://api.mapserv.utah.gov/api/v1/geocode/123 south main street/slc',
    timeout=5,
    headers={'referer': 'https://downtown-coding-slc.org'},
    params={'apikey': KEY}
)

response = request.json()

if request.status_code != 200:
    print('address not found')

    sys.exit()

match = response['result']
location = match['location']
x = location['x']
y = location['y']

print(f'address location: {Fore.MAGENTA}{x}, {y}\n')

request = requests.get(
    'https://api.mapserv.utah.gov/api/v1/search/sgid10.boundaries.counties/name',
    timeout=5,
    headers={'referer': 'https://downtown-coding-slc.org'},
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

print(f'address is in {Fore.CYAN}{name}{Fore.RESET} county')

request = requests.get(
    'https://api.mapserv.utah.gov/api/v1/search/sgid10.cadastre.landownership/owner',
    timeout=5,
    headers={'referer': 'https://downtown-coding-slc.org'},
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

print(f'the land is owned by a {Fore.CYAN}{owner}{Fore.RESET} entity')

request = requests.get(
    'https://api.mapserv.utah.gov/api/v1/search/sgid10.cadastre.parcels_saltlake_lir/total_mkt_value,bldg_sqft,floors_cnt,built_yr',
    timeout=5,
    headers={'referer': 'https://downtown-coding-slc.org'},
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
    f'the structure was built in {Fore.CYAN}{year_built}{Fore.RESET} worth {Fore.GREEN}{market_value}{Fore.RESET} with {Fore.YELLOW}{square_feet:,}{Fore.RESET} square feet across {Fore.RED}{number_of_floors}{Fore.RESET} floors'
)

request = requests.get(
    'https://api.mapserv.utah.gov/api/v1/search/sgid10.raster.usgs_dem_10meter/feet',
    timeout=5,
    headers={'referer': 'https://downtown-coding-slc.org'},
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

print(f'the elevation is {Fore.CYAN}{elevation:,.2f}{Fore.RESET} feet')
