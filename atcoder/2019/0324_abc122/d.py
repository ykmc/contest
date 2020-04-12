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

mod = 10**9+7
# dp[i][a][b][c] : 左からi番目まで文字を決めたときの右端から3文字をc,b,aとしたときの場合の数
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
# a,b,cについて : 0 -> "T", 1 -> "A", 2 -> "G", 3 -> "C"
# 初期値はTTTが左にあると考えても影響はない
dp[0][0][0][0] = 1

for i in range(N):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    # AG*C or A*CG
                    if (a==1 and b==2 and d==3) or (a==1 and c==2 and d==3):
                        continue
                    # *AGC
                    if (b==1 and c==2 and d==3):
                        continue
                    # *GAC or *ACG
                    if (b==2 and c==1 and d==3) or (b==1 and c==3 and d==2):
                        continue
                    dp[i+1][b][c][d] += dp[i][a][b][c]
                    dp[i+1][b][c][d] %= mod

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]

print(ans%mod)
