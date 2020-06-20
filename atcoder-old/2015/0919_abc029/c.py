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

from itertools import product
Ans = list(product("abc", repeat=N))
Ans.sort()

for ans in Ans:
    print("".join(ans))