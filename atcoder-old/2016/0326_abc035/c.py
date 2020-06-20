# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
n,q = map(int,input().split())
LR = [tuple(map(int,input().split())) for _ in range(q)]

A = [0]*(n+1)
for l,r in LR:
    A[l-1] += 1
    A[r] -= 1

for i in range(n):
    A[i] %= 2
    A[i+1] += A[i]

print("".join(map(str,A[:n])))
