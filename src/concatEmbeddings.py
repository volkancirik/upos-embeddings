#!/usr/bin/env python
'''
input[1] wsub pairs file
[2] target word embedding
[3] subs word embeddings
[4] # of line in test file

output
stdout, word, embedding size of [2]+[3], [4] many number of lines
'''

import sys

def readEmbed(infile):
    d = {}
    for line in open(infile):
        l = line.strip().split()
        emb = [float(v) for v in l[1:]]
        d[l[0]] = emb
    return d

L = int(sys.argv[4])
targetD = readEmbed(sys.argv[2])
contextD = readEmbed(sys.argv[3])

pairD = {}
K = 0
for i,line in enumerate(open(sys.argv[1])):
    l = line.strip().split()

    target = l[0]
    context = l[1]
    j = i%L

    if target not in targetD:
        target = "*UNKNOWN*"
    if context not in contextD:
        context = "*UNKNOWN*"
    if (j,target) not in pairD:
        pairD.setdefault((j,target),[])
    pairD[(j,target)].append(contextD[context])
    if j == 0:
        K += 1
for i,line in enumerate(open(sys.argv[1])):
    if i == L:
        break
    l = line.strip().split()

    target = l[0]
    if target not in targetD:
        target = "*UNKNOWN*"

    cval = []
    for j in xrange(len(pairD[(i,target)][0])):
        vsum = 0
        for k in xrange(K):
#            print >> sys.stderr, j ,len(pairD[(i,target)][0]),k,K
            vsum += pairD[(i,target)][k][j]

        cval.append(vsum*1.00/K)
    outv = targetD[target] + cval
    stringout = [str(o) for o in outv]
    print l[0],'\t'.join(stringout)
