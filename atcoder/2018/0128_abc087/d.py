# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.weight = [0]*n
    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y
    
    def union(self, x, y, w):
        px = self.find(x)
        py = self.find(y)
        d = w - self.weight[x] + self.weight[y]
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
            self.weight[px] = d
        else:
            self.par[py] = px
            self.weight[py] = -d
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
G = WeightedUnionFind(N)

for i in range(M):
    l,r,d = map(int,input().split())
    l -= 1
    r -= 1
    if G.same(l,r):
        if G.diff(l,r) != d:
            print("No")
            sys.exit()
    else:
        G.union(l,r,d)
    
print("Yes")
