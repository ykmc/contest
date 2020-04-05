# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
from collections import deque
import heapq

N,K = map(int,input().split())
V = list(map(int,input().split()))

ans = 0

maxPop = min(N,K)
# 左popする回数
for li in range(maxPop+1):
    # 右popする回数
    for ri in range(maxPop+1-li):
        # 初期化
        D = deque(V)
        jew = [] # 手持ちの宝石

        # pushの最大値
        maxPush = K - (ri+li)
        # 左popする
        for i in range(li):
            jew.append(D.popleft())
        # 右popする
        for i in range(ri):
            jew.append(D.pop())
        # 価値順にソート
        jew.sort()
        # push最大値の回数まで、負の価値の宝石をpushする（手持ちの価値を0にする）
        for i in range(min(maxPush, len(jew))):
            if jew[i] < 0:
                jew[i] = 0
        # 合計
        ans = max(ans,sum(jew))

print(ans)