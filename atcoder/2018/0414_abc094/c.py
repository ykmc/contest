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
X = list(map(int,input().split()))
 
l  = sorted(X)[N//2-1]
r = sorted(X)[N//2]

for i in range(N):
    if X[i] <= l:
        print(r)
    else:
        print(l)