# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()
from collections import Counter

D = dict(Counter(S))

Ans = []
for x in "ABCDEF":
    ans = D.get(x)
    if ans:
        Ans.append(ans)
    else:
        Ans.append(0)

print(*Ans)