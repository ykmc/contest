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
A = list(map(int,input().split()))

B = []
for a in A:
    if a > 0:
        B.append(a)

from math import ceil
print(ceil(sum(B)/len(B)))
