# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()
t = int(input())

x,y,z = 0,0,0
for s in S:
    if s == "R":
        x += 1
    elif s == "L":
        x -=  1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1
    else:
        z += 1

# max
if t == 1:
    print(abs(x) + abs(y) + z)
# min
else:
    d = abs(x) + abs(y) - z
    if d > 0:
        print(d)
    else:
        if d%2 == 0:
            print(0)
        else:
            print(1)