# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
A = list(map(int,input().split()))

A.sort()

ans = N
total = 0

for i in range(N):
    # 後ろ(大きい方) からみていく
    a = A[N-1-i]
    # 合計に加えても K を超えないなら, 最小の部分集合に必要
    if total + a < K:
        total += a
    # そうでない場合, 不要
    else:
        ans = min(ans, N-1-i)

print(ans)