# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
class Modinv:
    def __init__(self, n, mod):
        self.mod = mod
        self.fact = [1]*n
        self.finv = [1]*n
        self.inv  = [1]*n
        for i in range(2,n):
            self.fact[i] = (self.fact[i-1]*i) % self.mod
            self.inv[i]  = self.mod - self.inv[self.mod%i] * (self.mod//i)%self.mod
            self.finv[i] = self.finv[i-1] * self.inv[i] % self.mod

    def nPr(self, n, r):
        if n<r:
            return 0
        else:
            return self.fact[n] * self.finv[n-r] % self.mod

    def nCr(self, n, r):
        if n<r:
            return 0
        else:
            return self.fact[n] * (self.finv[r] * self.finv[n-r] % self.mod) % self.mod

    def nHr(self, n, r):
        return self.nCr(n-1+r, n-1)

mod = 10**9+7
Modinv = Modinv(200010, mod)

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
K = int(input())

print(Modinv.nHr(N,K))

