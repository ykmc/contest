#!/usr/bin/env python3

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(read())

odd = 0
for n in range(N):
    n += 1
    if n%2==1:
        odd += 1

print(odd/N)