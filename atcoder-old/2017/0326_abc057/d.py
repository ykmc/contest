# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,A,B = map(int,input().split())
V = list(map(int,input().split()))

# 価値の降順にソート
V.sort(reverse=True)

# 価値の高い方から A 個 選んだ場合が平均価値最大
sumV = 0
for i in range(A):
    sumV += V[i]
ans1 = sumV/A


# 価値最大の個数
cntV0 = 0
for i in range(N):
    if V[i]==V[0]:
        cntV0 += 1
ans2 = 1
# 価値最大の個数が A より大きいなら
if cntV0 > A:
    ans2 = 0
    for i in range(A,min(cntV0,B)+1):
        tmp = 1
        c = cntV0
        r = i
        # cntV0 より j個 選ぶ選び方
        for j in range(r):
            tmp *= c-j
            tmp //= j+1
        ans2 += tmp
else:
    cntV1,cntV2 = 0,0
    # A 番目の価値と同じ個数, それより価値が大きな個数を数える
    for i in range(N):
        if V[i]==V[A-1]:
            cntV1 += 1
        elif V[i]>V[A-1]:
            cntV2 += 1
    # 合わせて A より大きければ, 複数の組み合わせがありうる
    if cntV1+cntV2 > A:
        c = cntV1
        r = A-cntV2
        # A 番目の価値と同じものを, 適切な数選ぶ場合の数を計算する
        for i in range(r):
            ans2 *= c-i
            ans2 //= i+1


print(ans1, ans2)
