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
A = list(map(int,input().split()))

ans = -10000

# 高橋くんの選択
for ti in range(N):
    # 青木くんの選択
    tp0 = -10000
    ap0 = -10000
    for ai in range(N):
        # 同じ位置を選ぶのはルール違反
        if ti == ai:
            continue

        if ti < ai:
            l,r = ti,ai
        else:
            l,r = ai,ti
        tp,ap = 0,0
        cnt = 0
        for i in range(l, r+1):
            if cnt%2 == 0:
                tp += A[i]
            else:
                ap += A[i]
            cnt += 1
        # 青木くんの得点が更新されたら, 答えを更新
        if ap0 < ap:
            tp0 = tp
            ap0 = ap
    ans = max(ans,tp0)

print(ans)