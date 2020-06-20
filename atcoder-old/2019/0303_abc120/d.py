# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.size = [1]*(n+1)
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        else:
            if self.size[x] < self.size[y]:
                self.par[x] = y
                self.size[y] += self.size[x]
            else:
                self.par[y] = x
                self.size[x] += self.size[y]
    def check(self, x, y):
        return self.find(x) == self.find(y)
    def cnt(self, x):
        return self.size[self.find(x)]

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(M)]

uf = UnionFind(N+1)
cnt = N*(N-1)//2
Ans = [0]*(M+1)
Ans[-1] = cnt
for i in range(M):
    a,b = AB[M-1-i]
    # 元々連結な場合
    if uf.check(a,b):
        Ans[M-1-i] = cnt
    # 元々連結ではない場合
    else:
        cnt -= uf.cnt(a)*uf.cnt(b)
        Ans[M-1-i] = cnt
    uf.unite(a,b)

for i in range(1,M+1):
    print(Ans[i])