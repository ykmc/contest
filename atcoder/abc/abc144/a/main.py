#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    A,B = map(int,input().split())
    if A < 10 and B < 10:
        print(A*B)
    else:
        print(-1)

if __name__ == "__main__":
    main()