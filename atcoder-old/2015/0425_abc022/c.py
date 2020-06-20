# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
UVL = [tuple(map(int,input().split())) for _ in range(M)]

import numpy as np
import scipy.sparse.csgraph as csg

INF = float("inf")
A = np.array([[INF]*N]*N)
L = []
for u,v,l in UVL:
    # 始点 (1) からの辺
    if u==1:
        L.append((v-1,l))
    # それ以外
    else:
        A[u-1,v-1] = l
        A[v-1,u-1] = l

A = csg.floyd_warshall(A)

ans = INF
# 求める経路 : 始点からの異なる辺の組み合わせと, それ以外の部分の最短経路 
for li in L:
    for lj in L:
        if li != lj:
            i1,d1 = li
            i2,d2 = lj
            ans = min(ans, d1 + d2 + A[i1][i2])

print(int(ans) if ans != INF else -1)