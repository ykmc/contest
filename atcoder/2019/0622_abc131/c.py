# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)
def lcm(a,b):
    return a*b // gcd(a,b)

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B,C,D = map(int,input().split())

def f(x):
    return x - (x//C + x//D - x//lcm(C,D))

print(f(B) - f(A-1))