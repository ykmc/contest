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
R = [int(input()) for _ in range(N)]

R.sort(reverse=True)
ans = 0
for i in range(N):
    if i%2 == 0:
        ans += R[i]**2
    else:
        ans -= R[i]**2

import math
print(ans*math.pi)