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

total = 0
for i in range(1,10):
    for j in range(1,10):
        total += i*j

M = total - N
Ans = []
for i in range(1,M+1):
    j = M//i
    if i*j==M and 1<=i<=9 and 1<=j<=9:
        Ans.append((i,j))

for i,j in Ans:
    print(i, "x", j)