# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
R,C,K = map(int,input().split())
N = int(input())
RC = [tuple(map(int,input().split())) for _ in range(N)]

from collections import defaultdict
dr = defaultdict(int)
dc = defaultdict(int)

for r,c in RC:
    dr[r-1] += 1
    dc[c-1] += 1

sr = defaultdict(int)
for r in range(R):
    sr[dr[r]] += 1
sc = defaultdict(int)
for c in range(C):
    sc[dc[c]] += 1

ans = 0
for i in range(K+1):
    r = i
    c = K-r
    ans += sr[r] * sc[c]

# 飴がある場合, 二重にカウントしているので調整
for r,c in RC:
    if dr[r-1] + dc[c-1] == K:
        ans -= 1
    if dr[r-1] + dc[c-1] == K+1:
        ans += 1

print(ans)