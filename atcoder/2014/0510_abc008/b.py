# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
from collections import defaultdict
d = defaultdict(int)

N = int(input())
S = [input().rstrip() for _ in range(N)]

for s in S:
    d[s] += 1

a = sorted(d.items(), key = lambda x:x[1], reverse=True)
print(a[0][0])