#!/usr/bin/env python
  
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    phrase = "CAPITAL LETTER" 
    phrase_split = phrase.split()
    phrase_words = len(phrase_split)
 
    for i in list(range(len(words)-phrase_words+1)):
        # i points to the starting word
        flag = True
    
        for j in list(range(phrase_words)):
            if phrase_split[j] != words[i+j]:
                flag = False
                break 
            
        if flag==True:
            print ('%s\t%s' % (phrase, 1))