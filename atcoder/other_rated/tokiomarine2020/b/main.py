#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)

def main():
    A,V = map(int,input().split())
    B,W = map(int,input().split())
    T = int(input())

    dx = abs(A-B)
    dv = V-W

    if dv*T >= dx:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()