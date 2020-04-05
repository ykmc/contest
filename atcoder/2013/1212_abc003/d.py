# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
class Combination:
    def __init__(self, n, mod):
        self.mod = mod
        self.fact = [1]*n
        self.finv = [1]*n
        self.inv  = [1]*n
        for i in range(2,n):
            self.fact[i] = (self.fact[i-1]*i) % self.mod
            self.inv[i]  = self.mod - self.inv[self.mod%i] * (self.mod//i)%self.mod
            self.finv[i] = self.finv[i-1] * self.inv[i] % self.mod
 
    def nCr(self, n, r):
        if n<r:
            return 0
        else:
            return self.fact[n] * (self.finv[r] * self.finv[n-r] % self.mod) % self.mod

mod = 10**9+7
Combination = Combination(1000, mod)


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
R,C = map(int,input().split())
X,Y = map(int,input().split())
D,L = map(int,input().split())

# [x * y 区画]にデスクd個, サーバl個を配置する場合の数
def DL(x,y,d,l):
    if x <= 0 or y <= 0:
        return 0
    else:
        return (Combination.nCr(x*y, d) * Combination.nCr(x*y-d, l)) % mod

# [XY区画] にデスクD個 + サーバL個を配置する場合の数
ans = DL(X, Y, D, L)

ans -= DL((X-1), Y, D, L)*2 # X方向の両端どちらかに何も配置されていない場合
ans -= DL(X, (Y-1), D, L)*2 # Y方向の両端どちらかに何も配置されていない場合

ans += DL((X-1), (Y-1), D, L)*4 # X方向, Y方向ともに片方に何も配置されていない場合
ans += DL((X-2), Y, D, L) # X方向の両端ともに何も配置されていない場合
ans += DL(X, (Y-2), D, L) # Y方向の両端ともに何も配置されていない場合

ans -= DL((X-2), (Y-1), D, L)*2 # X方向が両端, Y方向が片方, 何も配置されていない場合
ans -= DL((X-1), (Y-2), D, L)*2 # X方向が片方, Y方向が両方, 何も配置されていない場合

ans += DL((X-2), (Y-2), D, L) # X方向Y方向とも, 両端に何も配置されていない場合

ans %= mod

# [RC区画] に [XY区画] を配置する場合の数
ans *= (R-X+1)*(C-Y+1)
ans %= mod

print(ans)