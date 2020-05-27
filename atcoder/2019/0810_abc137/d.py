# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N)]

AB.sort(reverse=True)

import heapq
hq = []
ans = 0
for i in range(1,M+1):
    # n日 (n : 1-M) 後に受け取れる仕事を優先度つきキューに入れる
    # 高いものを優先的に出したいので負にしておく
    while AB and AB[-1][0] <= i:
        a,b = AB.pop()
        heapq.heappush(hq, -b)
    # 可能な仕事があれば, 一番高い仕事を行う
    #  - 値が負なので減算する
    if hq:
        ans -= heapq.heappop(hq)

print(ans)