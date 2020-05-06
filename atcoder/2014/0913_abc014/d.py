# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
sys.setrecursionlimit(10**8)
class LowestCommonAncestor():
    def __init__(self,G,root = 0): #O(NlogN)
        self.N = len(G)
        self.G = G
        self.root = root
        self.K = self.N.bit_length() #2 ** K > nとなる最小のK
        self.parents = [[-1] * self.N for _ in range(self.K)]
        self.dist = [-1] * self.N
        
        self._dfs()
        for k in range(self.K - 1):
            for v in range(self.N):
                if self.parents[k][v] >= 0:
                    self.parents[k + 1][v] = self.parents[k][self.parents[k][v]]
    
    def _dfs(self):
        self.dist[self.root] = 0
        stack = [self.root]
        while stack:
            v = stack.pop()
            for e in self.G[v]:
                if self.dist[e] >= 0:
                    self.parents[0][v] = e
                    continue
                self.dist[e] = self.dist[v] + 1
                stack.append(e)
    
    def depth(self,v):
        return self.dist[v]
    
    def query(self,u,v): #O(logN)
        if self.dist[u] < self.dist[v]:
            u,v = v,u
        
        dif = self.dist[u] - self.dist[v]
        for k in range(self.K):
            if dif >> k & 1:
                u = self.parents[k][u]
        
        if u == v:
            return u
        
        for k in range(self.K - 1,-1,-1):
            if self.parents[k][u] != self.parents[k][v]:
                u = self.parents[k][u]
                v = self.parents[k][v]
        
        return self.parents[0][u]

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
XY = [tuple(map(int,input().split())) for _ in range(N-1)]
Q = int(input())
AB = [tuple(map(int,input().split())) for _ in range(Q)]

A = [[] for _ in range(N)]
for x,y in XY:
    A[x-1].append(y-1)
    A[y-1].append(x-1)

lca = LowestCommonAncestor(A)

for a,b in AB:
    l = lca.query(a-1,b-1)
    d = lca.depth(a-1) + lca.depth(b-1) - 2*lca.depth(l) + 1
    print(d)