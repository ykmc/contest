# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
W = int(input())
N,K = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N)]

# dp[i][j] : i枚目までから選択し, 重要度の合計がjとなる最小の幅
#   - 重要度の合計は余裕を持った長さにしている
dp = [[W+1 for _ in range(100*N+200)] for _ in range(N+1)]
# 初期化
dp[0][0] = 0
 
for k in range(N):
    a,b = AB[k]
    for i in range(k,-1,-1):
        # 価値の合計のループは, これまで使ったスクショの価値の総和を超えることはあり得ないので,
        # ループ上限を動的に更新していくことでPython3でも通せる (けどややこしいので...)
        for j in range(100*N,-1,-1):
            dp[i+1][j+b] = min(dp[i+1][j+b], dp[i][j]+a)
 
ans = 0
for i in range(1,K+1):
    for j in range(100*N+1):
        if dp[i][j] <= W:
            ans = max(ans, j)
 
print(ans)