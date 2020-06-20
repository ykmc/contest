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
S = [input().rstrip() for _ in range(N)]
M = int(input())
T = [input().rstrip() for _ in range(M)]

from collections import defaultdict
dic = defaultdict(int)

for s in S:
    dic[s] += 1
for t in T:
    dic[t] -= 1

ans = 0
for v in dic.values():
    ans = max(ans, v)

print(ans)