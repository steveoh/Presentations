# agrc/python

[![Build Status](https://travis-ci.com/agrc/python.svg?branch=master)](https://travis-ci.com/agrc/python)
[![Coverage Status](https://coveralls.io/repos/github/agrc/python/badge.svg?branch=master)](https://coveralls.io/github/agrc/python?branch=master)

AGRC's default Python project configuration/template

## Installation

1. Create new environment for the project
   - With python 3 (without arcpy)
     - `python -m venv .env`
     - activate the environment `source .env/bin/activate`
   - With conda
     - `conda create --clone arcgispro-py3 --name PROJECT_NAME`
1. Rename `src/projectname` folder to your desired project name
1. Edit the `setup.py:name, url, project_urls, keywords, and entry_points` to reflect your new project name
1. Edit the `test_projectname.py` to match your project name.
   - You will have one `test_filename.py` file for each file in your `src` directory and you will write tests for the specific file in the `test_filename.py` file
1. Install an editable package for development
   - `pip install -e ".[tests]"`
   - add any project requirements to the `setup.py:install_requires` array
1. Run the tests
   - `ptw`
     - **P**y**t**est **W**atch will restart the tests every time you save a file
1. Bring your test code coverage to 80% or above!
