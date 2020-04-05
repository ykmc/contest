# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------
def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))

# L[i] : A[0] 〜 A[i-1] までのgcd
# R[i] : A[N-1-i+1] 〜 A[N-1] までのgcd 
L = [0]*N
R = [0]*N

for i in range(1,N):
    L[i]     = gcd(L[i-1], A[i-1])
    R[N-1-i] = gcd(R[N-i], A[N-i])

ans = 0
for i in range(N):
    ans = max(ans, gcd(L[i],R[i]))

print(ans)