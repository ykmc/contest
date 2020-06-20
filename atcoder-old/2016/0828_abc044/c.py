# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,A = map(int,input().split())
X = [0] + list(map(int,input().split())) # 1枚も選ばない場合として 0 を足しておく

# dp[n][k][d] : n枚からk枚選んで合計dにする選び方
dp = [[[0 for _ in range(50*N+1)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for n in range(N+1):
    for k in range(n+1):
        for d in range(50*k+1):
            # 目指す "合計の数 : d" がn枚目のカードより小さい場合, そのカードは使えない
            if d < X[n]:
                dp[n][k][d] = dp[n-1][k][d]
            # そうでない場合
            else:
                # k==0のときはカードを選べないことに注意
                if k >= 1:
                    dp[n][k][d] = dp[n-1][k][d] + dp[n-1][k-1][d-X[n]]
                    # dp[n-1][k][d] : k枚目のカードを選ばない場合
                    # dp[n-1][k-1][d-X[n]] : k枚目のカードを選ぶ場合。n-1枚目までで合計 d-X[n] であれば良い。

ans = 0
for i in range(1,N+1): # 0を除く、0のときは「0枚から0枚選んで0にする」で1通りになるが、これは答えには含まれない
    # N枚からi枚選んで平均がA,つまり合計がA*i
    ans += dp[N][i][A*i]

print(ans)