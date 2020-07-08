#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    R = int(input())
    print(R**2)

if __name__ == "__main__":
    main()