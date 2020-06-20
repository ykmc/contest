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

ans = 0
div1,div2 = [],[]
for m in range(1,int(M**.5)+1):
    if M%m == 0:
        div1.append(m)

for d in div1:
    if M%d == 0:
        div2.append(M//d)

div3 = div1+div2
div3.sort()
for d in div3:
    if d <= M//N:
        ans = d

print(ans)