# Python3 (3.4.3)
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
Combination = Combination(2010, mod)

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())

# 青の連続部分の数で全探索
for i in range(1,K+1):
    ans = 1
    # 青を複数の連続部分に分割する場合の数
    ans *= Combination.nCr(K-1,i-1)
    # 赤を一列に並べた時の, 両端を含めた"青の連続部分の挿入可能箇所"
    x = N-K+1
    # x箇所から i箇所に 青を挿入する
    ans *= Combination.nCr(x,i)
    print(ans%mod)
