import pandas as pd

# Read the data from the text file
with open('reduce_output2_raw.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store the data
data = []
missing_values = {}

# Process each line
for line in lines:
    if 'geografine_zona' in line:
        missing_values['geografine_zona'] = int(line.split(':')[1].strip())
    elif 'sav_diena' in line:
        missing_values['sav_diena'] = int(line.split(':')[1].strip())
    elif 'siuntu_skaicius' in line:
        missing_values['siuntu_skaicius'] = int(line.split(':')[1].strip())
    elif 'klientu_skaicius' in line:
        missing_values['klientu_skaicius'] = int(line.split(':')[1].strip())
    else:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            zone_day = parts[0].split(',')
            zone = zone_day[0] if zone_day[0] != 'none' else '-'
            day = zone_day[1] if zone_day[1] != 'none' else '-'
            parsel, client = parts[1].split(',')
            data.append([zone, day, int(parsel), int(client)])

# Add the 'Nr' column directly from the start
data_with_nr = [[i + 1] + row for i, row in enumerate(data)]

# Create a DataFrame with the 'Nr' column
df = pd.DataFrame(data_with_nr, columns=['Nr', 'Geografine zona', 'Savaites diena', 'Siuntiniu skaicius (vnt.)', 'Klientu skaicius'])

# Add the missing values row
missing_values_row = pd.DataFrame([['missing values', missing_values['geografine_zona'], missing_values['sav_diena'], missing_values['siuntu_skaicius'], missing_values['klientu_skaicius']]], columns=['Nr', 'Geografine zona', 'Savaites diena', 'Siuntiniu skaicius (vnt.)', 'Klientu skaicius'])

# Use pd.concat to append the missing values row
df = pd.concat([df, missing_values_row], ignore_index=True)

# Ensure zone names appear only once for each group of days, but keep '-' as is
prev_zone = None
for i in range(len(df)):
    if df.loc[i, 'Geografine zona'] == prev_zone and df.loc[i, 'Geografine zona'] != '-':
        df.loc[i, 'Geografine zona'] = ''
    else:
        prev_zone = df.loc[i, 'Geografine zona']

# Write to Excel
df.to_excel('reduce_output2.xlsx', index=False)

print("Excel file created successfully.")