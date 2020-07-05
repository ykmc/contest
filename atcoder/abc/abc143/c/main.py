#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N = int(input())
    S = input()

    ans = 1
    for i in range(N-1):
        if S[i+1] != S[i]:
            ans += 1

    print(ans)
    
if __name__ == "__main__":
    main()