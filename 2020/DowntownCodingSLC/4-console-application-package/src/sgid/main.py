#!/usr/bin/env python
# * coding: utf8 *
"""
SGID CLI

Usage:
  sgid what is at [[--x=<x> --y=<y>] | [--api-key=<key> --zone=<zone> --street=<street>]] (--from-table=<table> --attributes=<attributes>) [--filter=<filter>]
"""

import pkg_resources
import psycopg2
import requests
from colorama import Fore, init
from docopt import docopt


def main():
    '''Main entry point for program. Parse arguments and dispatch.
    '''
    args = docopt(__doc__, version=pkg_resources.require('sgid')[0].version)

    init(autoreset=True)

    print(f'{Fore.YELLOW}{args}')

    easting = northing = None

    if args['--zone']:
        easting, northing = geocode(args['--street'], args['--zone'], args['--api-key'])
        if not easting:
            return
    elif args['--x']:
        easting = args['--x']
        northing = args['--y']

    query(easting, northing, args['--from-table'], args['--attributes'], args['--filter'])


def geocode(street, zone, key):
    '''geocode an address returning coordinate tuple
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


def query(easting, northing, table, attributes, filter_predicate):
    '''query the open sgid and print the results
    '''
    #: https://gis.utah.gov/sgid/open-sgid/
    conn = psycopg2.connect("dbname=opensgid host=opensgid.agrc.utah.gov user=agrc password=agrc")
    cur = conn.cursor()

    sql = f'SELECT {attributes} FROM {table} WHERE '
    if easting:
        sql += f'ST_Intersects(shape, ST_SetSRID(ST_MakePoint({easting}, {northing}), 26912))'

    if easting and filter_predicate:
        sql += ' AND '

    if filter_predicate:
        sql += filter_predicate

    cur.execute(sql)

    result = cur.fetchall()

    print(f'{Fore.CYAN}{result}')
