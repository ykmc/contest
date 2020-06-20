# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
L = input().rstrip()

lenL = len(L)
mod = 10**9+7

dp0 = [0]*(lenL+1) # dp0[i] : 上からi桁目まで L と一致する (A,B) の場合の数
dp1 = [0]*(lenL+1) # dp1[i] : 上からi桁目までで L と一致しない (A,B) の場合の数

dp0[0] = 1

for i,l in enumerate(L, 1):
    # 現在の桁が 0 の時
    if l=="0":
        dp0[i] = dp0[i-1]   # (0,0) のみ
        dp1[i] = dp1[i-1]*3 # (0,0), (0,1), (1,0) の3通り
    # 現在の桁が 1 の時
    else:
        dp0[i] = dp0[i-1]*2 # (0,1), (1,0)
        dp1[i] = dp0[i-1] + dp1[i-1]*3 
        # (i-1)桁まで一致している場合, (0,0) のみ
        # (i-1)桁まで一致していない場合, (0,0), (0,1), (1,0) の3通り
    dp0[i] %= mod
    dp1[i] %= mod

print((dp0[-1] + dp1[-1]) % mod)