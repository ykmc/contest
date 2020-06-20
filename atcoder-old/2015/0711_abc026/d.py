# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
import math
def solve(x):
    return A*x + B*math.sin(C*x*math.pi) < 100

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B,C = map(int,input().split())

ok = 0
ng = 200
while abs(ng - ok) > 0.0000000000001:
    mid = (ng + ok) / 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)