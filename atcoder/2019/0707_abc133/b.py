# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1,N):
        total = 0
        for k in range(D):
            total += (X[i][k] - X[j][k])**2
        if int(total**.5)**2 == total:
            ans += 1

print(ans)
