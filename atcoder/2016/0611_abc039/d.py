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
S = [list(input().rstrip()) for _ in range(H)]

# 白い画素の周囲は白, それ以外は黒, で復元
dx,dy = [-1,0,1],[-1,0,1]
T = [["#" for _ in range(W)] for _ in range(H)]
for hi in range(H):
    for wi in range(W):
        if S[hi][wi] == ".":
            for x in dx:
                for y in dy:
                    if 0 <= wi+x < W and 0 <= hi+y < H:
                        T[hi+y][wi+x] = "."

# 復元した画像を収縮
import copy
R = copy.deepcopy(T)
for hi in range(H):
    for wi in range(W):
        if T[hi][wi] == "#":
            for x in dx:
                for y in dy:
                    if 0 <= wi+x < W and 0 <= hi+y < H:
                        R[hi+y][wi+x] = "#"

# 復元→収縮した画像と, 元の画像が 同じかどうか
if S==R:
    print("possible")
    for i in range(H):
        print("".join(T[i]))
else:
    print("impossible")
