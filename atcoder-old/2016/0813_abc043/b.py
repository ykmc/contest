# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
from collections import deque

S = input().rstrip()
d = deque()

for s in S:
    if s == "B":
        if len(d) > 0:
            d.pop()
    else:
        d.append(s)

print("".join(d))