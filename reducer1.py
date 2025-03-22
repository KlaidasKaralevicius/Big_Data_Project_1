#!/usr/bin/env python
import sys
from collections import defaultdict

def reduce_function():
    # store value of each route, intinialize automatically when new route found
    route_data = defaultdict(lambda: {
        "siuntu_skaicius": 0, 
        "svoris": 0.0, 
        "geozonos": defaultdict(int)
    })

    # store missing data instances
    none_counts = {
        "marsrutas": 0,
        "siuntu_skaicius": 0,
        "svoris": 0,
        "geografine_zona": 0
    }
    # read line by line
    for line in sys.stdin:
        marsrutas, values = line.strip().split("\t")
        siuntu_skaicius, svoris, geografine_zona = values.split(",")

        # count blocks with missing key
        if marsrutas == "none":
            none_counts["marsrutas"] += 1
        # count blocks with missing values
        if siuntu_skaicius == "none":
            none_counts["siuntu_skaicius"] += 1
        if svoris == "none":
            none_counts["svoris"] += 1
        if geografine_zona == "none":
            none_counts["geografine_zona"] += 1

        # skip calculation if block is incomplete
        if "none" in (siuntu_skaicius, svoris, geografine_zona):
            continue

        # if no missing values, continue calculation
        route_data[marsrutas]["siuntu_skaicius"] += int(siuntu_skaicius)
        route_data[marsrutas]["svoris"] += float(svoris)
        route_data[marsrutas]["geozonos"][geografine_zona] += 1

    # write out valid routes with data
    for marsrutas, data in route_data.items():
        # convert dictionary to string "geo_zone_name:times_stopped"
        geozonos_str = "; ".join([f"{zona}:{count}" for zona, count in data["geozonos"].items()])
        print(f"{marsrutas}\t{data['siuntu_skaicius']},{round(data['svoris'],2)},{geozonos_str}")

    # write missing value counts
    for field, count in none_counts.items():
        print(f"{field} none:{count}")

reduce_function()