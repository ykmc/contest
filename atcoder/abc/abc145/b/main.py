#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N = int(input())
    S = input().decode().rstrip()

    if N%2==0 and S[0:N//2]==S[N//2:]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()