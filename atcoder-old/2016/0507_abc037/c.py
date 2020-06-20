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
A = list(map(int,input().split()))

K = min(K,N-K+1)
ans = 0
for i in range(N):
    if i < K:
        ans += A[i]*(i+1)
    elif i < N-K:
        ans += A[i]*K
    else:
        ans += A[i]*(N-i)

print(ans)