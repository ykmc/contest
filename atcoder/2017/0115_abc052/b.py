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
S = input().rstrip()

ans,x = 0,0
for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans,x)

print(ans)