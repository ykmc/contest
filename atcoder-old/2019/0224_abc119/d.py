# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B,Q = map(int,input().split())
S = [-float("inf")] + [int(input()) for _ in range(A)] + [float("inf")] # 両端にダミーを追加
T = [-float("inf")] + [int(input()) for _ in range(B)] + [float("inf")] # 両端にダミーを追加
X = [int(input()) for _ in range(Q)]
 
from bisect import bisect_left

for x in X:
    Si,Ti = bisect_left(S,x),bisect_left(T,x)
    Sw,Se = abs(x-S[Si-1]),abs(x-S[Si])
    Tw,Te = abs(x-T[Ti-1]),abs(x-T[Ti])
    ans = [0]*4
    ans[0] = max(Sw,Tw) # 両方ともwest
    ans[1] = max(Se,Te) # 両方ともeast
    ans[2] = 2*min(Sw,Te)+max(Sw,Te) # SwとTeの近い方に行き、反転して行ってない方に行く 
    ans[3] = 2*min(Tw,Se)+max(Tw,Se) # TwとSeの近い方に行き、反転して行ってない方に行く 
    print(min(ans))