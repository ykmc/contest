# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
R,C,K = map(int,input().split())
S = [input().rstrip() for _ in range(R)]

# UD[r][c][0] : (c,r)から見て, 上に存在するスペース数
# UD[r][c][1] : (c,r)から見て, 下に存在するスペース数
UD = [[[0,0] for _ in range(C)] for _ in range(R)]

for c in range(C):
    up,down = 0,0
    for r in range(R):
        # up
        if S[r][c] == "x":
            up = 0
        else:
            up += 1
        UD[r][c][0] = up
        # down
        if S[R-1-r][C-1-c] == "x":
            down = 0
        else:
            down += 1
        UD[R-1-r][C-1-c][1] = down

ans = 0
# 各マスを中心として描けるか全探索
for c in range(K-1,C-K+1):
    for r in range(K-1,R-K+1):
        flag = True
        for k in range(K):
            if min(min(UD[r][c-k]),min(UD[r][c+k])) < K-k:
                flag = False
                break
        if flag:
            ans += 1


print(ans)