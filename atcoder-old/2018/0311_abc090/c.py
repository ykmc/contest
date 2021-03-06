# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
 
if N<M:
    N,M = M,N

# 自身を含む周囲9マスが偶数なら表, 奇数なら表になる

ans = 0
# (_,1)
if M==1:
    # (1,1) # 1枚しかなく,裏になる
    if N==1:
        ans = 1
    # (x,1) : 両端以外が裏になる
    else:
        ans = N-2
# ( >=2, 2) : 全て表になる
elif M==2:
    ans = 0
# ( >=2, >=3) : 外周以外が裏になる
else:
    ans = (N-2)*(M-2)
 
print(ans)