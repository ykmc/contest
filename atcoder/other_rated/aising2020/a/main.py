#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    L,R,d = map(int,input().split())

    ans = 0
    for i in range(L,R+1):
        if i%d == 0:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()