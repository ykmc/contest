# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
H,W = map(int,input().split())
h,w = map(int,input().split())

print((H-h)*(W-w))