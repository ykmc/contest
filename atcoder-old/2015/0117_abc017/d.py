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
F = [int(input()) for _ in range(N)]

mod = 10**9+7

# dp[i] : ある日の終了時点で, i番目のサプリメントまでを摂取する組み合わせ
# dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k]
#  - i-k のサプリメントは i のサプリメントと同じ
#  - i-k+1 からのサプリメントは i のサプリメントと異なる
#    - dp[i-k] : i-k まで前日に摂取し、i-k+1 ... i まである日に摂取する組み合わせ
#      ...
#    - dp[i-1] : i-1 まで前日に摂取し、i をある日に摂取する組み合わせ
dp = [0]*(N+1)
dp[0] = 1

from collections import defaultdict
d = defaultdict(int)

total = dp[0]

left = 0
for i in range(N):
    # i番目のサプリを1つふやす
    d[F[i]] += 1
    # その結果, 同種のサプリが複数になったら, 1つになるまで左端を縮める
    while d[F[i]] > 1:
        d[F[left]] -= 1
        # 合計値も計算し直す
        total -= dp[left]
        if total < 0:
            total += mod
        total %= mod
        left += 1

    dp[i+1] = total

    total += dp[i+1]
    total %= mod

print(dp[N])
    
