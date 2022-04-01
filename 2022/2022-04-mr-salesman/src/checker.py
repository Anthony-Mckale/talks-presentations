from pydash import py_
from termcolor import colored

def pi_distance(x1, y1, x2, y2):
    """
    distance between two two dimensional points
    @see https://en.wikipedia.org/wiki/Euclidean_distance
    """
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5


def annotate_fellow_place_distances(locations: list) -> None:
    """
    annotate with distances to fellow
    """
    for location in locations:
        location["distances"] = []
        for fellow_location in locations:
            if location == fellow_location:
                continue
            fellow_distance = pi_distance(
                location["x"],
                location["y"],
                fellow_location["x"],
                fellow_location["y"],
            )
            fellow_name = fellow_location["name"]
            location["distances"].append([fellow_name, fellow_distance])


def calc_route_times(route: list, locations: list):
    """returns total and list of routes and timings"""
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
        print(
            f"  {place_current} -> {place_going_to} is : {location_distance} (total: {travel_distance})"
        )
        place_current = place_going_to
    print()
    print(f"Total travel distance was : {travel_distance} ({69.2 * travel_distance} miles)")
    return travel_distance


def warnings_check(route: list, locations: list):
    """warning checker
    looks for:
    - too few places visited
    - too many places visited
    - if does not begin and end at the same place
    - if there are invalid places in the route
    - if any places in the places list have been missed
    """
    place_names = list(map(lambda place: place["name"], locations))
    expected_size = len(locations) + 1
    if len(route) < len(locations) + 1:
        print(
            colored(
                f"  ERR: not sure everywhere has been visited, expected route to be at least {expected_size}",
                "red",
            )
        )
    if len(route) > len(locations) + 1:
        print(
            colored(
                f"  ERR: not sure optomal looks like too many places are being visited, expected route to be no more than {expected_size}",
                "red",
            )
        )
    if len(route) > 2 and py_.head(route) != py_.last(route):
        print(
            colored(
                f"  ERR: route does not end where it started, expected route to begin and end at {py_.head(route)}",
                "red",
            )
        )
    for place in route:
        if place not in place_names:
            print(
                colored(
                    f' ERR: "{place}" in the route, not in valid places "{place_names}"',
                    "red",
                )
            )
    for place in place_names:
        if place not in route:
            print(colored(f'  ERR: "{place}" has not been visited', "red"))
