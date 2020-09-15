# Downtown SLC User Group

- intro
- reasoning
  - we hire geographers
  - automation and programming are major daily tasks
  - documentation shows sequential samples
- resources
  - gis.utah.gov - jekyll / blog, news, data discovery, metadata
  - api.mapserv.utah.gov - asp.net web api / geocoding, searching, and info endpoints
    - web accessible sgid
  - open sgid - postgis cloud sql / public database access
    - visualization and analysis
  - opendata.gis.utah.gov - rails, ember / esri hub
    - data discovery
  - arcgis online - esri / feature services
    - query with geo service api

## Python Script Evolution

_Based on a [2017 blog post](https://gis.utah.gov/the-evolution-of-a-python-script/)._

### Command line tool

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

`python 1-command-line-without-parameters/main.py`

### Command line tool with arguments

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

1. `python 2-command-line-with-parameters/main.py`
1. `python 2-command-line-with-parameters/main.py AGRC-130B2425664697 '326 eat south temple' 'salt lake'`

### Console application

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

### Console application as a package

#### Pros

- pip install package and all dependencies to a known state
- have package name available in terminal anywhere
- sharable in the python package index

#### Example usage

1. `sgid what is at --from-table=boundaries.municipal_boundaries --attributes=name --filter="name like 'M%'"`
1. `sgid what is at --x 424818.88010852225 --y 4513223.70267614 --from-table=boundaries.municipal_boundaries --attributes=name`
1. `sgid what is at --street '2222 atkin ave' --zone 84109 --api-key AGRC-130B2425664697 --from-table=boundaries.municipal_boundaries --attributes=name`
