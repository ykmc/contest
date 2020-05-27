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
T,A = map(int,input().split())
H = list(map(int,input().split()))

ans = -1
ans_tp = 1000
for i in range(N):
    h = H[i]
    tp = T - 0.006*h
    if abs(ans_tp-A) > abs(tp-A):
        ans_tp = tp
        ans = i

print(ans+1)