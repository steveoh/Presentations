#!/usr/bin/env python
# * coding: utf8 *
"""
main.py - A script that extract spatial data from an address
"""

import sys

import requests

print('Parameter 0: {}'.format(sys.argv[0]))
print('Parameter 1: {}'.format(sys.argv[1]))
print('Parameter 2: {}'.format(sys.argv[2]))
print('Parameter 3: {}'.format(sys.argv[3]))

KEY = sys.argv[1]
STREET = sys.argv[2]
ZONE = sys.argv[3]

request = requests.get(
    f'https://api.mapserv.utah.gov/api/v1/geocode/{STREET}/{ZONE}',
    timeout=5,
    headers={'referer': 'https://downtown-coding-slc.org'},
    params={'apikey': KEY}
)

response = request.json()

if request.status_code != 200:
    print('address not found', response)

    sys.exit()

match = response['result']
location = match['location']
x = location['x']
y = location['y']

print(f'address is at {x}, {y}')
