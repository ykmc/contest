# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,X = map(int,input().split())
L = list(map(int,input().split()))

total = 0
ans = 1
for l in L:
    total += l
    if total <= X:
        ans += 1
    else:
        break

print(ans)