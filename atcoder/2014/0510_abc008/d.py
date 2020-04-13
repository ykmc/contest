# Python3 (3.4.3)
import sys
input = sys.stdin.readline
from functools import lru_cache

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
@lru_cache(maxsize=10**6)
def DFS(L,R,D,U):
    max_cnt = 0
    for x,y in XY:
        # 範囲外ならスキップ
        if not (L<=x<=R and D<=y<=U):
            continue
        cnt = R-L + U-D + 1
        cnt += DFS(x+1,R,y+1,U)
        cnt += DFS(L,x-1,y+1,U)
        cnt += DFS(L,x-1,D,y-1)
        cnt += DFS(x+1,R,D,y-1)
        max_cnt = max(max_cnt, cnt)
    return max_cnt


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
W,H = map(int,input().split())
N = int(input())
XY = [tuple(map(int,input().split())) for _ in range(N)]

ans = DFS(1,W,1,H)
print(ans)