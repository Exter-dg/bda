#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
phrase = None
current_phrase = None
current_count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    phrase, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
  
    
    if current_phrase == phrase:
        current_count += count
    else:
        current_count = count
        current_phrase = phrase
  

print ('%s\t%s' % (current_phrase, current_count))




    


