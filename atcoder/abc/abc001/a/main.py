#!/usr/bin/env python3

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H1,H2 = map(int,read().split())
print(H1-H2)