#!/usr/bin/env python
with open ('original_seq.txt','r') as f:
    next(f)
    for line in f:
        line = line.rstrip('\n').split('\t')
        seq_id = line[0]
        seq_content = line[1]
        out_put = open(seq_id,'w')
        out_put.write(">" + seq_id + "\n" + seq_content + "\n")