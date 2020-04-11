# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for ai in range(A+1):
    for bi in range(B+1):
        for ci in range(C+1):
            if 500*ai + 100*bi + 50*ci == X:
                ans += 1

print(ans)
