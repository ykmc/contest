# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,L = map(int,input().split())

total = L*N
for i in range(N):
    total += i

if L<=0 and L+N-1>=0:
    print(total)
elif L>0:
    print(total - L)
else:
    print(total - (L+N-1))    