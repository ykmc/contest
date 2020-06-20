# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A = int(input())
B = int(input())
C = int(input())
mod = 10**9+7
 
AB = (A*B)%mod
BC = (B*C)%mod
CA = (C*A)%mod
 
y = ((BC-AB)*pow((CA-BC+AB),mod-2,mod)) % mod
x = ((BC-CA)*pow((AB-BC+CA),mod-2,mod)) % mod
 
print(x,y)