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
S = list(map(int,input().split()))
T = list(map(int,input().split()))
mod = 10**9+7

# dp[i][j] : Sの左からi文字目までと Tの左からj文字目まででの 共通部分文字列の数
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        if 0<=i-1 and 0<=j-1 and S[i-1]==T[j-1]:
            dp[i][j] += dp[i-1][j-1]
        if 0<=i-1:
            dp[i][j] += dp[i-1][j]
        if 0<=j-1:
            dp[i][j] += dp[i][j-1]
        # 重複カウント部分を減算する
        if 0<=i-1 and 0<=j-1:
            dp[i][j] -= dp[i-1][j-1]
        dp[i][j] %= mod

print(dp[N][M])
