# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------

N,M = map(int,input().split())
A = list(map(int,input().split()))
BC = [tuple(map(int,input().split())) for _ in range(M)]

A.sort()
BC.sort(key = lambda x:x[1], reverse=True)

X = [0]*N
i = 0
for b,c in BC:
    for j in range(b):
        if i+j >= N:
            break
        X[i+j] = c
    i += b

ans = 0
for i in range(N):
    A[i] = max(A[i], X[i])
    ans += A[i]

print(ans)
