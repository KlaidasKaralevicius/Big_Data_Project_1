#!/usr/bin/env python
import sys
 
A = []
for line in sys.stdin:
  key, val = line.strip().split('\t', 1)
  A.append([key,val])

A.sort(key=lambda tup: tup[0])
for el in A:
  print("%s\t%s" % (el[0], el[1]))