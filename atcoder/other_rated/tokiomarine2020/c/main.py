#!/usr/bin/env pypy

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    for _ in range(min(K,50)):
        B = [0]*N
        for i in range(N):
            l = max(0,i-A[i])
            r = min(N-1,i+A[i])
            B[l] += 1
            if r+1 < N:
                B[r+1] -= 1
        for i in range(N-1):
            B[i+1] += B[i]
        A = B

    print(*B)

if __name__ == "__main__":
    main()