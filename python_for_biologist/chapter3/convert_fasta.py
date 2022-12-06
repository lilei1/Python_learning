#!/usr/bin/env python
out_file = open ('out.fasta','w')
with open('original_seq.txt','r') as f:
    next(f)
    for line in f:
        line = line.rstrip("\n")
        line = line.split('\t')
        #print (line[0])
        #line = line.rstrip('\n').split('\s+')
        seq_id = line[0]
        DNA_seq = line[1].upper()
        out_file.write (">" + seq_id + "\n" + DNA_seq + "\n")
f.close()
out_file.close()