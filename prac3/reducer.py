#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
current_num = None
current_count = 0
num = None
  
g_largest=0
g_avg = 0.0
g_count = 0
dict = {}


# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    num, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
        num = int(num)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
  
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: num) before it is passed to the reducer
    
    if current_num == num:
        current_count += count
    else:
        if current_num:
            # write result to STDOUT
            #print ('%s\t%s' % (current_num, current_count))
            dict[current_num] = current_count
        current_count = count
        current_num = num
  
# do not forget to output the last num if needed!
if current_num == num:
    #print ('%s\t%s' % (current_num, current_count))
    dict[current_num] = current_count

# Find avg, largest

for key, value in dict.items():
    g_avg += key*value
    g_count += value
    g_largest = max(g_largest, key)

g_avg/=g_count

print("The largest Integer is: ", g_largest)
print("The avg of Integers is: ", g_avg)
print("Total Distinct integers are:", len(dict))
print("All integers are:")

for key,value in dict.items():
    print(key)





    


