# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------

N = int(input())
CSF = [tuple(map(int,input().split())) for _ in range(N-1)]

Ans = []
for i in range(N):
    ans = 0
    for j in range(i,N-1):
        c,s,f = CSF[j]
        if ans < s:
            ans = s
        if ans%f != 0:
            ans += f - ans%f
        ans += c
    Ans.append(ans)

for ans in Ans:
    print(ans)
