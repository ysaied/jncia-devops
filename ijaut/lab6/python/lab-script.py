#! /usr/bin/python

# Perform required imports
import json
from pprint import pprint

# If this module is run as a standalone script
if __name__ == "__main__":

    print("Reading the file...")

    # Work with file using context manager syntax, which
    # opens and closes the file automatically
    with open("show_route_output.json") as f:
        # Load JSON data from file
        route_data = json.load(f)

    # Pretty-print data loaded from JSON
    pprint(route_data)
