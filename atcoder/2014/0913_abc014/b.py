# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,X = input().split()
A = list(map(int,input().split()))

bit = bin(int(X))[2:].zfill(int(N))
rbit = bit[::-1]

ans = 0
for i in range(len(rbit)):
    if rbit[i]=="1":
        ans += A[i]

print(ans)