#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N = int(input())

    F = [0]*(N+1)
    for x in range(1, int(N**.5)+1):
        for y in range(1, int(N**.5)+1):
            for z in range(1, int(N**.5)+1):
                a = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if a <= N:
                    F[a] += 1
    
    for i in range(1,N+1):
        print(F[i])

if __name__ == "__main__":
    main()