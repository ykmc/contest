#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N = int(input())
    A = list(map(int,input().split()))

    ans = 0
    for i in range(N):
        if i%2 == 0 and A[i]%2 == 1:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()