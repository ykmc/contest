# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B = map(int,input().split())
 
ans = 0
for i in range(A,B+1):
    s = str(i)
    if s == s[::-1]:
        ans += 1
 
print(ans)