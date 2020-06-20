# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
H,W,D = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
Q = int(input())
LR = [tuple(map(int,input().split())) for _ in range(Q)]

N = H*W

B = [0]*(N+1)
for h in range(H):
    for w in range(W):
        n = A[h][w]
        B[n] = (h,w)

C = [[0 for _ in range((H*W)//D+1)]for _ in range(D)]
for i in range(D+1,N+1):
    rem = i%D
    x0,y0 = B[i-D]
    x1,y1 = B[i]
    C[rem][i//D] = abs(x1-x0) + abs(y1-y0)

for i in range(D):
    for j in range(1,(H*W)//D+1):
        C[i][j] += C[i][j-1]

for l,r in LR:
    i = l%D
    print(C[i][r//D] - C[i][l//D])