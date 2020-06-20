# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]

from itertools import product
prod = product(range(K),repeat=N)

ans = "Nothing"
for p in prod:
    check = 0
    for i in range(N):
        check ^= T[i][p[i]]
    if check==0:
        ans = "Found"
        break

print(ans)
