# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N)]
CD = [tuple(map(int,input().split())) for _ in range(M)]

Ans = [-1]*N
for i in range(N):
    a,b = AB[i]
    md0 = 10**10

    for j in range(M):
        c,d = CD[j]
        md = abs(a-c) + abs(b-d)
        if md < md0:
            md0 = md
            Ans[i] = (j+1)

for ans in Ans:
    print(ans)
