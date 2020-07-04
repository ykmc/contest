#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import combinations

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M,P,Q,R = map(int,readline().split())
XYZ = [tuple(map(int,readline().split())) for _ in range(R)]

d = defaultdict(int)
for x,y,z in XYZ:
    d[(x-1,y-1)] = z

ans = 0
for pcomb in combinations(range(N), P):
    scores = [0]*M
    for m in range(M):
        for p in pcomb:
            scores[m] += d[(p,m)]
    scores.sort(reverse=True)
    total_score = sum(scores[:Q])

    if total_score > ans:
        ans = total_score

print(ans)