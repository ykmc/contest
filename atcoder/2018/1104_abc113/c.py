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
PY = [tuple(map(int,input().split())) for _ in range(M)]

# 県ごとに分類
A = [[] for _ in range(N+1)]
for i in range(M):
    p,y = PY[i]
    A[p].append((y,i))

for i in range(1,N+1):
    A[i].sort()

Ans = [0]*M
for i in range(1,N+1):
    for j in range(len(A[i])):
        y,k = A[i][j]
        Ans[k] = "{:06d}{:06d}".format(i,j+1)

for ans in Ans:
    print(ans)