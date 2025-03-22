#!/usr/bin/env python
import sys
import re

def parse_block(block):
    pattern = r'\{([^=]+)=([^}]+)\}'
    matches = re.findall(pattern, block)
    return {key: value for key, value in matches}

def map_function():
    for line in sys.stdin:
        blocks = re.findall(r'\{\{(.*?)\}\}', line)
        for block in blocks:
            data = parse_block('{' + block + '}')
            geografine_zona = data.get('geografine zona', 'none')
            sav_diena = data.get('sustojimo savaites diena', 'none')
            siuntu_skaicius = data.get('siuntu skaicius', 'none')
            klientu_skaicius = data.get('Sustojimo klientu skaicius', 'none')
            # write key pair and values (key is a string of 2 values)
            print(f"{geografine_zona},{sav_diena}\t{siuntu_skaicius},{klientu_skaicius}") 
            
map_function()