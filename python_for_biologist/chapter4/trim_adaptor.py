#!/usr/bin/env python
trimed = open('cleaned.txt','w')
with open ('input.txt','r') as f:
    for line in f:
        trimed.write (line[14:])
        print (str(len(line[14:])))