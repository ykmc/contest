# PyPy3 (2.4.0)
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
mod = 10**9+7

from collections import Counter
C = dict(Counter(A))

ans = 1
# 偶数の場合 : 1,3,5... が2人ずつ
if N%2==0:
    for i in range(N//2):
        if C.get(i*2+1) == 2:
            ans *= 2
            ans %= mod
        else:
            ans = 0
            break
# 奇数の場合 : 0が1人, 2,4,6...が2人ずつ
else:
    if C[0] == 1:
        for i in range(N//2):
            if C.get(i*2+2) == 2:
                ans *= 2
                ans %= mod
            else:
                ans = 0
                break
    else:
        ans = 0
 
print(ans)