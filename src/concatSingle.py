#!/usr/bin/env python
'''
input[1] words file, one word per line
[2] word embedding

output
stdout, word + embedding 
'''

import sys,gzip

def readEmbed(infile):
    d = {}
    for line in open(infile):
        l = line.strip().split()
        emb = [float(v) for v in l[1:]]
        d[l[0]] = emb
    return d

targetD = readEmbed(sys.argv[2])
for i,line in enumerate(gzip.open(sys.argv[1])):
    l = line.strip().split()

    target = l[0]

    if target not in targetD:
        target = "*UNKNOWN*"
    outv = targetD[target]
    stringout = [str(o) for o in outv]
    print l[0],'\t'.join(stringout)
