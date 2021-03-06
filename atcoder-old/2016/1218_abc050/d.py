# PyPy3 (2.4.0)
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
# 配列添字が大きい部分を上位桁にするために逆順にする
binN = format(N,"061b")[::-1]

# dp[i][j] : 上からi桁までみて, a+b = N-j となる通り数
# j は 2まで考えれば良い, 上からk桁までで 2以上小さい場合, k+1桁目から繰り上がりがあってもa+bを超えることはないため
dp = [[0,0,0] for _ in range(61)]
dp[60][0] = 1
 
for i in range(59,-1,-1):
    # i桁目のbitが 1
    if binN[i]=="1":
        # 一致
        #  - i+1桁目までは一致の場合, i桁目は(0,0)で一致
        dp[i][0] = dp[i+1][0]
        # 1差
        #  - i+1桁目までは一致の場合, i桁目は(0,0)で1差
        #  - i+1桁目までで1差の場合, i桁目では2差, (1,1)で1差
        dp[i][1] = dp[i+1][0] + dp[i+1][1]
        # 2差以上
        #  - i+1桁目までは1差の場合, i桁目では2差, (1,0)で2差
        #  - i+1桁目までで2差以上の場合, i桁目では4差以上,(0,0),(1,0),(1,1)全てで2差以上
        dp[i][2] = 2*dp[i+1][1] + 3*dp[i+1][2]
    # i桁目のbitが 0
    else:
        # 一致
        #  - i+1桁目までは一致の場合, i桁目は(0,0)で一致
        #  - i+1桁目までで1差の場合, i桁目では2差, (1,1)で一致
        dp[i][0] = dp[i+1][0] + dp[i+1][1]
        # 1差
        #  - i+1桁目までで1差の場合, i桁目では2差になるので, (1,0)で1差
        dp[i][1] = dp[i+1][1]
        # 2差以上
        #  - i+1桁目までは1差の場合, i桁目では2差, (0,0)で2差
        #  - i+1桁目までで2差以上の場合, i桁目では4差以上,(0,0),(1,0),(1,1)全てで2差以上
        dp[i][2] = dp[i+1][1] + 3*dp[i+1][2]
 
    for j in range(3):
        dp[i][j] %= mod
 
print((dp[0][0] + dp[0][1] + dp[0][2]) % mod)