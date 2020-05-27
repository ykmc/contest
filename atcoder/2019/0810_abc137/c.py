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
S = [list(input().rstrip()) for _ in range(N)]

from collections import defaultdict
d = defaultdict(int)

for s in S:
    s.sort()
    d["".join(s)] += 1

ans = 0
for i in d.values():
    ans += i*(i-1)//2

print(ans)