# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
R,G,B = map(int,input().split())

# cを中心とし, leftを左端として x個のマーブルを並べる時のコスト
def cost(c,left,x):
    left -= c
    right = left+x-1
    if left>0 and right>0 or left<0 and right<0:
        return abs(left+right)*x//2
    else:
        return right*(right+1)//2 + abs(left*(left-1)//2)

Ans = 10**9

# Gの広げ方で全探索
for g_left in range(-500,501):
    ans = 0

    g_right = g_left + (G-1)
    ans += cost(0, g_left, G)

    # RがGと干渉しない場合
    if -100 + (R-1)//2 < g_left:
        ans += cost(-100,-(R//2+100),R)
    else:
        ans += cost(-100,g_left-R,R)
    
    # BがGと干渉しない場合
    if 100 - (B-1)//2 > g_right:
        ans += cost(100,100-B//2,B)
    else:
        ans += cost(100,g_right+1,B)
    
    Ans = min(Ans,ans)

print(Ans)

