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
D,X = map(int,input().split())
A = [int(input()) for _ in range(N)]
 
from math import ceil
ans = 0
for i in range(N):
    ans += ceil(D/A[i])
 
print(ans+X)