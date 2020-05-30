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
XYH = [tuple(map(int,input().split())) for _ in range(N)]

# 高さの降順にソートしておく
#  -> これをしないと 高さ 0 を基準に中心の高さを決めてしまう可能性があるので
XYH.sort(key=lambda x:x[2], reverse=True)

# 中心座標で全探索
for xi in range(101):
    for yi in range(101):
        flg = True
        x,y,h = XYH[0]
        # 中心の高さ
        hh0 = abs(xi-x) + abs(yi-y) + h
        for i in range(1,N):
            x,y,h = XYH[i]
            if h == 0:
                hhi = abs(xi-x) + abs(yi-y) + h
                if hh0 > hhi:
                    flg = False
                    break
            else:
                hhi = abs(xi-x) + abs(yi-y) + h
                if hh0 != hhi:
                    flg = False
                    break
        if flg:
            print(xi,yi,hh0)
            sys.exit()