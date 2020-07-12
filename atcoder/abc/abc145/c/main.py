#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N = int(input())
    XY = [tuple(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        xi,yi = XY[i]
        for j in range(i+1,N):
            xj,yj = XY[j]
            ans += ((xi-xj)**2 + (yi-yj)**2)**.5
    
    print(ans*2/N)

if __name__ == "__main__":
    main()