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
S = input().rstrip() + "Z"
LR = [map(int,input().split()) for _ in range(Q)]

A = [0]*(N+1)
for i in range(N):
    if S[i]=="A" and S[i+1]=="C":
        A[i+1] = 1
for i in range(i):
    A[i+1] += A[i]

for l,r in LR:
    print(A[r-1]-A[l-1])