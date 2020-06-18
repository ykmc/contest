# Python3 (3.8.2)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

D = {}
for i in range(N):
    D[i+1] = A[i]

D = sorted(D.items(),key=lambda x: x[1], reverse=True)
for i in range(N):
    print(D[i][0])