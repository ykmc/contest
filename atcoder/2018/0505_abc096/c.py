# Python3 (3.4.3)
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

for h in range(H):
    for w in range(W):
        # 白マスなら次へ
        if S[h][w]==".":
            continue
        # 黒マスなら上下左右に黒マスが1つでもあれば ok, なければ ng
        flg = False
        for dh,dw in [(1,0), (-1,0), (0,1), (0,-1)]:
            nh = h+dh
            nw = w+dw
            if 0 <= nh < H and 0 <= nw < W:
                if S[nh][nw] == "#":
                    flg = True
                    break
        if not flg:
            print("No")
            sys.exit()

print("Yes")