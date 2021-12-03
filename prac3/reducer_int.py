#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
g_largest=0
g_avg = 0.0
g_count = 0
dict = {}

current_num = 0
current_count = 0
num = 0
  

for line in sys.stdin:

    line = line.strip()
    num, count = line.split('\t', 1)

    try:
        count = int(count)
        num = int(num)
    except ValueError:
        continue

    if current_num == num:
        current_count += count
    else:
        if current_num:
            dict[current_num] = current_count

        current_count = count
        current_num = num

dict[current_num] = current_count

# Find avg, largest

for key in dict:
    g_largest = max(g_largest, key)
    g_avg += (key*dict[key])
    g_count+=dict[key]

g_avg/=g_count

print("The largest Integer is: ", g_largest)
print("The avg of Integers is: ", g_avg)
print("Total Distinct integers are:", len(dict))
print("All integers are:")

for key in dict:
    print(key, end=' ')
