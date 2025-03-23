import pandas as pd

def parse_reducer_output(output_file):
    with open(output_file, 'r') as file:
        lines = file.readlines()
    # initialize lists to store the data
    area_data = []
    none_counts = {}
    # find none counts
    for line in lines:
        if 'geografine_zona' in line:
            none_counts['geografine_zona'] = int(line.split(':')[1].strip())
        elif 'sav_diena' in line:
            none_counts['sav_diena'] = int(line.split(':')[1].strip())
        elif 'siuntu_skaicius' in line:
            none_counts['siuntu_skaicius'] = int(line.split(':')[1].strip())
        elif 'klientu_skaicius' in line:
            none_counts['klientu_skaicius'] = int(line.split(':')[1].strip())
        else:
            # find full data
            parts = line.strip().split('\t')
            if len(parts) == 2:
                geozonos_diena = parts[0].split(',')
                geozona = geozonos_diena[0] if geozonos_diena[0] != 'none' else '-'
                sav_diena = geozonos_diena[1] if geozonos_diena[1] != 'none' else '-'
                siuntu_skaicius, klientu_skaicius = parts[1].split(',')
                area_data.append([geozona, sav_diena, int(siuntu_skaicius), int(klientu_skaicius)])
    
    return area_data, none_counts

def save_to_excel(output_file, area_data, none_counts):
    # automatic nr column increment
    data_with_nr = [[i + 1] + row for i, row in enumerate(area_data)]
    # define columns
    columns = ['Nr', 'Geografine zona', 'Savaites diena', 'Siuntiniu skaicius (vnt.)', 'Klientu skaicius']
    # create a DataFrame with the 'Nr' column
    df = pd.DataFrame(data_with_nr, columns = columns)
    # Add the missing values row
    none_counts_row = pd.DataFrame([['missing values', none_counts['geografine_zona'], none_counts['sav_diena'], none_counts['siuntu_skaicius'], none_counts['klientu_skaicius']]], columns = columns)
    # append missing values row
    df = pd.concat([df, none_counts_row], ignore_index = True)
    # one zone day for all week days, '-' where there is no zone day (repeating for all days)
    prev_zone = None
    for i in range(len(df)):
        if df.loc[i, 'Geografine zona'] == prev_zone and df.loc[i, 'Geografine zona'] != '-':
            df.loc[i, 'Geografine zona'] = ''
        else:
            prev_zone = df.loc[i, 'Geografine zona']
            
    print(f"Excel file saved as {output_file}")

output_file = 'reduce_output2_raw.txt'
area_data, none_counts = parse_reducer_output(output_file)
save_to_excel(output_file, area_data, none_counts)