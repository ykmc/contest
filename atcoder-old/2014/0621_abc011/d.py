# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
import math
def nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,D = map(int,input().split())
X,Y = map(int,input().split())

ans = 0
# ジャンプ幅で割り切れる場合のみ考えれば良い
if X%D==0 and Y%D==0:
    X,Y = abs(X//D),abs(Y//D)
    D = 1
    # x軸方向の移動回数で全探索
    for dx in range(N+1):
        dy = N-dx
        # 届かない
        if X > dx or Y > dy:
            continue
        # 止まれない
        if (dx-X)%2==1 or (dy-Y)%2==1:
            continue
        # X軸,Y軸それぞれ求める
        pX = nCr(dx, (dx-X)//2)
        pY = nCr(dy, (dy-Y)//2)
        ans += pX/(2**N) * pY/(2**N) * nCr(N, dx) # /(4**N) とやるとoverflowする...

print(ans)
