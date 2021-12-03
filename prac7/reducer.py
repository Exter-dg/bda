#!/usr/bin/env python
import sys
 
counts = dict()
for phrase in sys.stdin:
    phrase = phrase.strip()
    if phrase not in counts.keys():
        counts[phrase]=1
    else:
        counts[phrase]+=1
counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
for k,v in counts.items():
    print(f'{k} : {v}')
print("New Reducer")