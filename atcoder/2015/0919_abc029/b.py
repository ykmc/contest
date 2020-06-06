# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = [input().rstrip() for _ in range(12)]

ans = 0
for s in S:
    if s.count("r") > 0:
        ans += 1

print(ans)