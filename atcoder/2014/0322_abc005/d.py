# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
D = [list(map(int,input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
Q = int(input())
P = [int(input()) for _ in range(Q)]

# D[h][w] : (h,w)から右下にあるマスの合計
for h in range(N):
    for w in range(N-1):
        D[h][N-1-w-1] += D[h][N-1-w]
for h in range(N-1):
    for w in range(N):
        D[N-1-h-1][w] += D[N-1-h][w]

A = [0]*(N*N+1)
for h1 in range(N):
    for h2 in range(h1+1,N+1):
        h = h2-h1
        for w1 in range(N):
            for w2 in range(w1+1,N+1):
                w = w2-w1
                total = D[h1][w1] - D[h1][w2] - D[h2][w1] + D[h2][w2]
                A[h*w] = max(A[h*w], total)

# 少ない焼き方の方が得する場合を考慮
for i in range(N*N):
    A[i+1] = max(A[i+1],A[i])

for p in P:
    print(A[p]) 