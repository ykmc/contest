#!/usr/bin/env python

import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
input = sys.stdin.buffer.readline
INF = float("inf")

def main():
    N,M = map(int,input().split())
    G = [[] for _ in range(N)]
    AB = [tuple(map(int,input().split())) for _ in range(M)]
    for a,b in AB:
        G[a-1].append(b-1)

    Ans = [1]*(N+1)
    
    # 全ての頂点から, 閉路が存在しないかを確認する
    for s in range(N):
        prev = [-1]*N
        dist = [-1]*N
        dist[s] = 0
        dq = deque([s])
        while dq:
            v = dq.popleft()
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    prev[nv] = v
                    dq.append(nv)
                # 次が 0番目(開始地点) なら閉路あり
                if dist[nv] == 0 and prev[nv] == -1:
                    prev[nv] = v

        # 開始地点の前 が -1でない => 閉路あり
        if prev[s] != -1:
            v = prev[s]
            ans = set()
            for _ in range(max(dist)+1):
                ans.add(prev[v])
                v = prev[v]
            if len(Ans) > len(ans):
                Ans = list(ans)
    
    if len(Ans) == N+1:
        print(-1)
    else:
        print(len(Ans))
        Ans.sort()
        for v in Ans:
            print(v+1)

if __name__ == "__main__":
    main()