# Overview

Welcome to Mr McKale's bits and bobs shipping incorporated.

Your challenge if you choose to accept it, is to improve Mr McKale's shoddy scheduling code.

Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city ?

https://en.wikipedia.org/wiki/Travelling_salesman_problem

# Task
You'll find anthony's super sort algorithm in src/route_master.py::create_route

```py
def create_route(places: list) -> list:
    """
    take a list of place dictionaries
    {name:string, x:double, y:double, distances:list (distances to other places)}

    and turn them into a list of name:string
    """
    ...
    return ["place1", "place2"...]
```

Your task is to fork the github project, and modify `create_route` to make it better

## Criteria
Entries will be marked on:
- speed of calculating route
- shortness of routes calculated
- any funky location jsons you create for testing
- coding standards (aka is it PEP8 complaint)
- STRETCH: unit tests coverage

## Rules
- you can use any libraries you want
- work must be your own
- code must compile/run in python 3.9

# Getting Started
- install make

  https://chocolatey.org/install
  
  ```choco install make```
- install python

  https://www.python.org/downloads/
- install dependencies
  
  ```make install```

How to run scheduler with uk data:

```bash
python src/ --sale_locations uk.json
```

How to run scheduler linting:
```bash
make lint
```

## Speed Run

```
"If you want your code to run faster,
you should probably just use PyPy."
-- Guido van Rossum (creator of Python)
```

```bash
chocolatey install pypy3 -y
pypy3 -m ensurepip
pypy3 -mpip install -r requirements-dev.txt  -r requirements.txt 

pypy3 src/ --sale_locations uk.json

# took 1.59282 seconds per 10,000
pypy3 src/ --sale_locations uk.json --algorithm BRUTE
# took 7.38831 seconds per 10,000
python src/ --sale_locations uk.json --algorithm BRUTE


# took 1.65833 seconds per 1,000,000
pypy3 src/ --sale_locations uk.json --algorithm BRUTE2
# took 7.96515 seconds per 1,000,000
python src/ --sale_locations uk.json --algorithm BRUTE2

# BRUTE IS x447 SLOWER THAN BRUTE2 + pypy
```

## Route File Format

You'll find a simple file with x, y coords on the routes

Feel free to create your own for testing or showing off purposes

```json
{
	"name": "name of Locations",
	"places": [
	{
		"name": "name of place",
		"x": 53.958332,
		"y": -1.080278
	},
```