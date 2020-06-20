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

ans = 0
total = 0
ri = 0
for li in range(N):
    # 右端を更新
    while ri < N:
        if total < K:
            total += A[ri]
            ri += 1
        else:
            break
    if total < K:
        break
    # 数え上げ
    ans += N-ri+1
    # 左端を更新
    total -= A[li]

print(ans)