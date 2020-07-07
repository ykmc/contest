#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N = int(input())

    ans = INF
    for i in range(1,int(N**.5)+1):
        if N%i == 0:
            ans = min(ans, i + N//i - 2)

    print(ans)

if __name__ == "__main__":
    main()