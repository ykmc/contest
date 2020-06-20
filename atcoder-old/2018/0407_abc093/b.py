# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B,K = map(int,input().split())

s = set()

for i in range(K):
    if A <= A+i <= B:
        s.add(A+i)
    if A <= B-i <= B:
        s.add(B-i)

Ans = list(s)
Ans.sort()

for ans in Ans:
    print(ans)