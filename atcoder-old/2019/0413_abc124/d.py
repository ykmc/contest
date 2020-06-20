# python 3.4.3
import sys
input = sys.stdin.readline
import numpy as np

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
S = input().rstrip() + "x"

# 連続する0,1の数を調べる
A = []
cnt = 1
for i in range(N):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        A.append(cnt)
        cnt = 1

# 両端が1だと計算が楽、端が1でない場合、[0] を加えることで「偶数番目は1」になるようにする
if S[0] != "1":
    A = [0] + A
if S[N-1] != "1":
    A = A + [0]

for i in range(len(A)-1):
    A[i+1] += A[i]

if 2*K+1 > len(A):
    print(A[-1])
else:
    si = 2*K
    ans = A[si]
    for i in range(2,len(A)-si,2):
        ans = max(ans, A[si+i]-A[i-1]) # 配列の添字がわかりにくすぎる、もう少し簡単にかけないか？
    print(ans)