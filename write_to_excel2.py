import pandas as pd
import re

def parse_reducer_output(file_path):
    return

def save_to_excel(output_file, routes_data, none_counts):
    return

output_file = 'reduce_output2_raw.txt'
routes_data, unique_zones, none_counts = parse_reducer_output(output_file)
save_to_excel('reduce_output2.xlsx', routes_data, none_counts)