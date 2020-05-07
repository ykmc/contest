# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
L,R = map(int,input().split())

ans = 2019
for i in range(L,R+1):
    if ans==0:
        break
    for j in range(i+1,R+1):
        ans = min(ans, (i*j)%2019)
        if ans==0:
            break

print(ans)