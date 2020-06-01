# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = input().rstrip()

ans = ""
for n in N:
    if n == "1":
        ans += "9"
    elif n == "9":
        ans += "1"
    else:
        ans += n

print(ans)