#!/usr/bin/env python
import sys
from collections import defaultdict

def reduce_function():
    # store value for each key pair
    area_data = defaultdict(lambda: {
        'siuntu_skaicius': 0,
        'klientu_skaicius': 0
    })
    # store missing key combinations
    missing_keys_data = defaultdict(lambda: {
        "siuntu_skaicius": 0,
        "klientu_skaicius": 0
    })

    none_counts = {
        'geografine_zona': 0,
        'sav_diena': 0,
        'siuntu_skaicius': 0,
        'klientu_skaicius': 0
    }
    
    for line in sys.stdin:
        # split lines in key and value pairs
        key, values = line.strip().split('\t')
        geografine_zona, sav_diena = key.split(',')
        siuntu_skaicius, klientu_skaicius = values.split(',')
        # count blocks with missing key
        if geografine_zona == 'none':
            none_counts['geografine_zona'] += 1
        if sav_diena == 'none':
            none_counts['sav_diena'] += 1
        # count block with missing value
        if siuntu_skaicius == 'none':
            none_counts['siuntu_skaicius'] += 1
        if klientu_skaicius == 'none':
            none_counts['klientu_skaicius'] += 1
        # convert values into integers
        siuntu_skaicius = int(siuntu_skaicius) if siuntu_skaicius != 'none' else 0
        klientu_skaicius = int(klientu_skaicius) if klientu_skaicius != 'none' else 0
        # write data normally if both keys exist
        if geografine_zona != 'none' and sav_diena != 'none':
            area_data[(geografine_zona, sav_diena)]['siuntu_skaicius'] += siuntu_skaicius
            area_data[(geografine_zona, sav_diena)]['klientu_skaicius'] += klientu_skaicius
        else:
            # if any key is missing, write data collected from missing key instances
            missing_keys_data[(geografine_zona, sav_diena)]['siuntu_skaicius'] += siuntu_skaicius
            missing_keys_data[(geografine_zona, sav_diena)]['klientu_skaicius'] += klientu_skaicius

    # output result of full data
    for (geografine_zona, sav_diena), data in area_data.items():
        print(f"{geografine_zona},{sav_diena}\t{data['siuntu_skaicius']},{data['klientu_skaicius']}")
    # output result of data with missing key
    for (geografine_zona, sav_diena), data in missing_keys_data.items():
        print(f"{geografine_zona},{sav_diena}\t{data['siuntu_skaicius']},{data['klientu_skaicius']}")
    # output missing values
    for field, count in none_counts.items():
        print(f"{field} none:{count}")

reduce_function()