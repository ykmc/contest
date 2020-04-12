# Python3 (3.4.3)
import sys
input = sys.stdin.readline
from collections import deque

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
            if 0<=yi<=Y and 0<=xi<=X:
                if A[yi][xi] != "#" and A[yi][xi] == ".":
                    A[yi][xi] = A[y][x] + 1 
                    dq.append((yi,xi))


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
Y,X = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
A = [list(input().rstrip()) for _ in range(Y)]

A[sy-1][sx-1] = 0
dq = deque([(sy-1,sx-1)])
BFS(dq)
print(A[gy-1][gx-1])