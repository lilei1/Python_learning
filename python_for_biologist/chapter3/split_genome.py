#!/usr/bin/env python

my_file = open ("genomic_dna.txt")
my_out = open("out_put.txt","w")
frag = my_file.read().rstrip("\n")

exon1 = frag[0:62]
exon2 = frag[90:]
intron1 = frag[62:90].lower()

cds = exon1 + exon2
print (cds)

frac = 100 * (len(cds)/len(frag))

print ("the coding fraction of the sequence is: " + str(frac) )
mask_frag = exon1 + intron1 + exon2
my_out.write ("masked DNA is: " + mask_frag)