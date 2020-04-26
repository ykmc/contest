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
ABT = [tuple(map(int,input().split())) for _ in range(M)]

import numpy as np
import scipy.sparse.csgraph as csg
inf = float("inf")

A = np.array([[inf]*N]*N)
for a,b,t in ABT:
    A[a-1][b-1] = t
    A[b-1][a-1] = t

A = csg.floyd_warshall(A)
 
ans = inf
for i in range(N):
    ans = min(ans, max(A[i]))
 
print(int(ans))