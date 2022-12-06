#!/usr/bin/env python
frag = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
motif = 'GAATTC'
len_frag1 = frag.find(motif)+1
len_frag2 = len(frag)-len_frag1
print ("fragment left is: " +  str(len_frag1))
print ("fragment right is: " +  str(len_frag2))