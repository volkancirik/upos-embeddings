#!/usr/bin/env python
'''
input stdin = words and their clusters
[1] word to be mapped wsj.word.gz 

output
stdout, one cluster id per line
'''

import sys

targetD = readEmbed(sys.argv[2])
contextD = readEmbed(sys.argv[3])

pairD = {}
K = 0
for i,line in enumerate(open(sys.argv[1])):
    l = line.strip().split()



