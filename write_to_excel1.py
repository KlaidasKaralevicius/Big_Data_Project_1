import pandas as pd
import re
# extract values from file
def parse_reducer_output(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    # save data
    routes_data = []
    none_counts = {
        'marsrutas': 0,
        'siuntu_skaicius': 0,
        'svoris': 0,
        'geografine_zona': 0
    }
    unique_zones = set()
    
    for line in lines:
        parts = line.strip().split('\t')
        # find none counts
        if parts[0].startswith('marsrutas none'):
            none_counts['marsrutas'] = int(parts[0].split(':')[1])
        elif parts[0].startswith('siuntu_skaicius none'):
            none_counts['siuntu_skaicius'] = int(parts[0].split(':')[1])
        elif parts[0].startswith('svoris none'):
            none_counts['svoris'] = int(parts[0].split(':')[1])
        elif parts[0].startswith('geografine_zona none'):
            none_counts['geografine_zona'] = int(parts[0].split(':')[1])
        # get values of 'marsrutas', 'siuntu_skaicius' and 'svoris'
        else:
            marsrutas = parts[0]
            values = parts[1].split(',')
            siuntu_skaicius = int(values[0])
            svoris = float(values[1])
            # find different geozones
            geozone_counts = {}
            # if there is more than 2 values, there are multiple zones
            if len(values) > 2:
                zones = values[2].split('; ')
                for zone in zones:
                    # find zone names and counts
                    match = re.match(r'(Z\d+):(\d+)', zone)
                    if match:
                        # store found values
                        zone_name, count = match.groups()
                        geozone_counts[zone_name] = int(count)
                        unique_zones.add(zone_name)
            # store all found data            
            routes_data.append([marsrutas, siuntu_skaicius, svoris, geozone_counts])
            
    return routes_data, unique_zones, none_counts
# save values to excel
def save_to_excel(output_file, routes_data, unique_zones, none_counts):
    # sort unizue zones
    unique_zones = sorted(list(unique_zones))
    # define columns
    columns = ['Nr', 'Marsrutas', 'Siuntu skaicius (vnt.)', 'Siuntu svoric (kg)'] + unique_zones
    data = []
    # fill in data
    for idx, (marsrutas, siuntu_skaicius, svoris, geozone_counts) in enumerate(routes_data, start = 1):
        row = [idx, marsrutas, siuntu_skaicius, svoris]
        for zone in unique_zones:
            row.append(geozone_counts.get(zone, 0))
        data.append(row)
    
    df = pd.DataFrame(data, columns = columns)
    # add missing data row
    none_data = [
        'missing data count',
        none_counts['marsrutas'],
        none_counts['siuntu_skaicius'],
        none_counts['svoris']
    ] + [none_counts['geografine_zona']] + [''] * (len(unique_zones) - 1)
    # add missing data to all data
    df.loc[len(df)] = none_data
    # save to excel
    df.to_excel(output_file, index = False)
    print(f"Excel file saved as {output_file}")
    
output_file = 'reduce_output1_raw.txt'
routes_data, unique_zones, none_counts = parse_reducer_output(output_file)
save_to_excel(output_file, routes_data, unique_zones, none_counts)