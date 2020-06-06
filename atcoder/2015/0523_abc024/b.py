# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,T = map(int,input().split())
A = [int(input()) for _ in range(N)]

# 最後の1名のあとは T 秒開いたまま
ans = T
for i in range(N-1):
    # 次の人がくるか, T 秒経つか, 早い方を足していけば良い
    ans += min(T, A[i+1]-A[i])

print(ans)