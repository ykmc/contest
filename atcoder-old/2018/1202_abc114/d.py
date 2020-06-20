# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
N = 100
primes = []
is_prime = [True]*N
for i in range(2,N):
    if is_prime[i]:
        primes.append(i)
        j = 2
        while i*j < N:
            is_prime[i*j] = False
            j += 1

def get(x):
    cnt = 0
    for e in E:
        if e >= x-1:
            cnt += 1
    return cnt

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())

E = [0]*101
for i in range(2,N+1):
    for p in primes:
        while i%p==0:
            E[p] += 1
            i //= p

ans = 0

# e1^74
ans += get(75)

# e1^24, e2^2
ans += get(25) * (get(3)-1)

# e1^14, e2^4
ans += get(15) * (get(5)-1)

# e1^4, e2^4, e3^2
ans += get(5) * (get(5)-1) * (get(3)-2) // 2

print(ans)