# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = list(map(int,input().split())) # N[0],N[1] = N,M
D = list(map(int,input().split())) # D[0],D[1] = X,Y
T = [[]]*2
T = [list(map(int,input().split())) for _ in range(2)] #A,B

from bisect import bisect_left

# 空港の初期値
ap = 0 
# 現在時刻
now = 0
# 往復カウント
ans = 0

# 最終便に乗れなくなるまでループ
while now <= T[ap][N[ap]-1]:
    i = bisect_left(T[ap], now)
    # 時間経過
    now = T[ap][i] + D[ap]
    # 空港を反転
    ap ^= 1
    # 到着空港が A なら往復カウント
    if ap == 0:
        ans += 1

print(ans)
