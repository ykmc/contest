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

ans = 0
for b in range(K+1,N+1):
    ans += (N//b)*max(0,b-K) + max(0,N%b-K+1)
    if K==0:
        ans -= 1

print(ans)