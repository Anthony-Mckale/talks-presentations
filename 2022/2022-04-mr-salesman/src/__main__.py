"""
Main entry point for project
"""
import argparse
from colorama import init
from termcolor import colored
import time

from utils.io.file import load_json
from route_master import create_route
from checker import warnings_check, calc_route_times, annotate_fellow_place_distances

init()

if __name__ == "__main__":
    print(colored("Welcome to the McKale Travelling Salesman Company", "yellow"))
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sale_locations",
        dest="sale_locations",
        type=str,
        help="json file containing sale_locations",
    )
    parser.add_argument(
        "--algorithm",
        dest="algorithm",
        type=str,
        help="algorithm to use, defaults to random",
    )
    args = parser.parse_args()
    if not args.sale_locations:
        print(colored("  ERR:you need to add --sale_locations <file.json>", "red"))
        exit(1)
    if not args.algorithm:
        args.algorithm = 'RANDOM'
    json_blob = load_json(args.sale_locations)
    name = json_blob["name"]
    places = json_blob["places"]
    annotate_fellow_place_distances(places)
    print(f'Creating route for "{name}" (place count: {len(places)})')
    print()
    tic = time.perf_counter()
    #
    # WHERE USER CODE LIVES >>>>
    #
    print(f"Creating Route")
    print(f"============================")
    route = create_route(places, args.algorithm)
    #
    # WHERE USER CODE LIVES <<<<
    #
    # TIMING
    toc = time.perf_counter()
    print(f"took {(toc - tic):.05f} seconds to calculate route")
    print()
    # say any warnings (ps some warnings will crash Route Calc)
    warnings_check(route, places)
    # Calculate Route Time
    print(f"Calculating Route Distance")
    print(f"============================")
    print(f"")
    calc_route_times(route, places)
