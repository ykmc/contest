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
AA = []
for _ in range(N):
    KA = list(map(int,input().split()))
    AA.append(KA[1::])

from collections import defaultdict
dic = defaultdict(int)
for A in AA:
    for a in A:
        dic[a] += 1

ans = 0
for v in dic.values():
    if v==N:
        ans += 1

print(ans)