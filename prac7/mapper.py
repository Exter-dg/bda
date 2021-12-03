#!/usr/bin/env python
import sys
 
from itertools import chain, combinations
 
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
 
 
 
for line in sys.stdin:
    line = line.strip()
    items = sorted(line.split(' '))
    print(items)
    freq = list(powerset(items))
    print(freq)
    for i in powerset(items):
        print(i)