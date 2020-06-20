# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
A = list(int(input()) for _ in range(M))

mod = 10**9+7

# 床が壊れてる階段を高速に判別できるように
B = [True]*(N+1)
for a in A:
    B[a] = False

# dp[i] : i番目の階段までの場合の数
dp = [0]*(N+1) 
dp[0] = 1
dp[1] = 1 if 1 not in A else 0 

for i in range(2,N+1):
    if B[i]:
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= mod

print(dp[N])
