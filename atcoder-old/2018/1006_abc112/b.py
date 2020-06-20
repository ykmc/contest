# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,T = map(int,input().split())
CT = [tuple(map(int,input().split())) for _ in range(N)]

INF = float("inf")
ans = INF
for c,t in CT:
    if t <= T and c < ans:
        ans = c

print(ans if ans != INF else "TLE")