#!/usr/bin/env python
my_file = open('genomic_dna.txt','r')
genomic_DNA = my_file.read()

exon_out = open('exon_seq.txt','w')
#print (genomic_DNA[0])
with open ('exons.txt','r') as f:
    exon_seq = ''
    for line in f:
        line = line.rstrip('\n').split(',')
        start = line[0]
        end = line[1]
        #print (start)
        exon_seq =exon_seq + genomic_DNA[int(start):int(end)]
        #print (genomic_DNA[int(end+1)])
    exon_out.write (exon_seq)