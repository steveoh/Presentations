# Downtown SLC User Group

- about me
  - [@steveagrc](https://twitter.com/steveagrc)
  - i like writing code with c#, python, javascript
  - i enjoy designing web api's and automating processes
- about [AGRC](https://gis.utah.gov/about/)
  - SGID ~400 spatial layers
    - compile local data to state; parcels, roads, address points
  - Build custom web applications (dojo/react/angular), components, workflows, etc
    - locate.utah.gov, [wri.utah.gov](https://wri.utah.gov/wri/map/map.html#id=2485)
    - validating voter precincts, [unclaimed property](https://mycash.utah.gov) analytics
    - support 911 dispatch centers
  - Aerial Imagery, Lidar, and base maps [atlas](https://atlas.utah.gov)
  - GPS Network
    - sub centimeter accuracy for surveyors with connected GPS receivers correcting satellite data in real time
  - Coordination
    - Spread geospatial news, events, etc
      - maps on the hill
      - UGIC
      - User groups
- reasons for choosing to talk about python
  - most common language for spatial and non technicals
  - we hire geographers
  - automation and programming are major daily tasks
  - esri documentation shows sequential samples
    - copy paste programming
- resources
  - [Agency website](https://gis.utah.gov) - jekyll / blog, news, data discovery, metadata
  - Github: [agrc](https://github.com/agrc), [agrc-widgets](https://github.com/agrc-widgets)
  - [AGRC Web API](https://api.mapserv.utah.gov) - asp.net web api / geocoding, searching, and info endpoints
    - web accessible sgid
  - [Open SGID](https://gis.utah.gov/sgid/open-sgid/) - postgis cloud sql / public database access
    - visualization and analysis
  - [Open Data](https://opendata.gis.utah.gov) - rails, ember / esri hub
    - data discovery
  - [arcgis online](https://www.arcgis.com/home/index.html) - esri / feature services
    - query with geo service api
  - [AGRC python template](https://github.com/agrc/python)

## Python Script Evolution

_Based on a [2017 blog post](https://gis.utah.gov/the-evolution-of-a-python-script/)._

### Command line tool (1)

Using [Web API](https://api.mapserv.utah.gov) web access to the SGID

#### Pros

- simple, quick, great for prototyping or disposable functionality
- no documentation required
- run the script and it does what you last left it to do

#### Cons

- hard coded values; file paths, api keys, etc
- dependencies and their versions are unknown to others
  - `requirements.txt` is ok but we can do better
- difficult to share - needs extensive documentation and source code editing
  - the `.env` file with the api key is a secret to others
  - where did it come from? what did it contain?
- will be running in production in less than a week™

#### Example

1. `python 1-command-line-without-parameters/main.py`
1. `deactivate`
1. `source .env/bin/activate`
1. `python 1-command-line-without-parameters/main.py`
1. `pip install -r requirements.txt`

### Command line tool with arguments (2)

- Using [Open SGID](https://gis.utah.gov/sgid/open-sgid/) data
- [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)

#### Pros

- script is more generic
  - can geocode any address input with any api key
- no hard coded values
- no script editing to have success

#### Cons

- command line arguments are not discoverable without reading the code
- requires good documentation to have success
- dependencies and their versions are unknown to others

#### Example usage

1. `python 2-command-line-with-parameters/main.py AGRC-130B2425664697 '326 eat south temple' 'salt lake'`
1. `python 2-command-line-with-parameters/main.py`

### Console application (3)

- Using ArcGIS Online geo service data found from [Open Data](https://opendata.gis.utah.gov/)
- [doctopt](http://docopt.org/)

#### Pros

- application is self documented, descriptive, and simple to understand
  - docopt forces documentation
- feedback given with incorrect syntax

#### Cons

- dependencies and their versions are unknown to others

#### Example usage

1. `python 3-console-application/main.py --help`
1. `python 3-console-application/main.py utilities at '866 E 4Th Ave' slc --key AGRC-130B2425664697`
1. `python 3-console-application/main.py utilities at '866 E 4Th Ave' slc --key AGRC-130B2425664697 --gas`
1. `python 3-console-application/main.py utilities at '866 E 4Th Ave' slc --key AGRC-130B2425664697 --all`

### Console application as a package (4)

- [agrc python template](https://github.com/agrc/python)
- open sgid

#### Pros

- pip install package and all dependencies to a known state
- have package name available in terminal anywhere
- sharable in the python package index

#### Example usage

1. `pip install --editable ./`
1. `sgid what is at --x 424818.88010852225 --y 4513223.70267614 --from-table=boundaries.municipal_boundaries --attributes=name`
1. `sgid what is at --street '2222 atkin ave' --zone 84109 --api-key AGRC-130B2425664697 --from-table=boundaries.municipal_boundaries --attributes=name`
1. `sgid what is at --from-table=boundaries.municipal_boundaries --attributes=name --filter="name like 'M%'"`
