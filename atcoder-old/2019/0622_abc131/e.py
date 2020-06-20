# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())

Ans = []
for i in range(N-1):
    Ans.append((N-1,i))

cnt = (N-1)*(N-2)//2
if cnt < K:
    print(-1)
    sys.exit()

for i in range(N-1):
    for j in range(i+1,N-1):
        if cnt>K:
            Ans.append((i,j))
            cnt -= 1

print(len(Ans))
for u,v in Ans:
    print(u+1,v+1)
