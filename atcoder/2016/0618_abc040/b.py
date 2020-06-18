# Python3 (3.8.2)
import sys
input = sys.stdin.readline

N = int(input())

ans = 10**10
for x in range(1,int(N**.5)+1):
    y = N//x
    ans = min(ans, abs(x-y) + N%x)

print(ans)