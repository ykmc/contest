# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
L,H = map(int,input().split())
N = int(input())
A = [int(input()) for _ in range(N)]

for a in A:
    if L <= a <= H:
        print(0)
    elif a < L:
        print(L-a)
    else:
        print(-1)