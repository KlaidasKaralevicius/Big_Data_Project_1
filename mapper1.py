#!/usr/bin/env python
import sys
import re

def parse_block(block):
    # rasti visus {key=value} duotame inpute
    pattern = r'\{([^=]+)=([^}]+)\}'
    matches = re.findall(pattern, block)
    # grazinti dictionary 'key':'value'
    return {key: value for key, value in matches}

def map_function():
    for line in sys.stdin:
        # find different full blocks '{{}}'
        blocks = re.findall(r'\{\{(.*?)\}\}', line)
        for block in blocks:
            # find data in each block - '{key':'value}'
            data = parse_block('{' + block + '}')
            # get data, if it is missing, write 'none'
            marsrutas = data.get('marsrutas', 'none')
            siuntu_skaicius = data.get('siuntu skaicius', 'none')
            svoris = data.get('svoris', 'none')
            geografine_zona = data.get('geografine zona', 'none')
            # write out data
            print(f"{marsrutas}\t{siuntu_skaicius},{svoris},{geografine_zona}") 

map_function()