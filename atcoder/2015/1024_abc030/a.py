# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B,C,D = map(int,input().split())

takahashi = B/A
aoki = D/C

if takahashi > aoki:
    print("TAKAHASHI")
elif aoki > takahashi:
    print("AOKI")
else:
    print("DRAW")