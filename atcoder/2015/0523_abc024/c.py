# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,D,K = map(int,input().split())
LR = [tuple(map(int,input().split())) for _ in range(D)]
ST = [tuple(map(int,input().split())) for _ in range(K)]

Ans = []

for s,t in ST:
    # 正の方向に進む場合
    if s < t:
        for i in range(D):
            l,r = LR[i]
            if l<=s<=r:
                s = r
            if s>=t:
                Ans.append(i+1)
                break
    # 負の方向に進む場合
    else:
        for i in range(D):
            l,r = LR[i]
            if l<=s<=r:
                s = l
            if s<=t:
                Ans.append(i+1)
                break

for ans in Ans:
    print(ans)
