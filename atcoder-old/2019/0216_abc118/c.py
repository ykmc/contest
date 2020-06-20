# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))

ans = A[0]
for i in range(1,N):
    ans = gcd(ans,A[i])
 
print(ans)