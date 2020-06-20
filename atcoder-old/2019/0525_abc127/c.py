# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------

N,M = map(int,input().split())
LR = [tuple(map(int,input().split())) for _ in range(M)]

maxL,minR = 0,10**5+1
for l,r in LR:
    maxL = max(maxL,l)
    minR = min(minR,r)

print(max(0, minR - maxL + 1))