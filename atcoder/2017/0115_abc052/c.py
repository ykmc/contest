# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
mod = 10**9+7

# 素数列挙
primes = []
is_prime = [True]*(N+1)
for i in range(2,N+1):
    if is_prime[i]:
        primes.append(i)
        j = 2
        while i*j < N+1:
            is_prime[i*j] = False
            j += 1

# 約数の集計用
from collections import defaultdict
div = defaultdict(int)

ans = 1
# N = 2 から全探索
for i in range(2,N+1):
    for p in primes:
        if p > i:
            break
        cnt = 0
        while i%p==0:
            i //= p
            cnt += 1
        div[p] += cnt

for d in div.values():
    ans *= d+1
    ans %= mod

print(ans)