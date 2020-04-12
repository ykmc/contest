# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def f(s):
    L = len(str(s))
    dp = [[0 for _ in range(2)] for _ in range(L+1)]
    dp[0][0] = 1

    for i in range(L):
        n = int(str(s)[i])
        if n<=4:
            k = n
        else:
            k = n-1

        dp[i+1][0] = 0 if n in [4,9] else dp[i][0]
        dp[i+1][1] = dp[i][0]*k + dp[i][1]*8
    
    return dp[L][0] + dp[L][1]

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B = map(int,input().split())

print(B-A+1 - (f(B)-f(A-1)))