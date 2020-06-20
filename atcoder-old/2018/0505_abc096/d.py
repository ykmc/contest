# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
N = 55555
primes = []
is_prime = [True]*N
for i in range(2,N):
    if is_prime[i]:
        primes.append(i)
        j = 2
        while i*j < N:
            is_prime[i*j] = False
            j += 1

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())

Ans = []

# 5で割って1余る素数なら, どの異なる5個を足しても5で割れるので合成数になる
for p in primes:
    if p%5 == 1:
        Ans.append(p)

print(*Ans[0:N])