# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A = int(input())
B = int(input())
C = int(input())

scores = sorted([A,B,C], reverse=True)
print(scores.index(A)+1)
print(scores.index(B)+1)
print(scores.index(C)+1)