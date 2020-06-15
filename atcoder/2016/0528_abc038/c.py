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

ans = 0
cnt = 0
prev = 0
for a in A:
    if prev < a:
        cnt += 1
    else:
        cnt = 1
    ans += cnt
    prev = a

print(ans)