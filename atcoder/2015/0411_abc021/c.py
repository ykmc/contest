# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
A,B = map(int,input().split())
M = int(input())
XY = [tuple(map(int,input().split())) for _ in range(M)]
mod = 10**9+7

from collections import deque
dq = deque([A])

inf = float("inf")
dist = [[inf,0] for _ in range(N+1)]
dist[A][0] = 0
dist[A][1] = 1

E = [[] for _ in range(N+1)]
for x,y in XY:
    E[x].append(y)
    E[y].append(x)

while dq:
    v = dq.popleft()
    for e in E[v]:
        if dist[v][0] + 1 < dist[e][0]:
            dist[e][0] = dist[v][0] + 1
            dist[e][1] = dist[v][1]
            if e != B:
                dq.append(e)
        elif dist[v][0] + 1 == dist[e][0]:
            dist[e][1] += dist[v][1]

print(dist[B][1] % mod)
