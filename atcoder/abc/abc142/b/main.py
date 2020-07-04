#!/usr/bin/env python3

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,K = map(int,readline().split())
H = list(map(int,readline().split()))

ans = 0
for h in H:
    if h >= K:
        ans += 1

print(ans)