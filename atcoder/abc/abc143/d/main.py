#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

from bisect import bisect_right

def main():
    N = int(input())
    L = list(map(int,input().split()))

    L.sort()
    ans = 0
    for b in range(N):
        for a in range(b+1,N):
            upper = b
            lower = bisect_right(L, L[a] - L[b])
            ans += max(0, upper - lower)
    
    print(ans)
    
if __name__ == "__main__":
    main()