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
P = list(map(int,input().split()))

for i in range(N):
    if P[i] != i+1:
        j = P.index(i+1)
        P[i],P[j] = P[j],P[i]
        break

print("YES" if P == list(range(1,N+1)) else "NO")