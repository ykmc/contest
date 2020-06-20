# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
H = [int(input()) for _ in range(N)]

H.sort()

ans = 10**10
for i in range(N-K+1):
    ans = min(ans, H[i+K-1]-H[i])

print(ans)