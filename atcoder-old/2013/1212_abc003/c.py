# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
R = list(map(int,input().split()))

R.sort(reverse=True)

rate = 0
for i in range(K):
    rate = (rate + R[K-1-i])/2

print(rate)