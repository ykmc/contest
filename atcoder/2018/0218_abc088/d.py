# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(dq):
    while dq:
        e = dq.popleft()
        y,x = e
        for i in range(4):
            yi = y+dy[i]
            xi = x+dx[i]
            if 0<=yi<Y and 0<=xi<X:
                if A[yi][xi] != "#" and A[yi][xi] == ".":
                    A[yi][xi] = A[y][x] + 1 
                    dq.append((yi,xi))


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
H,W = map(int,input().split())
S = [list(input().rstrip()) for _ in range(H)]

Y,X = H,W
A = S

A[0][0] = 1
from collections import deque
dq = deque([(0,0)])
BFS(dq)

if A[Y-1][X-1] == ".":
    print(-1)
else:
    cnt = 0
    for a in A:
        cnt += a.count("#")
    print(X*Y - cnt - A[Y-1][X-1])