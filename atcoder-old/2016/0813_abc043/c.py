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
A = list(map(int,input().split()))

ans = 10**8
for x in range(-100,100+1):
    total = 0
    for i in range(N):
        total += (A[i] - x)**2
    ans = min(ans, total)

print(ans)