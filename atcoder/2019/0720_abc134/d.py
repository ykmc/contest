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

B = [0]*(N+1)
Ans = []

for k in range(N,0,-1):
    cnt = 0
    for i in range(k,N+1,k):
        cnt += B[i]
    cnt %= 2
    if A[k-1] != cnt:
        B[k] = 1
        Ans.append(k)

print(len(Ans))
if Ans:
    print(*Ans)
