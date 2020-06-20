# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(M)]

A = [[float("inf") for _ in range(N)] for _ in range(N)]
for a,b in AB:
    A[a-1][b-1] = 1
    A[b-1][a-1] = 1
for i in range(N):
    A[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            A[i][j] = min(A[i][j], A[i][k]+A[k][j])

for i in range(N):
    print(A[i].count(2))