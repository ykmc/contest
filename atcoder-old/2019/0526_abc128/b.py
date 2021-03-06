# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
SP = []
for i in range(N):
    s,p = input().split()
    SP.append((s, -int(p), i+1))

SP.sort()

for s,p,i in SP:
    print(i)