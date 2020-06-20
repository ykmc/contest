# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x = C
    for j in range(M):
        x += A[i][j]*B[j]
    if x > 0:
        ans += 1

print(ans)