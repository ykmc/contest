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

# 2で何度割れるか
i = 0
M = N
while M>1:
    M //= 2
    i += 1

# 2で奇数回割れるなら T: *2, A: *2+1
if i%2 == 1:
    R = [0,1]
# 2で奇数回割れるなら T: *2+1, A: *2
else:
    R = [1,0]

A,j = 1,0
while A <= N:
    A = A*2 + R[j]
    j ^= 1

Ans = ["Takahashi","Aoki"]
print(Ans[j])
