#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
inf = float("inf")

import numpy as np
import scipy.sparse.csgraph as csg

def main():
    N,M,L = map(int,input().split())
    ABC = [tuple(map(int,input().split())) for _ in range(M)]
    Q = int(input())
    ST = [tuple(map(int,input().split())) for _ in range(Q)]

    # 町の最短距離を求める
    A = np.array([[inf]*N]*N)
    for a,b,c in ABC:
        A[a-1][b-1] = c
        A[b-1][a-1] = c
    A = csg.floyd_warshall(A)
    
    # 求めた町の距離が L以下 に 1の辺をはる (給油なしでたどり着ける)
    B = np.array([[inf]*N]*N)
    for i in range(N):
        for j in range(N):
            if A[i][j] <= L:
                B[i][j] = 1
    # 最短距離を求める
    B = csg.floyd_warshall(B)
    
    for s,t in ST:
        if B[s-1][t-1] == inf:
            print(-1)
        else:
            print(int(B[s-1][t-1] - 1))

if __name__ == "__main__":
    main()