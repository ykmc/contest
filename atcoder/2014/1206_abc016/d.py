# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def SignedArea(x0,y0,x1,y1,x2,y2):
    xa,ya = x1-x0,y1-y0
    xb,yb = x2-x0,y2-y0
    return (xa*yb - xb*ya) / 2


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
Ax,Ay,Bx,By = map(int,input().split())
N = int(input())
XY = [tuple(map(int,input().split())) for _ in range(N)]

# 扱いやすくするために, 末尾に始点を追加
XY.append(XY[0])

cnt = 0
for i in range(N):
    x1,y1 = XY[i]
    x2,y2 = XY[i+1]
    # 多角形の辺の端点それぞれが, 線分を挟んで反対側にあるか？
    if SignedArea(Ax,Ay,Bx,By,x1,y1) * SignedArea(Ax,Ay,Bx,By,x2,y2) < 0:
        if SignedArea(x1,y1,x2,y2,Ax,Ay) * SignedArea(x1,y1,x2,y2,Bx,By) < 0:
            cnt += 1

print(cnt//2 + 1)