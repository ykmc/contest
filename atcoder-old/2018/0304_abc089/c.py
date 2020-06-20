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

from collections import defaultdict
d = defaultdict(int)

for s in S:
    key = s[0]
    d[key] += 1

from itertools import combinations
c = combinations("MARCH",3)
ans = 0
for x,y,z in c:
    ans += d[x]*d[y]*d[z]

print(ans)