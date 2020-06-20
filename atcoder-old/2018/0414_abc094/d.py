# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))

# nCr : nが大きく、rがnの半分くらいの時が最大
maxA = max(A)
half = maxA/2

t = 10**10
for i in range(N):
    # 最大の要素ではない and 真ん中からの絶対値が小さい → 値を更新
    if A[i] != maxA and abs(A[i]-half) < abs(t-half):
        t = A[i]

print(maxA,t)