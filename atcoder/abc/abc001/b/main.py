#!/usr/bin/env python3

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

m = int(read())

ans = 0
if m < 100:
    ans = 0
elif m <= 5000:
    ans = m//100
elif m <= 30000:
    ans = m//1000 + 50
elif m <= 70000:
    ans = (m//1000-30)//5 + 80
else:
    ans = 89
 
print("{0:02d}".format(ans))