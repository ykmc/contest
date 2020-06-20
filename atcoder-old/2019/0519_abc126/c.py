import sys
input = sys.stdin.readline

N,K = map(int,input().split())

ans = 0
for i in range(1,N+1):
    e = 1/N
    t = i
    while t<K:
        t *= 2
        e /= 2
    ans += e

print(ans)
