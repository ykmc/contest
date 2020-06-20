# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

# A,Bの組み合わせを全探索し, 上位のみ切り出す
AB = [a+b for a in A for b in B]
AB.sort(reverse=True)
AB = AB[:min(3001,X*Y*Z+1)]

# 切り出したa+bの上位要素と, cで全探索する
ABC = [ab+c for ab in AB for c in C]
ABC.sort(reverse=True)

for i in range(K):
    print(ABC[i])
