# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B,T = map(int,input().split())

ans = 0
for _ in range(A,T+1,A):
    ans += B

print(ans)