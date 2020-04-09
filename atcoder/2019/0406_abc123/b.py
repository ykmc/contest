# Python3 (3.4.3)
import sys
input = sys.stdin.readline
from math import ceil,floor

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A = [int(input()) for _ in range(5)]

total = 0
rem = 10
for a in A:
    total += ceil(a/10)*10
    rem = min(rem, (a-1)%10+1)

print(total-10+rem)