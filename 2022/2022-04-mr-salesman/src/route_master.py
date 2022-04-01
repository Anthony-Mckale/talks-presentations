import time
from random import random
from pydash import py_
from checker import pi_distance
import math
from pants import World, Edge, world, solver, Solver, ant, Ant


def _create_random_route(places: list) -> list:
    """
    Anthony's super efficient algorithm
    otherwise known as the crazy sort

    PS: the cake is a lie"""
    place_names: list = list(map(lambda place: place["name"], places))
    sorted_cough_cough_place_names: list = sorted(
        place_names, key=lambda x: random(), reverse=True
    )
    sorted_cough_cough_place_names.append(py_.head(sorted_cough_cough_place_names))
    return sorted_cough_cough_place_names


def _create_best_of_10_route(places: list) -> list:
    """
    crazy sort * 10
    """
    route = None
    best_score = 1000000000000
    for x in range(1, 10):
        test_route = _create_random_route(places)
        test_score = _calc_route_length(test_route, places)
        print(f"""CREATED: {test_score} = {test_route}""")
        if test_score < best_score:
            print(f"""- NEW BEST""")
            route = test_route
            best_score = test_score
    return route


def _create_brute_route(places: list) -> list:
    """
    slow but sure
    """
    # print_var = 'full'
    print_var = 'debug'

    # print_var = 'none'
    class Container:
        pass

    c = Container()
    c.tic = time.perf_counter()
    tic_counter = 10 * 1000

    def _recursive_brute_route(start_location: str, current_route: list, place_names_left: list,
                               global_vars: dict) -> []:
        if len(place_names_left) == 1:
            test_route = [start_location] + current_route + [place_names_left[0], start_location]
            test_score = _calc_route_length(test_route, places)
            global_vars["counter"] += 1
            if global_vars["counter"] % tic_counter == 0:
                toc = time.perf_counter()
                print(
                    f"""[{global_vars["counter"]}:{global_vars["expected_calls"]} ({math.floor(global_vars["counter"] * 100 / global_vars["expected_calls"])}%)] status ({(toc - c.tic):.05f} seconds per {tic_counter})""")
                c.tic = toc
            if print_var == 'full':
                print(f"brute_forcing NODE: {current_route}")
            return [test_score, test_route]
        if print_var == 'full':
            print(f"brute_forcing: {current_route}")
        best_route = None
        best_score = 1000000000000
        for index, test_place_name in enumerate(place_names_left):
            test_place_name = place_names_left[index]
            test_place_names_left = place_names_left.copy()
            del test_place_names_left[index]
            [test_score, test_route] = _recursive_brute_route(start_location, current_route + [test_place_name],
                                                              test_place_names_left, global_vars)
            if test_score < best_score:
                best_route = test_route
                best_score = test_score
                if print_var == 'debug':
                    if test_score < global_vars["global_best_score"]:
                        print(
                            f"""[{global_vars["counter"]}:{global_vars["expected_calls"]}] - NEW BEST: {test_score}<{global_vars["global_best_score"]} [{global_vars["global_best_route"]}]""")
                        global_vars["global_best_route"] = test_route
                        global_vars["global_best_score"] = test_score
        return [best_score, best_route]

    # due to cyclical nature, can fix first point
    place_names: list = list(map(lambda place: place["name"], places))
    starting_place = place_names[0]
    resting_places = place_names[1:]

    global_vars = {
        "global_best_route": None,
        "global_best_score": 1000000000000,
        "counter": 0,
        "expected_calls": math.factorial(len(resting_places))
    }

    print(f"starting_place: {starting_place}")
    print(f"resting_places: {resting_places}")
    [score, route] = _recursive_brute_route(starting_place, [], resting_places, global_vars)
    return route


def _create_brute_route2(places: list) -> list:
    """
    slow but optimised
    - much much faster route length checking 0.16807s ->0.00526s
    """
    print_var = 'debug'
    # print_var = 'none'
    places_kv = py_.key_by(places, 'name')

    # due to cyclical nature, can fix first point
    place_names: list = list(map(lambda place: place["name"], places))
    starting_place = place_names[0]
    resting_places = place_names[1:]

    class Container:
        pass

    c = Container()
    c.global_best_route = None
    c.global_best_score = 1000000000000
    c.counter = 0
    c.expected_calls = math.factorial(len(resting_places))
    c.tic = time.perf_counter()
    tic_counter = 1000 * 1000

    def _recursive_brute_route(start_location: str, current_route: list, place_names_left: list):
        for index, test_place_name in enumerate(place_names_left):
            test_place_name = place_names_left[index]
            test_place_names_left = place_names_left.copy()
            del test_place_names_left[index]

            # Reduce depth of factional brute
            if len(place_names_left) > 1:
                _recursive_brute_route(start_location, current_route + [test_place_name], test_place_names_left)
                continue

            # Reduce depth of recursive by 1, push into loop
            test_route = [start_location] + current_route + [place_names_left[0], start_location]
            test_score = _fast_calc_route_length(test_route, places_kv)
            c.counter += 1
            if c.counter % tic_counter == 0 and print_var == 'debug':
                toc = time.perf_counter()
                print(
                    f"""[{c.counter}:{c.expected_calls} ({math.floor(c.counter * 100 / c.expected_calls)}%)] status ({(toc - c.tic):.05f} seconds per {tic_counter})""")
                c.tic = toc

            # Only use global best
            if test_score < c.global_best_score:
                print(
                    f"""[{c.counter}:{c.expected_calls}] - NEW BEST: {test_score}<{c.global_best_score} [{test_route}]""")
                c.global_best_route = test_route
                c.global_best_score = test_score

    print(f"starting_place: {starting_place}")
    print(f"resting_places: {resting_places}")
    _recursive_brute_route(starting_place, [], resting_places)
    return c.global_best_route


def _create_antcolony_route(places: list) -> list:
    """
    cheat - https://pypi.org/project/ACO-Pants/
    https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
    """
    nodes = []
    # for place in places:
    #    x = place['x']
    #    y = place['y']
    #    nodes.append((x, y))
    world = World(places, _calc_route_place_distance)
    solver = Solver()
    solution = solver.solve(world)
    print(solution.distance)
    print(solution.tour)  # Nodes visited in order
    print(solution.path)  # Edges taken in order
    place_names: list = list(map(lambda place: place["name"], solution.tour))
    starting_place: str = place_names[0]
    place_names.append(starting_place)
    return place_names


RANDOM_ALGORITHM = 'RANDOM'
BEST_OF_10_ALGORITHM = 'BEST_OF_10'
BRUTE_ALGORITHM = 'BRUTE'
BRUTE2_ALGORITHM = 'BRUTE2'
MANUAL_ALGORITHM = 'MANUAL'
ANT_ALGORITHM = 'ANT'


def get_algorithm() -> list:
    return [RANDOM_ALGORITHM, BEST_OF_10_ALGORITHM, BRUTE_ALGORITHM, MANUAL_ALGORITHM]


def create_route(places: list, algorithm: str = RANDOM_ALGORITHM) -> list:
    """
    take a list of place dictionaries
    {name:string, x:double, y:double, distances:list (distances to other places)}

    and turn them into a list of name:string
    """
    # uncomment this to see places and structure
    # for place in places:
    #     print(f"name: {place['name']}")
    #     print(f" x: {place['x']}")
    #     print(f" y: {place['y']}")
    #     print(f" distances to other places:")
    #     for [fellow_place, fellow_distance] in place['distances']:
    #         print(f"  to {fellow_place}: {fellow_distance}")
    print(f"using algorithm: {algorithm}")
    if algorithm == RANDOM_ALGORITHM:
        # average ~39, sub second 0.0014
        return _create_random_route(places)
    if algorithm == BEST_OF_10_ALGORITHM:
        # average ~30, sub second 0.012
        return _create_best_of_10_route(places)
    if algorithm == BRUTE_ALGORITHM:
        # 18.07 perfect, 5888 mins
        # ['Edinburgh', 'Liverpool', 'Salford', 'Manchester', 'Oxford', 'London', 'York', 'Newcastle', 'Aberdeen', 'Dundee', 'Perth', 'Inverness', 'Glasgow', 'Edinburgh']
        return _create_brute_route(places)
    if algorithm == BRUTE2_ALGORITHM:
        # 18.07 perfect, 13 mins
        # ['Edinburgh', 'Liverpool', 'Salford', 'Manchester', 'Oxford', 'London', 'York', 'Newcastle', 'Aberdeen', 'Dundee', 'Perth', 'Inverness', 'Glasgow', 'Edinburgh']
        return _create_brute_route2(places)
    if algorithm == ANT_ALGORITHM:
        # 17.80 perfect, 0.087 seconds! wtf with python 3
        # 17.80 perfect, took 0.23 ! wtf with python 3
        # ['Edinburgh', 'Liverpool', 'Salford', 'Manchester', 'Oxford', 'London', 'York', 'Newcastle', 'Aberdeen', 'Dundee', 'Perth', 'Inverness', 'Glasgow', 'Edinburgh']
        return _create_antcolony_route(places)
    if algorithm == MANUAL_ALGORITHM:
        # average
        return [
            'Edinburgh',
            'Perth',
            'Inverness',
            'Glasgow',
            'Liverpool',
            'Salford',
            'Manchester',
            'Oxford',
            'London',
            'York',
            'Newcastle',
            'Aberdeen',
            'Dundee',
            'Edinburgh'
        ]
        return ['Edinburgh', 'Liverpool', 'Salford', 'Manchester', 'Oxford', 'London', 'York', 'Newcastle', 'Aberdeen',
                'Dundee', 'Perth', 'Inverness', 'Glasgow', 'Edinburgh']


def _calc_route_place_distance(place_a: dict, place_b: dict):
    """fast helper function for detecting how long a route is"""
    return ((place_a["x"] - place_b["x"]) ** 2) + ((place_a["y"] - place_b["y"]) ** 2)


def _calc_route_length(route: list, locations: list):
    """helper function for detecting how long a route is"""
    route_locations = route.copy()
    place_current = route_locations.pop(0)
    travel_distance = 0
    for place_going_to in route_locations:
        location_current = py_.find(locations, {"name": place_current})
        location_going_to = py_.find(locations, {"name": place_going_to})
        location_distance = pi_distance(
            location_current["x"],
            location_current["y"],
            location_going_to["x"],
            location_going_to["y"],
        )
        travel_distance += location_distance
        place_current = place_going_to
    return travel_distance


def _fast_calc_route_length(route: list, places_kv: dict):
    """fast helper function for detecting how long a route is"""
    place_current = None
    travel_distance = 0
    # 1) stopped copying and recreating arrays
    for index, place_going_to in enumerate(route):
        if index == 0:
            place_current = place_going_to
            continue
        # 2) updated brute force search to look up
        location_current = places_kv[place_current]
        location_going_to = places_kv[place_going_to]
        # 3) updated _fast_relative_distance ditch slow square route
        location_distance = ((location_going_to["x"] - location_current["x"]) ** 2) + (
                    (location_going_to["y"] - location_current["y"]) ** 2)
        travel_distance += location_distance
        place_current = place_going_to
    return travel_distance
