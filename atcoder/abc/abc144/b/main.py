#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i*j == N:
                print("Yes")
                exit()
    print("No")

if __name__ == "__main__":
    main()