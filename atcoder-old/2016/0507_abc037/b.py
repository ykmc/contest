# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,Q = map(int,input().split())
LRT = [tuple(map(int,input().split())) for _ in range(Q)]

Ans = [0]*N

for l,r,t in LRT:
    for i in range(l-1,r):
        Ans[i] = t

for ans in Ans:
    print(ans)