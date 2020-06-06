# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A = list(map(int,input().split()))

Ans = []
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            Ans.append(A[i] + A[j] + A[k])

Ans.sort()
print(Ans[-3])