# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
SE = list(tuple(map(int,input().split())) for _ in range(3))

total = 0
for s,e in SE:
    total += s*e

print(total//10)    
