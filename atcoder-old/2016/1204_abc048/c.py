# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,X = map(int,input().split())
A = list(map(int,input().split()))

ans = 0 
if A[0]>X:
    ans = A[0]-X
    A[0] -= ans

for i in range(N-1):
    r = max(A[i]+A[i+1]-X,0)
    A[i+1] -= r
    ans += r

print(ans)