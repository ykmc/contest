#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    A,B = map(int,input().split())
    print(max(0, A-B*2))


if __name__ == "__main__":
    main()