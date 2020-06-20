# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
H,W = map(int,input().split())
S = [input().rstrip() for _ in range(H)]

LR = [[0 for _ in range(W)] for _ in range(H)]
UD = [[0 for _ in range(W)] for _ in range(H)]

# 横方向
for h in range(H):
    cnt = 0
    for w in range(W):
        if S[h][w] == "#":
            cnt = 0
        else:
            cnt += 1
        LR[h][w] = cnt
for h in range(H):
    cnt = 0
    for w in range(W):
        if LR[h][W-1-w] == 0:
            cnt = 0
        else:
            if cnt==0:
                cnt = LR[h][W-1-w]
            else:
                LR[h][W-1-w] = cnt

# 縦方向
for w in range(W):
    cnt = 0
    for h in range(H):
        if S[h][w] == "#":
            cnt = 0
        else:
            cnt += 1
        UD[h][w] = cnt
for w in range(W):
    cnt = 0
    for h in range(H):
        if UD[H-1-h][w] == 0:
            cnt = 0
        else:
            if cnt==0:
                cnt = UD[H-1-h][w]
            else:
                UD[H-1-h][w] = cnt

ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, LR[h][w] + UD[h][w] - 1)

print(ans)