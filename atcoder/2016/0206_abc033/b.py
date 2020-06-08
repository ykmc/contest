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
SP = []
for _ in range(N):
    s,p = input().split()
    SP.append((s,int(p)))

SP.sort(key=lambda x:x[1], reverse=True)

maxP = SP[0][1]
totalP = 0
for s,p in SP:
    totalP += p

print(SP[0][0] if maxP > totalP/2 else "atcoder")