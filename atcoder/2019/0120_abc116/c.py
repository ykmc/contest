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
H = list(map(int,input().split()))

ans = 0
x = [H]

while len(x) > 0:
    A = x.pop()
    # 一番小さい値まで全域に水やり
    minA = min(A)
    ans += minA
    k = A.index(minA)
    # した結果の残り
    for i in range(len(A)):
        A[i] -= minA
    # 一番小さい値 の左右に残りが存在するなら, 処理を継続する
    if A[0:k] != []:
        x.append(A[0:k])
    if A[k+1:] != []:
        x.append(A[k+1:])

print(ans)