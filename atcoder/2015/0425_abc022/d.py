# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def getG(XY):
    n = len(XY)
    total_x,total_y = 0,0
    for x,y in XY:
        total_x += x
        total_y += y
    return (total_x/n, total_y/n)

def getD(XY,Gx,Gy):
    ret = 0
    for x,y in XY:
        d = ((x - Gx)**2 + (y - Gy)**2)**.5
        ret = max(ret, d)
    return ret

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
AA = [tuple(map(int,input().split())) for _ in range(N)]
BB = [tuple(map(int,input().split())) for _ in range(N)]

# 重心 : G
GAx,GAy = getG(AA)
GBx,GBy = getG(BB)

# 重心から最も遠い点までの距離 : D
DA = getD(AA,GAx,GAy)
DB = getD(BB,GBx,GBy)

# 拡大比率
ans = DB / DA

print(ans)