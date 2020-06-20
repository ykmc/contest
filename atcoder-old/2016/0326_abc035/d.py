# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
import heapq
inf = float("inf")
def dijkstra(nodeNum, start, adjList):
    cost = [inf]*nodeNum
    cost[start] = 0
    hq = [(0,start)]
    heapq.heapify(hq)
    while hq:
        hc, hv = heapq.heappop(hq)
        for to, c in adjList[hv]:
            if hc + c >= cost[to]:
                continue
            cost[to] = hc + c
            heapq.heappush(hq, (cost[to],to))
    return cost

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
n,m,t = map(int,input().split())
A = list(map(int,input().split()))
Adj1 = [[] for _ in range(n)]
Adj2 = [[] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    Adj1[a-1].append((b-1,c))
    Adj2[b-1].append((a-1,c))

Cost1 = dijkstra(n,0,Adj1)
Cost2 = dijkstra(n,0,Adj2)

ans = 0
for i in range(n):
    ans = max(ans, A[i]*(t - Cost1[i] - Cost2[i]))

print(ans)
