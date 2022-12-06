#!/usr/bin/env python

seq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
A_count = seq.count('A')
T_count = seq.count('T')
seq_len = len(seq)
AT_content = (A_count + T_count)/seq_len
print ("AT content: " + str(AT_content)+ "%")
    
#if __name__ == '__main__':
    #globals()[sys.argv[1]]()