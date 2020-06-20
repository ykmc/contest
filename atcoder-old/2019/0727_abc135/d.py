# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()
mod = 10**9+7

# dp[i][j] : 上から i 桁までの数字で, 13で割ったあまりが j になる場合の数
dp = [[0 for _ in range(13)] for _ in range(len(S))]

# 初期化
if S[0] == "?":
    for i in range(10):
        dp[0][i] += 1
else:
    dp[0][int(S[0])] = 1

# dp更新
for i in range(1,len(S)):
    if S[i] == "?":
        for j in range(13):
            for k in range(10):
                dp[i][(j*10 + k) % 13] += dp[i-1][j]
                dp[i][(j*10 + k) % 13] %= mod
    else:
        for j in range(13):
            dp[i][(j*10 + int(S[i])) % 13] += dp[i-1][j]
            dp[i][(j*10 + int(S[i])) % 13] %= mod

print(dp[-1][5])