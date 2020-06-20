# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M,D = map(int,input().split())
A = list(map(int,input().split()))

# X[i] : 阿弥陀くじを1回適用した時の, iから始めたらどこにたどり着くか
X = [i for i in range(N)]
for a in A:
    X[a],X[a-1] = X[a-1],X[a]

# BX[k][i] : 阿弥陀くじを2^k 適用した時の, iから始めたらどこにたどり着くか
BX = [[0 for _ in range(N)] for _ in range(32)]
for i in range(N):
    BX[0][i] = X[i]
for k in range(31):
    for i in range(N):
        BX[k+1][i] = BX[k][BX[k][i]]

Ans = list(range(N))
for i in range(N):
    ci = i
    for k in range(32):
        if D>>k & 1:
            ci = BX[k][ci]
    Ans[ci] = i+1

for ans in Ans:
    print(ans)