# Python3 (3.4.3)
import sys
input = sys.stdin.readline
from collections import deque

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def solve(x):
    cost = [[10**13]*W for _ in range(H)]
    cost[sy][sx] = 0
    dq = deque([(sy,sx)])
    while dq:
        cy,cx = dq.popleft()
        for dy,dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W:
                if S[ny][nx] == "#":
                    d = x
                else:
                    d = 1
                if cost[cy][cx] + d < cost[ny][nx]:
                    cost[ny][nx] = cost[cy][cx] + d
                    dq.append((ny,nx))
    return T >= cost[gy][gx]

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
H,W,T = map(int,input().split())
S = [input().rstrip() for _ in range(H)]

for y in range(H):
    for x in range(W):
        if S[y][x] == "S":
            sx,sy = x,y
        if S[y][x] == "G":
            gx,gy = x,y

ok = 0
ng = T
while ng > ok + 1:
    mid = (ng + ok) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)