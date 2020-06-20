# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans += max(0, V[i]-C[i])

print(ans)