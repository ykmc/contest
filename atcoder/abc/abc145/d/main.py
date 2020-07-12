#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

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

def main():
    X,Y = map(int,input().split())

    if (X+Y)%3 != 0:
        print(0)
    else:
        # 操作回数
        n = (X+Y)//3
        # 移動を簡略化, (1,2) => (0,1), (2,1) => (1,0) に
        X -= n
        Y -= n
        # 負の領域には移動不可能
        if X < 0 or Y < 0:
            print(0)
        else:
            modinv = Modinv(10**6+10, 10**9+7)
            print(modinv.nCr(X+Y,X))


if __name__ == "__main__":
    main()