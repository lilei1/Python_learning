#!/usr/bin/env/ python

rc_dict = {'A':'T','T':'A','C':'G','G':'C','N':'N','-':'-'}
DNA = "ATCGgcN-"
DNA_ct = DNA.upper()
rc_DNA = ''
for i in DNA_ct:
    rc_DNA = rc_DNA + rc_dict[i]

print (rc_DNA)

