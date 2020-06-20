# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,A,B = map(int,input().split())
SD = [tuple(input().split()) for _ in range(N)]

pos = 0
for s,d in SD:
    d = int(d)
    # 距離
    if d <= A:
        x = A
    elif d >= B:
        x = B
    else:
        x = d
    # 方角
    if s == "West":
        x *= -1
    
    pos += x

if pos == 0:
    print(0)
elif pos > 0:
    print("East", pos)
else:
    print("West", -pos)
