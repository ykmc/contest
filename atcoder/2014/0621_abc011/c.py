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
NG = [int(input()) for _ in range(3)]

inf = float("inf")
dp = [inf]*(N+4)
dp[N] = 0
for i in range(N):
    dp[N-1-i] = min(
        dp[N-1-i+1]+1 if N-1-i+1 not in NG else inf, \
        dp[N-1-i+2]+1 if N-1-i+2 not in NG else inf, \
        dp[N-1-i+3]+1 if N-1-i+3 not in NG else inf, \
    )

print("YES" if dp[0]<=100 else "NO")