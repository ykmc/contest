# python 3.4.3
import sys
input = sys.stdin.readline
import numpy as np

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
H,W = map(int,input().split())
C = [input().rstrip() for _ in range(H)]

for i in range(H):
    print(C[i])
    print(C[i])
