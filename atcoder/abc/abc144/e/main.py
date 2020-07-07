#!/usr/bin/env pypy

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

import math

def solve(x, N, K, A, F):
    total = 0
    for i in range(N):
        total += max(0, math.ceil((A[i]*F[i] - x) / F[i]))
    if total <= K:
        return True
    else:
        return False

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    F = list(map(int,input().split()))

    A.sort()
    F.sort(reverse=True)

    ok = 10**13+1
    ng = -1
    while ok - ng > 1:
        mid = (ng + ok) // 2
        if solve(mid, N, K, A, F):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == "__main__":
    main()