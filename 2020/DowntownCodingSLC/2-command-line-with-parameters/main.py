#!/usr/bin/env python
# * coding: utf8 *
"""
main.py - A script that extract spatial data from an address
"""

#: pros
#: - hard coded dependencies removed
#: - script is more generic and can geocode any address input with any api key
#: cons
#: - command line arguments are not documented or discoverable without reading the code
#: - dependencies are still not easily installable

import sys

import requests
import psycopg2

print('Parameter 0: {}'.format(sys.argv[0]))
print('Parameter 1: {}'.format(sys.argv[1]))
print('Parameter 2: {}'.format(sys.argv[2]))
print('Parameter 3: {}\n'.format(sys.argv[3]))

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

print(f'address location: {x}, {y}')

#: https://gis.utah.gov/sgid/open-sgid/
conn = psycopg2.connect("dbname=opensgid host=opensgid.agrc.utah.gov user=agrc password=agrc")
cur = conn.cursor()

cur.execute(
    f'SELECT name, ST_SetSRID(ST_MakePoint({x},{y}), 26912) <-> shape as dist '
    'FROM society.liquor_stores '
    'ORDER BY dist '
    'LIMIT 1;'
)

booze, _ = cur.fetchone()

print(f'the closest cold beverage is at {booze}')

cur.execute(
    f'SELECT name, ST_SetSRID(ST_MakePoint({x},{y}), 26912) <-> shape as dist '
    'FROM recreation.golf_courses '
    'ORDER BY dist '
    'LIMIT 1;'
)

golf_course, _ = cur.fetchone()

print(f'the closest golf course is {golf_course}')

cur.execute(
    f'SELECT name, ST_SetSRID(ST_MakePoint({x},{y}), 26912) <-> shape as dist '
    'FROM recreation.ski_area_resort_locations '
    'ORDER BY dist '
    'LIMIT 1;'
)

ski_resort, _ = cur.fetchone()

print(f'the closest ski resort is {ski_resort}')

cur.execute(
    f'SELECT primaryname, ST_SetSRID(ST_MakePoint({x},{y}), 26912) <-> shape as dist '
    'FROM recreation.trailheads '
    'ORDER BY dist '
    'LIMIT 1;'
)

trailhead, _ = cur.fetchone()

print(f'the closest trailhead is {trailhead}')
