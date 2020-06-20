import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def check(self, x, y):
        return self.find(x) == self.find(y)

N,M = map(int,input().split())
XYZ = list()
for i in range(M):
    x,y,z = map(int,input().split())
    XYZ.append((x,y,z))

uf = UnionFind(N)
for xyz in XYZ:
    x,y,z = xyz
    uf.unite(x-1,y-1)

ans = set()
for i in range(N):
    ans.add(uf.find(i))

print(len(ans))
