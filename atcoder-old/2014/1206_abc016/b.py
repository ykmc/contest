# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B,C = map(int,input().split())

if A+B==C:
    if A-B==C:
        ans = "?"
    else:
        ans = "+"
else:
    if A-B==C:
        ans = "-"
    else:
        ans = "!"

print(ans)