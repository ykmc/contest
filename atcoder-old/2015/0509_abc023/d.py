# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def solve(n):
    turns = []
    for h,s in HS:
        # 目標の高さを初期状態で超えている
        if h > n: return False
        # 目標の高さに到達するまでの秒数
        t = (n-h)/s
        turns.append(t)
    # 余裕がない方から順番に射撃し, 間に合うかどうか
    return all(i<=t for i,t in enumerate(sorted(turns)))

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
HS = [tuple(map(int,input().split())) for _ in range(N)]

ok = 10**15
ng = 0
while ok - ng > 1:
    mid = (ok+ng)//2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)