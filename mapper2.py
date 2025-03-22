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
            

map_function()