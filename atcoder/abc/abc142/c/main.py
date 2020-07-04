#!/usr/bin/env python3

import sys

input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int,input().split()))

XY = list()
for i in range(N):
    XY.append((A[i], i+1))
XY.sort()

Ans = list()
for x,y in XY:
    Ans.append(y)

print(*Ans)