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
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans = max(ans, sum(A1[0:i+1])+sum(A2[i:N]))

print(ans)