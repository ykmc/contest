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
LRS = [tuple(map(int,input().split())) for _ in range(N)]

# Sの合計
total = 0
# 累積和
A = [0]*(M+1)
for l,r,s in LRS:
    A[l-1] += s
    A[r] -= s
    total += s

for i in range(M):
    A[i+1] += A[i]

print(total - min(A[:M]))
