# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
TXa,TYa,TXb,TYb,T,V = map(int,input().split())
N = int(input())
XY = [tuple(map(int,input().split())) for _ in range(N)]

ans = "NO"
for x,y in XY:
    if ((TXa - x)**2 + (TYa - y)**2)**.5 + ((TXb - x)**2 + (TYb - y)**2)**.5 <= T*V:
        ans = "YES"
        break

print(ans)