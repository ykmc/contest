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
XU = [tuple(input().split()) for _ in range(N)]

ans = 0
for x,u in XU:
    if u == "JPY":
        ans += float(x)
    else:
        ans += float(x)*380000

print(ans)