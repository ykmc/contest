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
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
for i in range(N):
    # 食べた料理
    k = A[i] - 1
    # 得た満足度
    ans += B[k]
    # 追加満足度の判定
    if i < N-1 and A[i] == A[i+1]-1:
        ans += C[k]

print(ans)