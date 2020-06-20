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

# N で割り切れなければ端数が出るので不可能
if sum(A)%N != 0:
    print(-1)
else:
    ans = 0
    # ある島までの合計人数
    total = 0
    # 島あたりの目標人数
    avg = sum(A)/N
    for i in range(N):
        total += A[i]
        if total/(i+1) == avg:
            continue
        ans += 1
    print(ans)