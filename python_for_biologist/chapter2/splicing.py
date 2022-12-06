#!/sur/bin/env python

frag = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'
exon1 = frag[0:62]
exon2 = frag[90:]
intron1 = frag[62:90].lower()

cds = exon1 + exon2
print (cds)

frac = 100 * (len(cds)/len(frag))

print ("the coding fraction of the sequence is: " + str(frac) )
mask_frag = exon1 + intron1 + exon2
print ("masked DNA is: " + mask_frag)