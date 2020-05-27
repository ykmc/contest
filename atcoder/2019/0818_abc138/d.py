# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def BFS(dq):
    while dq:
        e = dq.popleft()
        visited[e] = True
        for i in G[e]:
            if not visited[i]:
                P[i] += P[e]
                dq.append(i)

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,Q = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N-1)]
PX = [tuple(map(int,input().split())) for _ in range(Q)]

G = [[] for _ in range(N)]
for a,b in AB:
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# 各頂点が "カウンター増加の根" として直接増加する数
P = [0]*N
for p,x in PX:
    P[p-1] += x

# 訪問済みフラグ
visited = [False]*N
visited[0] = True

Ans = [0]*N
from collections import deque
BFS(deque([0]))

print(*P)