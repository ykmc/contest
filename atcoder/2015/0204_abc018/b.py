# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()
N = int(input())
LR = [tuple(map(int,input().split())) for _ in range(N)]

ans = list(S)
for l,r in LR:
    l,r = l-1,r-1
    ans = ans[0:l] + ans[l:r+1][::-1] + ans[r+1:]

print("".join(ans))