# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,T = map(int,input().split())
A = list(map(int,input().split()))
 
lowest = 10**9+1
profit = 0
ans = 0

# 買った価格 - 売った価格 が等しくなる区間がいくつあるか が答え(それらの店全てで1円ずつ値上げすればよいので)
# 現時点で購入可能な最安値を記録しておき, 移動するたびに利益が更新可能かチェックする
for a in A:
    lowest = min(lowest, a)
    if a - lowest == profit:
        ans += 1
    elif a - lowest > profit:
        profit = a - lowest
        ans = 1
 
print(ans)